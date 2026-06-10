# -*- coding: utf-8 -*-
"""Generate WeChat article and Xiaohongshu draft from 4 JSON data files."""
import json, os

DATE = "2026-06-10"
DATE_CN = "2026年6月10日"
WEEKDAY = "星期三"
BASE = r"C:\Users\Wu Shanchi\WorkBuddy\2026-05-22-AI news"

# Load all data
data = {}
for key, fn in [("ai","news_data.json"), ("world","news_data_world.json"),
                ("tech","news_data_tech.json"), ("sports","news_data_sports.json")]:
    with open(os.path.join(BASE, fn), 'r', encoding='utf-8') as f:
        loaded = json.load(f)
        data[key] = loaded.get(key, loaded)

# ========== WeChat Article ==========

def wechat_article():
    """Generate a WeChat public account style article with highlights from all 4 reports."""

    def section_html(sec, accent):
        """Render a section with 3-4 highlight items."""
        items = sec['items'][:5]  # top 5 per section
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
    <h2>{sec.get('emoji','')} {sec['title']}</h2>
  </div>
  <div class="item-list">
{cards}
  </div>
</div>"""

    # Build full content
    content = ""

    # Header
    content += f"""<header class="header">
  <div class="header-date">{DATE_CN} · {WEEKDAY}</div>
  <h1>每日晨报 · 综合版</h1>
  <div class="header-sub">AI + 国际 + 科技 + 运动健康 · 一站速览今日要闻</div>
</header>
"""

    # AI sections
    content += '<div class="report-block"><div class="report-label" style="background:#ff6a3d">AI 晨报</div>'
    for sec in data['ai']['sections']:
        content += section_html(sec, data['ai']['accent'])
    content += '</div>'

    # World sections
    content += '<div class="report-block"><div class="report-label" style="background:#3b82f6">国际焦点</div>'
    for sec in data['world']['sections'][:3]:  # top 3 sections
        content += section_html(sec, data['world']['accent'])
    content += '</div>'

    # Tech sections
    content += '<div class="report-block"><div class="report-label" style="background:#10b981">科技日报</div>'
    for sec in data['tech']['sections'][:3]:
        content += section_html(sec, data['tech']['accent'])
    content += '</div>'

    # Sports sections
    content += '<div class="report-block"><div class="report-label" style="background:#f59e0b">运动健康</div>'
    for sec in data['sports']['sections'][:3]:
        content += section_html(sec, data['sports']['accent'])
    content += '</div>'

    # Footer
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

    fp = os.path.join(BASE, f'wechat-article-{DATE}.html')
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
    sz = os.path.getsize(fp)
    print(f"[OK] wechat-article-{DATE}.html ({sz:,} bytes)")
    return fp


# ========== Xiaohongshu Draft ==========

def xhs_draft():
    """Generate a Xiaohongshu-style text draft based on AI morning report."""

    ai = data['ai']
    lines = []
    lines.append(f"===== 小红书草稿 · {DATE_CN} =====")
    lines.append("")
    lines.append(f"【{DATE_CN}  AI 晨报速递】")
    lines.append("")
    lines.append("今日 AI 圈大事一览，一文带你刷完！")
    lines.append("")

    global_num = 0
    for sec in ai['sections']:
        emoji = sec.get('emoji', '')
        lines.append(f"{emoji} {sec['title']}（{len(sec['items'])}条）")
        for item in sec['items'][:5]:  # top 5 per section
            global_num += 1
            t, src, summary, url = item[0], item[1], item[2], item[3]
            lines.append(f"  #{global_num:02d} {t}")
            lines.append(f"     {summary}")
            if len(url) < 50:
                lines.append(f"     来源: {url}")
        lines.append("")

    lines.append("---")
    lines.append("完整 32 条 AI 资讯 + 国际焦点 / 科技日报 / 运动健康")
    lines.append(f"查看每日晨报 GitHub: https://github.com/wushanchi/news")
    lines.append("")
    lines.append("#AI晨报 #每日AI #科技资讯 #人工智能")

    content = '\n'.join(lines)
    fp = os.path.join(BASE, f'xhs-draft-{DATE}.txt')
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[OK] xhs-draft-{DATE}.txt ({len(content)} chars)")
    return fp


# ========== Main ==========
wechat_article()
xhs_draft()
print("\n[DONE] Both wechat article and xiaohongshu draft generated.")
