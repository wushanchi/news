# -*- coding: utf-8 -*-
"""从 5.30 的 4 个 HTML 反向提取数据，生成 wechat-article + xhs-draft。"""
import re, os, json

BASE = r"C:\Users\Wu Shanchi\WorkBuddy\2026-05-22-AI news"
DATE = "2026-05-30"
DATE_CN = "2026年5月30日"
WEEKDAY = "星期六"

# 报告元数据
META = {
    "ai":     {"file": "ai-morning-2026-05-30.html",      "title": "AI 晨报",     "accent": "#ff6a3d", "label": "AI 晨报"},
    "world":  {"file": "world-news-2026-05-30.html",       "title": "国际焦点日报", "accent": "#3b82f6", "label": "国际焦点"},
    "tech":   {"file": "tech-news-2026-05-30.html",        "title": "科技日报",     "accent": "#10b981", "label": "科技日报"},
    "sports": {"file": "sports-health-2026-05-30.html",    "title": "运动健康日报", "accent": "#f59e0b", "label": "运动健康"},
}

def parse_html(fp):
    """解析单文件 HTML，提取 sections 列表。"""
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    sections = []
    # 分割每个 <section>
    section_pattern = re.compile(r'<section class="section" id="(sec-[^"]+)">(.*?)(?=<section|</main>)', re.S)
    for m in section_pattern.finditer(c):
        sec_id = m.group(1)
        body = m.group(2)

        # section 标题
        title_m = re.search(r'<h2>([^<]+)</h2>', body)
        title = title_m.group(1).strip() if title_m else sec_id

        # section emoji（从 nav 中找）
        nav_m = re.search(r'<a href="#' + re.escape(sec_id) + r'">([^<]+)<', c)
        emoji_m = re.search(r'<a href="#' + re.escape(sec_id) + r'">([^<]+)<span class="nav-count"', c)
        emoji = ''
        if emoji_m:
            em = emoji_m.group(1).strip()
            # 提取开头的 emoji（第一个非中英文标点字符前的部分）
            for ch in em:
                if ord(ch) > 127 and ch not in ' /|':
                    if ch.isprintable() and ch not in '模型发布产品行业论文观点体育健身科学营养饮食':
                        emoji = em[:em.find(ch)+len(ch)]
                        break

        # 提取每个 article
        items = []
        article_pattern = re.compile(r'<article class="card card-animate">(.*?)</article>', re.S)
        for am in article_pattern.finditer(body):
            card = am.group(1)
            src_m  = re.search(r'<span class="card-source">([^<]+)</span>', card)
            title_m = re.search(r'<h3 class="card-title">([^<]+)</h3>', card)
            summ_m  = re.search(r'<p class="card-summary">([^<]+)</p>', card)
            url_m   = re.search(r'<a class="card-link" href="([^"]+)"', card)
            if title_m and src_m and summ_m and url_m:
                items.append([title_m.group(1).strip(),
                              src_m.group(1).strip(),
                              summ_m.group(1).strip(),
                              url_m.group(1).strip()])

        if items:
            sections.append({"id": sec_id, "title": title, "emoji": emoji, "items": items})

    return sections

# 解析所有 4 个文件
data = {}
for key, meta in META.items():
    fp = os.path.join(BASE, meta["file"])
    sections = parse_html(fp)
    data[key] = {
        "title": meta["title"],
        "accent": meta["accent"],
        "label": meta["label"],
        "sections": sections,
    }
    total = sum(len(s["items"]) for s in sections)
    print(f"[{key}] {len(sections)} sections, {total} items parsed")

# ========== WeChat Article ==========
def section_html(sec, accent):
    items = sec["items"][:5]
    cards = ""
    for item in items:
        t, src, summary, url = item[0], item[1], item[2], item[3]
        cards += f"""<div class="item">
  <div class="item-source">{src}</div>
  <div class="item-title">{t}</div>
  <div class="item-desc">{summary}</div>
</div>
"""
    return f"""<div class="section">
  <div class="section-head" style="border-left:4px solid {accent}">
    <h2>{sec.get("emoji","")} {sec["title"]}</h2>
  </div>
  <div class="item-list">
{cards}
  </div>
</div>"""

content = ""
content += f"""<header class="header">
  <div class="header-date">{DATE_CN} · {WEEKDAY}</div>
  <h1>每日晨报 · 综合版</h1>
  <div class="header-sub">AI + 国际 + 科技 + 运动健康 · 一站速览今日要闻</div>
</header>
"""

# AI 全部 sections
content += '<div class="report-block"><div class="report-label" style="background:#ff6a3d">AI 晨报</div>'
for sec in data["ai"]["sections"]:
    content += section_html(sec, data["ai"]["accent"])
