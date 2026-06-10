# -*- coding: utf-8 -*-
"""Generate all 5 daily report HTML files for 2026-06-08"""
import os

DATE = "2026-06-08"
DATE_CN = "2026 年 6 月 8 日"
WEEKDAY = "星期一"
BASE = r"C:\Users\Wu Shanchi\WorkBuddy\2026-05-22-AI news"

SVG_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>'

def card(num, title, source, summary, link):
    return f'''<div class="card card-animate">
  <div class="card-top">
    <span class="card-num">#{num:02d}</span>
    <span class="card-source">{source}</span>
  </div>
  <div class="card-title">{title}</div>
  <div class="card-summary">{summary}</div>
  <div class="card-actions">
    <a class="card-link" href="{link}" target="_blank" rel="noopener noreferrer">
      阅读原文 {SVG_ICON}
    </a>
  </div>
</div>'''

def section(sec_id, badge, badge_cls, emoji, title, count, cards_html):
    return f'''<section class="section" id="{sec_id}">
  <div class="section-header">
    <span class="section-badge {badge_cls}">{badge}</span>
    <h2>{emoji} {title}</h2>
    <span class="section-count">{count} 条</span>
  </div>
  <div class="cards">
{cards_html}
  </div>
</section>'''

def stats_html(items):
    parts = []
    for label, count, color_var in items:
        parts.append(f'<div class="stat"><span class="stat-dot" style="background:var({color_var})"></span> {label} <strong>{count}</strong></div>')
    return '\n    '.join(parts)

def nav_html(items):
    parts = []
    for href, label, count in items:
        parts.append(f'<a href="#{href}"><span>{label}</span><span class="nav-count">{count}</span></a>')
    return '\n  '.join(parts)

def build_html(theme, title_text, total, stat_items, nav_items, sections_html, footer_html):
    accent = theme["accent"]
    accent2 = theme["accent2"]
    bg = theme["bg"]
    surface = theme["surface"]
    card_bg = theme["card"]
    border = theme["border"]
    text = theme["text"]
    text_dim = theme["text_dim"]
    grad = theme["grad"]
    accent_glow = theme.get("accent_glow", f"rgba({accent[1:]},0.18)")
    
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_text} · {DATE}</title>
<style>
:root{{--c-bg:{bg};--c-surface:{surface};--c-card:{card_bg};--c-border:{border};--c-text:{text};--c-text-dim:{text_dim};--c-accent:{accent};--c-accent2:{accent2};--c-accent-glow:{accent_glow};--c-grad-start:{grad[0]};--c-grad-mid:{grad[1]};--c-grad-end:{grad[2]};--radius:14px;--radius-sm:8px;--transition:0.28s cubic-bezier(0.4,0,0.2,1);--font-mono:'SF Mono','Cascadia Code','Consolas','Menlo',monospace;--font-sans:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei','Helvetica Neue',sans-serif}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:var(--font-sans);background:var(--c-bg);color:var(--c-text);line-height:1.6;min-height:100vh;-webkit-font-smoothing:antialiased}}
a{{color:inherit;text-decoration:none}}
.hero{{position:relative;background:linear-gradient(135deg,var(--c-grad-start),var(--c-grad-mid) 50%,var(--c-grad-end));padding:60px 24px 56px;text-align:center;overflow:hidden}}
.hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,0.08),transparent 60%),radial-gradient(circle at 70% 80%,rgba({accent[1:]},0.12),transparent 50%)}}
.hero-date{{position:relative;font-size:15px;font-weight:500;color:rgba(255,255,255,0.75);letter-spacing:0.06em;margin-bottom:8px}}
.hero-title{{position:relative;font-size:clamp(32px,6vw,52px);font-weight:800;letter-spacing:-0.02em;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,0.25)}}
.hero-total{{position:relative;display:inline-block;margin-top:12px;font-size:13px;font-weight:500;background:rgba(255,255,255,0.15);backdrop-filter:blur(6px);padding:6px 18px;border-radius:20px;color:rgba(255,255,255,0.9)}}
.stats-wrap{{position:relative;margin-top:-28px;padding:0 16px;z-index:2}}
.stats{{max-width:900px;margin:0 auto;display:flex;flex-wrap:wrap;gap:10px;justify-content:center;background:var(--c-surface);border:1px solid var(--c-border);border-radius:var(--radius);padding:18px 20px;box-shadow:0 2px 12px rgba(0,0,0,0.25)}}
.stat{{display:flex;align-items:center;gap:7px;font-size:14px;color:var(--c-text-dim)}}
.stat-dot{{width:10px;height:10px;border-radius:50%;flex-shrink:0}}
.stat strong{{color:var(--c-text);font-weight:600}}
.nav-wrap{{position:sticky;top:0;z-index:10;background:rgba({bg[1:]},0.92);backdrop-filter:blur(16px);border-bottom:1px solid var(--c-border);padding:0 16px}}
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
.card-link{{margin-left:auto;font-size:12px;font-weight:600;color:var(--c-accent2);padding:5px 14px;border:1px solid rgba({accent2[1:]},0.3);border-radius:var(--radius-sm);transition:var(--transition);display:inline-flex;align-items:center;gap:4px}}
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
<header class="hero">
  <div class="hero-date">{DATE_CN} · {WEEKDAY}</div>
  <h1 class="hero-title">{title_text}</h1>
  <div class="hero-total">今日 {total} 条 · 北京时间 08:50 生成</div>
</header>
<div class="stats-wrap">
  <div class="stats">
    {stats_html(stat_items)}
  </div>
</div>
<nav class="nav-wrap"><div class="nav">
  {nav_html(nav_items)}
</div></nav>
<main class="main">
{sections_html}
</main>
<footer class="footer">
  {footer_html}
