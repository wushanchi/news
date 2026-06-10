# -*- coding: utf-8 -*-
import json, os

DATE = "2026-06-09"
DATE_CN = "2026 年 6 月 9 日"
WEEKDAY = "星期二"
BASE = r"C:\Users\Wu Shanchi\WorkBuddy\2026-05-22-AI news"

# ===================== AI Morning Data =====================
ai_data = {
    "accent": "#ff6a3d", "accent2": "#ff8c5a",
    "bg": "#0f0c0a", "surface": "#1a1410", "card": "#221a14",
    "border": "#3a2a1e", "text": "#f0e6dc", "text_dim": "#a89880",
    "grad": ["#ff5c28", "#e8452e", "#c8203a"],
    "tags": {"models": "#e85d3a", "products": "#f08c4a", "industry": "#d4a24e", "paper": "#c07a5e", "tip": "#b8956e"},
    "stat_names": {"models": "模型", "products": "产品", "industry": "行业", "paper": "论文", "tip": "观点"},
    "title": "AI 晨报",
    "footer": '数据来源：<a href="https://aihot.virxact.com" target="_blank" rel="noopener noreferrer">aihot.virxact.com</a> · AI HOT 每日聚合',
    "sections": [
        {"id": "models", "badge": "MODELS", "title": "模型发布 / 更新", "emoji": "🤖", "items": [
            ["小米 MiMo-V2.5-Pro-UltraSpeed：1T MoE 模型突破 1000 tokens/s", "小米 MiMo", "联合 TileRT_AI 发布，首次在1万亿参数MoE模型上实现超1000 tokens/s输出，仅用单台8-GPGPU节点，限时免费体验。", "https://x.com/XiaomiMiMo/status/2063993790587904362"],
            ["苹果发布第三代 Apple Foundation Models（AFM）", "Apple ML Research", "与Google合作定制，包含五个模型，覆盖设备端到Private Cloud Compute服务器端，驱动全新Siri和Apple Intelligence。", "https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models"],
            ["VoxCPM2 技术报告：2B参数语音生成模型开源", "面壁智能", "2B参数语音生成模型，200万+小时多语言语音数据训练，支持30种语言和9种中文方言，Apache 2.0开源。", "https://x.com/OpenBMB/status/2063991963133903317"],
            ["高德发布全球首个3D原生城市世界模型 ABot-Earth0.5", "IT之家", "阿里巴巴旗下高德发布，覆盖190+国家和地区，输入卫星图或文字10分钟生成公里级3D城市，成本为传统百分之一。", "https://www.ithome.com/0/961/378.htm"],
        ]},
        {"id": "products", "badge": "PRODUCTS", "title": "产品发布 / 更新", "emoji": "🚀", "items": [
            ["Runway Aleph 2.0 编辑模型：一键适配任意视频格式", "Runway", "上传现有视频选择宽高比，Aleph 2.0自动填充场景其余部分，实现一键适配任意信息流和格式。", "https://x.com/runwayml/status/2064012425884569627"],
            ["Apple Core AI 框架正式发布", "Hacker News", "苹果Core AI框架开发者文档上线，Hacker News获109点赞，为开发者提供构建AI应用的核心工具集。", "https://developer.apple.com/documentation/coreai"],
            ["Kimi Code 焕新升级：新增视频理解与ACP协议", "月之暗面", "开源Coding Agent大版本升级：毫秒级启动、视频理解能力、集成同花顺/天眼查数据源、支持ACP协议和JetBrains/Zed。", "https://mp.weixin.qq.com/s?__biz=MzkzMTY4NTIyNA%3D%3D&mid=2247484250&idx=1&sn=d0a07f5358250f3a54df8fbabe61f09a"],
            ["微信AI官宣内测：两种接入模式供开发者选择", "IT之家", "自动模式授权平台读取小程序源码无需额外开发，开发模式可自主开发技能审核后由微信AI调用，两种模式可同时开启。", "https://www.ithome.com/0/961/480.htm"],
            ["Claude 为 Connector 开发者推出性能监控仪表盘", "Claude Blog", "公开测试版新增活跃用户、工具调用次数、目录排名、健康评分、错误率、延迟追踪，按工具细分错误归因。", "https://claude.com/blog/observability-for-developers-building-connectors"],
            ["Apple Intelligence 将强大 AI 能力融入日常体验", "Apple Newsroom", "下一代Apple Intelligence集成到iPhone、iPad和Mac，Siri AI支持跨设备使用，新增Visual Intelligence和对话式快捷指令。", "https://www.apple.com/newsroom/2026/06/apple-intelligence-brings-powerful-ai-capabilities-into-everyday-experiences"],
            ["NotebookLM 重大升级：智能体能力与高级推理", "Google NotebookLM", "新增对话中智能体能力、更高级推理和新输出格式，处理复杂多步骤研究问题更简单，面向AI Ultra订阅者推出。", "https://x.com/NotebookLM/status/2064016460964585549"],
            ["ChatGPT 新增数据图表生成功能", "OpenAI", "将数据和比较直接转化为图表，支持移动端和网页端，无需额外工具即可在对话中完成数据可视化。", "https://x.com/ChatGPTapp/status/2064018770839113769"],
        ]},
        {"id": "industry", "badge": "INDUSTRY", "title": "行业动态", "emoji": "🌍", "items": [
            ["OpenAI 向 SEC 机密提交 S-1 草案，正式启动IPO流程", "OpenAI", "OpenAI正式向SEC机密提交S-1注册声明草案，启动首次公开募股程序，上市时间尚未确定。", "https://openai.com/index/openai-submits-confidential-s-1"],
            ["奥尔特曼宣布 OpenAI 进入第三发展阶段", "IT之家", "与首席科学家联合发文，三大核心目标：打造自动化AI研究员、推动经济提升、让AI普及易用且安全。", "https://www.ithome.com/0/961/721.htm"],
            ["苹果WWDC 2026：Siri AI由Gemini驱动，库克谢幕之作", "Hacker News", "WWDC 2026主题演讲直播，Hacker News讨论热度110点，Siri AI成为焦点，库克最后一次以CEO身份主持。", "https://www.apple.com/apple-events/event-stream"],
            ["NVIDIA与LG集团合作建设AI工厂，加速物理AI与自动驾驶", "NVIDIA AI Blog", "整合NVIDIA AI工厂平台与LG消费电子/机器人技术，为自动驾驶、数据中心和GPU云服务提供加速计算基础设施。", "https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory"],
            ["受DMA影响，Siri AI在欧盟将随iOS 27和iPadOS 27延迟上线", "Apple Newsroom", "因欧盟《数字市场法案》限制，Siri AI无法在iOS 27和iPadOS 27发布时于欧盟地区推出，上线时间晚于其他地区。", "https://www.apple.com/newsroom/2026/06/due-to-dma-siri-ai-delayed-in-eu-for-ios-27-and-ipados-27"],
            ["生数科技与华策影视达成战略合作，共建AI视听创制中心", "生数科技", "以Vidu视频生成大模型为技术底座，设立AI视听创制中心，探索AI虚拟制作与实拍融合的影视工业化流程。", "https://mp.weixin.qq.com/s?__biz=MzkzMDQ5NTQwMQ%3D%3D&mid=2247488842&idx=1&sn=3dab63189fa60b3b78c5ad72e3358791"],
            ["英国借助NVIDIA技术将主权AI雄心转化为行动", "NVIDIA AI Blog", "AI云提供商数量翻倍，Nebius部署三套NVIDIA AI基础设施，预计2027年满负荷达65兆瓦，基于5400个Blackwell GPU。", "https://blogs.nvidia.com/blog/uk-sovereign-ai-advancements"],
            ["OpenAI推出Economic Research Exchange经济研究交流平台", "OpenAI", "研究AI对就业、生产力和经济的影响，现已开放研究项目申请，关注AI对劳动市场的长期结构性变化。", "https://openai.com/index/economic-research-exchange"],
        ]},
        {"id": "paper", "badge": "PAPERS", "title": "论文研究", "emoji": "📄", "items": [
            ["Anthropic：为生物学AI智能体铺路", "Anthropic Research", "实验让Claude等科研智能体从NCBI Virus检索序列数据，即使最强模型也无法稳定达到可靠数据集构建所需准确率。", "https://www.anthropic.com/research/agents-in-biology"],
            ["Perplexity与哈佛：AI智能体提效87%降本94%", "Perplexity", "3个月研究表明，使用Computer智能体的工人完成任务速度快87%，成本低94%，且满意度更高，从聊天界面转向自主智能体。", "https://x.com/perplexity_ai/status/2064023455453110286"],
            ["腾讯混元联合多家机构发布首个音频编辑基准MMAE", "腾讯混元", "联合上海交大、南洋理工等推出MMAE，首个全面评估AI语音/音频编辑能力的基准，要求模型理解和修改音频内容。", "https://x.com/TencentHunyuan/status/2063862263434613237"],
        ]},
        {"id": "tip", "badge": "TIPS", "title": "技巧与观点", "emoji": "💡", "items": [
            ["OpenAI计划到2028年由AI主导研究", "Rohan Paul", "Altman新博客称到2028年3月大量研究将由AI完成，三大目标：构建自动AI研究员、加速科学和生产、给每个人个人AGI。", "https://x.com/rohanpaul_ai/status/2064096574142390755"],
            ["微软AI CEO：超级智能即将到来但不会取代你的工作", "The Verge", "Mustafa Suleyman在Decoder访谈中表示超级智能不会导致大规模失业，透露微软与OpenAI去年10月签署新合同。", "https://www.theverge.com/podcast/944138/microsoft-ai-ceo-mustafa-suleyman-superintelligence-agi-openai-automation"],
            ["小互开源视频翻译工具：一句话自动下载转写翻译烧字幕", "小互", 'xiaohu-video-translate开源工具，只需说一句\u201c把链接翻译成中文字幕视频\u201d即可全自动完成下载、Whisper转写、AI翻译烧字幕。', "https://x.com/xiaohu/status/2063972223170556302"],
            ["Hivemind推出面向AI编程智能体的持续学习功能", "Kim", "收集团队运行的每个智能体轨迹，转化为可复用技能并推送到整个团队，支持Claude Code、Codex、Cursor等工具。", "https://x.com/kimmonismus/status/2064001045391462907"],
            ["邵猛开源 Brand to DESIGN.md 技能，提醒复刻易生AI Slop", "邵猛", "关注Design Skill、Taste Skill、Anti-AI-slop design skill，开源Brand to DESIGN.md Skill，提醒AI生成内容需避免低质。", "https://x.com/shao__meng/status/2063902211978223678"],
            ["Claude Code GA一周年回顾：验证与自动模式", "Claude Devs", "GA一周年之际回顾验证最佳实践、为何构建自动模式、例程和循环功能，以及下一步计划。", "https://x.com/ClaudeDevs/status/2064032814392352816"],
            ["Pakistan Notice Helper：面向本地安全问题的轻量AI工具", "Hugging Face", "帮助巴基斯坦用户识别可疑消息的风险等级，接受文本或截图输入，返回风险等级、解释和警示标志。", "https://huggingface.co/blog/build-small-hackathon/building-pakistan-notice-helper"],
            ["OpenRouter Advisor：助小模型问高级模型", "OpenRouter", '新服务器工具Advisor让较小模型咨询更高智能的\u201c顾问\u201d模型，帮助逃出困境循环并迁移到更便宜的模型。', "https://x.com/OpenRouter/status/2064004944613527730"],
        ]},
    ]
}

