#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 2026-05-30 全套日报 HTML 文件
用法: python generate_0530.py
"""

import os, datetime

DATE = "2026-05-30"
DATE_CN = "2026 年 5 月 30 日 · 星期六"
WEEKDAY = "星期六"
OUT = r"C:\Users\Wu Shanchi\WorkBuddy\2026-05-22-AI news"

# ========== AI 晨报 24条 ==========
ai_items = [
  # 模型发布/更新 4条
  {"cat":"模型","num":1,"title":"OpenAI推出实时翻译模型，支持70+语言输入","summary":"OpenAI 实时翻译功能使用70多种输入语言说话，翻译成13种输出语言，在智能眼镜上运行。","source":"X：Greg Brockman","url":"https://x.com/gdb/status/2060452095279415725","time":"05-30"},
  {"cat":"模型","num":2,"title":"阶跃星辰 Step 3.7 Flash 发布，聚焦智能体效率","summary":"阶跃星辰发布开源大模型 Step 3.7 Flash，198B参数MoE，约11B活跃参数，支持256K上下文，ClawEval-1.1排名第一。","source":"X：阶跃星辰","url":"https://x.com/StepFun_ai/status/2060149124117475791","time":"05-30"},
  {"cat":"模型","num":3,"title":"小米开源可控视频音效生成模型 ControlFoley","summary":"小米大模型团队发布开源可控视频音效生成模型 ControlFoley，统一支持文本/视频/参考音频三种引导方式，VGGSound-Test benchmark 开源SOTA。","source":"IT之家","url":"https://www.ithome.com/0/957/282.htm","time":"05-30"},
  {"cat":"模型","num":4,"title":"Qwen-VLA：从理解世界到在其中行动","summary":"Qwen-VLA 多模态模型发布，支持聊天、图像视频理解、图像生成、文档处理、网络搜索及工具调用，配套 Qwen Studio 全套开发环境。","source":"Qwen Blog","url":"https://qwen.ai/blog?id=qwenvla","time":"05-30"},
  # 产品发布/更新 8条
  {"cat":"产品","num":5,"title":"Codex 可自主管理对话线程与并行任务","summary":"Codex 现在可以创建对话线程、搜索、整理、固定重要线程，并为并行任务启动工作树，帮助开发者更高效管理编码会话。","source":"X：Greg Brockman","url":"https://x.com/gdb/status/2060486309886443787","time":"05-30"},
  {"cat":"产品","num":6,"title":"Gemini Omni 可将草图变为现实","summary":"Gemini Omni 能将简单草图转化为实际生成结果，用户可在 Gemini 应用中上传草图并输入提示词体验该功能。","source":"X：Gemini","url":"https://x.com/GeminiApp/status/2060435981946503243","time":"05-30"},
  {"cat":"产品","num":7,"title":"Codex 现已支持 Windows 端计算机使用功能","summary":"Windows 用户现可通过 Codex 在 Windows 电脑上执行操作，ChatGPT 移动应用支持远程启动、审查和引导任务，工作随时随地持续进行。","source":"X：OpenAI","url":"https://x.com/OpenAI/status/2060428604727771421","time":"05-30"},
  {"cat":"产品","num":8,"title":"Guardrails：保护你的智能体、数据与成本","summary":"Guardrails 提供预算执行、零数据保留、模型与提供商限制、提示词注入防御及数据丢失预防等功能，全面保障 AI 智能体安全。","source":"OpenRouter","url":"https://openrouter.ai/announcements/guardrails","time":"05-30"},
  {"cat":"产品","num":9,"title":"Runway API 持续扩展模型与端点支持","summary":"Runway API 新增 Seedance 2.0、GPT Image 2、HappyHorse 1.0、Nano Banana Pro、Magnific Precision Upscaler V2 等模型端点。","source":"X：Runway","url":"https://x.com/runwayml/status/2060453805519765548","time":"05-30"},
  {"cat":"产品","num":10,"title":"OpenRouter 支持模型生成文件补丁","summary":"OpenRouter 现支持 apply_patch 服务器工具，允许任何模型通过 Responses API 使用 V4A diffs 提出文件编辑建议。","source":"X：OpenRouter","url":"https://x.com/OpenRouter/status/2060395056196936054","time":"05-30"},
  {"cat":"产品","num":11,"title":"ChatGPT 对话目录功能现已上线","summary":"ChatGPT 目录功能正式推出，适用于包含5条以上回复的对话，帮助用户更好管理和浏览长对话内容。","source":"X：ChatGPT","url":"https://x.com/ChatGPTapp/status/2060467129066070182","time":"05-30"},
  {"cat":"产品","num":12,"title":"Gemini 本月更新：全新界面与智能体助手","summary":"Gemini 本月迎来全新设计的用户界面，以及 Gemini Spark 提供的全天候智能体辅助，全面提升 AI 助手使用体验。","source":"X：Gemini","url":"https://x.com/GeminiApp/status/2060389565052096911","time":"05-30"},
  # 行业动态 3条
  {"cat":"行业","num":13,"title":"中央网信办等四部门：提升全民人工智能素养","summary":"中央网信办等四部门联合印发《2026年提升全民数字素养与技能工作要点》，明确强化 AI 赋能教育、加快 AI 人才培育、深化 AI 普及应用。","source":"IT之家","url":"https://www.ithome.com/0/957/319.htm","time":"05-30"},
  {"cat":"行业","num":14,"title":"波士顿儿童医院利用 AI 解锁新诊断","summary":"波士顿儿童医院通过部署 OpenAI 技术改善患者护理并减轻运营负担，已帮助诊断超过40种罕见病病例。","source":"OpenAI","url":"https://openai.com/index/boston-childrens-hospital","time":"05-30"},
  {"cat":"行业","num":15,"title":"滑铁卢大学未来实验室展示 AI 原型","summary":"滑铁卢大学未来实验室的学生开发了用于重塑教育和工作未来的 AI 原型，其中包括手语辅导工具等创新项目。","source":"Google Blog","url":"https://blog.google/innovation-and-ai/technology/ai/university-waterloo-labs","time":"05-30"},
  # 论文研究 1条
  {"cat":"论文","num":16,"title":"GPIC：大规模视觉生成基准数据集发布","summary":"GPIC 适用于大规模生成模型新时代的视觉生成基准数据集正式发布，为图像生成质量评估提供标准化评价基准。","source":"X：Fei-Fei Li","url":"https://x.com/drfeifei/status/2060404846734512205","time":"05-30"},
  # 技巧与观点 8条
  {"cat":"观点","num":17,"title":"claude-design-card：文字/URL 直接生成公众号首图","summary":"claude-design-card 专为中文创作者设计，能将文字、URL 或文章直接转化为可发布的视觉卡片，支持28种布局与10种主题。","source":"X：洪明","url":"https://x.com/hongming731/status/2060487110906527820","time":"05-30"},
  {"cat":"观点","num":18,"title":"Kog 团队实现 3000 tokens/s 超高推理速度","summary":"Kog 团队在标准数据中心 GPU 上实现极高单用户推理速度，8×AMD MI300X 达3000 tokens/s，核心思路是将 LLM 解码视为内存流问题。","source":"X：Rohan Paul","url":"https://x.com/rohanpaul_ai/status/2060409504693645440","time":"05-30"},
  {"cat":"观点","num":19,"title":"Adam's Law：用高频词写 Prompt 效果更好","summary":"FaceMind 团队用100种语言实验发现，使用预训练语料中出现频率更高的词汇撰写提示词，可显著提升大语言模型表现。","source":"X：Berry Xia","url":"https://x.com/berryxia/status/2060212428584202428","time":"05-30"},
  {"cat":"观点","num":20,"title":"Cursor 团队发布《开发者习惯报告》","summary":"报告显示 AI 正深刻改变开发工作形态，开发者周均代码产出从约3.6K行增至8.6K行，AI 智能体工具调用数增加约30%。","source":"X：邵猛","url":"https://x.com/shao__meng/status/2060167182777249886","time":"05-30"},
  {"cat":"观点","num":21,"title":"Claude Code——文档中未提及的所有可配置选项","summary":"文章深入解析 Claude Code 源码中隐藏的可配置选项，揭示大量未在官方文档中说明但非常实用的配置参数。","source":"Hacker News","url":"https://buildingbetter.tech/p/i-read-the-claude-code-source-code","time":"05-30"},
  {"cat":"观点","num":22,"title":"当公司过于"AI 上瘾"时会发生什么？","summary":"Box 创始人指出决定用 AI 替代员工的人往往最不了解工作实际内容，ClickUp 近期因部署 AI 智能体裁员22%即是例证。","source":"TechCrunch","url":"https://techcrunch.com/video/what-happens-when-companies-become-too-ai-pilled","time":"05-30"},
  {"cat":"观点","num":23,"title":"特斯拉 FSD 安全性宣称遭质疑","summary":"特斯拉声称 FSD 安全性最高可达人类10倍，但路透社调查发现此数据经不起推敲，统计方法被11位交通安全研究人员指出存在缺陷。","source":"IT之家","url":"https://www.ithome.com/0/956/864.htm","time":"05-30"},
  {"cat":"观点","num":24,"title":"Cognition 的 Scott Wu：AI 编程智能体不应取代人类","summary":"Cognition 公司开发了号称首个最成功的 AI 编程智能体 Devvin，其创始人 Scott Wu 明确表示该智能体并非旨在取代人类程序员。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/29/cognitions-scott-wu-says-ai-coding-agents-shouldnt-replace-humans","time":"05-30"},
]

# ========== 国际焦点 20条 ==========
world_items = [
  {"cat":"政治","num":1,"title":"美副总统万斯：不保证能与伊朗就剩余问题达成协议","summary":"美伊谈判持续胶着，美方对能否解决剩余分歧持谨慎态度，协议条件尚未商定完毕，停火前景仍存变数。","source":"Sputnik","url":"https://sputniknews.cn/20260530/1071571189.html","time":"05-30"},
  {"cat":"政治","num":2,"title":"伊朗武装力量向霍尔木兹海峡附近船只实施警告性射击","summary":"伊朗南部防空系统发现敌军空中目标，拦截1架美军无人机，区域军事紧张持续升级，霍尔木兹海峡局势引人关注。","source":"Sputnik","url":"https://sputniknews.cn/20260530/1071568903.html","time":"05-30"},
  {"cat":"政治","num":3,"title":"以军越过利塔尼河，黎以军事谈判无果而终","summary":"黎以双方军事谈判未能取得成果，以色列军队主力已越过利塔尼河推进，贝鲁特南郊等地持续遭到打击。","source":"新华网","url":"https://www.news.cn/world/20260530/6a43df11c0974ccdbcd22bb12d17caf9/c.html","time":"05-30"},
  {"cat":"政治","num":4,"title":"日菲启动 GSOMIA 谈判，对东海和南海表示"严重关切"","summary":"日本与菲律宾就军事情报保护协定启动磋商，联合声明对东海南海安全形势表达关切，引发地区安全关注。","source":"Sputnik","url":"https://sputniknews.cn/20260530/1071569953.html","time":"05-30"},
  {"cat":"政治","num":5,"title":"王毅会见巴基斯坦副总理兼外长和乌拉圭外长","summary":"中国外长同巴乌两国外长会面，就双边关系与共同关心的国际地区问题深入交换意见，推动多边外交合作。","source":"新华网","url":"https://www.news.cn/world/20260530/ad61dd6e9d9e44619f5eee5eb98131a2/c.html","time":"05-30"},
  {"cat":"政治","num":6,"title":"欧盟制裁以色列极端定居者相关实体和个人","summary":"欧盟宣布对涉及巴勒斯坦领土的以色列极端定居者实体及个人实施新一轮制裁措施，中东和平进程再添变数。","source":"新华网","url":"https://www.news.cn/world/20260530/ace5459f8c744a07bd38915ebe7beed7/c.html","time":"05-30"},
  {"cat":"政治","num":7,"title":"匈牙利总统：匈牙利不会向乌克兰提供武器","summary":"匈牙利继续坚持不向乌克兰提供武器的立场，在欧盟内部与德国等国就对俄政策产生明显分歧，影响欧盟对乌政策一致性。","source":"Sputnik","url":"https://sputniknews.cn/20260530/1071568803.html","time":"05-30"},
  {"cat":"经济","num":8,"title":"欧盟以违反数字服务法为由对 Temu 罚款 2.32 亿美元","summary":"欧盟认定 Temu 未能充分防止平台销售危险玩具与电子产品等非法商品，开出 DSA 法案迄今为止最重罚单。","source":"Reuters","url":"https://www.livemint.com/news/world/eu-slaps-232-million-fine-on-chinese-online-retailer-temu-for-violations-under-its-digital-services-act-11779997511213.html","time":"05-30"},
  {"cat":"经济","num":9,"title":"华尔街收高，布伦特原油因美伊停火传闻回落","summary":"受美伊接近达成停火协议报道影响，美股收涨，油价走势因消息矛盾出现分歧，大宗商品市场波动加剧。","source":"Reuters","url":"https://www.livemint.com/market/wall-street-ends-higher-brent-crude-eases-on-reports-of-us-iran-truce-extension-11780000266705.html","time":"05-30"},
  {"cat":"经济","num":10,"title":"美财长：阿曼称不会征收霍尔木兹海峡通行费","summary":"美国与阿曼就霍尔木兹海峡通行问题进行沟通，阿曼方面表示不会征收海峡通行费，缓解全球石油运输关键航道担忧。","source":"新华社","url":"https://www.news.cn/world/20260530/a1245231baed43ce80c72355cecc8008/c.html","time":"05-30"},
  {"cat":"经济","num":11,"title":"铜价因美伊停火协议报道跳涨至两周高位","summary":"停火预期提振大宗商品市场，铜价因风险情绪改善和供应链预期好转显著走高，工业金属全线走强。","source":"LiveMint","url":"https://www.livemint.com/market/copper-jumps-to-two-week-high-after-us-iran-truce-deal-report-11779997669207.html","time":"05-30"},
  {"cat":"重大","num":12,"title":"瑞士火车站持刀袭击定性恐袭，嫌疑人细节披露","summary":"瑞士当局将火车站持刀袭击事件定性为恐怖主义行为，调查中更多嫌疑人背景细节浮出水面，欧洲安全形势引人担忧。","source":"新华网","url":"https://www.news.cn/world/20260530/df6106a2ab33483fae4796fd86bcfc0f/c.html","time":"05-30"},
  {"cat":"重大","num":13,"title":"罗马尼亚一居民楼被无人机击中","summary":"罗马尼亚境内发生无人机袭击居民楼事件，引发对俄乌冲突外溢效应的进一步担忧，北约东欧成员国安全形势急剧收紧。","source":"新华网","url":"https://www.news.cn/world/20260530/63cba0b3c2e84637b20f891b97b7d578/c.html","time":"05-30"},
  {"cat":"重大","num":14,"title":"以色列加强对真主党攻势，贝鲁特附近遭打击","summary":"以色列在谈判前夕对黎巴嫩真主党加大攻势，贝鲁特郊区遭遇沉重打击，局势升级，停火协议面临严峻考验。","source":"LiveMint","url":"https://www.livemint.com/news/world/at-least-14-killed-as-israel-ramps-up-offensive-against-hezbollah-launches-strike-near-beirut-ahead-of-negotiations-11780001952635.html","time":"05-30"},
  {"cat":"重大","num":15,"title":"第23届香格里拉对话会在新加坡开幕","summary":"第23届香格里拉对话会正式开幕，越南总书记苏林发表主旨演讲，中国防长董军再次缺席引发地区安全讨论热议。","source":"新华网","url":"https://www.news.cn/world/20260530/4a2bd438027146dab6d8f9c935e1e6d9/c.html","time":"05-30"},
  {"cat":"社会","num":16,"title":"美国挨饿人口超新冠疫情高峰","summary":"纽约联邦储备银行报告揭示，当前美国面临食品短缺的人口比例已超过疫情最严重时期，社会稳定风险持续累积。","source":"Sputnik","url":"https://sputniknews.cn/20260530/1071570247.html","time":"05-30"},
  {"cat":"社会","num":17,"title":"C罗连续四年霸榜福布斯运动员收入榜","summary":"以3亿美元总收入连续第四年蝉联榜首，日均入账超82万美元，比第二名多出1.3亿美元，足球商业价值持续领跑。","source":"福布斯","url":"https://www.forbes.com/profile/cristiano-ronaldo/","time":"05-30"},
  {"cat":"社会","num":18,"title":"东京审判开庭80周年：铭记正义审判","summary":"纪念东京审判开庭80周年，中外嘉宾参观侵华日军南京大屠杀遇难同胞纪念馆，呼吁铭记历史、严防战争悲剧重演。","source":"光明网","url":"https://news.gmw.cn/2026-05/30/content_131029312.htm","time":"05-30"},
  {"cat":"社会","num":19,"title":"外交部：正告日本右翼势力，勿在"新型军国主义"穷途末路上狂奔","summary":"中国外交部就日本右翼势力动向发出严正警告，强调二战历史教训不容忘却，地区和平稳定需要各方共同维护。","source":"中国日报","url":"https://www.chinadaily.com.cn","time":"05-30"},
  {"cat":"社会","num":20,"title":"中老铁路累计开行旅客列车突破10万列","summary":"中老铁路运营里程碑，累计开行旅客列车突破10万列，被誉为"黄金通道"，助力中老两国合作共赢和区域互联互通。","source":"人民网","url":"http://world.people.com.cn/n1/2026/0518/c1002-40721722.html","time":"05-30"},
]

# ========== 科技日报 18条 ==========
tech_items = [
  {"cat":"互联网","num":1,"title":"程序员拒绝在没有 AI 的情况下工作——这可能会反噬他们","summary":"越来越多开发者表示离开 AI 就无法工作，专家警告这种过度依赖可能带来长期风险，职业韧性面临新考验。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/29/coders-are-refusing-to-work-without-ai-and-that-could-come-back-to-bite-them/","time":"05-30"},
  {"cat":"互联网","num":2,"title":"Microsoft 因威胁安全研究员进行刑事调查而遭到强烈批评","summary":"微软向一名披露漏洞的安全研究员发出刑事调查威胁，引发安全社区强烈反弹，企业安全披露文化引发广泛讨论。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/29/microsoft-under-fire-for-threatening-security-researcher-with-criminal-investigation/","time":"05-30"},
  {"cat":"互联网","num":3,"title":"Anthropic 发布 Opus 4.8，带来全新"动态工作流"工具","summary":"Anthropic 推出新版旗舰模型 Opus 4.8，新增动态工作流功能，进一步强化 AI 智能体能力，在编码和推理任务中表现突出。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/","time":"05-30"},
  {"cat":"互联网","num":4,"title":"Meta 正式推出 Instagram、Facebook 和 WhatsApp 订阅服务","summary":"Meta 宣布三大平台付费订阅正式上线，并透露未来将推出 AI 专属订阅套餐，社交平台货币化进入新阶段。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/27/meta-officially-launches-instagram-facebook-and-whatsapp-subscriptions-with-more-to-come-including-ai-plans/","time":"05-30"},
  {"cat":"互联网","num":5,"title":"DuckDuckGo 安装量增长 30%，用户拒绝被"强喂"Google AI 搜索","summary":"越来越多用户因不满 Google 强制推送 AI 搜索结果而转向 DuckDuckGo，其安装量大幅攀升，隐私搜索需求持续增长。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/26/duckduckgo-installs-are-up-30-as-users-reject-being-force-fed-googles-ai-search/","time":"05-30"},
  {"cat":"硬件","num":6,"title":"SpaceX 在 IPO 前获得 64.5 亿美元太空部队合同","summary":"SpaceX 在准备上市之际，获得了美国太空部队的大额合同，进一步巩固其商业航天地位，星链军事化应用加速落地。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/29/spacex-awarded-6-45b-in-space-force-contracts-ahead-of-ipo/","time":"05-30"},
  {"cat":"硬件","num":7,"title":"Blue Origin 的 New Glenn 火箭在佛罗里达测试中发生爆炸","summary":"贝索斯旗下 Blue Origin 的 New Glenn 火箭在地面测试期间发生爆炸事故，发射台及配套设施严重损毁，商业航天竞赛受挫。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/28/blue-origins-new-glenn-rocket-explodes-during-testing-in-florida/","time":"05-30"},
  {"cat":"硬件","num":8,"title":"Nvidia 200亿美元"非收购式招募"后，AI 芯片初创公司 Groq 据报融资 6.5 亿美元","summary":"在 NVIDIA 完成对其团队的大规模引进后，Groq 据报正寻求新一轮 6.5 亿美元融资，AI 芯片赛道竞争持续白热化。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/29/after-nvidias-20b-not-acqui-hire-ai-chip-startup-groq-reportedly-raising-650m/","time":"05-30"},
  {"cat":"硬件","num":9,"title":"Xcena 获 1.35 亿美元融资，押注 AI 最大瓶颈是内存","summary":"Xcena 以 5.7 亿美元估值完成融资，认为内存带宽才是制约 AI 发展的核心瓶颈，而非单纯算力，存储架构创新获资本青睐。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/29/xcena-secures-135m-at-570m-valuation-betting-on-memory-as-ais-real-bottleneck/","time":"05-30"},
  {"cat":"硬件","num":10,"title":"新 Siri 应用抢先看：苹果计划挑战 ChatGPT 及更多竞争对手","summary":"泄露的新版 Siri 应用截图显示，苹果正在大幅重构 Siri，剑指 ChatGPT 等 AI 助手市场，智能语音助手竞争进入新阶段。","source":"TechCrunch","url":"https://techcrunch.com/2026/05/28/sneak-peek-at-new-siri-app-reveals-apples-plans-to-take-on-chatgpt-and-more/","time":"05-30"},
  {"cat":"航天","num":11,"title":"香格里拉对话会聚焦印太安全，中美博弈成核心议题","summary":"第23届香格里拉对话会开幕，中美防务战略博弈、南海航行自由、台海局势等议题成为各方关注的焦点。","source":"新华网","url":"https://www.news.cn/world/20260530/4a2bd438027146dab6d8f9c935e1e6d9/c.html","time":"05-30"},
  {"cat":"航天","num":12,"title":"中国载人航天工程办公室发布空间站最新科学实验进展","summary":"中国空间站多项科学实验取得重要进展，涵盖微重力物理、空间生命科学、新材料制备等前沿领域，科研成果持续产出。","source":"央视网","url":"https://news.cctv.com/tech/","time":"05-30"},
  {"cat":"航天","num":13,"title":"2026 年 ACM 戈登贝尔奖提名公布，中国团队多项成果入围","summary":"高性能计算领域最高荣誉戈登贝尔奖提名名单公布，中国多个超算应用项目入围，展现中国在超算应用领域的全球领先地位。","source":"科技日报","url":"https://www.ithome.com","time":"05-30"},
  {"cat":"数字","num":14,"title":"ACSM 2026 全球健身趋势报告发布，AI 个性化训练成核心方向","summary":"美国运动医学会发布 2026 年全球健身趋势调查，AI 驱动的个性化训练方案、虚拟健身教练、可穿戴设备深度整合成为年度最热趋势。","source":"ACSM Health & Fitness Journal","url":"https://journals.lww.com/acsm-healthfitness/fulltext/2025/11000/2026_acsm_worldwide_fitness_trends__future.8.aspx","time":"05-30"},
  {"cat":"数字","num":15,"title":"Cursor 开发者习惯报告：AI 正在重塑软件工程工作方式","summary":"报告显示 AI 编程工具使开发者周均代码产出增长超 2 倍，AI 智能体单次会话工具调用数增加约 30%，开发效率实现质的飞跃。","source":"X：邵猛","url":"https://x.com/shao__meng/status/2060167182777249886","time":"05-30"},
  {"cat":"数字","num":16,"title":"2026 年大模型产业变局：资本狂奔下商业化突围战打响","summary":"全球大模型产业正经历关键转型，竞争焦点从技术参数比拼转向商业化能力验证，中国科技巨头 AI 资本投入持续加码。","source":"IT熊","url":"https://www.itbear.com.cn/html/2026-05/1345715.html","time":"05-30"},
  {"cat":"数字","num":17,"title":"中国大模型调用量领跑全球，产业落地加速","summary":"据 Openrate 统计，2026 年 5 月中国大模型调用量持续领跑全球，AI 应用商业化落地进程明显加快，企业级 AI 服务市场规模迅速扩张。","source":"搜狐","url":"https://www.sohu.com/a/1025143029_122775070","time":"05-30"},
  {"cat":"数字","num":18,"title":"欧盟高官挑拨：都自以为从中国捞到甜头，比别人多","summary":"欧盟高官就中欧贸易关系发表争议性言论，称中国竞争性政策让欧洲吃亏，中方官媒回应称不惧贸易摩擦。","source":"RFI","url":"https://www.rfi.fr/cn","time":"05-30"},
]

# ========== 运动健康 18条 ==========
sports_items = [
  {"cat":"体育","num":1,"title":"尼克斯横扫骑士晋级，时隔 27 年重返 NBA 总决赛","summary":"纽约尼克斯以 4-0 横扫骑士赢得东部冠军，自 1999 年以来首次进入 NBA 总决赛，6 月 3 日开打，对阵西部优胜者。","source":"ESPN","url":"https://www.espn.com/nba/story/_/id/48419498/nba-playoffs-2026-playoffs-schedule-scores-news-highlights-bracket-dates","time":"05-30"},
  {"cat":"体育","num":2,"title":"西部决赛激战：雷霆 vs 马刺争夺最后一张总决赛门票","summary":"雷霆与马刺西决较量异常激烈，胜者将与尼克斯在 6 月 3 日开打的 NBA 总决赛中对决，西部冠军悬念仍存。","source":"ESPN","url":"https://www.espn.com/nba/story/_/id/48419498/nba-playoffs-2026-playoffs-schedule-scores-news-highlights-bracket-dates","time":"05-30"},
  {"cat":"体育","num":3,"title":"2026 美加墨世界杯倒计时 15 天，门票销售引发争议","summary":"距离 2026 年美加墨世界杯鸣哨开赛仅剩 15 天，多座主办城市仍囤积上万张门票无人认购，国际足联高价策略遭遇市场冷遇。","source":"搜狐","url":"https://www.sohu.com/a/1028128876_120012562","time":"05-30"},
  {"cat":"体育","num":4,"title":"中国移动宣布咪咕拿下 2026 世界杯官方转播权","summary":"中国移动宣布咪咕正式成为 2026 美加墨世界杯官方持权转播商，用户可通过咪咕视频、移动高清、咪视界等平台观看全量直播。","source":"快科技","url":"https://www.msn.cn","time":"05-30"},
  {"cat":"体育","num":5,"title":"福布斯发布 2026 年运动员收入榜：C 罗与梅西各领风骚","summary":"福布斯公布 2026 年体育界收入最高运动员前十名，C 罗以 3 亿美元总收入领跑，詹姆斯 8500 万美元场外收入位列第二。","source":"福布斯","url":"https://www.forbes.com/profile/cristiano-ronaldo/","time":"05-30"},
  {"cat":"体育","num":6,"title":"2026 年中国男篮国际热身赛 6 月下旬将在杭州举行","summary":"6 月 21 日至 23 日，中国男篮将在杭州奥体中心体育馆先后迎战澳大利亚男篮与荷兰男篮，采取赛会制模式进行。","source":"央视网","url":"https://sports.cctv.com/2026/05/28/ARTItesyLIZQDSA9MT2AHXc3260528.shtml","time":"05-30"},
  {"cat":"体育","num":7,"title":"法网高温政策详解：巴黎红土赛场如何应对