</footer>
<script>
const obs = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{ if (e.isIntersecting) {{ e.target.classList.add('visible'); obs.unobserve(e.target); }} }});
}}, {{ threshold: 0.1 }});
document.querySelectorAll('.card-animate').forEach(c => obs.observe(c));
</script>
</body>
</html>'''

# ===================== 1. AI 晨报 =====================
ai_theme = {
    "accent": "#ff6a3d", "accent2": "#ff8c5a",
    "bg": "#0f0c0a", "surface": "#1a1410", "card": "#221a14",
    "border": "#3a2a1e", "text": "#f0e6dc", "text_dim": "#a89880",
    "grad": ["#ff5c28", "#e8452e", "#c8203a"],
    "accent_glow": "rgba(255,106,61,0.18)"
}

ai_sections_data = [
    ("models", "MODELS", "badge-models", "🤖", "模型发布 / 更新", [
        ["Gemini 3.5 Pro 六月发布窗口开启", "Google I/O", "谷歌确认Gemini 3.5 Pro将于6月发布，已发布Flash版得分55超Claude，输出284t/s是竞品4倍，定价$1.5/$9。", "https://memeburn.com/gemini-3-5-flash-vs-claude-gpt-pricing/"],
        ["六月模型发布地图：已确认与传闻全览", "WaveSpeed", "已确认：Gemini 3.5 Flash/Claude Opus 4.8/GPT-5.5/Grok 4.3；传闻：Claude Sonnet 4.8/Gemini 3.5 Pro；训练中：Grok 5/GPT-5.6。", "https://wavespeed.ai/blog/posts/june-2026-ai-launch-wave/"],
        ["微软Majorana 2量子芯片可靠性提升1000倍", "Microsoft Build", "微软Build 2026宣布Majorana 2量子芯片可靠性比前代提升1000倍，使用拓扑量子比特，定位Azure为量子-AI混合工作负载首选云平台。", "https://www.aguidetocloud.com/blog/microsoft-build-2026-recap/"],
    ]),
    ("products", "PRODUCTS", "badge-products", "🚀", "产品发布 / 更新", [
        ["Apple WWDC 2026：Gemini驱动全新Siri+iOS 27发布", "Bloomberg", "Tim Cook最后一次WWDC主题演讲，全新Siri由1.2万亿参数Gemini模型驱动，iOS 27 Beta当天开放，iPhone 12及以上支持。", "https://www.36kr.com/p/3842589800499716"],
        ["Apple每年10亿美元Gemini授权战略揭秘", "Bloomberg", "Apple以约10亿美元/年向谷歌授权Gemini模型，而非自建大模型。隐私架构上Gemini推理运行在Apple私有云计算，非谷歌基础设施。", "https://aitoolsrecap.com/Blog/apple-wwdc-2026-gemini-siri-ios-27-tim-cook-final-keynote"],
        ["Claude成为iPhone选项——触达22亿台设备", "Anthropic", "Claude正式成为Apple Intelligence的AI选项之一，用户可在写作/研究/跨应用任务中使用Claude语音和人格，即使5%用户选择也将超1亿新用户。", "https://www.buildfastwithai.com/blogs/ai-news-today-june-8-2026"],
        ["Claude合作伙伴中心发布——1亿美元企业计划", "Anthropic", "Anthropic正式推出Claude合作伙伴中心和服务轨道，将1亿美元合作伙伴计划正式化，面向系统集成商和咨询公司。", "https://releasebot.io/updates/anthropic"],
        ["微软Foundry：11,000+模型，Claude进入Excel Agent", "Microsoft Build", "Foundry模型目录已含11,000+模型，Claude Opus 4.8进入Foundry并扩展至Copilot Researcher/Studio，新增Excel Agent模式——7.5亿用户直接调用Claude。", "https://www.aguidetocloud.com/blog/microsoft-build-2026-recap/"],
        ["ChatGPT应用全面重新设计，集成Canva和Booking.com", "Tech in Asia", "OpenAI对ChatGPT应用进行重大重新设计，将第三方应用直接嵌入界面，初始合作Canva和Booking.com，标志从对话界面转向综合平台。", "https://www.techinasia.com/news/openai-plans-broader-chatgpt-app-redesign"],
        ["MemPalace成为性能最佳开源AI记忆系统", "GitHub Trending", "高性能开源AI记忆系统MemPalace发布，在最新基准评估中位居榜首，完全免费，为AI Agent和长上下文应用提供强大方案。", "https://github.com/MemPalace/mempalace"],
    ]),
    ("industry", "INDUSTRY", "badge-industry", "🌍", "行业动态", [
        ["AI聊天机器人市场份额：ChatGPT 54.7%，Claude增306%", "Momentic", "ChatGPT以54.7%领先但较去年76.5%下降，Gemini 27.4%第二，Claude份额8.2%但单季增长306%，DeepSeek 4.1%，Grok 2.8%。", "https://momenticmarketing.com/blog/top-ai-chatbots"],
        ["SpaceX IPO距定价仅3天，目标1.75万亿美元", "Goldman Sachs", "SpaceX将于6月11日定价，6月12日纳斯达克上市代码SPCX，融资750亿美元，30%流通股分配散户，xAI部门2025年营收32亿美元但消耗140亿现金。", "https://finance.sina.com.cn/stock/usstock/summary/2026-06-04/doc-iniaeiyh0683659.shtml"],
        ["AI API定价战：2026年6月前沿模型对比", "Memeburn", "GPT-5.5 $1.5/$9，Opus 4.8 $5/$25(Fast Mode约3倍便宜)，Gemini 3.5 Flash $1.5/$9，Grok 4.3 $0.5/$2(有补贴)。Anthropic Fast Mode被认为最具创新定价策略。", "https://memeburn.com/gemini-3-5-flash-vs-claude-gpt-pricing/"],
        ["AI市值记分卡：IPO浪潮中各公司估值", "Goldman Sachs", "SpaceX目标1.75万亿，Anthropic 9650亿，OpenAI 7300-8500亿，高盛预测2026年IPO总融资额可达1600亿美元，三家公司合计超4万亿。", "https://www.buildfastwithai.com/blogs/ai-news-today-june-8-2026"],
        ["五角大楼AI竞赛：测试OpenAI/谷歌替代Claude", "Google AI Weekly", "五角大楼测试OpenAI和谷歌AI模型替代Claude用于机密军事系统。Claude Mythos在网络安全领域信誉强，但拒绝武器系统分析，OpenAI和谷歌更宽松。", "https://www.buildfastwithai.com/blogs/ai-news-today-june-8-2026"],
        ["CDT报告：37种操纵性暗模式存在于ChatGPT/Claude/Gemini", "CDT", "民主与技术中心在三大AI产品中识别37种操纵性暗模式，包括参与度最大化、情感依赖培养、能力欺骗和摩擦不对称，部分可能违反EU AI Act。", "https://www.buildfastwithai.com/blogs/ai-news-today-june-8-2026"],
        ["Token末日：AI公司在IPO前纷纷涨价", "TechCrunch", "AI行业面临Tokenpocalypse经济格局转变，主要公司进一步提高服务价格，与从私营转向上市公司战略密切相关，重心转向财务可持续性。", "https://techcrunch.com/2026/06/07/is-this-the-dawn-of-the-tokenpocalypse/"],
        ["科罗拉多AI法案22天倒计时+欧盟AI法案55天倒计时", "Colorado/EU", "科罗拉多消费者AI保护法6月30日生效，适用高风险AI系统；欧盟AI法案8月2日生效，最高罚款3500万欧元或全球年营业额7%。", "https://www.buildfastwithai.com/blogs/ai-news-today-june-8-2026"],
    ]),
    ("paper", "PAPERS", "badge-paper", "📄", "论文研究", [
        ["LARYBench：具身动作表示的ImageNet时刻", "美团技术", "美团推出LARYBench基准评估通用潜在动作表示，发现通用视觉模型在动作泛化和控制精度上显著优于专业模型，具身动作可从大规模人类视频数据涌现。", "https://tech.meituan.com/2026/04/27/LongCat-LARYBench.html"],
        ["LongCat-AudioDiT：零样本TTS声音克隆", "美团技术", "美团LongCat团队发布AudioDiT，放弃传统Mel频谱图直接在波形潜空间用扩散框架运行，消除多阶段级联误差，实现更高保真声音克隆。", "https://tech.meituan.com/2026/04/20/LongCat-AudioDiT.html"],
        ["General 365：严格AI推理新基准", "美团技术", "美团发布General 365基准，对26个主流模型评估显示最强Gemini 3 Pro仅62.8%，多数未达60%及格线，揭示复杂推理仍是AI重大挑战。", "https://tech.meituan.com/2026/05/15/LongCat-General-365.html"],
        ["挑战拟人化：如果LLM有类人属性，帝国时代II也应如此", "arXiv", "研究者挑战AI拟人化倾向，通过在帝国时代II上训练简单网络，论证道德感或语言理解在经验上并非LLM独有，呼吁建立非唯一性零假设。", "https://arxiv.org/abs/2605.31514"],
    ]),
    ("tip", "TIPS", "badge-tip", "💡", "技巧与观点", [
        ["美团31万行代码重构的Agent评估策略", "美团技术", "美团披露AI驱动开发管理框架，31万行代码重构中AI生成超90%代码，核心挑战从提升生成速度转为实施有效约束，采用Agent评估+Pre-PR机制。", "https://tech.meituan.com/2026/05/07/Agent-AI-Coding.html"],
        ["实施自动化怀疑：AI辅助开发可信度新框架", "Hacker News", "开发者提出自动化怀疑方法论，放弃对LLM盲目依赖，使用专门子Agent（架构师/验证器/假设挖掘器）在设计阶段前置审查，识别规范缺陷。", "https://www.alexself.dev/blog/automated-doubt"],
        ["Notion恢复Anthropic AI访问，凸显第三方AI依赖", "TechCrunch", "Notion在服务中断后恢复Anthropic AI模型访问，事件引发社交媒体广泛关注，凸显生产力软件生态系统对第三方AI集成的高度依赖。", "https://techcrunch.com/2026/06/07/notion-restores-access-to-anthropic-after-service-disruption/"],
        ["OpenAI转向超级应用：Chat is dead", "TechCrunch", "OpenAI正开发超级应用标志重大战略转型，一位高级员工称Chat is dead，暗示正超越传统对话界面转向综合多功能平台生态系统。", "https://techcrunch.com/2026/06/07/openai-is-still-working-on-that-super-app/"],
    ]),
]

# Build AI morning HTML
num = 0
ai_section_tags = {}
ai_total = 0
ai_sections_html = ""
ai_stat_items = []
ai_nav_items = []
tag_colors = {"models": "#e85d3a", "products": "#f08c4a", "industry": "#d4a24e", "paper": "#c07a5e", "tip": "#b8956e"}
stat_names = {"models": "模型", "products": "产品", "industry": "行业", "paper": "论文", "tip": "观点"}
section_emojis = {"models": "🤖", "products": "🚀", "industry": "🌍", "paper": "📄", "tip": "💡"}
section_badges = {"models": "MODELS", "products": "PRODUCTS", "industry": "INDUSTRY", "paper": "PAPERS", "tip": "TIPS"}

for entry in ai_sections_data:
    sec_id, badge, badge_cls, emoji, title, items_data = entry
    cards = []
    for item in items_data:
        num += 1
        cards.append(card(num, item[0], item[1], item[2], item[3]))
    cnt = len(items_data)
    ai_total += cnt
    ai_section_tags[sec_id] = cnt
    cards_str = '\n'.join(cards)
    badge_cls = f"badge-{sec_id}"
    ai_sections_html += section(sec_id, section_badges[sec_id], badge_cls, section_emojis[sec_id], stat_names[sec_id] + "发布 / 更新" if sec_id == "models" else ("产品发布 / 更新" if sec_id == "products" else stat_names[sec_id]), cnt, cards_str) + '\n'
    ai_stat_items.append((stat_names[sec_id], cnt, f"--c-tag-{sec_id}"))
    ai_nav_items.append((sec_id, f"{section_emojis[sec_id]} {stat_names[sec_id]}", cnt))

# Fix section titles
ai_sections_html = ai_sections_html.replace('行业发布 / 更新', '行业动态').replace('论文发布 / 更新', '论文研究').replace('观点发布 / 更新', '技巧与观点')

ai_footer = '数据来源：<a href="https://aihot.virxact.com" target="_blank" rel="noopener noreferrer">aihot.virxact.com</a> · AI HOT 每日聚合 + BuildFastWithAI / AIToolly 多源补充'

# Add badge CSS
badge_css = "".join([f".badge-{k}{{background:{v}}}" for k, v in tag_colors.items()])

ai_html = build_html(ai_theme, "AI 晨报", ai_total, ai_stat_items, ai_nav_items, ai_sections_html, ai_footer)
ai_html = ai_html.replace('.section-badge{', badge_css + '\n.section-badge{')

with open(os.path.join(BASE, f"ai-morning-{DATE}.html"), "w", encoding="utf-8") as f:
    f.write(ai_html)
print(f"✅ ai-morning-{DATE}.html ({ai_total}条)")

# ===================== 2. 国际焦点 =====================
world_theme = {
    "accent": "#3b82f6", "accent2": "#60a5fa",
    "bg": "#0a0f1a", "surface": "#101828", "card": "#182030",
    "border": "#1e3a5f", "text": "#e0e8f0", "text_dim": "#8899aa",
    "grad": ["#1e40af", "#2563eb", "#1d4ed8"],
    "accent_glow": "rgba(59,130,246,0.18)"
}

world_sections_data = [
    ("politics", "POLITICS", "🏛️", "政治外交", [
        ["伊朗以色列互射导弹，中东停火协议面临破裂", "NPR / France24", "以色列和伊朗自4月停火以来首次交换导弹火力，伊朗宣布停止打击但威胁若再次遭袭将扩大至地区所有美以目标。", "https://www.wlrn.org/npr-breaking-news/2026-06-08/israel-and-iran-exchange-missile-fire-threatening-middle-east-truce"],
        ["特朗普称内塔尼亚胡别无选择只能接受美伊协议", "Sina Finance", "特朗普表示伊朗袭击以色列不会影响美伊谈判进程，若谈判失败可能考虑对伊朗发动突袭，伊朗宣布对霍尔木兹海峡通行船只收费150-200万美元。", "https://finance.sina.com.cn/headline/2026-06-08/doc-iniarzha4036620.shtml"],
        ["乌克兰泽连斯基愿冻结当前战线以结束战争", "Livemint / AP", "乌克兰总统泽连斯基表示愿意以冻结当前战线方式推动停战，确认俄罗斯富豪阿布拉莫维奇曾充当双方信使传递普京信息。", "https://www.livemint.com/news/world/total-world-latest-news-on-june-8-2026-live-updates-11780864332311.html"],
        ["G7峰会6月15-17日将在法国依云举行", "Élysée", "2026年G7峰会将于6月15-17日在法国依云举行，面临中东局势骤然升级、霍尔木兹海峡危机等复杂背景。", "https://www.elysee.fr/en/G7evian"],
        ["英国计划削减医院和学校资金增加国防预算", "Livemint", "英国政府计划削减医院和学校资金投入，将资源重新分配至国防预算，引发广泛关注。", "https://www.livemint.com/news/world/total-world-latest-news-on-june-8-2026-live-updates-11780864332311.html"],
        ["以色列情报机构被曝监听美方谈判人员", "Sina Finance", "美国五角大楼报告指出以色列情报机构持续监听负责斡旋美伊和平协议的美方谈判人员，反间谍风险已从高风险上调至危急级别。", "https://finance.sina.com.cn/headline/2026-06-07/doc-iniapryu1212724.shtml"],
        ["伊朗宣布停止对以色列打击", "France24 / Yahoo", "伊朗军方宣布停止对以色列的袭击，此前以色列袭击了伊朗中西部地区，特朗普敦促立即停止打击。", "https://www.france24.com/en/middle-east/20260608-middle-east-war-live-israel-plans-to-strike-iran-with-force-once-given-green-light"],
    ]),
    ("economy", "ECONOMY", "💰", "经济财经", [
        ["日本Q1 GDP年率增长1.8%超预期", "Sina Finance", "日本2026年Q1折合年率增长1.8%，超过预估1.4%；名义GDP环比增长0.6%，实际GDP环比增长0.5%均超预期。", "https://finance.sina.com.cn/headline/2026-06-08/doc-iniarzha4036620.shtml"],
        ["黄金突破4340美元/盎司，地缘紧张推升避险", "Sina Finance", "现货黄金突破4340美元/盎司涨0.29%，纽约期金一度失守4340后反弹突破4360，中东局势持续推升避险需求。", "https://finance.sina.com.cn/headline/2026-06-08/doc-iniarzha4036620.shtml"],
        ["以太坊突破1700美元涨8.42%，比特币突破63000美元", "Sina Finance", "加密市场大涨，以太坊突破1700美元日内涨8.42%，比特币突破63000美元涨3.64%，市场风险偏好回升。", "https://finance.sina.com.cn/headline/2026-06-08/doc-iniarzha4036620.shtml"],
        ["布伦特原油触及96.47美元/桶，中东局势推升", "CNBC / Sina", "伊朗向以色列发射导弹后布伦特原油最高触及96.47美元涨3.6%，WTI涨3%报93.28美元，特朗普表态后涨幅收窄。", "https://www.cnbc.com/2026/06/08/earthquake-of-magnitude-7point8-strikes-off-southern-philippines-tsunami-warnings-issued.html"],
        ["美股期货下跌，标普500期货跌0.1%", "Sina Finance", "中东冲突升级下美股期货承压，标普500期货最大跌幅0.6%后收窄至0.1%，纳斯达克100期货跌超0.3%。", "https://finance.sina.com.cn/headline/2026-06-08/doc-iniarzha4036620.shtml"],
    ]),
    ("major", "MAJOR", "⚡", "重大事件", [
        ["菲律宾棉兰老岛7.8级地震至少32死200余伤", "Xinhua / CNBC", "菲律宾棉兰老岛海域7.8级地震震源深度15公里，已致32死200余伤，触发海啸预警，为1990年以来最强震。", "http://en.ce.cn/main/latest/202606/t20260608_3017756.shtml"],
        ["SpaceX IPO 6月11日定价，目标1.75万亿美元", "Sina Finance", "SpaceX锁定6月11日定价6月12日上市，发行价135美元，融资750亿美元，将成美国史上最大IPO。", "https://finance.sina.com.cn/stock/usstock/summary/2026-06-04/doc-iniaeiyh0683659.shtml"],
        ["Apple WWDC 2026开幕：Tim Cook最后一次主题演讲", "Bloomberg / 36kr", "Tim Cook发表最后一次WWDC主题演讲，宣布全新Gemini驱动Siri和iOS 27，9月1日将CEO移交John Ternus。", "https://www.36kr.com/p/3842589800499716"],
        ["2026年中国高考开考，多地启用AI智能巡查系统", "Ifeng Tech", "2026年高考7日开考，多地考场投入使用AI智能巡查系统，运用视觉分析算法精准定位考生异常行为，自动标记作弊迹象。", "https://tech.ifeng.com/c/8tkwGQzzD6p"],
        ["联合国：南苏丹数百万人流离失所", "UN Geneva", "联合国报告称南苏丹数月战乱迫使数百万人流离失所，全球肉类供应四倍增长，中东危机加深全球饥饿。", "https://www.ungeneva.org/en/news-media/news-list"],
    ]),
    ("society", "SOCIETY", "🌏", "社会人文", [
        ["中国《科技创新百强指数报告2026》发布", "China Daily", "八月瓜科技创新研究院发布报告，首次将高校和研究机构遴选从TOP50扩展至TOP100，呈现更立体科技创新格局。", "https://cn.chinadaily.com.cn/a/202606/01/WS6a1d0174a310942cc49af438.html"],
        ["美联储政策走向成全球市场焦点", "Sina Finance", "中国人民银行连续两日逆回购零操作后重启2150亿元操作，净投放920亿元，全球关注美联储利率决策走向。", "https://finance.sina.com.cn/stock/y/2026-06-08/doc-iniaruxw9012130.shtml"],
        ["北京榜样2026年5月榜单发布，科技领域多人上榜", "Beijing.gov", "20人当选5月北京榜样，包括人形机器人公司松延动力创始人姜哲源等科技创新领域人物，覆盖面广代表性强。", "https://www.beijing.gov.cn/ywdt/yaowen/202606/t20260608_4690181.html"],
    ]),
]

world_tag_colors = {"politics": "#3b82f6", "economy": "#6366f1", "major": "#ef4444", "society": "#8b5cf6"}
num = 0
world_total = 0
world_sections_html = ""
world_stat_items = []
world_nav_items = []

for sec_id, badge, emoji, title, items_data in world_sections_data:
    cards = []
    for item in items_data:
        num += 1
        cards.append(card(num, item[0], item[1], item[2], item[3]))
    cnt = len(items_data)
    world_total += cnt
    cards_str = '\n'.join(cards)
    badge_cls = f"badge-{sec_id}"
    world_sections_html += section(sec_id, badge, badge_cls, emoji, title, cnt, cards_str) + '\n'
    world_stat_items.append((title, cnt, f"--c-tag-{sec_id}"))
    world_nav_items.append((sec_id, f"{emoji} {title}", cnt))

world_badge_css = "".join([f".badge-{k}{{background:{v}}}" for k, v in world_tag_colors.items()])
world_footer = '数据来源：Reuters / BBC / NPR / France24 / CNBC / 新华网 / 新浪财经 等公开新闻源'

world_html = build_html(world_theme, "国际焦点日报", world_total, world_stat_items, world_nav_items, world_sections_html, world_footer)
world_html = world_html.replace('.section-badge{', world_badge_css + '\n.section-badge{')

with open(os.path.join(BASE, f"world-news-{DATE}.html"), "w", encoding="utf-8") as f:
    f.write(world_html)
print(f"✅ world-news-{DATE}.html ({world_total}条)")

# ===================== 3. 科技日报 =====================
tech_theme = {
    "accent": "#10b981", "accent2": "#34d399",
    "bg": "#0a120e", "surface": "#101a14", "card": "#18241c",
    "border": "#1e3a2a", "text": "#dce8e0", "text_dim": "#88aa90",
    "grad": ["#065f46", "#059669", "#047857"],
    "accent_glow": "rgba(16,185,129,0.18)"
}

tech_sections_data = [
    ("internet", "INTERNET", "🌐", "互联网 / 软件", [
        ["Apple WWDC 2026：Gemini驱动Siri+iOS 27发布", "Bloomberg / 36氪", "Tim Cook最后一次WWDC演讲，全新Siri由1.2万亿参数Gemini驱动，iOS 27 Beta当天开放，苹果Apple Glasses AR眼镜85g售价$2999。", "https://www.36kr.com/p/3842589800499716"],
        ["ChatGPT应用全面重新设计，集成Canva和Booking.com", "Tech in Asia", "OpenAI对ChatGPT应用重大重新设计，将第三方应用直接嵌入界面，初始合作Canva和Booking.com，从对话界面转向综合平台。", "https://www.techinasia.com/news/openai-plans-broader-chatgpt-app-redesign"],
        ["百度文心一言5.0：1.2万亿MoE中文超越GPT-4", "腾讯云开发者", "文心一言5.0采用1.2万亿MoE架构，中文基准CLUE+得分93.7%超GPT-4的92.1%，API定价¥0.08/千tokens为GPT-4-turbo的1/20。", "https://cloud.tencent.com/developer/article/2684137"],
        ["谷歌Gemini 3.0：80%端侧推理，脱离云端依赖", "腾讯云开发者", "首个将80%推理负载移至端侧的旗舰模型，基于TensorSoC Gen3功耗仅5W可在Pixel 11运行70B模型，支持127种语言实时翻译。", "https://cloud.tencent.com/developer/article/2684137"],
        ["OpenAI GPT-5 Preview：GPQA推理88.7%", "腾讯云开发者", "GPT-5 Preview面向开发者早期预览，GPQA推理88.7%超GPT-4的63.2%，新增Active Reasoning可自主回溯，传闻上下文16M tokens。", "https://cloud.tencent.com/developer/article/2684137"],
    ]),
    ("hardware", "HARDWARE", "🔧", "硬件 / 半导体", [
        ["英伟达Rubin架构GPU：2nm工艺5 PFLOPS FP8", "Computex 2026", "基于台积电2nm N2工艺，单GPU FP8算力5 PFLOPS，288GB HBM4带宽8TB/s，Rubin Ultra双晶粒10 PFLOPS，算力密度较H100提升10倍。", "https://cloud.tencent.com/developer/article/2684137"],
        ["台积电2nm N2量产：良率85%超越预期", "腾讯云开发者", "2nm工艺正式量产首批良率85%超N3/N5同期，逻辑密度提升15%速度提升12%功耗降25-30%，首批客户苹果/英伟达/AMD/高通/联发科。", "https://cloud.tencent.com/developer/article/2684137"],
        ["三星晶圆代工Q3恢复盈利，2nm良率突破60%", "Tech in Asia", "三星晶圆代工预计Q3恢复盈利，Q1 2nm芯片良率突破60%，标志下一代半导体制造工艺稳定化。", "https://www.techinasia.com/news/samsung-foundry-return-profit-q3-2026"],
        ["NVIDIA Vera CPU采用SK Hynix内存，专为AI Agent设计", "Tech in Asia", "英伟达CEO确认Vera CPU将使用SK Hynix内存，计划秋季在合作伙伴系统中首发，标志向专用AI Agent硅芯片战略转型。", "https://www.techinasia.com/news/nvidia-ceo-vera-cpu-sk-hynix-memory"],
        ["NVIDIA与SK Hynix多年战略合作推进AI工厂内存", "NVIDIA Newsroom", "NVIDIA与SK Hynix签署多年技术合作协议，推进下一代内存技术并加速半导体设计与制造，为AI基础设施提供核心硬件支撑。", "https://nvidianews.nvidia.com/news/sk-hynix-ai-factory"],
    ]),
    ("space", "SPACE", "🚀", "航天 / 新能源", [
        ["SpaceX IPO 6月11日定价，目标1.75万亿美元", "Sina Finance", "SpaceX锁定6月11日定价6月12日纳斯达克上市，发行价135美元融资750亿美元，30%流通股分配散户，将成美国史上最大IPO。", "https://finance.sina.com.cn/stock/usstock/summary/2026-06-04/doc-iniaeiyh0683659.shtml"],
        ["华为×比亚迪璇玑智能座舱：鸿蒙5.0+L4自驾", "腾讯云开发者", "深度整合鸿蒙座舱5.0与比亚迪L4自驾方案，搭载昇腾920芯片自驾算力1200 TOPS，无高精地图依赖复杂路口通过率99.7%。", "https://cloud.tencent.com/developer/article/2684137"],
        ["NVIDIA与斗山集团合作推进物理AI与机器人", "NVIDIA Newsroom", "NVIDIA与斗山集团扩大合作，聚焦物理AI、机器人及AI工厂基础设施，涉及斗山机器人/山猫/重工/电子材料等子公司。", "https://blogs.nvidia.com/blog/nvidia-and-doosan-group-physical-ai/"],
        ["NAVER与NVIDIA合作扩展主权AI至吉瓦级", "NVIDIA Newsroom", "NAVER与NVIDIA合作以55MW为起点规划扩展至吉瓦级，借助DSX平台快速部署全栈AI平台，满足企业/工业/政府主权AI需求。", "https://nvidianews.nvidia.com/news/naver-ai-infrastructure"],
        ["NVIDIA与SK Telecom合作建吉瓦级AI云", "NVIDIA Newsroom", "NVIDIA与SK Telecom合作开发吉瓦级AI云，首座AI工厂计划2027年运营，利用DSX平台建设专用AI工厂。", "https://nvidianews.nvidia.com/news/sk-telecom-ai-infrastructure"],
    ]),
    ("digital", "DIGITAL", "💡", "数字创新", [
        ["微软Build 2026：Foundry 11K+模型+Majorana 2量子", "Microsoft", "Build 2026宣布Foundry模型目录11,000+模型，Majorana 2量子芯片可靠性提升1000倍，Claude Opus 4.8进入Excel Agent模式。", "https://www.aguidetocloud.com/blog/microsoft-build-2026-recap/"],
        ["多地高考启用AI智能巡查系统防作弊", "Ifeng Tech", "2026年高考多地考场投入使用AI智能巡查系统，运用视觉分析算法精准定位考生异常行为，自动标记作弊迹象截取录像供审核。", "https://tech.ifeng.com/c/8tkwGQzzD6p"],
        ["万兴科技携万兴剧厂亮相华为云INSPIRE 2026", "Sina Tech", "万兴科技携万兴剧厂亮相华为云INSPIRE 2026，展示AI驱动的视频创作和数字内容生产新方案。", "https://tech.sina.com.cn/roll/"],
        ["《中国新一代AI科技产业发展报告2026》发布", "Sina Finance", "报告显示中国AI企业超6000家核心产业规模突破1.2万亿元，2026年为AI发展转折之年，智能体和具身智能大量走向应用。", "https://finance.sina.com.cn/wm/2026-05-30/doc-inhzsssf8560160.shtml"],
    ]),
]

tech_tag_colors = {"internet": "#10b981", "hardware": "#0ea5e9", "space": "#f59e0b", "digital": "#8b5cf6"}
num = 0
tech_total = 0
tech_sections_html = ""
tech_stat_items = []
tech_nav_items = []

for sec_id, badge, emoji, title, items_data in tech_sections_data:
    cards = []
    for item in items_data:
        num += 1
        cards.append(card(num, item[0], item[1], item[2], item[3]))
    cnt = len(items_data)
    tech_total += cnt
    cards_str = '\n'.join(cards)
    badge_cls = f"badge-{sec_id}"
    tech_sections_html += section(sec_id, badge, badge_cls, emoji, title, cnt, cards_str) + '\n'
    tech_stat_items.append((title, cnt, f"--c-tag-{sec_id}"))
    tech_nav_items.append((sec_id, f"{emoji} {title}", cnt))

tech_badge_css = "".join([f".badge-{k}{{background:{v}}}" for k, v in tech_tag_colors.items()])
tech_footer = '数据来源：TechCrunch / The Verge / 36氪 / IT之家 / NVIDIA Newsroom / 腾讯云开发者 等公开科技媒体'

tech_html = build_html(tech_theme, "科技日报", tech_total, tech_stat_items, tech_nav_items, tech_sections_html, tech_footer)
tech_html = tech_html.replace('.section-badge{', tech_badge_css + '\n.section-badge{')

with open(os.path.join(BASE, f"tech-news-{DATE}.html"), "w", encoding="utf-8") as f:
    f.write(tech_html)
print(f"✅ tech-news-{DATE}.html ({tech_total}条)")

# ===================== 4. 运动健康 =====================
sports_theme = {
    "accent": "#f59e0b", "accent2": "#fbbf24",
    "bg": "#120e06", "surface": "#1a140a", "card": "#241c10",
    "border": "#3a2e18", "text": "#f0e8d0", "text_dim": "#aa9860",
    "grad": ["#b45309", "#d97706", "#f59e0b"],
    "accent_glow": "rgba(245,158,11,0.18)"
}

sports_sections_data = [
    ("sports", "SPORTS", "⚽", "体坛快讯", [
        ["NBA总决赛G3今晚打响：马刺vs尼克斯，尼克斯2-0领先", "ESPN / NBA", "NBA总决赛G3今晚8:30在纽约开战，尼克斯G1以105-95、G2以105-104连赢两场，文班亚马场均27.5分10.5篮板领衔得分榜。", "https://www.espn.com/nba/game/_/gameId/401859965/spurs-knicks"],
        ["NBA总决赛G2：尼克斯105-104险胜马刺", "NBA.com", "尼克斯凭借关键时刻表现以105-104险胜马刺，系列赛2-0领先，唐斯场均19.5分12.5篮板4助攻，文班亚马空砍27+10。", "https://www.nba.com/playoffs/2026/nba-finals"],
        ["2026世界杯6月11日开幕：墨西哥vs南非", "FIFA", "2026世界杯6月11日在墨西哥阿兹特克球场开幕，东道主墨西哥对阵南非，48队104场比赛横跨美加墨三国。", "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/opening-ceremony-mexico"],
        ["法网2026进入决赛周", "ESPN / Roland Garros", "2026年法国网球公开赛进入最后阶段，男女单打决赛即将上演，各路高手争夺罗兰加洛斯冠军。", "https://www.espn.com/tennis/scoreboard/tournament/_/year/2024/eventId/172-2026"],
        ["文班亚马总决赛场均27.5分10.5篮板领衔得分榜", "NBA.com", "马刺球星文班亚马虽球队0-2落后，但个人表现亮眼场均27.5分10.5篮板2助攻，为总决赛得分王。", "https://www.nba.com/playoffs/2026/nba-finals"],
        ["NBA总决赛为世界杯改期，G4提前至6月10日", "Sohu", "NBA将原定6月12日的总决赛G4提前至6月10日周三，为6月11日世界杯开幕让路，体坛赛程协调前所未有。", "https://www.sohu.com/a/1033141974_122404919"],
        ["2026青岛首届全民健身家庭运动会600组家庭参与", "MSN", "青岛妇联和体育局联合主办全民健身家庭运动会，600组家庭约1500人参与，设置运动会、嘉年华和主题讲座。", "https://www.msn.cn/zh-cn/news/other/2026%E5%B9%B4%E9%9D%92%E5%B2%9B%E5%B8%82%E9%A6%96%E5%B1%8A%E5%85%A8%E6%B0%91%E5%81%A5%E8%BA%AB%E5%AE%B6%E5%BA%AD%E8%BF%90%E5%8A%A8%E4%BC%9A%E6%88%90%E5%8A%9F%E4%B8%BE%E5%8A%9E/ar-AA254MfC"],
    ]),
    ("fitness", "FITNESS", "💪", "健身科学", [
        ["ACSM发布2026年全球健身趋势报告", "ACSM / QQ News", "美国运动医学会发布年度全球健身趋势调查，未来健身从一次性项目转向可持续生活策略，可穿戴技术仍居首位。", "https://news.qq.com/rain/a/20251107A05G2A00"],
        ["新型糖尿病药丸可燃烧脂肪，无Ozempic副作用", "ScienceDaily", "实验性糖尿病和肥胖症药丸作用机制与Ozempic完全不同，不抑制食欲而是激活骨骼肌代谢实现燃脂效果。", "https://www.sciencedaily.com/news/health_medicine/"],
        ["迄今最大规模胶原蛋白研究揭示真实效果", "ScienceDaily", "覆盖近8000名参与者的综述显示，持续长期服用胶原蛋白补充剂可改善皮肤健康、缓解骨关节炎症状，对肌肉也有一定益处。", "https://www.sciencedaily.com/news/health_medicine/"],
        ["2026年北京青少年科学健身指导活动启动", "MSN", "北京市体育局主办首场活动1400余人参加，通过科学健身大讲堂、体质测试、新型体育项目体验等形式引导青少年科学健身。", "https://www.msn.cn/zh-cn/sports/%E7%94%B0%E5%BE%84/2026%E5%B9%B4%E5%8C%97%E4%BA%AC%E5%B8%82%E9%9D%92%E5%B0%91%E5%B9%B4%E4%B8%BB%E9%A2%98%E5%81%A5%E8%BA%AB%E6%B4%BB%E5%8A%A8%E5%90%AF%E5%8A%A8-%E9%A6%96%E5%9C%BA%E6%B4%BB%E5%8A%A81400%E4%BD%99%E4%BA%BA%E5%8F%82%E5%8A%A0/ar-AA24D7iB"],
    ]),
    ("nutrition", "NUTRITION", "🥗", "营养饮食", [
        ["饮用水中硝酸盐与痴呆风险相关，蔬菜硝酸盐反降风险", "ScienceDaily", "覆盖5.4万人研究显示硝酸盐来源比摄入量影响更大，每日约1杯菠菜分量的蔬菜硝酸盐反而降低痴呆风险。", "https://www.sciencedaily.com/news/health_medicine/"],
        ["8300名老年人盐摄入习惯与认知下降相关", "ScienceDaily", "巴西大型老年人研究显示用餐时额外加盐习惯在男性中更普遍，过量盐摄入与严重健康问题和认知功能加速下降相关。", "https://www.sciencedaily.com/news/health_medicine/"],
        ["每周3份炸薯条，2型糖尿病风险升高20%", "ScienceDaily", "跟踪20.5万人近40年研究显示，每周吃3份炸薯条2型糖尿病风险升高20%，马铃薯危害主要来自炸薯条烹饪方式。", "https://www.sciencedaily.com/news/health_medicine/"],
        ["GLP-1减肥药与乳腺癌风险降低30%相关", "ScienceDaily", "大型研究显示服用GLP-1类药物（Ozempic/Wegovy/Mounjaro/Zepbound）的女性，乳腺癌患病风险降低约30%。", "https://www.sciencedaily.com/news/health_medicine/"],
    ]),
    ("wellness", "WELLNESS", "🧘", "身心养护", [
        ["科学家修复微小脑回路逆转焦虑", "ScienceDaily", "杏仁核中新发现的神经元是焦虑和社交行为的核心调控因素，恢复该微小脑回路的正常活性可逆转焦虑和社交缺陷。", "https://www.sciencedaily.com/news/health_medicine/"],
        ["AI设计通用冠状病毒疫苗通过首次人体试验", "ScienceDaily", "首次在人体内测试的AI设计的通用冠状病毒疫苗安全性良好，可诱导针对多种冠状病毒的免疫反应。", "https://www.sciencedaily.com/news/health_medicine/"],
        ["科学家攻克不可成药胰腺癌靶点，生存期近乎翻倍", "ScienceDaily", "针对驱动多数胰腺癌的KRAS突变的新药daraxonrasib，有望改变胰腺癌治疗困境，显著延长患者生存期。", "https://www.sciencedaily.com/news/health_medicine/"],
        ["科学家警告：危险阿米巴原虫正全球扩散", "ScienceDaily", "自由生活的阿米巴原虫是未被充分重视的公共卫生威胁，可致致命感染，气候变化和基础设施老化可能加速传播。", "https://www.sciencedaily.com/news/health_medicine/"],
    ]),
]

sports_tag_colors = {"sports": "#f59e0b", "fitness": "#10b981", "nutrition": "#ef4444", "wellness": "#8b5cf6"}
num = 0
sports_total = 0
sports_sections_html = ""
sports_stat_items = []
sports_nav_items = []

for sec_id, badge, emoji, title, items_data in sports_sections_data:
    cards = []
    for item in items_data:
        num += 1
        cards.append(card(num, item[0], item[1], item[2], item[3]))
    cnt = len(items_data)
    sports_total += cnt
    cards_str = '\n'.join(cards)
    badge_cls = f"badge-{sec_id}"
    sports_sections_html += section(sec_id, badge, badge_cls, emoji, title, cnt, cards_str) + '\n'
    sports_stat_items.append((title, cnt, f"--c-tag-{sec_id}"))
    sports_nav_items.append((sec_id, f"{emoji} {title}", cnt))

sports_badge_css = "".join([f".badge-{k}{{background:{v}}}" for k, v in sports_tag_colors.items()])
sports_footer = '数据来源：ESPN / NBA.com / FIFA / ScienceDaily / ACSM / 新浪体育 等公开体育健康媒体'

sports_html = build_html(sports_theme, "运动健康日报", sports_total, sports_stat_items, sports_nav_items, sports_sections_html, sports_footer)
sports_html = sports_html.replace('.section-badge{', sports_badge_css + '\n.section-badge{')

with open(os.path.join(BASE, f"sports-health-{DATE}.html"), "w", encoding="utf-8") as f:
    f.write(sports_html)
print(f"✅ sports-health-{DATE}.html ({sports_total}条)")

# ===================== 5. 公众号适配文章 =====================
wechat_sections = [
    {
        "title": "AI 晨报",
        "color": "#ff6a3d",
        "color2": "#ff8c5a",
        "sub_sections": [
            ("🤖 模型发布", [
                ("Gemini 3.5 Pro 六月发布窗口开启", "Google I/O确认6月发布，Flash版已超Claude得分"),
                ("六月模型发布地图全览", "已确认GPT-5.5/Opus 4.8/Gemini 3.5 Flash，传闻Sonnet 4.8"),
                ("微软Majorana 2量子芯片", "可靠性提升1000倍，定位Azure量子-AI混合云平台"),
            ]),
            ("🚀 产品发布", [
                ("Apple WWDC 2026：Gemini驱动Siri+iOS 27", "Tim Cook最后一次演讲，1.2万亿参数Gemini模型驱动新Siri"),
                ("Claude成为iPhone选项", "触达22亿台设备，5%用户选择即超1亿新用户"),
                ("微软Foundry 11K+模型+Excel Agent", "7.5亿Excel用户可直接调用Claude"),
            ]),
            ("🌍 行业动态", [
                ("AI聊天机器人市场份额", "ChatGPT 54.7%领先，Claude单季增长306%"),
                ("SpaceX IPO 3天倒计时", "6月11日定价，目标1.75万亿美元成美国最大IPO"),
                ("五角大楼AI竞赛", "测试OpenAI/谷歌替代Claude用于军事系统"),
            ]),
            ("📄 论文研究", [
                ("LARYBench具身动作表示基准", "通用视觉模型在动作泛化上显著优于专业模型"),
                ("General 365推理基准", "最强模型仅62.8%，复杂推理仍是AI重大挑战"),
            ]),
            ("💡 技巧与观点", [
                ("美团31万行代码Agent评估", "AI生成超90%代码，核心挑战从速度转为约束"),
                ("OpenAI转向超级应用", "Chat is dead，从对话界面转向综合平台"),
            ]),
        ]
    },
    {
        "title": "国际焦点",
        "color": "#3b82f6",
        "color2": "#60a5fa",
        "sub_sections": [
            ("🏛️ 政治外交", [
                ("伊朗以色列互射导弹", "4月停火以来首次交火，中东局势再度紧张"),
                ("特朗普称内塔尼亚胡须接受美伊协议", "伊朗宣布对霍尔木兹海峡通行船只收费"),
                ("泽连斯基愿冻结战线以结束战争", "确认阿布拉莫维奇曾充当俄乌双方信使"),
            ]),
            ("💰 经济财经", [
                ("日本Q1 GDP年率增长1.8%超预期", "名义和实际GDP均超预期增长"),
                ("布伦特原油触及96.47美元/桶", "中东冲突推升油价，WTI涨3%报93.28美元"),
                ("黄金突破4340美元避险需求升温", "以太坊涨8.42%破1700美元，比特币破63000美元"),
            ]),
            ("⚡ 重大事件", [
                ("菲律宾7.8级地震至少32死", "棉兰老岛海域地震触发海啸预警，1990年以来最强"),
                ("SpaceX IPO 6月11日定价", "融资750亿美元，估值1.75万亿美元成美史上最大IPO"),
                ("2026高考开考启用AI巡查系统", "多地考场运用视觉分析算法精准定位异常行为"),
            ]),
            ("🌏 社会人文", [
                ("科技创新百强指数报告2026发布", "高校和研究机构遴选扩展至TOP100"),
                ("北京榜样5月榜发布", "人形机器人松延动力创始人等科技领域人物上榜"),
            ]),
        ]
    },
    {
        "title": "科技日报",
        "color": "#10b981",
        "color2": "#34d399",
        "sub_sections": [
            ("🌐 互联网/软件", [
                ("Apple WWDC 2026发布iOS 27", "全新Gemini驱动Siri，Apple Glasses AR眼镜85g $2999"),
                ("百度文心一言5.0中文超越GPT-4", "1.2万亿MoE，CLUE+ 93.7%超GPT-4，定价仅1/20"),
                ("谷歌Gemini 3.0 80%端侧推理", "首个将80%推理移至端侧的旗舰模型，功耗仅5W"),
            ]),
            ("🔧 硬件/半导体", [
                ("英伟达Rubin GPU 2nm 5 PFLOPS", "算力密度较H100提升10倍，288GB HBM4带宽8TB/s"),
                ("台积电2nm量产良率85%", "超N3/N5同期，首批客户苹果/英伟达/AMD/高通"),
                ("三星2nm良率突破60%预计Q3盈利", "代工业务走向财务复苏，制造工艺稳定化"),
            ]),
            ("🚀 航天/新能源", [
                ("SpaceX IPO 6月12日上市", "发行价135美元融资750亿美元，将成美国史上最大IPO"),
                ("华为×比亚迪璇玑智能座舱", "鸿蒙5.0+L4自驾，昇腾920芯片1200 TOPS"),
                ("NVIDIA多笔战略合作", "与斗山/SK Hynix/SK Telecom/NAVER推进AI基础设施"),
            ]),
            ("💡 数字创新", [
                ("微软Build 2026 Foundry 11K+模型", "Majorana 2量子芯片+Claude进入Excel Agent"),
                ("高考AI巡查系统防作弊", "视觉分析算法精准定位考生异常行为自动标记"),
            ]),
        ]
    },
    {
        "title": "运动健康",
        "color": "#f59e0b",
        "color2": "#fbbf24",
        "sub_sections": [
            ("⚽ 体坛快讯", [
                ("NBA总决赛G3今晚打响", "尼克斯2-0领先马刺，文班亚马场均27.5分领衔得分榜"),
                ("2026世界杯6月11日开幕", "墨西哥vs南非在阿兹特克球场，48队104场比赛"),
                ("NBA总决赛为世界杯改期", "G4提前至6月10日为世界杯开幕让路"),
            ]),
            ("💪 健身科学", [
                ("ACSM发布2026全球健身趋势", "健身从一次性项目转向可持续生活策略"),
                ("新型糖尿病药丸可燃烧脂肪", "不抑制食欲而是激活骨骼肌代谢，无Ozempic副作用"),
                ("最大规模胶原蛋白研究", "长期服用可改善皮肤和骨关节炎，覆盖8000人"),
            ]),
            ("🥗 营养饮食", [
                ("饮用水硝酸盐与痴呆风险相关", "5.4万人研究显示蔬菜硝酸盐反而降低痴呆风险"),
                ("每周3份炸薯条糖尿病风险升20%", "20.5万人近40年跟踪，危害主要来自烹饪方式"),
                ("GLP-1减肥药与乳腺癌风险降30%", "Ozempic/Wegovy等药物大型研究新发现"),
            ]),
            ("🧘 身心养护", [
                ("科学家修复脑回路逆转焦虑", "杏仁核新发现神经元是焦虑核心调控因素"),
                ("AI设计通用冠状病毒疫苗通过人体试验", "首次人体测试安全性良好，诱导多种冠状病毒免疫"),
                ("攻克不可成药胰腺癌靶点", "新药daraxonrasib显著延长患者生存期"),
            ]),
        ]
    }
]

# Count items per section
ai_items = sum(len(sub[1]) for sec in wechat_sections if sec["title"]=="AI 晨报" for sub in sec["sub_sections"])
world_items = sum(len(sub[1]) for sec in wechat_sections if sec["title"]=="国际焦点" for sub in sec["sub_sections"])
tech_items_count = sum(len(sub[1]) for sec in wechat_sections if sec["title"]=="科技日报" for sub in sec["sub_sections"])
sports_items = sum(len(sub[1]) for sec in wechat_sections if sec["title"]=="运动健康" for sub in sec["sub_sections"])

# Build WeChat HTML
wechat_body = f'''<div style="max-width:680px;margin:0 auto;background:#f5f5f5;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;color:#333;line-height:1.8;font-size:14px;">