# ===================== World News Data =====================
world_data = {
    "accent": "#3b82f6", "accent2": "#60a5fa",
    "bg": "#0a0f1a", "surface": "#101828", "card": "#182030",
    "border": "#1e3a5f", "text": "#e0e8f0", "text_dim": "#8899aa",
    "grad": ["#1e40af", "#2563eb", "#1d4ed8"],
    "tags": {"politics": "#3b82f6", "economy": "#6366f1", "major": "#ef4444", "society": "#8b5cf6"},
    "stat_names": {"politics": "政治外交", "economy": "经济财经", "major": "重大事件", "society": "社会人文"},
    "title": "国际焦点日报",
    "footer": '数据来源：Reuters / BBC / CNN / AP News / 新华网 / 环球网 / Livemint / UN News 等公开新闻源',
    "sections": [
        {"id": "politics", "badge": "POLITICS", "title": "政治外交", "emoji": "🏛️", "items": [
            ["内塔尼亚胡称赞特朗普帮助缓和以色列-伊朗紧张局势", "Reuters", "以总理公开感谢特朗普在缓和以伊紧张关系中发挥的作用，此前特朗普呼吁双方停止交火防止冲突升级为更大范围地区战争。", "https://www.livemint.com/news/world/total-world-latest-news-on-june-9-2026-live-updates-11780946022526.html"],
            ["伊朗高官对达成和平协议表示怀疑", "WNG", "一名伊朗高级官员对与美国达成和平协议的前景表示怀疑，美伊和平谈判仍面临重大障碍。", "https://wng.org/podcasts/tuesday-morning-news-june-9-2026-1780937750"],
            ["以色列空袭黎巴嫩南部，至少12人遇难", "新华网", "以色列对黎巴嫩南部多轮空袭造成至少12人死亡，纳巴提耶区Zefta遭黎明前空袭7人罹难，推罗区车辆遭袭4人死亡。", "https://english.news.cn/20260609/7ac13340cdcb49f0844575727c21c478/c.html"],
            ["玻利维亚总统签署紧急状态新法应对持续39天抗议", "新华网", "玻利维亚总统签署第1740号法律规范紧急状态宣布程序，该国已持续39天抗议和道路封锁，新法允许总统通过最高法令宣布紧急状态。", "https://english.news.cn/20260609/7ac13340cdcb49f0844575727c21c478/c.html"],
            ["全球人权治理高端论坛将于6月11日在北京举行", "中国外交部", "来自近百个国家和联合国等国际组织的400余名嘉宾将与会，纪念联合国《发展权利宣言》通过40周年。", "https://om.china-embassy.gov.cn/fyrth/202606/t20260608_11939733.htm"],
            ["中国6月外交转向全球经贸投资平台", "环球时报", "5月高级别外交密集后，中国6月议程转向全球商业、贸易和投资，一系列重大经济平台陆续启动。", "https://www.globaltimes.cn/page/202605/1362006.shtml"],
        ]},
        {"id": "economy", "badge": "ECONOMY", "title": "经济财经", "emoji": "💰", "items": [
            ["投资者以创纪录速度撤离看空石油基金", "Bloomberg", "上周投资者以创历史纪录速度从看空石油的基金中撤资，反映市场对油价走势预期的重大转变，美伊局势缓和为主要驱动。", "https://www.livemint.com/news/world/total-world-latest-news-on-june-9-2026-live-updates-11780946022526.html"],
            ["OpenAI机密提交S-1草案启动IPO，AI超级上市年启幕", "Wired", "继Anthropic和SpaceX之后，OpenAI正式提交S-1注册声明草案，华尔街为万亿美元级AI IPO浪潮做准备。", "https://www.wired.com/story/openai-confidentially-files-for-ipo/"],
            ["中国央行重启7天期逆回购操作，净投放920亿元", "新浪财经", "6月3-4日连续零操作后，6月5日重启7天期逆回购操作2150亿元，对冲到期量后实现净投放920亿元。", "https://finance.sina.com.cn/stock/y/2026-06-08/doc-iniaruxw9012130.shtml"],
            ["科技创新50强出炉，全球资金关注AI产业链", "新浪财经", '证监会主席吴清强调坚守信义义务，从\u201c重规模\u201d向\u201c重回报\u201d转型，AI产业链成为全球资金重点配置方向。', "https://finance.sina.com.cn/stock/y/2026-06-08/doc-iniarzfy7265812.shtml"],
            ["第十届中国-南亚博览会6月11日昆明开幕", "商务部", "以「团结协作，共谋发展」为主题，历经9届发展沉淀，国际化、专业化、市场化水平持续提升。", "http://expo.ce.cn/gd/202606/t20260601_3001984.shtml"],
        ]},
        {"id": "major", "badge": "MAJOR", "title": "重大事件", "emoji": "⚡", "items": [
            ["菲律宾强烈地震造成35人死亡，数千人流离失所", "Reuters", "菲律宾民答那峨岛发生强烈地震，已造成至少35人死亡，大量民众被迫撤离家园，时值数百万儿童上课时段。", "https://www.livemint.com/news/world/total-world-latest-news-on-june-9-2026-live-updates-11780946022526.html"],
            ["刚果（金）埃博拉疫情快速扩散，已蔓延至乌干达", "新华网/WHO", 'WHO警告刚果埃博拉疫情快速扩大，515例确诊91人死亡，乌干达19例确诊2人死亡，刚果风险评级\u201c极高\u201d。', "https://english.news.cn/20260609/7ac13340cdcb49f0844575727c21c478/c.html"],
            ["美军在阿曼湾拦截并致残一艘油轮", "新华网", "美军中央司令部宣布在阿曼湾国际水域拦截帕劳籍油轮Marivex号，F/A-18战机向工程和操舵舱发射精确制导弹药。", "https://english.news.cn/20260609/7ac13340cdcb49f0844575727c21c478/c.html"],
            ["FIFA世界杯倒计时2天：6月11日美加墨联合开幕", "FIFA", "2026年FIFA世界杯48支球队首次参赛，6月11日墨西哥城阿兹特克球场开幕战，横跨加拿大、墨西哥和美国三国联合举办。", "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026"],
            ["苹果WWDC 2026：Tim Cook谢幕之作，Siri AI由Gemini驱动", "The Verge", "Tim Cook最后一次以CEO身份主持WWDC，9月1日由John Ternus接任，发布Siri AI和iOS 27等全系更新。", "https://www.theverge.com/tech/944110/wwdc-2026-news-announcements"],
        ]},
        {"id": "society", "badge": "SOCIETY", "title": "社会人文", "emoji": "🌏", "items": [
            ["苹果投资者对新Siri及AI平台反应冷淡", "Bloomberg", "尽管苹果发布新一代Siri和AI平台，但市场投资者反应平平，股价未见明显提振，核心AI能力依赖Gemini引发质疑。", "https://www.livemint.com/technology/tech-news/apple-wwdc-2026-live-updates-ios-27-siri-ai-revamp-macos-27-key-announcements-and-highlights-11780923667605.html"],
            ["A24首部2亿美元影片《Backrooms》10天票房破2亿", "Livemint", "恐怖片《Backrooms》成为A24史上首部达此成绩的影片，标志着独立电影公司进入大片时代。", "https://www.livemint.com/news/world/total-world-latest-news-on-june-9-2026-live-updates-11780946022526.html"],
            ["美伊局势影响全球海运：霍尔木兹海峡通行风险上升", "Reuters", "美军在阿曼湾拦截油轮后，霍尔木兹海峡通行风险进一步上升，全球海运保险费率大幅攀升。", "https://www.livemint.com/news/world/total-world-latest-news-on-june-9-2026-live-updates-11780946022526.html"],
            ["中国\u201c北京榜样\u201d5月榜发布：人形机器人创始人上榜", "北京市政府", "20人当选5月榜样，科技创新领域松延动力创始人姜哲源上榜，人形机器人产业化提速获社会认可。", "https://www.beijing.gov.cn/ywdt/yaowen/202606/t20260608_4690181.html"],
        ]},
    ]
}