content += '</div>'

# World top 3
content += '<div class="report-block"><div class="report-label" style="background:#3b82f6">国际焦点</div>'
for sec in data["world"]["sections"][:3]:
    content += section_html(sec, data["world"]["accent"])
content += '</div>'

# Tech top 3
content += '<div class="report-block"><div class="report-label" style="background:#10b981">科技日报</div>'
for sec in data["tech"]["sections"][:3]:
    content += section_html(sec, data["tech"]["accent"])
content += '</div>'

# Sports top 3
content += '<div class="report-block"><div class="report-label" style="background:#f59e0b">运动健康</div>'
for sec in data["sports"]["sections"][:3]:
    content += section_html(sec, data["sports"]["accent"])
content += '</div>'

footer = """<footer class="footer">
  <p>每日 08:50 自动生成 · 数据来源 AI HOT / 公开新闻源 · 完整版请查看 GitHub</p>
</footer>"""

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>每日晨报 · {DATE_CN}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;background:#f5f5f5;color:#333;line-height:1.7;max-width:680px;margin:0 auto;-webkit-font-smoothing:antialiased}}
.header{{background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%);color:#fff;text-align:center;padding:40px 20px 32px}}
.header-date{{font-size:13px;opacity:0.7;letter-spacing:0.1em;margin-bottom:8px}}
.header h1{{font-size:26px;font-weight:700;margin-bottom:8px}}
.header-sub{{font-size:14px;opacity:0.8;font-weight:400}}
.report-block{{margin:16px 12px}}
.report-label{{display:inline-block;color:#fff;font-size:12px;font-weight:700;padding:4px 14px;border-radius:4px;margin-bottom:12px;letter-spacing:0.05em}}
.section{{background:#fff;border-radius:10px;padding:18px 16px;margin-bottom:12px;box-shadow:0 1px 4px rgba(0,0,0,0.06)}}
.section-head{{padding-left:14px;margin-bottom:12px}}
.section-head h2{{font-size:17px;font-weight:700;color:#222}}
.item-list{{display:flex;flex-direction:column;gap:14px}}
.item{{border-bottom:1px solid #f0f0f0;padding-bottom:12px}}
.item:last-child{{border-bottom:none;padding-bottom:0}}
.item-source{{font-size:11px;color:#999;margin-bottom:3px}}
.item-title{{font-size:15px;font-weight:600;color:#1a1a2e;margin-bottom:4px;line-height:1.5}}
.item-desc{{font-size:13px;color:#666;line-height:1.6}}
.footer{{text-align:center;padding:24px 20px 40px;font-size:12px;color:#aaa}}
</style>
</head>
<body>
{content}
{footer}
</body>
</html>"""

wechat_fp = os.path.join(BASE, f"wechat-article-{DATE}.html")
with open(wechat_fp, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"[OK] {os.path.basename(wechat_fp)} ({os.path.getsize(wechat_fp):,} bytes)")

# ========== Xiaohongshu Draft ==========
ai = data["ai"]
total_ai = sum(len(s["items"]) for s in ai["sections"])
lines = []
lines.append(f"===== 小红书草稿 · {DATE_CN} =====")
lines.append("")
lines.append(f"【{DATE_CN}  AI 晨报速递】")
lines.append("")
lines.append("今日 AI 圈大事一览，一文带你刷完！")
lines.append("")

global_num = 0
for sec in ai["sections"]:
    emoji = sec.get("emoji", "")
    lines.append(f"{emoji} {sec['title']}（{len(sec['items'])}条）")
    for item in sec["items"][:5]:
        global_num += 1
        t, src, summary, url = item[0], item[1], item[2], item[3]
        lines.append(f"  #{global_num:02d} {t}")
        lines.append(f"     {summary}")
        if len(url) < 50:
            lines.append(f"     来源: {url}")
    lines.append("")

lines.append("---")
lines.append(f"完整 {total_ai} 条 AI 资讯 + 国际焦点 / 科技日报 / 运动健康")
lines.append(f"查看每日晨报 GitHub: https://github.com/wushanchi/news")
lines.append("")
lines.append("#AI晨报 #每日AI #科技资讯 #人工智能")

xhs_content = '\n'.join(lines)
xhs_fp = os.path.join(BASE, f"xhs-draft-{DATE}.txt")
with open(xhs_fp, 'w', encoding='utf-8') as f:
    f.write(xhs_content)
print(f"[OK] {os.path.basename(xhs_fp)} ({len(xhs_content)} chars)")
print("\n[DONE] 5.30 wechat + xhs generated.")