<!-- Header -->
<div style="background:linear-gradient(135deg,#1a1a2e,#16213e);padding:40px 24px 32px;text-align:center;">
  <div style="font-size:13px;color:rgba(255,255,255,0.7);letter-spacing:0.1em;margin-bottom:8px;">2026 年 6 月 8 日 · 星期一</div>
  <div style="font-size:28px;font-weight:800;color:#fff;letter-spacing:-0.02em;">📰 每日晨报</div>
  <div style="margin-top:12px;font-size:13px;color:rgba(255,255,255,0.6);">
    <span style="color:#ff6a3d;">●</span> AI ·
    <span style="color:#3b82f6;">●</span> 国际 ·
    <span style="color:#10b981;">●</span> 科技 ·
    <span style="color:#f59e0b;">●</span> 运动
  </div>
</div>

<!-- TOC Card -->
<div style="margin:20px 16px;background:#fff;border-radius:12px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,0.06);">
  <div style="font-size:16px;font-weight:700;margin-bottom:14px;">📋 今日概览</div>
  <div style="display:flex;flex-wrap:wrap;gap:10px;">
    <div style="flex:1;min-width:140px;background:linear-gradient(135deg,#ff6a3d,#ff8c5a);border-radius:8px;padding:12px;color:#fff;">
      <div style="font-size:12px;opacity:0.8;">AI 晨报</div>
      <div style="font-size:20px;font-weight:800;">{ai_items} 条</div>
    </div>
    <div style="flex:1;min-width:140px;background:linear-gradient(135deg,#3b82f6,#60a5fa);border-radius:8px;padding:12px;color:#fff;">
      <div style="font-size:12px;opacity:0.8;">国际焦点</div>
      <div style="font-size:20px;font-weight:800;">{world_items} 条</div>
    </div>
    <div style="flex:1;min-width:140px;background:linear-gradient(135deg,#10b981,#34d399);border-radius:8px;padding:12px;color:#fff;">
      <div style="font-size:12px;opacity:0.8;">科技日报</div>
      <div style="font-size:20px;font-weight:800;">{tech_items_count} 条</div>
    </div>
    <div style="flex:1;min-width:140px;background:linear-gradient(135deg,#f59e0b,#fbbf24);border-radius:8px;padding:12px;color:#fff;">
      <div style="font-size:12px;opacity:0.8;">运动健康</div>
      <div style="font-size:20px;font-weight:800;">{sports_items} 条</div>
    </div>
  </div>