# ===================== Tech News Data =====================
tech_data = {
    "accent": "#10b981", "accent2": "#34d399",
    "bg": "#0a120e", "surface": "#101a14", "card": "#18241c",
    "border": "#1e3a2a", "text": "#dce8e0", "text_dim": "#88aa90",
    "grad": ["#065f46", "#059669", "#047857"],
    "tags": {"internet": "#10b981", "hardware": "#0ea5e9", "space": "#f59e0b", "digital": "#8b5cf6"},
    "stat_names": {"internet": "互联网/软件", "hardware": "硬件/半导体", "space": "航天/新能源", "digital": "数字创新"},
    "title": "科技日报",
    "footer": '数据来源：TechCrunch / The Verge / Ars Technica / IT之家 / 36氪 / Wired 等公开科技媒体',
    "sections": [
        {"id": "internet", "badge": "INTERNET", "title": "互联网 / 软件", "emoji": "🌐", "items": [
            ["苹果WWDC 2026：Siri AI由Gemini驱动，iOS 27发布", "The Verge", "Siri AI全新重写由Google Gemini驱动，新增专属App、跨设备对话、Agent能力；iOS 27支持iPhone 11及以上，新增Liquid Glass设计。", "https://www.theverge.com/tech/944110/wwdc-2026-news-announcements"],
            ["macOS 27 Golden Gate发布：Siri AI集成与Liquid Glass", "TechCrunch", "macOS新版本命名Golden Gate，集成Siri AI、重新设计的Liquid Glass控件，跨平台一致的AI功能更新。", "https://techcrunch.com/2026/06/08/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/"],
            ["微信AI官宣内测：小程序接入AI助手两种模式", "IT之家", "自动模式授权平台读取源码无需额外开发，开发模式可自主开发技能审核后由微信AI调用，小程序AI化迈出关键一步。", "https://www.ithome.com/0/961/480.htm"],
            ["OpenAI提交S-1草案：AI史上最大IPO启幕", "Wired", "继Anthropic和SpaceX之后，OpenAI正式提交IPO注册声明，估值介于8520亿至1万亿美元之间，9月挂牌。", "https://www.wired.com/story/openai-confidentially-files-for-ipo/"],
            ["Kimi Code大版本升级：视频理解与多数据源集成", "月之暗面", "开源Coding Agent新增视频理解能力、集成同花顺/天眼查数据源、支持ACP协议和JetBrains/Zed编辑器。", "https://mp.weixin.qq.com/s?__biz=MzkzMTY4NTIyNA%3D%3D&mid=2247484250&idx=1&sn=d0a07f5358250f3a54df8fbabe61f09a"],
        ]},
        {"id": "hardware", "badge": "HARDWARE", "title": "硬件 / 半导体", "emoji": "🔧", "items": [
            ["小米MiMo-V2.5-Pro-UltraSpeed：1T MoE模型突破1000 TPS", "小米", "联合TileRT_AI发布，首次在1万亿参数MoE模型上实现超1000 tokens/s输出，仅用单台8-GPGPU节点，非Cerebras方案。", "https://x.com/XiaomiMiMo/status/2063993790587904362"],
            ["苹果第三代AFM运行于Nvidia+Google云端", "The Verge", "Apple Foundational Model运行于Nvidia硬件+Google云端，苹果坚称云端处理与本地处理隐私保护级别等同。", "https://www.theverge.com/ai-artificial-intelligence/946705/apple-private-cloud-compute-ai-siri-intelligence-wwdc"],
            ["NVIDIA与LG集团合作建设AI工厂", "NVIDIA", "整合NVIDIA AI工厂平台与LG消费电子/机器人技术，为自动驾驶、数据中心和GPU云服务提供加速计算基础设施。", "https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory"],
            ["英国主权AI计划提速：AI云提供商翻倍，5400个Blackwell GPU部署", "NVIDIA", "Nebius部署三套NVIDIA AI基础设施，预计2027年满负荷达65兆瓦，基于5400个Blackwell GPU。", "https://blogs.nvidia.com/blog/uk-sovereign-ai-advancements"],
            ["2026年6月上旬科技产业全景：Computex+GTC双会引爆半导体", "搜狐", "全产业链从技术研发转向商业化落地，业内共识确立2026年为AI应用落地元年。", "https://www.sohu.com/a/1031584618_120426565"],
        ]},
        {"id": "space", "badge": "SPACE", "title": "航天 / 新能源", "emoji": "🚀", "items": [
            ["SNEC 2026：太空光伏与钙钛矿叠层技术成为全场焦点", "腾讯新闻", "第十九届国际太阳能光伏大会开幕，太空光伏参展内容显著增多，钙钛矿叠层技术成为全场聚焦方向。", "https://news.qq.com/rain/a/20260605A05CBU00"],
            ["中国商业航天扎堆冲刺IPO，2026超级上市年启幕", "搜狐", "SpaceX、OpenAI、Anthropic三大巨头上市将注入数万亿美元流动性，中国商业航天企业也加速IPO进程。", "https://www.sohu.com/a/971780384_122554353"],
            ["苹果Private Cloud Compute：AI云端计算与隐私的博弈", "The Verge", "苹果在WWDC技术讲座中披露AI模型运行于Nvidia+Google云端，隐私承诺面临外界质疑，将成为苹果AI成败关键。", "https://www.theverge.com/ai-artificial-intelligence/946705/apple-private-cloud-compute-ai-siri-intelligence-wwdc"],
            ["FIFA世界杯6月11日开幕：科技赋能全球赛事", "FIFA", "2026年世界杯横跨北美三国48支球队104场比赛，多项科技首次应用于赛事管理、转播和观赛体验。", "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026"],
        ]},
        {"id": "digital", "badge": "DIGITAL", "title": "数字创新", "emoji": "💡", "items": [
            ["高德发布全球首个3D原生城市世界模型ABot-Earth0.5", "IT之家", "覆盖190+国家和地区，输入卫星图或文字10分钟生成公里级3D城市，制图成本为传统百分之一，效率提升约千倍。", "https://www.ithome.com/0/961/378.htm"],
            ["Runway Aleph 2.0：AI视频编辑模型一键适配任意格式", "Runway", "上传视频选择宽高比，AI自动填充场景其余部分，极大降低视频制作适配多平台的技术门槛和成本。", "https://x.com/runwayml/status/2064012425884569627"],
            ["生数科技与华策影视合作：AI+影视工业化流程", "生数科技", "以Vidu视频生成大模型为技术底座设立AI视听创制中心，探索AI虚拟制作与实拍融合的新一代影视工业化流程。", "https://mp.weixin.qq.com/s?__biz=MzkzMDQ5NTQwMQ%3D%3D&mid=2247488842&idx=1&sn=3dab63189fa60b3b78c5ad72e3358791"],
            ["Apple Intelligence升级：Safari AI扩展与Home AI摄像头", "Apple", "用户可自然语言描述生成自定义Safari扩展；HomeKit摄像头利用AI分析画面生成文字摘要和自然语言搜索。", "https://www.apple.com/newsroom/2026/06/apple-intelligence-brings-powerful-ai-capabilities-into-everyday-experiences"],
        ]},
    ]
}

