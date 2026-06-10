# -*- coding: utf-8 -*-
import json, os

DATE = "2026-06-10"
DATE_CN = "2026 年 6 月 10 日"
WEEKDAY = "星期三"
BASE = r"C:\Users\Wu Shanchi\WorkBuddy\2026-05-22-AI news"

# Load all data
data = {}
for key, fn in [("ai","news_data.json"), ("world","news_data_world.json"),
                ("tech","news_data_tech.json"), ("sports","news_data_sports.json")]:
    with open(os.path.join(BASE, fn), 'r', encoding='utf-8') as f:
        loaded = json.load(f)
        data[key] = loaded.get(key, loaded)  # unwrap if nested under key

def generate_html(report_key, report_data):
    accent = report_data['accent']
    accent2 = report_data['accent2']
    bg = report_data['bg']
    surface = report_data['surface']
    card_bg = report_data['card']
    border = report_data['border']
    text = report_data['text']
    text_dim = report_data['text_dim']
    grad = report_data['grad']
    tags = report_data['tags']
    sections = report_data['sections']
    stat_names = report_data['stat_names']
    footer_text = report_data['footer']
    title = report_data['title']

    tag_css = ''.join(f"--c-tag-{k}:{v};" for k, v in tags.items())
    badge_css = ''.join(f".badge-{k}{{background:var(--c-tag-{k})}}" for k in tags.keys())
    accent_rgb = accent.replace('#', '')
    accent2_rgb = accent2.replace('#', '')
    bg_rgb = bg.replace('#', '')

    # Build sections
    global_num = 0
    sections_html = ""
    nav_links = ""
    stats_dots = ""
    total_count = 0

    for sec in sections:
        sid = sec['id']
        badge = sec['badge']
        sec_title = sec['title']
        emoji = sec.get('emoji', '')
        items = sec['items']
        count = len(items)
        total_count += count

        cards = ""
        for item in items:
            global_num += 1
            t, src, summary, url = item[0], item[1], item[2], item[3]
            cards += f"""<div class="card card-animate">
  <div class="card-top">
    <span class="card-num">#{global_num:02d}</span>
    <span class="card-source">{src}</span>
  </div>
  <div class="card-title">{t}</div>
  <div class="card-summary">{summary}</div>
  <div class="card-actions">
    <a class="card-link" href="{url}" target="_blank" rel="noopener noreferrer">
      阅读原文
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
    </a>
  </div>
</div>
"""
        sections_html += f"""<section class="section" id="{sid}">
  <div class="section-header">
    <span class="section-badge badge-{sid}">{badge}</span>
    <h2>{emoji} {sec_title}</h2>
    <span class="section-count">{count} 条</span>
  </div>
  <div class="cards">
{cards}
  </div>
</section>
"""
        nav_links += f'  <a href="#{sid}"><span>{emoji} {sec_title}</span><span class="nav-count">{count}</span></a>\n'
        stats_dots += f'    <div class="stat"><span class="stat-dot" style="background:var(--c-tag-{sid})"></span> {stat_names[sid]} <strong>{count}</strong></div>\n'

    hero = f"""<header class="hero">
  <div class="hero-date">{DATE_CN} · {WEEKDAY}</div>
  <h1 class="hero-title">{title}</h1>
  <div class="hero-total">今日 {total_count} 条 · 北京时间 08:50 生成</div>
</header>"""

    stats_block = f"""<div class="stats-wrap">
  <div class="stats">
{stats_dots}  </div>
</div>"""

    nav = f"""<nav class="nav-wrap"><div class="nav">
{nav_links}</div></nav>"""

    footer = f"""<footer class="footer">
  <p>{footer_text}</p>
</footer>"""

    file_map = {'ai': f'ai-morning-{DATE}.html', 'world': f'world-news-{DATE}.html',
                'tech': f'tech-news-{DATE}.html', 'sports': f'sports-health-{DATE}.html'}

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · {DATE}</title>
<style>
:root{{--c-bg:{bg};--c-surface:{surface};--c-card:{card_bg};--c-border:{border};--c-text:{text};--c-text-dim:{text_dim};--c-accent:{accent};--c-accent2:{accent2};--c-accent-glow:rgba({accent_rgb},0.18);{tag_css}--c-grad-start:{grad[0]};--c-grad-mid:{grad[1]};--c-grad-end:{grad[2]};--radius:14px;--radius-sm:8px;--transition:0.28s cubic-bezier(0.4,0,0.2,1);--font-mono:'SF Mono','Cascadia Code','Consolas','Menlo',monospace;--font-sans:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei','Helvetica Neue',sans-serif}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:var(--font-sans);background:var(--c-bg);color:var(--c-text);line-height:1.6;min-height:100vh;-webkit-font-smoothing:antialiased}}
a{{color:inherit;text-decoration:none}}
.hero{{position:relative;background:linear-gradient(135deg,var(--c-grad-start),var(--c-grad-mid) 50%,var(--c-grad-end));padding:60px 24px 56px;text-align:center;overflow:hidden}}
.hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,0.08),transparent 60%),radial-gradient(circle at 70% 80%,rgba({accent_rgb},0.12),transparent 50%)}}
.hero-date{{position:relative;font-size:15px;font-weight:500;color:rgba(255,255,255,0.75);letter-spacing:0.06em;margin-bottom:8px}}
.hero-title{{position:relative;font-size:clamp(32px,6vw,52px);font-weight:800;letter-spacing:-0.02em;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,0.25)}}
.hero-total{{position:relative;display:inline-block;margin-top:12px;font-size:13px;font-weight:500;background:rgba(255,255,255,0.15);backdrop-filter:blur(6px);padding:6px 18px;border-radius:20px;color:rgba(255,255,255,0.9)}}
.stats-wrap{{position:relative;margin-top:-28px;padding:0 16px;z-index:2}}
.stats{{max-width:900px;margin:0 auto;display:flex;flex-wrap:wrap;gap:10px;justify-content:center;background:var(--c-surface);border:1px solid var(--c-border);border-radius:var(--radius);padding:18px 20px;box-shadow:0 2px 12px rgba(0,0,0,0.25)}}
.stat{{display:flex;align-items:center;gap:7px;font-size:14px;color:var(--c-text-dim)}}
.stat-dot{{width:10px;height:10px;border-radius:50%;flex-shrink:0}}
.stat strong{{color:var(--c-text);font-weight:600}}
.nav-wrap{{position:sticky;top:0;z-index:10;background:rgba({bg_rgb},0.92);backdrop-filter:blur(16px);border-bottom:1px solid var(--c-border);padding:0 16px}}
.nav{{max-width:900px;margin:0 auto;display:flex;gap:4px;overflow-x:auto;padding:10px 0;scrollbar-width:none}}
.nav::-webkit-scrollbar{{display:none}}
.nav a{{display:flex;align-items:center;gap:5px;padding:8px 16px;border-radius:20px;font-size:13px;font-weight:500;white-space:nowrap;color:var(--c-text-dim);transition:var(--transition)}}
.nav a:hover{{color:var(--c-text);background:var(--c-card)}}
.nav a .nav-count{{font-size:11px;background:var(--c-border);padding:1px 7px;border-radius:10px;color:var(--c-text-dim)}}
.main{{max-width:900px;margin:0 auto;padding:32px 16px 60px}}
.section{{margin-bottom:40px}}
.section-header{{display:flex;align-items:center;gap:10px;margin-bottom:18px;padding-bottom:10px;border-bottom:2px solid var(--c-border)}}
.section-badge{{font-size:11px;font-weight:700;letter-spacing:0.04em;padding:4px 12px;border-radius:4px;text-transform:uppercase;color:#fff}}
.section-header h2{{font-size:20px;font-weight:700;color:var(--c-text)}}
.section-count{{font-size:13px;color:var(--c-text-dim);margin-left:auto}}
{badge_css}
.cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}}
.card{{background:var(--c-card);border:1px solid var(--c-border);border-radius:var(--radius);padding:18px;display:flex;flex-direction:column;gap:10px;transition:transform var(--transition),box-shadow var(--transition);position:relative;overflow:hidden}}
.card:hover{{transform:translateY(-2px);box-shadow:0 8px 28px rgba(0,0,0,0.35);border-color:var(--c-accent)}}
.card::after{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--c-accent),var(--c-accent2));opacity:0;transition:opacity var(--transition)}}
.card:hover::after{{opacity:1}}
.card-top{{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}}
.card-num{{font-family:var(--font-mono);font-size:12px;font-weight:700;color:var(--c-accent);background:var(--c-accent-glow);padding:2px 10px;border-radius:var(--radius-sm);flex-shrink:0}}
.card-source{{font-size:11px;font-weight:500;padding:3px 10px;border-radius:12px;background:rgba(255,255,255,0.06);color:var(--c-text-dim);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:160px}}
.card-title{{font-size:15px;font-weight:700;line-height:1.45;color:var(--c-text);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}
.card-summary{{font-size:13px;line-height:1.55;color:var(--c-text-dim);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}
.card-actions{{display:flex;align-items:center;gap:8px;margin-top:auto}}
.card-link{{margin-left:auto;font-size:12px;font-weight:600;color:var(--c-accent2);padding:5px 14px;border:1px solid rgba({accent2_rgb},0.3);border-radius:var(--radius-sm);transition:var(--transition);display:inline-flex;align-items:center;gap:4px}}
.card-link:hover{{background:var(--c-accent);color:#fff;border-color:var(--c-accent)}}
.card-link svg{{width:14px;height:14px;flex-shrink:0}}
.card-animate{{opacity:0;transform:translateY(24px);transition:opacity 0.5s ease,transform 0.5s ease}}
.card-animate.visible{{opacity:1;transform:translateY(0)}}
.footer{{text-align:center;padding:24px 16px 40px;font-size:12px;color:var(--c-text-dim);opacity:0.6;border-top:1px solid var(--c-border)}}
.footer a{{color:var(--c-accent2)}}
@media(max-width:600px){{.hero{{padding:44px 16px 40px}}.cards{{grid-template-columns:1fr}}.stats{{gap:6px;padding:14px}}.stat{{font-size:12px}}.nav a{{padding:6px 12px;font-size:12px}}}}
</style>
</head>
<body>
{hero}
{stats_block}
{nav}
<main class="main">
{sections_html}
</main>
{footer}
<script>
(function(){{var o=new IntersectionObserver(function(e){{e.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('visible');o.unobserve(e.target)}}}})}},{{threshold:0.15}});document.querySelectorAll('.card-animate').forEach(function(c){{o.observe(c)}})}})();
</script>
</body>
</html>"""

    fn = file_map[report_key]
    fp = os.path.join(BASE, fn)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
    sz = os.path.getsize(fp)
    print(f"[OK] {fn}: {total_count} items ({sz:,} bytes)")
    return total_count

# Generate all
counts = {}
for key in ['ai', 'world', 'tech', 'sports']:
    counts[key] = generate_html(key, data[key])

print(f"\n=== Summary: AI={counts['ai']} | World={counts['world']} | Tech={counts['tech']} | Sports={counts['sports']} | Total={sum(counts.values())}")
