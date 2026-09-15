#!/usr/bin/env python3
"""Validate bilingual prompt coverage, placeholders, hashes, and README links."""
import hashlib
import json
from pathlib import Path
import re
from build_readmes import outputs

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'catalog.json').read_text())
cases=data['cases'];seen=set();counts={}
for c in cases:
    assert c['id'] not in seen, f"Duplicate ID: {c['id']}"
    seen.add(c['id']);cat=c['category'];counts[cat]=counts.get(cat,0)+1
    assert c['display_number']==f'{cat}.{counts[cat]}', c['id']
    assert c['status']=='prompt-only' and not c['media'] and c['tested'] is False, c['id']
    assert c['updated']<=data['updated']
    assert len(c['prompts'])==1
    for en in c['prompts']:
        original=(ROOT/en).read_text();translation=(ROOT/c['prompts_zh'][en]).read_text()
        assert original.strip() and translation.strip()
        assert hashlib.sha256((ROOT/en).read_bytes()).hexdigest()==c['translation_source_sha256'][en], f"Translation review required: {en}"
        assert set(re.findall(r'\[[^\]\n]+\]',original))==set(re.findall(r'\[[^\]\n]+\]',translation)), f"Placeholder mismatch: {en}"
        assert 'prompt pending' not in original.lower()
    if c['source']['kind']=='inspired':
        assert c['source']['platform']=='X' and c['source']['url'].startswith('https://x.com/')
        assert c['source']['prompt_url'].startswith('https://x.com/')
for rel,expected in outputs(data).items():
    assert (ROOT/rel).read_text()==expected, f'Regenerate {rel}'
for name in ['README.md','README_zh.md']:
    text=(ROOT/name).read_text()
    anchors=re.findall(r'<a id="([^"]+)"',text)
    assert len(anchors)==len(set(anchors))
    assert all(link in anchors for link in re.findall(r'\]\(#([^)]*)\)',text))
    assert text.count('```text')==len(cases)
    assert text.count('<sub>')==len(cases)
    assert len(re.findall(r'^### ',text,re.M))==len(cases)
    assert not re.search(r'^> ',text,re.M)
    assert 'Workflow' not in text and '工作流' not in text
mini=(ROOT/'prompts/mini-me/prompt.txt').read_text()
for literal in ['"shine"','"bright day"','"happy"']:
    assert literal in mini and literal in (ROOT/'prompts/mini-me/prompt.zh-CN.txt').read_text()
print(f'Validated {len(cases)} bilingual prompts; category counts: {counts}')
