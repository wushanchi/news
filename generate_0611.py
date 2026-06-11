#!/usr/bin/env python3
"""Generate all 5 daily report HTML files for 2026-06-11."""
import os

DATE = "2026-06-11"
DATE_CN = "2026 年 6 月 11 日"
WEEKDAY = "星期四"
WORKDIR = r"C:\Users\Wu Shanchi\WorkBuddy\2026-05-22-AI news"

# ============================================================
# AI Morning Report Data (from AI HOT API)
# ============================================================
ai_categories = {
    "models": {
        "name": "模型发布/更新", "badge": "MODELS", "icon": "🤖", "cls": "badge-models",
        "items": [
            {"title": "DiffusionGemma：文本生成速度提升4倍的开源扩散模型", "source": "Google DeepMind", "summary": "26B MoE模型推理仅激活3.8B参数，量化后适配18GB显存消费级GPU，H100上达1000+ tokens/s，Apache 2.0开源。", "url": "https://deepmind.google/blog/diffusiongemma-4x-faster-text-generation"},
            {"title": "Grok Voice 性能出色价格低廉", "source": "xAI", "summary": "Grok Voice提供最先进的性能，具有类人的时机、语调和温暖感，价格为竞争对手的一小部分。", "url": "https://x.com/xai/status/2064777588036530309"},
        ]
    },
    "products": {
        "name": "产品发布/更新", "badge": "PRODUCTS", "icon": "🚀", "cls": "badge-products",
        "items": [
            {"title": "小米发布 MiMo Code V0.1 开源终端 AI 编程助手", "source": "小米 MiMo", "summary": "开源终端AI编程助手，支持无限上下文、Agent-模型深度协同、Compose模式、MIT许可兼容Claude Code。", "url": "https://x.com/XiaomiMiMo/status/2064772356443394441"},
            {"title": "MiniMax M3 上链 0G，限时免费运行", "source": "MiniMax", "summary": "M3在0G Labs上链，支持可验证+私有计算，6月15-18日免费运行。", "url": "https://x.com/MiniMax_AI/status/2064791800884363286"},
            {"title": "Google 将保存用户的 Lens 图片和搜索音频用于 AI 训练", "source": "The Verge", "summary": "Google新增Search Services History设置，保存Lens图片和Search Live录音用于AI模型训练，用户可关闭。", "url": "https://www.theverge.com/tech/947836/google-search-privacy-settings-images-audio"},
            {"title": "Cursor Bugbot 更新：速度提升超3倍、成本降低22%", "source": "Cursor", "summary": "Bugbot代码审查运行速度提升3倍，每轮审查多发现10%bug，90%运行在三分钟内完成，新增/review命令。", "url": "https://cursor.com/blog/bugbot-updates-june-2026"},
            {"title": "Apache Burr：构建可靠 AI 代理的框架正式发布", "source": "Apache", "summary": "Apache基金会发布Burr框架，帮助开发者构建可靠AI智能体应用，强调可观测性和生产级部署能力。", "url": "https://burr.apache.org/"},
            {"title": "华为云发布全球首个端到端具身 AI 平台 CloudRobo", "source": "华为云", "summary": "华为云推出CloudRobo具身AI开发平台，覆盖从数据到部署全生命周期，基于PB级可信数据底座。", "url": "https://x.com/HuaweiCloud1/status/2064637581652852831"},
            {"title": "火山方舟版权商业化平台上线，周星驰三大电影IP入驻", "source": "火山引擎", "summary": "火山引擎上线版权合作平台，搭载Seedance 2.0视频生成模型，获周星驰《喜剧之王》等三部影片AI创作授权。", "url": "https://mp.weixin.qq.com/s/g3DxNO_3aYI4g26gQ2Yvig"},
            {"title": "OpenRouter 推出 Activity Explorer 活动探索器", "source": "OpenRouter", "summary": "可查看用户和团队在每个模型上的花费，包括token、缓存命中率、智能体及趋势，所有数据实时更新。", "url": "https://x.com/OpenRouter/status/2064730000956489889"},
        ]
    },
    "industry": {
        "name": "行业动态", "badge": "INDUSTRY", "icon": "🌍", "cls": "badge-industry",
        "items": [
            {"title": '工信部印发\u300a人工智能+信息通信\u300b创新发展实施意见', "source": "IT之家", "summary": "要求加快建设400G/800G骨干传输网络，推动5G-A/6G与AI融合发展，鼓励电信企业AI赋能传统业务。", "url": "https://www.ithome.com/0/962/456.htm"},
            {"title": "欧盟要求 Meta 向第三方 AI 助手免费开放 WhatsApp", "source": "IT之家", "summary": "欧盟委员会发布临时措施，责令Meta在反垄断调查结束前免费向第三方AI助手开放WhatsApp访问。", "url": "https://www.ithome.com/0/962/206.htm"},
            {"title": "180亿美元基金 Magnetar 用数百 AI 智能体替代分析师", "source": "Rohan Paul", "summary": "对冲基金Magnetar Capital在新产品中依靠数百个AI智能体进行股票研究，人类仅负责批准交易。", "url": "https://x.com/rohanpaul_ai/status/2064524448582267047"},
            {"title": "谷歌财务担保支撑 Anthropic 350 亿美元芯片租赁交易", "source": "Bloomberg", "summary": "Anthropic在谷歌帮助下于五个数据中心租赁高性能芯片，谷歌为租赁付款提供兜底担保。", "url": "https://www.bloomberg.com/news/videos/2026-06-10/google-s-backstops-underpin-35-bln-anthropic-chip-deal-video"},
            {"title": "eToro AI 智能体 Tori 集成 xAI 模型实现实时市场情绪分析", "source": "xAI", "summary": "eToro AI智能体Tori集成SpaceXAI文本模型，从X平台实时读取市场情绪，覆盖75国4000万用户。", "url": "https://x.ai/news/grok-etoro"},
            {"title": "Google 因 AI 模型幻觉被判负有法律责任", "source": "Gary Marcus", "summary": "一项法律裁决判定Google对其AI模型产生的幻觉内容负有法律责任，可能产生巨大影响。", "url": "https://garymarcus.substack.com/p/breaking-google-liable-for-hallucinations"},
            {"title": "OpenAI 与 Oracle 合作，用户可借助云承诺访问 Codex", "source": "OpenAI", "summary": "OpenAI与Oracle合作，用户可利用现有云服务承诺额度在Oracle云上访问OpenAI模型和Codex。", "url": "https://openai.com/index/openai-on-oracle-cloud"},
        ]
    },
    "paper": {
        "name": "论文研究", "badge": "PAPER", "icon": "📄", "cls": "badge-paper",
        "items": [
            {"title": "Anthropic 研究：AI 数小时内即可从安全补丁构建漏洞利用", "source": "The Decoder", "summary": "Anthropic安全团队发现Mythos Preview AI模型能在几小时内将安全补丁转化为可工作的漏洞利用，成本仅需数千美元。", "url": "https://the-decoder.com/anthropic-study-shows-ai-needs-hours-not-weeks-to-build-exploits-from-security-patches"},
            {"title": "Google Research 提出审计机器遗忘新框架（AISTATS 2026）", "source": "Google Research", "summary": "正则化f-散度核检验高效审计LLM机器遗忘，相比MMD等现有工具可自然控制假阳性。", "url": "https://research.google/blog/new-framework-for-auditing-machine-unlearning"},
            {"title": "百度百舸联合复旦提出 LU-KV 框架，被 ICML 2026 录用", "source": "百度智能云", "summary": "将头级KV Cache预算分配建模为全局组合优化问题，80%压缩比下性能损失小，降低显存占用和推理延迟。", "url": "https://mp.weixin.qq.com/s/oKhawmph49YYPR63T-ekaw"},
        ]
    },
    "tip": {
        "name": "技巧与观点", "badge": "TIPS", "icon": "💡", "cls": "badge-tip",
        "items": [
            {"title": "Anthropic CEO Dario Amodei 发文呼吁缩小 AI 政策差距", "source": "Anthropic", "summary": "Dario Amodei指出AI发展远超现有政策流程应对能力，Anthropic同步宣布启动三项新举措。", "url": "https://x.com/AnthropicAI/status/2064783418844762489"},
            {"title": "用好 Claude Design 的5点经验", "source": "宝玉", "summary": "加入设计系统避免AI味；先少量功能再调整；用Markup框选局部评论；注意上下文管理；通过Tweaks面板调整。", "url": "https://x.com/dotey/status/2064601571397185639"},
            {"title": "Bloomberg 深度探访：走进估值 9650 亿美元的 Anthropic", "source": "Bloomberg", "summary": "Emily Chang与Dario和Daniela Amodei深度对话，探讨创业起源、五角大楼摩擦及AI安全战略。", "url": "https://www.bloomberg.com/news/videos/2026-06-10/inside-anthropic-the-965-billion-ai-juggernaut-video"},
            {"title": "豆包 AI 误导用户损失 600 元，还帮用户起诉自己", "source": "X.PIN", "summary": "河北李先生向豆包咨询退票费被误导多花600元，豆包还帮他起草起诉状，该案已在互联网法院立案。", "url": "https://x.com/thexpin/status/2064772489310527713"},
            {"title": "Text-To-Lottie：Agent Skill + 本地预览工具开源", "source": "邵猛", "summary": "让Codex/Claude Code等Agent生成Bodymovin JSON，通过Skottie引擎在浏览器中实时验收。", "url": "https://x.com/shao__meng/status/2064508455051043008"},
            {"title": "毕业典礼频现'谈 AI 色变'，微软总裁呼吁行业回应公众担忧", "source": "IT之家", "summary": "近几周多场毕业典礼宣传AI遭嘘声，微软总裁史密斯主张AI应增强人而非取代人。", "url": "https://www.ithome.com/0/962/680.htm"},
            {"title": "亚马逊的大规模扁平化数据中心网络实践", "source": "James Hamilton", "summary": "亚马逊分享在大规模数据中心实现扁平化网络架构的工程实践，支撑超大规模集群高带宽低延迟通信。", "url": "https://perspectives.mvdirona.com/2026/06/flat-datacenter-networks-at-scale"},
            {"title": "ChatGPT 推头发变国旗颜色趣味功能 #MessiMode", "source": "ChatGPT", "summary": "用户上传照片后可使用提示词将头发变成本国国旗颜色但要看起来自然，生成创意图片。", "url": "https://x.com/ChatGPTapp/status/2064728793785450526"},
        ]
    }
}