# ===================== Sports/Health Data =====================
sports_data = {
    "accent": "#f59e0b", "accent2": "#fbbf24",
    "bg": "#120e06", "surface": "#1a140a", "card": "#241c10",
    "border": "#3a2e18", "text": "#f0e8d0", "text_dim": "#aa9860",
    "grad": ["#b45309", "#d97706", "#f59e0b"],
    "tags": {"sports": "#f59e0b", "fitness": "#10b981", "nutrition": "#ef4444", "wellness": "#8b5cf6"},
    "stat_names": {"sports": "体坛快讯", "fitness": "健身科学", "nutrition": "营养饮食", "wellness": "身心养护"},
    "title": "运动健康日报",
    "footer": '数据来源：ESPN / NBA / FIFA / 新华网体育 / WHO / NIH / ScienceDaily 等公开体育健康媒体',
    "sections": [
        {"id": "sports", "badge": "SPORTS", "title": "体坛快讯", "emoji": "⚽", "items": [
            ["NBA总决赛：尼克斯2-0领先马刺，文班亚马面临考验", "ESPN", "尼克斯连赢G1和G2取得2-0领先，这是尼克斯本赛季季后赛第13场连胜，文班亚马需要在G3主场找回状态。", "https://www.espn.com/nba/story/_/id/48419498/nba-playoffs-2026-play-finals-schedule-scores-news-highlights-bracket-dates"],
            ["FIFA世界杯倒计时2天：6月11日墨西哥城开幕战", "FIFA", "2026年世界杯48支球队104场比赛，6月11日墨西哥城阿兹特克球场迎来开幕战，历史首次三国联合主办。", "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026"],
            ["美加墨世界杯分组赛程全解析：48队新赛制亮相", "Yahoo Sports", "2026年世界杯采用48队新赛制，完整赛程已确认，从6月11日小组赛到7月19日决赛共104场比赛。", "https://sports.yahoo.com/soccer/article/2026-fifa-world-cup-daily-schedule-every-match-date-kickoff-time-and-venue-for-all-48-teams-234515087.html"],
            ['\u201c黑马\u201d蓄势：谁将驰骋美加墨世界杯？', "新华网体育", '世界杯开赛在即，多支\u201c黑马\u201d球队蓄势待发，新赛制下小组出线名额增加，冷门概率大幅提升。', "https://www.xinhuanet.com/sports/news.htm"],
            ["国足开启世界杯前热身赛之旅", "中国新闻网", "中国国家男子足球队开启世界杯前系列热身赛，教练组通过实战检验阵容搭配和战术体系，为大赛做最后准备。", "https://www.chinanews.com.cn/sports/"],
            ["2026上海大众体育季火热开启，超百场赛事来袭", "上海体育", "2026年上海大众体育季从6月正式拉开帷幕，计划推出超百场赛事活动，涵盖路跑、骑行、球类等多个大众体育项目。", "https://www.chinanews.com.cn/ty/"],
            ["NBA总决赛G3今晚马刺主场：文班亚马能否率队扳回一城", "NBA.com", "G3将于马刺主场进行，0-2落后的马刺背水一战，文班亚马需要在主场球迷面前展现统治力。", "https://www.nba.com/news/2026-nba-finals-schedule"],
        ]},
        {"id": "fitness", "badge": "FITNESS", "title": "健身科学", "emoji": "💪", "items": [
            ["菲律宾地震后救援与运动医学应急响应", "新华网", "菲律宾强烈地震造成大量人员受伤，运动医学专家参与伤员救治与康复，凸显运动医学在灾害救援中的重要角色。", "https://english.news.cn/20260609/7ac13340cdcb49f0844575727c21c478/c.html"],
            ["NIH批准卡痛叶提取物mitragynine人体安全研究", "NIH", "美国国立卫生研究院批准卡痛叶活性成分mitragynine进入人体安全性研究，该物质可能成为阿片类药物使用障碍的潜在治疗选择。", "https://www.nih.gov/news-events/news-releases"],
            ["北京\u201c奔跑吧·少年\u201d青少年科学健身指导启动", "中新网", "北京市体育局主办青少年科学健身指导暨体质促进趣味运动会，全校1400余名师生参与，推动青少年体质提升。", "https://www.chinanews.com.cn/ty/2026/06-02/10633011.shtml"],
            ["MLB赛季进入白热化阶段：本垒打大赛即将开打", "ESPN", "2026年MLB赛季进入6月白热化阶段，全明星赛和本垒打大赛即将举行，多支球队为季后赛席位展开激烈争夺。", "https://www.espn.com/mlb"],
        ]},
        {"id": "nutrition", "badge": "NUTRITION", "title": "营养饮食", "emoji": "🥗", "items": [
            ["埃博拉疫情扩散：刚果515例确诊，WHO发布防控指南", "WHO/Lancet", "WHO和Africa CDC宣布2026年埃博拉疫情为公共卫生紧急事件，由Bundibugyo病毒引起，已蔓延至乌干达。", "https://www.who.int/emergencies/situations/ebola-outbreak---drc-2026"],
            ["地中海饮食与认知功能：新证据支持神经保护效应", "Harvard Health", "坚持地中海饮食模式与老年认知功能衰退减缓显著相关，橄榄油和坚果中多酚类物质被认为是保护大脑的关键因素。", "https://www.health.harvard.edu"],
            ["植物蛋白在运动营养领域新进展：与乳清蛋白效果相当", "ScienceDaily", "最新研究显示豌豆蛋白和大豆蛋白在促进肌肉蛋白合成方面与乳清蛋白效果相当，为素食运动员提供更多科学选择。", "https://www.sciencedaily.com/news/health_medicine/"],
        ]},
        {"id": "wellness", "badge": "WELLNESS", "title": "身心养护", "emoji": "🧘", "items": [
            ["ECDC发布刚果埃博拉疫情风险评估：跨境传播风险高", "ECDC", "欧洲疾控中心评估刚果埃博拉疫情，Bundibugyo病毒传播风险高，建议加强入境监测和跨境卫生合作。", "https://www.ecdc.europa.eu/en/ebola-outbreak-democratic-republic-congo-and-uganda"],
            ["CDC发布埃博拉旅行健康通知：关注DRC和乌干达", "CDC", "美国疾控中心发布健康咨询网络通知，提醒前往刚果和乌干达的旅行者注意埃博拉疫情，加强个人防护。", "https://www.cdc.gov/han/php/notices/han00530.html"],
            ["心理健康数字疗法监管缺失：元分析揭示仅30%有证据", "Medical News Today", "覆盖50万用户的元分析显示心理健康App效果参差不齐，仅约30%的应用有临床证据支持，专家呼吁加强数字疗法监管。", "https://www.news-medical.net/category/Medical-Research-News.aspx"],
            ["Perplexity与哈佛研究：AI智能体可降低工作压力提升满意度", "Perplexity", "3个月研究表明使用AI智能体的工人完成任务速度快87%成本低94%，且工作满意度更高，有助缓解职业压力。", "https://x.com/perplexity_ai/status/2064023455453110286"],
        ]},
    ]
}

# Write all data files
for key, data, fn in [
    ("ai", ai_data, "news_data.json"),
    ("world", world_data, "news_data_world.json"),
    ("tech", tech_data, "news_data_tech.json"),
    ("sports", sports_data, "news_data_sports.json"),
]:
    payload = {key: data}
    fp = os.path.join(BASE, fn)
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"[DATA] {fn} written ({sum(len(sec['items']) for sec in data['sections'])} items)")

print("\nAll data files ready. Now generating HTML...")
