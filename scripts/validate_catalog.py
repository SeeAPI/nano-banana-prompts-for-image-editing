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
    assert c['tested'] is False, c['id']
    assert c['status'] == ('image-included' if c['media'] else 'prompt-only'), c['id']
    if c['media']:
        assert any(m['role']=='reference' for m in c['media'])
        assert any(m['role']=='result' for m in c['media'])
    for m in c['media']:
        assert m['role'] in ['reference','result']
        assert m['provenance']=='user-supplied'
        assert m['width']>0 and m['height']>0
        assert hashlib.sha256((ROOT/m['path']).read_bytes()).hexdigest()==m['sha256'], m['path']
    assert c['updated']<=data['updated']
    assert c['workflow'].strip() and c['workflow_zh'].strip()
    assert len(c['prompts'])==1
    for en in c['prompts']:
        original=(ROOT/en).read_text();translation=(ROOT/c['prompts_zh'][en]).read_text()
        assert original.strip() and translation.strip()
        assert hashlib.sha256((ROOT/en).read_bytes()).hexdigest()==c['translation_source_sha256'][en], f"Translation review required: {en}"
        assert set(re.findall(r'\[[^\]\n]+\]',original))==set(re.findall(r'\[[^\]\n]+\]',translation)), f"Placeholder mismatch: {en}"
        assert 'prompt pending' not in original.lower()
        keys = set(re.findall(r'\[[^\]\n]+\]', original))
        for field in ['workflow', 'workflow_zh']:
            assert set(re.findall(r'\[[^\]\n]+\]', c[field])) == keys, f'Workflow placeholder mismatch: {en}'
    if c['source']['kind']=='inspired':
        assert c['source']['platform']=='X' and c['source']['url'].startswith('https://x.com/')
        assert c['source']['prompt_url'].startswith('https://x.com/')
for rel,expected in outputs(data).items():
    assert (ROOT/rel).read_text()==expected, f'Regenerate {rel}'
    for url in re.findall(r'(?:src|href)="([^"]+)"', expected):
        if not url.startswith(('https://', '#')):
            assert ((ROOT/rel).parent/url).is_file(), f'Missing asset/link in {rel}: {url}'
    assert '{{' not in expected, f'Unresolved template token: {rel}'
for name in ['README.md','README_zh.md']:
    text=(ROOT/name).read_text()
    anchors=re.findall(r'<a id="([^"]+)"',text)
    assert len(anchors)==len(set(anchors))
    assert all(link in anchors for link in re.findall(r'\]\(#([^)]*)\)',text))
    assert text.count('```text')==len(cases)
    assert text.count('<sub>')==len(cases)
    assert len(re.findall(r'^### ',text,re.M))==len(cases)
    assert not re.search(r'^> ',text,re.M)
    label = '#### 👇 工作流' if name == 'README_zh.md' else '#### 👇 Workflow'
    assert text.count(label) == len(cases)
    for section in re.split(r'^### ', text, flags=re.M)[1:]:
        headings = re.findall(r'^#### (.+)$', section, re.M)
        expected = ['🖼️ 预览', '👇 工作流', '📝 完整提示词'] if name == 'README_zh.md' else ['🖼️ Preview', '👇 Workflow', '📝 Full Prompt']
        assert headings == expected, headings
mini=(ROOT/'prompts/mini-me/prompt.txt').read_text()
for literal in ['"shine"','"bright day"','"happy"']:
    assert literal in mini and literal in (ROOT/'prompts/mini-me/prompt.zh-CN.txt').read_text()
print(f'Validated {len(cases)} bilingual prompts; category counts: {counts}')