# ============================================================
# World News Data
# ============================================================
world_categories = {
    "politics": {
        "name": "政治外交", "badge": "POLITICS", "icon": "🏛️", "cls": "badge-politics",
        "items": [
            {"title": "美伊海上冲突急剧升级：伊朗称击中18个美军目标", "source": "新华网", "summary": "伊朗革命卫队宣称击中并摧毁18个美军重要目标，同时打击位于伊拉克的美军基地和第五舰队爱国者系统。", "url": "https://www.news.cn/world/jsxw/index.html"},
            {"title": "美军否认军舰遭伊朗袭击，特朗普称与伊朗官员直接通话", "source": "新华网", "summary": "美方否认有任何军舰遭伊朗袭击，特朗普声称已与伊朗官员直接通话，但伊朗方面予以否认。", "url": "https://www.news.cn/world/jsxw/index.html"},
            {"title": "特朗普提议：伊朗一半石油换美国帮助重建", "source": "观察者网", "summary": "特朗普提出将帮助伊朗重建但要求拿走其一半石油，美伊和谈前景岌岌可危。", "url": "https://news.china.com/international/"},
            {"title": "伊朗称全面关闭霍尔木兹海峡，违规通行将受打击", "source": "正观新闻", "summary": "伊朗宣布全面关闭霍尔木兹海峡，警告任何违规通行将受到打击，国际油价应声大涨。", "url": "https://news.china.com/international/"},
            {"title": "哥伦比亚总统再次要求特朗普停止干涉哥总统选举", "source": "新华网", "summary": "哥伦比亚总统发表声明，再次强烈要求特朗普政府停止对其国内总统选举的干涉行为。", "url": "https://www.news.cn/world/jsxw/index.html"},
            {"title": "中国代表就推进中东和平提出四点主张", "source": "新华网", "summary": "中国常驻联合国代表在安理会就推进中东和平提出四点主张，呼吁各方保持克制、推动政治解决。", "url": "https://www.news.cn/world/jsxw/index.html"},
            {"title": "俄国家杜马谴责美国对古巴侵略性政策", "source": "新华社", "summary": "俄罗斯国家杜马通过决议谴责美国对古巴的侵略性政策，呼吁国际社会解除对古封锁。", "url": "https://news.china.com/international/"},
        ]
    },
    "economy": {
        "name": "经济财经", "badge": "ECONOMY", "icon": "💰", "cls": "badge-economy",
        "items": [
            {"title": "国际油价大涨金价大跌，地缘风险主导市场", "source": "新华网", "summary": "受美伊冲突升级影响，国际油价大幅上涨，金价则因美联储加息预期承压下跌，跌回2025年水平。", "url": "https://www.news.cn/world/jsxw/index.html"},
            {"title": "SpaceX 周五上市，市场热议\u201c值不值\u201d", "source": "环球时报", "summary": "SpaceX即将于周五上市，认购规模达2500亿美元超额近4倍，但市场对其估值合理性仍存分歧。", "url": "https://news.china.com/international/"},
            {"title": "德国经济面临萎缩风险，订单大减", "source": "环球时报", "summary": "德国制造业订单大幅减少，经济面临萎缩风险，作为欧洲最大经济体陷入困境引发广泛关注。", "url": "https://news.china.com/international/"},
            {"title": "日韩关注印尼\u201c收紧\u201d煤炭出口政策", "source": "环球时报", "summary": "印尼调整煤炭出口政策引发日本和韩国高度关注，两国能源供应安全面临新的不确定性。", "url": "https://news.china.com/international/"},
            {"title": "印度多地自动取款机遭遇现金荒", "source": "财联社", "summary": "印度二三线城市ATM现金短缺问题加剧，民众取现困难，折射该国金融基础设施的潜在问题。", "url": "https://news.china.com/international/"},
        ]
    },
    "major": {
        "name": "重大事件", "badge": "MAJOR", "icon": "⚡", "cls": "badge-major",
        "items": [
            {"title": "菲律宾南部地震已造成45人死亡", "source": "一财网", "summary": "菲律宾南部发生强烈地震，官方确认已有45人不幸遇难，救援工作仍在紧张进行中。", "url": "https://news.china.com/international/"},
            {"title": "伊朗战事不停，美国农民深受高油价之苦", "source": "新华网", "summary": "美伊冲突持续推高国际油价，美国农民耕种成本激增，农业部门面临严峻成本压力。", "url": "https://www.news.cn/world/jsxw/index.html"},
            {"title": "极端气候事件正成为常态，全球行动刻不容缓", "source": "光明网", "summary": "5月欧洲热如盛夏、全球极端气候事件频发，气象专家详解背后成因，警告全球行动刻不容缓。", "url": "https://news.china.com/international/"},
            {"title": "报告称2025年全球核武支出创新高，美国居首", "source": "中华网", "summary": "最新报告指出2025年全球核武器支出创下历史新高，美国一国支出超过其余八国总和。", "url": "https://news.china.com/international/"},
        ]
    },
    "society": {
        "name": "社会人文", "badge": "SOCIETY", "icon": "🌏", "cls": "badge-society",
        "items": [
            {"title": "三分之二美国人不再相信\u201c美国梦\u201d", "source": "新华网", "summary": "最新民调显示约三分之二的美国人不再相信美国梦，年轻一代对未来更加悲观。", "url": "https://news.china.com/international/"},
            {"title": "从世界杯看\u201c义乌制造\u201d以变应变", "source": "环球时报", "summary": "2026美加墨世界杯带动义乌小商品出口热潮，中国制造业以快速应变能力满足全球球迷需求。", "url": "https://news.china.com/international/"},
            {"title": "比尔·盖茨就爱泼斯坦案调查自愿作证", "source": "央视新闻", "summary": "微软创始人比尔·盖茨就爱泼斯坦案件调查自愿出庭作证，表示将协助伸张正义。", "url": "https://news.china.com/international/"},
            {"title": "票价更亲民，世界杯热身赛受追捧", "source": "环球时报", "summary": "2026世界杯临近，各队热身赛票价相较正赛更亲民，受到全球球迷热烈追捧。", "url": "https://news.china.com/international/"},
        ]
    }
}