</div>
'''

for sec in wechat_sections:
    color = sec["color"]
    color2 = sec["color2"]
    title = sec["title"]
    total = sum(len(sub[1]) for sub in sec["sub_sections"])
    
    wechat_body += f'''
<!-- {title} Section -->
<div style="margin:20px 16px;">
  <div style="background:linear-gradient(90deg,{color},{color2});border-radius:8px 8px 0 0;padding:12px 16px;">
    <span style="font-size:16px;font-weight:700;color:#fff;">{title} · {total}条</span>
  </div>
  <div style="background:#fff;border-radius:0 0 8px 8px;padding:16px;">
'''
    for sub_title, items in sec["sub_sections"]:
        wechat_body += f'    <div style="font-size:14px;font-weight:600;color:{color};margin:12px 0 6px;">{sub_title}</div>\n'
        for item_title, item_desc in items:
            wechat_body += f'    <div style="font-size:13px;line-height:1.8;padding:3px 0;">▸ <b>{item_title}</b> — {item_desc}</div>\n'
    
    wechat_body += '  </div>\n</div>\n'

wechat_body += f'''
<!-- Footer -->
<div style="margin:20px 16px;text-align:center;padding:16px;font-size:12px;color:#999;line-height:1.8;">
  <div>数据来源：AI HOT / Reuters / BBC / NPR / TechCrunch / 36氪 / ESPN / ScienceDaily 等公开媒体</div>
  <div style="margin-top:6px;">🔗 <a href="https://wushanchi.github.io/news/" style="color:#3b82f6;">完整日报：wushanchi.github.io/news</a></div>
  <div style="margin-top:4px;">GitHub：github.com/wushanchi/news</div>
</div>

</div>'''

with open(os.path.join(BASE, f"wechat-article-{DATE}.html"), "w", encoding="utf-8") as f:
    f.write(wechat_body)
print(f"✅ wechat-article-{DATE}.html")
print(f"\n📊 生成完毕：AI晨报{ai_total}条 / 国际焦点{world_total}条 / 科技日报{tech_total}条 / 运动健康{sports_total}条")
