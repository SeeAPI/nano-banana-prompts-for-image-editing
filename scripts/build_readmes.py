#!/usr/bin/env python3
"""Build both README languages and case pages from reviewed prompt files."""
import argparse
from datetime import date
import json
from html import escape
from posixpath import relpath
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
 ('portraits-outfits','👗','Portraits & Outfits','人像与穿搭'),
 ('products-commercial','🛍️','Products & Commercial Images','产品与商业图片'),
 ('homes-spaces','🏡','Homes & Spaces','家居与空间'),
 ('style-transformations','🎨','Style Transformations & Playful Edits','风格转换与趣味创作'),
 ('restoration-adjustments','🪄','Photo Restoration & Local Adjustments','照片修复与局部调整'),
]

def credit(c, zh):
    s = c['source']
    if s['kind'] == 'original':
        value = '提示词：SeeAPI' if zh else 'Prompt by SeeAPI'
    elif s['kind'] == 'user-supplied':
        value = '用户提供提示词 · 原作者与来源待补充' if zh else 'User-supplied prompt · Original author and source pending'
    elif s['kind'] == 'user-adapted':
        value = ('基于用户提供提示词 · 原作者与来源待补充 · SeeAPI 改编：补充人物与宠物参考图约束，调整前景描述并去除年龄、性别限定' if zh else 'Based on a user-supplied prompt · Original author and source pending · Adapted by SeeAPI: reference binding, clearer pet foreground, and age/gender-neutral wording')
    else:
        value = f"{'创意参考' if zh else 'Inspired by'} [@{s['author']}]({s['url']}) · [Source: X]({s['url']}) · [{'原帖提示词' if zh else 'Source prompt'}]({s['prompt_url']}) · {'SeeAPI 重新编写为参考图编辑提示词，非原文转载；未实测' if zh else 'Reference-image editing prompt rewritten by SeeAPI; not a verbatim copy; untested'}"
        if s.get('context_url'):
            value += f" · [{'作者补充：用于概念探索' if zh else 'Author clarification: concept exploration'}]({s['context_url']})"
            value += f" · {'上游灵感' if zh else 'Earlier inspiration'}: [{s['inspiration_author']}]({s['inspiration_url']})"
    return f'<sub>{value}</sub>'

def media_tag(item, zh, page_dir='.', max_size=320):
    url = relpath(item['path'], page_dir)
    scale = min(max_size/item['width'], max_size/item['height'], 1)
    width, height = round(item['width']*scale), round(item['height']*scale)
    alt = escape(item['label_zh'] if zh else item['label'], quote=True)
    return f'<a href="{url}"><img src="{url}" width="{width}" height="{height}" alt="{alt}"></a>'

def preview(c, zh, standalone):
    page_dir = ('cases/zh-CN' if zh else 'cases') if standalone else '.'
    refs = [m for m in c['media'] if m['role']=='reference']
    results = [m for m in c['media'] if m['role']=='result']
    if refs:
        size = 150 if len(refs)>1 else 320
        before = ' &nbsp; '.join(media_tag(m,zh,page_dir,size) for m in refs)
        before += '<br>' + escape(c['inputs_zh'] if zh else c['inputs'])
    else:
        before = (c['inputs_zh']+'<br>原图待补充') if zh else (c['inputs']+'<br>Input image pending')
    after = ' '.join(media_tag(m,zh,page_dir) for m in results) if results else ('效果图待补充' if zh else 'Result image pending')
    return f'| Before | After |\n| :---: | :---: |\n| {before} | {after} |'

def featured(data, zh):
    by_id = {c['id']: c for c in data['cases']}
    names, images, workflows = [], [], []
    for item in data['featured']:
        c = by_id[item['id']]
        names.append(f"[{c['title_zh'] if zh else c['title']}](#{c['readme_anchor']})")
        results = [m for m in c['media'] if m['role']=='result']
        images.append(media_tag(results[0],zh,max_size=180) if results else ('示例图待补充' if zh else 'Preview coming soon'))
        workflows.append('`'+item['workflow_zh' if zh else 'workflow']+'`')
    return '\n'.join(['| '+' | '.join(names)+' |','| :---: | :---: | :---: |','| '+' | '.join(images)+' |','| '+' | '.join(workflows)+' |'])

def body(c, zh, standalone=False):
    level = '##' if standalone else '####'
    path = c['prompts_zh'][c['prompts'][0]] if zh else c['prompts'][0]
    prompt = (ROOT/path).read_text().rstrip('\n')
    return '\n\n'.join([
      f"{level} 🖼️ {'预览' if zh else 'Preview'}",
      preview(c, zh, standalone),
      f"{level} 👇 {'工作流' if zh else 'Workflow'}",
      '`' + (c['workflow_zh'] if zh else c['workflow']) + '`',
      f"{level} 📝 {'完整提示词' if zh else 'Full Prompt'}",
      f'```text\n{prompt}\n```', credit(c, zh)
    ])

def outputs(data):
    result = {}
    for zh in [False, True]:
        name = 'README_zh.md' if zh else 'README.md'
        intro = (ROOT/'templates'/name).read_text()
        dt = date.fromisoformat(data['updated'])
        intro = intro.replace('{{COUNT}}',str(len(data['cases']))).replace('{{DATE}}',data['updated']).replace('{{DATE_EN}}',dt.strftime('%B %d, %Y').replace(' 0',' '))
        intro = intro.replace('{{IMAGE_COUNT}}', str(sum(c['status']=='image-included' for c in data['cases']))).replace('{{FEATURED}}',featured(data,zh))
        blocks = [intro.rstrip()]
        for n,(anchor,emoji,en,cn) in enumerate(CATEGORIES,1):
            blocks += [f'<a id="{anchor}"></a>',f'## {emoji} {n}. {cn if zh else en}']
            for c in data['cases']:
                if c['category'] != n: continue
                title = c['title_zh'] if zh else c['title']
                blocks += [f'<a id="{c["readme_anchor"]}"></a>', f'### {c["display_number"]}. {title}', body(c, zh)]
                casepath = ('cases/zh-CN/'+c['slug']+'.md') if zh else c['case']
                result[casepath] = f'# {c["id"]} · {title}\n\n'+body(c,zh,True)+'\n'
        result[name] = '\n\n'.join(blocks)+'\n'
    return result

def main():
    parser = argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    data=json.loads((ROOT/'catalog.json').read_text());errors=[]
    for rel,content in outputs(data).items():
        path=ROOT/rel
        if args.check:
            if not path.exists() or path.read_text()!=content:errors.append(rel)
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content)
    if errors:raise SystemExit('Out of date: '+', '.join(errors))
    print(('Checked' if args.check else 'Built')+f" bilingual README and {len(data['cases'])} bilingual case pages")
if __name__ == '__main__':main()