# ============================================================
# Tech News Data
# ============================================================
tech_categories = {
    "internet": {
        "name": "互联网/软件", "badge": "INTERNET", "icon": "🌐", "cls": "badge-internet",
        "items": [
            {"title": "苹果 WWDC26 重磅发布：Siri 重构为独立 App，深度整合Gemini", "source": "苹果", "summary": "库克最后一届WWDC主持，Siri从弹窗助手升级为独立App，底层采用苹果自研+谷歌Gemini联合模型。", "url": "https://www.pconline.com.cn/qs/pc/online/10986/"},
            {"title": "iOS 27 续航延长1-2小时，macOS 27 彻底淘汰Intel芯片", "source": "苹果", "summary": "苹果WWDC26发布新系统：iOS 27续航优化、macOS 27仅支持M1及以上芯片，全面转向自研芯片。", "url": "https://www.pconline.com.cn/qs/pc/online/10986/"},
            {"title": "Anthropic 发布 Claude Fable 5，5000万行代码1天迁移", "source": "Anthropic", "summary": "Claude Fable 5性能行业领先，可在1天内完成5000万行Ruby代码迁移（人工需2个月），已提交IPO申请。", "url": "https://blog.csdn.net/BluerCat/article/details/161850284"},
            {"title": "OpenAI 秘密提交 S-1 招股文件，估值或达1万亿美元", "source": "CSDN", "summary": "OpenAI正式启动IPO进程，市场预计估值高达1万亿美元，有望成为全球估值最高的AI企业。", "url": "https://blog.csdn.net/BluerCat/article/details/161850284"},
            {"title": "微软 Build 2026 发布全系7款自研模型及二代量子芯片", "source": "微软", "summary": "微软Build大会发布首款AI推理旗舰模型，全面转向智能体时代，同时推出第二代量子芯片。", "url": "https://www.thepaper.cn/newsDetail_forward_33298254"},
            {"title": "CES Asia 2026 今日开幕，200+企业集结国产AI与芯片亮相", "source": "CES Asia", "summary": "亚洲消费电子展6月10-12日北京举办，华为、英伟达、SK电信等巨头齐聚，6G终端和人形机器人集中展示。", "url": "https://blog.csdn.net/BluerCat/article/details/161850284"},
        ]
    },
    "hardware": {
        "name": "硬件/半导体", "badge": "HARDWARE", "icon": "🔧", "cls": "badge-hardware",
        "items": [
            {"title": "MIT 芯片散热突破：金刚石+氮化镓助力6G与卫星通信", "source": "MIT", "summary": "MIT团队实现氮化镓芯片嵌入单晶金刚石散热层，彻底解决高功率芯片散热瓶颈，赋能6G通信和卫星互联网。", "url": "https://blog.csdn.net/BluerCat/article/details/161850284"},
            {"title": "工信部+国资委启动人形机器人实景实训，万台级落地在即", "source": "IT之家", "summary": "工信部与国资委联合启动2026年度人形机器人实景实训，目标年底前实现万台级规模落地。", "url": "https://blog.csdn.net/BluerCat/article/details/161850284"},
            {"title": "6G部省协同试点推进，空天地海网络成型", "source": "CSDN", "summary": "工信部启动6G试点，三年内各省最多遴选3赛道，中国6G核心专利全球占比超40%。", "url": "https://blog.csdn.net/BluerCat/article/details/161850284"},
            {"title": "全球最大27.1万立方米LNG船开工，国产高端造船领跑", "source": "CSDN", "summary": "中船集团沪东中华开工世界最大LNG运输船，我国LNG船全球市占率突破30%，订单总量全球第一。", "url": "https://blog.csdn.net/BluerCat/article/details/161850284"},
            {"title": "2026 智源大会明日开幕，图灵奖得主领衔中国大模型", "source": "量子位", "summary": "2026智源大会6月12-13日北京举办，图灵奖得主领衔，中国大模型第一梯队集结探讨AI前沿。", "url": "https://www.qbitai.com/2026/05/424551.html"},
        ]
    },
    "space": {
        "name": "航天/新能源", "badge": "SPACE", "icon": "🚀", "cls": "badge-space",
        "items": [
            {"title": "SpaceX 认购规模达2500亿美元，超额近4倍", "source": "CSDN", "summary": "SpaceX最新融资认购达2500亿美元超额近4倍，Starlink、星舰载人登月、商业发射三大业务高速增长。", "url": "https://blog.csdn.net/BluerCat/article/details/161850284"},
            {"title": "太空主题 ETF 半年吸金80亿美元，投资热潮持续", "source": "东方财富网", "summary": "太空主题ETF仅半年就吸引80亿美元资金流入，反映全球太空经济投资热潮持续升温。", "url": "https://news.china.com/international/"},
            {"title": "2026勒芒24小时耐力赛练习赛启动", "source": "勒芒赛事", "summary": "2026年勒芒24小时耐力赛练习赛正式启动，全球顶尖车队和车手齐聚法国勒芒赛道。", "url": "https://sports.qq.com/"},
            {"title": "欧佩克国家应对\u201c能源咽喉\u201d被卡的新策略", "source": "环球时报", "summary": "面对全球能源格局变化，欧佩克成员国探索应对能源出口通道受限的新策略，保障能源安全。", "url": "https://news.china.com/international/"},
        ]
    },
    "digital": {
        "name": "数字创新", "badge": "DIGITAL", "icon": "💡", "cls": "badge-digital",
        "items": [
            {"title": "世界经济论坛公布2026年技术先锋百强企业", "source": "WEF", "summary": "世界经济论坛评选100家技术先锋企业来自23国，聚焦AI基础设施构建下一代技术生态。", "url": "https://www.weforum.org/press/2026/06/new-technology-pioneers-are-building-the-infrastructure-for-the-next-era-of-ai-96a8d3e248/"},
            {"title": "苹果延迟\u201c上新\u201d引欧盟争议，欧委会拒\u201c背锅\u201d", "source": "新华社", "summary": "苹果新功能延迟在欧洲上线引发争议，欧委会否认与监管有关，称苹果未提交相关申请。", "url": "https://news.china.com/international/"},
            {"title": "韩国 AI 行情泡沫风险引发市场关注", "source": "时代周报", "summary": "韩国AI相关股票市场波动加剧，投资者担忧AI行情是否已经形成泡沫，分析人士观点分歧。", "url": "https://news.china.com/international/"},
        ]
    }
}

# ============================================================
# Sports & Health Data
# ============================================================
sh_categories = {
    "sports": {
        "name": "体坛快讯", "badge": "SPORTS", "icon": "⚽", "cls": "badge-sports",
        "items": [
            {"title": "NBA 总决赛：尼克斯 2-0 领先马刺，创季后赛13连胜", "source": "ESPN", "summary": "尼克斯在总决赛前两场客胜马刺，取得13连胜创季后赛纪录。文班亚马在纽约遭球迷辱骂。", "url": "https://www.espn.com/nba/story/_/id/48419498/nba-playoffs-2026-play-finals-schedule-scores-news-highlights-bracket-dates"},
            {"title": "NBA 总决赛 G3 激战：尼克斯回到主场迎关键战役", "source": "腾讯体育", "summary": "总决赛第三战移师纽约麦迪逊花园，尼克斯有望3-0拿到赛点，马刺亟需文班带队反扑。", "url": "https://sports.qq.com/"},
            {"title": "曝詹姆斯将向湖人索要顶薪，勇士难组四巨头", "source": "腾讯体育", "summary": "詹姆斯休赛期将向湖人索要顶薪续约合同，勇士在薪金空间紧张情况下组建四巨头前景渺茫。", "url": "https://sports.qq.com/"},
            {"title": "Faker 入选 TIME 100 Sports，六冠王传奇延续", "source": "MSN Sports", "summary": "T1战队Faker入选时代杂志百大体育人物，已斩获创纪录六届LOL全球总决赛冠军包括最近三连冠。", "url": "https://www.msn.cn/zh-cn/sports/"},
            {"title": "2026 世界杯前瞻：墨西哥 VS 南非揭幕在即", "source": "腾讯体育", "summary": "世界杯东道主墨西哥全力备战揭幕战对阵南非，希门尼斯领衔三前锋强攻阵容。", "url": "https://sports.qq.com/"},
            {"title": "凯恩：这届世界杯是我冲击冠军最佳机会", "source": "腾讯体育", "summary": "英格兰队长凯恩接受采访表示本届世界杯是其职业生涯冲击最高荣誉的最佳机会。", "url": "https://sports.qq.com/"},
            {"title": "WTA500 伦敦站激战正酣，郑钦文备受关注", "source": "腾讯体育", "summary": "WTA500伦敦站第3日比赛进行中，阿尼西莫娃、姆博科、约维奇出战，中国选手郑钦文备受关注。", "url": "https://sports.qq.com/"},
        ]
    },
    "fitness": {
        "name": "健身科学", "badge": "FITNESS", "icon": "💪", "cls": "badge-fitness",
        "items": [
            {"title": "喝茶或可预防心脏病、糖尿病及认知衰退", "source": "ScienceDaily", "summary": "大型综述研究表明饮茶有助于预防心脏病、糖尿病、癌症及年龄相关肌肉流失，但饮用方式有讲究。", "url": "https://www.sciencedaily.com/news/health_medicine/fitness/"},
            {"title": "超加工食品与注意力下降、思维迟缓关联", "source": "ScienceDaily", "summary": "对2100多名成年人研究发现，食用更多超加工食品与注意力和思维处理速度较差相关。", "url": "https://www.sciencedaily.com/news/mind_brain/"},
            {"title": "NIH 研究揭示环境暴露组对健康的全方位影响", "source": "NIH", "summary": "NIH最新研究利用新工具和方法探索环境因素从多维度影响人类健康，推动精准公共卫生。", "url": "https://www.nih.gov/news-events/nih-research-matters"},
            {"title": "国际足联禁止球迷带水瓶进场馆引发争议", "source": "NBC", "summary": "国际足联更新世界杯场馆行为准则不再允许携带可重复使用水瓶，球迷只能在场馆内购买瓶装水。", "url": "https://baijiahao.baidu.com/s?id=1867140171641770389"},
        ]
    },
    "nutrition": {
        "name": "营养饮食", "badge": "NUTRITION", "icon": "🥗", "cls": "badge-nutrition",
        "items": [
            {"title": "NIH 启动 mitragynine（kratom 提取物）阿片类戒断研究", "source": "NIH", "summary": "NIH批准mitragynine人体安全性研究，探索kratom提取物用于阿片类药物使用障碍的潜在治疗方案。", "url": "https://www.nih.gov/news-events/news-releases"},
            {"title": "美国农民深受高油价之苦：耕种成本激增", "source": "新华网", "summary": "美伊冲突推高油价，美国农民耕种和运输成本大幅攀升，对农业生产和食品价格产生连锁影响。", "url": "https://www.news.cn/world/jsxw/index.html"},
            {"title": "2026 世界沙滩排球巡回赛杭州站即将开赛", "source": "体育", "summary": "世界沙排巡回赛6月25-28日在杭州举办，全球顶尖沙排选手将竞逐，赛事融合体育与旅游。", "url": "https://baijiahao.baidu.com/s?id=1866779042344748108"},
        ]
    },
    "wellness": {
        "name": "身心养护", "badge": "WELLNESS", "icon": "🧘", "cls": "badge-wellness",
        "items": [
            {"title": "全球极端气候常态化：心理健康挑战日益突出", "source": "光明网", "summary": "气象专家警告极端气候事件正成为常态，全球各地高温、洪水频发对居民心理健康构成新挑战。", "url": "https://news.china.com/international/"},
            {"title": "2026 中俄成人足球对抗赛哈尔滨开赛，促体育文化交流", "source": "人民网", "summary": "2026中俄成人足球对抗赛在哈尔滨开赛，以足球为纽带深化两国体育文化互鉴和民间友好交流。", "url": "http://ent.people.com.cn/n1/2026/0607/c1012-40735302.html"},
            {"title": "杭州多项体育赛事密集举行：男篮热身+沙排巡回", "source": "体育", "summary": "杭州6月迎来中澳荷男篮热身赛和世界沙排巡回赛等顶级赛事，全民体育氛围浓厚。", "url": "https://baijiahao.baidu.com/s?id=1866779042344748108"},
        ]
    }
}

# ============================================================
# CSS Templates
# ============================================================

CSS_AI = """:root{--c-bg:#0f0c0a;--c-surface:#1a1410;--c-card:#221a14;--c-border:#3a2a1e;--c-text:#f0e6dc;--c-text-dim:#a89880;--c-accent:#ff6a3d;--c-accent2:#ff8c5a;--c-accent-glow:rgba(ff6a3d,0.18);--c-tag-models:#e85d3a;--c-tag-products:#f08c4a;--c-tag-industry:#d4a24e;--c-tag-paper:#c07a5e;--c-tag-tip:#b8956e;--c-grad-start:#ff5c28;--c-grad-mid:#e8452e;--c-grad-end:#c8203a;--radius:14px;--radius-sm:8px;--transition:0.28s cubic-bezier(0.4,0,0.2,1);--font-mono:'SF Mono','Cascadia Code','Consolas','Menlo',monospace;--font-sans:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei','Helvetica Neue',sans-serif}"""

CSS_WORLD = """:root{--c-bg:#0a0f1a;--c-surface:#101828;--c-card:#182030;--c-border:#1e3a5f;--c-text:#e0e8f0;--c-text-dim:#8899aa;--c-accent:#3b82f6;--c-accent2:#60a5fa;--c-accent-glow:rgba(3b82f6,0.18);--c-tag-politics:#3b82f6;--c-tag-economy:#6366f1;--c-tag-major:#ef4444;--c-tag-society:#8b5cf6;--c-grad-start:#1e40af;--c-grad-mid:#2563eb;--c-grad-end:#1d4ed8;--radius:14px;--radius-sm:8px;--transition:0.28s cubic-bezier(0.4,0,0.2,1);--font-mono:'SF Mono','Cascadia Code','Consolas','Menlo',monospace;--font-sans:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei','Helvetica Neue',sans-serif}"""

CSS_TECH = """:root{--c-bg:#0a120e;--c-surface:#101a14;--c-card:#18241c;--c-border:#1e3a2a;--c-text:#dce8e0;--c-text-dim:#88aa90;--c-accent:#10b981;--c-accent2:#34d399;--c-accent-glow:rgba(10b981,0.18);--c-tag-internet:#10b981;--c-tag-hardware:#0ea5e9;--c-tag-space:#f59e0b;--c-tag-digital:#8b5cf6;--c-grad-start:#065f46;--c-grad-mid:#059669;--c-grad-end:#047857;--radius:14px;--radius-sm:8px;--transition:0.28s cubic-bezier(0.4,0,0.2,1);--font-mono:'SF Mono','Cascadia Code','Consolas','Menlo',monospace;--font-sans:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei','Helvetica Neue',sans-serif}"""

CSS_SH = """:root{--c-bg:#120e06;--c-surface:#1a140a;--c-card:#241c10;--c-border:#3a2e18;--c-text:#f0e8d0;--c-text-dim:#aa9860;--c-accent:#f59e0b;--c-accent2:#fbbf24;--c-accent-glow:rgba(f59e0b,0.18);--c-tag-sports:#f59e0b;--c-tag-fitness:#10b981;--c-tag-nutrition:#ef4444;--c-tag-wellness:#8b5cf6;--c-grad-start:#b45309;--c-grad-mid:#d97706;--c-grad-end:#f59e0b;--radius:14px;--radius-sm:8px;--transition:0.28s cubic-bezier(0.4,0,0.2,1);--font-mono:'SF Mono','Cascadia Code','Consolas','Menlo',monospace;--font-sans:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei','Helvetica Neue',sans-serif}"""

COMMON_CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--font-sans);background:var(--c-bg);color:var(--c-text);line-height:1.6;min-height:100vh;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.hero{position:relative;background:linear-gradient(135deg,var(--c-grad-start),var(--c-grad-mid) 50%,var(--c-grad-end));padding:60px 24px 56px;text-align:center;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,0.08),transparent 60%),radial-gradient(circle at 70% 80%,rgba(ff6a3d,0.12),transparent 50%)}
.hero-date{position:relative;font-size:15px;font-weight:500;color:rgba(255,255,255,0.75);letter-spacing:0.06em;margin-bottom:8px}
.hero-title{position:relative;font-size:clamp(32px,6vw,52px);font-weight:800;letter-spacing:-0.02em;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,0.25)}
.hero-total{position:relative;display:inline-block;margin-top:12px;font-size:13px;font-weight:500;background:rgba(255,255,255,0.15);backdrop-filter:blur(6px);padding:6px 18px;border-radius:20px;color:rgba(255,255,255,0.9)}
.stats-wrap{position:relative;margin-top:-28px;padding:0 16px;z-index:2}
.stats{max-width:900px;margin:0 auto;display:flex;flex-wrap:wrap;gap:10px;justify-content:center;background:var(--c-surface);border:1px solid var(--c-border);border-radius:var(--radius);padding:18px 20px;box-shadow:0 2px 12px rgba(0,0,0,0.25)}
.stat{display:flex;align-items:center;gap:7px;font-size:14px;color:var(--c-text-dim)}
.stat-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.stat strong{color:var(--c-text);font-weight:600}
.nav-wrap{position:sticky;top:0;z-index:10;background:var(--c-bg);backdrop-filter:blur(16px);border-bottom:1px solid var(--c-border);padding:0 16px}
.nav{max-width:900px;margin:0 auto;display:flex;gap:4px;overflow-x:auto;padding:10px 0;scrollbar-width:none}
.nav::-webkit-scrollbar{display:none}
.nav a{display:flex;align-items:center;gap:5px;padding:8px 16px;border-radius:20px;font-size:13px;font-weight:500;white-space:nowrap;color:var(--c-text-dim);transition:var(--transition)}
.nav a:hover{color:var(--c-text);background:var(--c-card)}
.nav a .nav-count{font-size:11px;background:var(--c-border);padding:1px 7px;border-radius:10px;color:var(--c-text-dim)}
.main{max-width:900px;margin:0 auto;padding:32px 16px 60px}
.section{margin-bottom:40px}
.section-header{display:flex;align-items:center;gap:10px;margin-bottom:18px;padding-bottom:10px;border-bottom:2px solid var(--c-border)}
.section-badge{font-size:11px;font-weight:700;letter-spacing:0.04em;padding:4px 12px;border-radius:4px;text-transform:uppercase;color:#fff}
.section-header h2{font-size:20px;font-weight:700;color:var(--c-text)}
.section-count{font-size:13px;color:var(--c-text-dim);margin-left:auto}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.card{background:var(--c-card);border:1px solid var(--c-border);border-radius:var(--radius);padding:18px;display:flex;flex-direction:column;gap:10px;transition:transform var(--transition),box-shadow var(--transition);position:relative;overflow:hidden}
.card:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(0,0,0,0.35);border-color:var(--c-accent)}
.card::after{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--c-accent),var(--c-accent2));opacity:0;transition:opacity var(--transition)}
.card:hover::after{opacity:1}
.card-top{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}
.card-num{font-family:var(--font-mono);font-size:12px;font-weight:700;color:var(--c-accent);background:var(--c-accent-glow);padding:2px 10px;border-radius:var(--radius-sm);flex-shrink:0}
.card-source{font-size:11px;font-weight:500;padding:3px 10px;border-radius:12px;background:rgba(255,255,255,0.06);color:var(--c-text-dim);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:160px}
.card-title{font-size:15px;font-weight:700;line-height:1.45;color:var(--c-text);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.card-summary{font-size:13px;line-height:1.55;color:var(--c-text-dim);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.card-actions{display:flex;align-items:center;gap:8px;margin-top:auto}
.card-link{margin-left:auto;font-size:12px;font-weight:600;color:var(--c-accent2);padding:5px 14px;border:1px solid rgba(ff8c5a,0.3);border-radius:var(--radius-sm);transition:var(--transition);display:inline-flex;align-items:center;gap:4px}
.card-link:hover{background:var(--c-accent);color:#fff;border-color:var(--c-accent)}
.card-link svg{width:14px;height:14px;flex-shrink:0}
.card-animate{opacity:0;transform:translateY(24px);transition:opacity 0.5s ease,transform 0.5s ease}
.card-animate.visible{opacity:1;transform:translateY(0)}
.footer{text-align:center;padding:24px 16px 40px;font-size:12px;color:var(--c-text-dim);opacity:0.6;border-top:1px solid var(--c-border)}
.footer a{color:var(--c-accent2)}
@media(max-width:600px){.hero{padding:44px 16px 40px}.cards{grid-template-columns:1fr}.stats{gap:6px;padding:14px}.stat{font-size:12px}.nav a{padding:6px 12px;font-size:12px}}
"""

JS_SCRIPT = """
<script>
const observer=new IntersectionObserver((e)=>{e.forEach((e)=>{e.isIntersecting&&e.target.classList.add('visible')})},{threshold:0.1});
document.querySelectorAll('.card-animate').forEach((e)=>observer.observe(e));
</script>
"""

SVG_ARROW = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>"""


def card_html(num, item, accent=None):
    return f"""<div class="card card-animate">
  <div class="card-top">
    <span class="card-num">#{num:02d}</span>
    <span class="card-source">{item['source']}</span>
  </div>
  <div class="card-title">{item['title']}</div>
  <div class="card-summary">{item['summary']}</div>
  <div class="card-actions">
    <a class="card-link" href="{item['url']}" target="_blank" rel="noopener noreferrer">
      阅读原文
      {SVG_ARROW}
    </a>
  </div>
</div>"""


def build_section(key, cat, global_num):
    items_html = []
    n = global_num
    for item in cat["items"]:
        items_html.append(card_html(n, item))
        n += 1
    count = len(cat["items"])
    badge_cls = cat.get("cls", f"badge-{key}")
    return f"""<section class="section" id="{key}">
  <div class="section-header">
    <span class="section-badge {badge_cls}">{cat['badge']}</span>
    <h2>{cat['icon']} {cat['name']}</h2>
    <span class="section-count">{count} 条</span>
  </div>
  <div class="cards">
{chr(10).join(items_html)}
  </div>
</section>""", n


def gen_daily_html(css_root, hero_title, hero_total, stats_items, nav_items, sections_html, footer_text, date, weekday, extra_head="", accent_override=""):
    """Generate a complete daily report HTML."""
    # Build stats
    stats_parts = []
    for _, label, count, color in stats_items:
        parts = []
        parts.append(f'    <div class="stat"><span class="stat-dot" style="background:{color}"></span> {label} <strong>{count}</strong></div>')
        stats_parts.append('\n'.join(parts) if isinstance(parts, list) else parts)
    stats_html = '\n'.join([f'    <div class="stat"><span class="stat-dot" style="background:{color}"></span> {label} <strong>{count}</strong></div>' for _, label, count, color in stats_items])

    # Build nav
    nav_parts = []
    for key, label, count in nav_items:
        nav_parts.append(f'  <a href="#{key}"><span>{label}</span><span class="nav-count">{count}</span></a>')
    nav_html = '\n'.join(nav_parts)

    hero_before = accent_override or css_root.split('--c-grad-end:')[1].split(';')[0] if '--c-grad-end' in css_root else ''

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{hero_title} · {date}</title>
<style>
{css_root}
{COMMON_CSS}
</style>
{extra_head}
</head>
<body>
<header class="hero">
  <div class="hero-date">{DATE_CN} · {WEEKDAY}</div>
  <h1 class="hero-title">{hero_title}</h1>
  <div class="hero-total">今日 {hero_total} · 北京时间 08:50 生成</div>
</header>
<div class="stats-wrap">
  <div class="stats">
{stats_html}
  </div>
</div>
<nav class="nav-wrap"><div class="nav">
{nav_html}
</div></nav>
<main class="main">
{sections_html}
</main>
<footer class="footer">
{footer_text}
</footer>
{JS_SCRIPT}
</body>
</html>"""


def gen_ai():
    """Generate AI morning report."""
    css = CSS_AI + """
.badge-models{background:var(--c-tag-models)}.badge-products{background:var(--c-tag-products)}.badge-industry{background:var(--c-tag-industry)}.badge-paper{background:var(--c-tag-paper)}.badge-tip{background:var(--c-tag-tip)}
"""

    sections = []
    gn = 1
    cat_order = [("models", ai_categories["models"]), ("products", ai_categories["products"]),
                 ("industry", ai_categories["industry"]), ("paper", ai_categories["paper"]),
                 ("tip", ai_categories["tip"])]
    for key, cat in cat_order:
        sec, gn = build_section(key, cat, gn)
        sections.append(sec)

    total = gn - 1
    counts = {k: len(v["items"]) for k, v in ai_categories.items()}
    stats = [
        ("models", "模型", counts["models"], "var(--c-tag-models)"),
        ("products", "产品", counts["products"], "var(--c-tag-products)"),
        ("industry", "行业", counts["industry"], "var(--c-tag-industry)"),
        ("paper", "论文", counts["paper"], "var(--c-tag-paper)"),
        ("tip", "观点", counts["tip"], "var(--c-tag-tip)"),
    ]
    nav = [
        ("models", "🤖 模型发布/更新", counts["models"]),
        ("products", "🚀 产品发布/更新", counts["products"]),
        ("industry", "🌍 行业动态", counts["industry"]),
        ("paper", "📄 论文研究", counts["paper"]),
        ("tip", "💡 技巧与观点", counts["tip"]),
    ]
    footer = '<p>数据来源：<a href="https://aihot.virxact.com" target="_blank">aihot.virxact.com</a> ｜ AI 资讯社区日报</p>\n<p>生成时间：2026-06-11 08:50 北京时间</p>'

    html = gen_daily_html(css, "AI 晨报", f"{total} 条", stats, nav, "\n".join(sections), footer, DATE, WEEKDAY)
    return html, total, counts


def gen_world():
    """Generate world news report."""
    css = CSS_WORLD + """
.badge-politics{background:var(--c-tag-politics)}.badge-economy{background:var(--c-tag-economy)}.badge-major{background:var(--c-tag-major)}.badge-society{background:var(--c-tag-society)}
"""

    sections = []
    gn = 1
    cat_order = [("politics", world_categories["politics"]), ("economy", world_categories["economy"]),
                 ("major", world_categories["major"]), ("society", world_categories["society"])]
    for key, cat in cat_order:
        sec, gn = build_section(key, cat, gn)
        sections.append(sec)

    total = gn - 1
    counts = {k: len(v["items"]) for k, v in world_categories.items()}
    stats = [
        ("politics", "政治外交", counts["politics"], "var(--c-tag-politics)"),
        ("economy", "经济财经", counts["economy"], "var(--c-tag-economy)"),
        ("major", "重大事件", counts["major"], "var(--c-tag-major)"),
        ("society", "社会人文", counts["society"], "var(--c-tag-society)"),
    ]
    nav = [
        ("politics", "🏛️ 政治外交", counts["politics"]),
        ("economy", "💰 经济财经", counts["economy"]),
        ("major", "⚡ 重大事件", counts["major"]),
        ("society", "🌏 社会人文", counts["society"]),
    ]
    footer = '<p>数据来源：新华网 / 环球时报 / 央视新闻 / Reuters / CNN / BBC 等公开新闻源</p>\n<p>生成时间：2026-06-11 08:50 北京时间</p>'

    html = gen_daily_html(css, "国际焦点日报", f"{total} 条", stats, nav, "\n".join(sections), footer, DATE, WEEKDAY)
    return html, total, counts


def gen_tech():
    """Generate tech news report."""
    css = CSS_TECH + """
.badge-internet{background:var(--c-tag-internet)}.badge-hardware{background:var(--c-tag-hardware)}.badge-space{background:var(--c-tag-space)}.badge-digital{background:var(--c-tag-digital)}
"""

    sections = []
    gn = 1
    cat_order = [("internet", tech_categories["internet"]), ("hardware", tech_categories["hardware"]),
                 ("space", tech_categories["space"]), ("digital", tech_categories["digital"])]
    for key, cat in cat_order:
        sec, gn = build_section(key, cat, gn)
        sections.append(sec)

    total = gn - 1
    counts = {k: len(v["items"]) for k, v in tech_categories.items()}
    stats = [
        ("internet", "互联网/软件", counts["internet"], "var(--c-tag-internet)"),
        ("hardware", "硬件/半导体", counts["hardware"], "var(--c-tag-hardware)"),
        ("space", "航天/新能源", counts["space"], "var(--c-tag-space)"),
        ("digital", "数字创新", counts["digital"], "var(--c-tag-digital)"),
    ]
    nav = [
        ("internet", "🌐 互联网/软件", counts["internet"]),
        ("hardware", "🔧 硬件/半导体", counts["hardware"]),
        ("space", "🚀 航天/新能源", counts["space"]),
        ("digital", "💡 数字创新", counts["digital"]),
    ]
    footer = '<p>数据来源：TechCrunch / The Verge / IT之家 / 36氪 / CSDN / 量子位 等公开科技媒体</p>\n<p>生成时间：2026-06-11 08:50 北京时间</p>'

    html = gen_daily_html(css, "科技日报", f"{total} 条", stats, nav, "\n".join(sections), footer, DATE, WEEKDAY)
    return html, total, counts


def gen_sh():
    """Generate sports & health report."""
    css = CSS_SH + """
.badge-sports{background:var(--c-tag-sports)}.badge-fitness{background:var(--c-tag-fitness)}.badge-nutrition{background:var(--c-tag-nutrition)}.badge-wellness{background:var(--c-tag-wellness)}
"""

    sections = []
    gn = 1
    cat_order = [("sports", sh_categories["sports"]), ("fitness", sh_categories["fitness"]),
                 ("nutrition", sh_categories["nutrition"]), ("wellness", sh_categories["wellness"])]
    for key, cat in cat_order:
        sec, gn = build_section(key, cat, gn)
        sections.append(sec)

    total = gn - 1
    counts = {k: len(v["items"]) for k, v in sh_categories.items()}
    stats = [
        ("sports", "体坛快讯", counts["sports"], "var(--c-tag-sports)"),
        ("fitness", "健身科学", counts["fitness"], "var(--c-tag-fitness)"),
        ("nutrition", "营养饮食", counts["nutrition"], "var(--c-tag-nutrition)"),
        ("wellness", "身心养护", counts["wellness"], "var(--c-tag-wellness)"),
    ]
    nav = [
        ("sports", "⚽ 体坛快讯", counts["sports"]),
        ("fitness", "💪 健身科学", counts["fitness"]),
        ("nutrition", "🥗 营养饮食", counts["nutrition"]),
        ("wellness", "🧘 身心养护", counts["wellness"]),
    ]
    footer = '<p>数据来源：ESPN / NBA / Sky Sports / 腾讯体育 / ScienceDaily / NIH / Harvard Health 等公开媒体</p>\n<p>生成时间：2026-06-11 08:50 北京时间</p>'

    html = gen_daily_html(css, "运动健康日报", f"{total} 条", stats, nav, "\n".join(sections), footer, DATE, WEEKDAY)
    return html, total, counts


def gen_wechat(all_data):
    """Generate WeChat article HTML."""
    ai_models, ai_products, ai_industry, ai_paper, ai_tip = all_data["ai"]
    world_politics, world_economy, world_major, world_society = all_data["world"]
    tech_internet, tech_hardware, tech_space, tech_digital = all_data["tech"]
    sh_sports, sh_fitness, sh_nutrition, sh_wellness = all_data["sh"]

    def wechat_item(source, title, desc=""):
        desc_html = f'  <div class="item-desc">{desc}</div>' if desc else ""
        return f"""<div class="item">
  <div class="item-source">{source}</div>
  <div class="item-title">{title}</div>{desc_html}
</div>"""

    def wechat_section(color, icon, title, items):
        items_html = "\n".join(wechat_item(s, t, d if d else "") for t, s, d in items[:4])
        if not items:
            items_html = '<div class="item"><div class="item-desc">（今日暂未收录）</div></div>'
        return f"""<div class="section">
  <div class="section-head" style="border-left:4px solid {color}">
    <h2>{icon} {title}</h2>
  </div>
  <div class="item-list">
{items_html}
  </div>
</div>"""

    # Extract simplified items
    def extract(items_list):
        return [(it["title"], it["source"], it["summary"]) for it in items_list]

    # Build sections
    sections = []

    # AI block
    sections.append(f'<div class="report-block"><div class="report-label" style="background:#ff6a3d">AI 晨报 · {all_data["ai_counts"]["models"] + all_data["ai_counts"]["products"] + all_data["ai_counts"]["industry"] + all_data["ai_counts"]["paper"] + all_data["ai_counts"]["tip"]}条</div>')
    sections.append(wechat_section("#ff6a3d", "🤖", "模型发布/更新" + (f"（{all_data['ai_counts']['models']}条）" if all_data['ai_counts']['models'] else "（今日暂未收录）"), extract(ai_models)))
    sections.append(wechat_section("#ff6a3d", "🚀", "产品发布/更新", extract(ai_products)))
    sections.append(wechat_section("#ff6a3d", "🌍", "行业动态", extract(ai_industry)))
    sections.append(wechat_section("#ff6a3d", "📄", "论文研究" + (f"（{all_data['ai_counts']['paper']}条）" if all_data['ai_counts']['paper'] else "（今日暂未收录）"), extract(ai_paper)))
    sections.append(wechat_section("#ff6a3d", "💡", "技巧与观点", extract(ai_tip)))
    sections.append('</div>')

    # World block
    sections.append(f'<div class="report-block"><div class="report-label" style="background:#3b82f6">国际焦点 · {all_data["world_counts"]["politics"] + all_data["world_counts"]["economy"] + all_data["world_counts"]["major"] + all_data["world_counts"]["society"]}条</div>')
    sections.append(wechat_section("#3b82f6", "🏛️", "政治外交", extract(world_politics)))
    sections.append(wechat_section("#3b82f6", "💰", "经济财经", extract(world_economy)))
    sections.append(wechat_section("#3b82f6", "⚡", "重大事件", extract(world_major)))
    sections.append(wechat_section("#3b82f6", "🌏", "社会人文", extract(world_society)))
    sections.append('</div>')

    # Tech block
    sections.append(f'<div class="report-block"><div class="report-label" style="background:#10b981">科技日报 · {all_data["tech_counts"]["internet"] + all_data["tech_counts"]["hardware"] + all_data["tech_counts"]["space"] + all_data["tech_counts"]["digital"]}条</div>')
    sections.append(wechat_section("#10b981", "🌐", "互联网/软件", extract(tech_internet)))
    sections.append(wechat_section("#10b981", "🔧", "硬件/半导体", extract(tech_hardware)))
    sections.append(wechat_section("#10b981", "🚀", "航天/新能源", extract(tech_space)))
    sections.append(wechat_section("#10b981", "💡", "数字创新", extract(tech_digital)))
    sections.append('</div>')

    # Sports block
    sections.append(f'<div class="report-block"><div class="report-label" style="background:#f59e0b">运动健康 · {all_data["sh_counts"]["sports"] + all_data["sh_counts"]["fitness"] + all_data["sh_counts"]["nutrition"] + all_data["sh_counts"]["wellness"]}条</div>')
    sections.append(wechat_section("#f59e0b", "⚽", "体坛快讯", extract(sh_sports)))
    sections.append(wechat_section("#f59e0b", "💪", "健身科学", extract(sh_fitness)))
    sections.append(wechat_section("#f59e0b", "🥗", "营养饮食", extract(sh_nutrition)))
    sections.append(wechat_section("#f59e0b", "🧘", "身心养护", extract(sh_wellness)))
    sections.append('</div>')

    wechat_html = f"""<!DOCTYPE html>
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
<header class="header">
  <div class="header-date">{DATE_CN} · {WEEKDAY}</div>
  <h1>📰 每日晨报 · 综合版</h1>
  <div class="header-sub">AI + 国际 + 科技 + 运动健康 · 一站速览今日要闻</div>
</header>

{chr(10).join(sections)}

<footer class="footer">
  <p>📌 每日更新，欢迎关注</p>
  <p>🔗 完整日报：<a href="https://wushanchi.github.io/news/" target="_blank">https://wushanchi.github.io/news/</a></p>
  <p style="margin-top:8px">数据来源：AI HOT API / 新华网 / 环球时报 / TechCrunch / ESPN / NIH 等公开信息源</p>
  <p>生成时间：2026-06-11 08:50 北京时间</p>
</footer>
</body>
</html>"""
    return wechat_html


def main():
    os.chdir(WORKDIR)

    # Collect all data for wechat
    all_data = {
        "ai": [ai_categories["models"]["items"], ai_categories["products"]["items"],
               ai_categories["industry"]["items"], ai_categories["paper"]["items"],
               ai_categories["tip"]["items"]],
        "world": [world_categories["politics"]["items"], world_categories["economy"]["items"],
                  world_categories["major"]["items"], world_categories["society"]["items"]],
        "tech": [tech_categories["internet"]["items"], tech_categories["hardware"]["items"],
                 tech_categories["space"]["items"], tech_categories["digital"]["items"]],
        "sh": [sh_categories["sports"]["items"], sh_categories["fitness"]["items"],
               sh_categories["nutrition"]["items"], sh_categories["wellness"]["items"]],
        "ai_counts": {k: len(v["items"]) for k, v in ai_categories.items()},
        "world_counts": {k: len(v["items"]) for k, v in world_categories.items()},
        "tech_counts": {k: len(v["items"]) for k, v in tech_categories.items()},
        "sh_counts": {k: len(v["items"]) for k, v in sh_categories.items()},
    }

    # Generate AI morning
    ai_html, ai_total, ai_counts = gen_ai()
    with open("ai-morning-2026-06-11.html", "w", encoding="utf-8") as f:
        f.write(ai_html)
    print(f"✅ AI 晨报: ai-morning-2026-06-11.html ({ai_total}条) 模型{ai_counts['models']}/产品{ai_counts['products']}/行业{ai_counts['industry']}/论文{ai_counts['paper']}/观点{ai_counts['tip']}")

    # Generate World
    world_html, world_total, world_counts = gen_world()
    with open("world-news-2026-06-11.html", "w", encoding="utf-8") as f:
        f.write(world_html)
    print(f"✅ 国际焦点: world-news-2026-06-11.html ({world_total}条) 政治{world_counts['politics']}/经济{world_counts['economy']}/重大{world_counts['major']}/社会{world_counts['society']}")

    # Generate Tech
    tech_html, tech_total, tech_counts = gen_tech()
    with open("tech-news-2026-06-11.html", "w", encoding="utf-8") as f:
        f.write(tech_html)
    print(f"✅ 科技日报: tech-news-2026-06-11.html ({tech_total}条) 互联网{tech_counts['internet']}/硬件{tech_counts['hardware']}/航天{tech_counts['space']}/创新{tech_counts['digital']}")

    # Generate Sports & Health
    sh_html, sh_total, sh_counts = gen_sh()
    with open("sports-health-2026-06-11.html", "w", encoding="utf-8") as f:
        f.write(sh_html)
    print(f"✅ 运动健康: sports-health-2026-06-11.html ({sh_total}条) 体坛{sh_counts['sports']}/健身{sh_counts['fitness']}/营养{sh_counts['nutrition']}/身心{sh_counts['wellness']}")

    # Generate WeChat article
    wechat_html = gen_wechat(all_data)
    with open("wechat-article-2026-06-11.html", "w", encoding="utf-8") as f:
        f.write(wechat_html)
    print(f"✅ 公众号文章: wechat-article-2026-06-11.html")

    print("\n🎉 所有 5 个日报文件已生成完毕！")


if __name__ == "__main__":
    main()
