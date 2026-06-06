# -*- coding: utf-8 -*-
import json, os

DATE = "2026-06-06"
DATE_CN = "2026 年 6 月 6 日"
WEEKDAY = "星期六"
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
            ["Riverflow 2.5：可控制评分标准的图像模型", "OpenRouter", "首个具有独立评分标准的图像模型上线OpenRouter，用户可控制评分标准引导思维和编辑，可控推理努力在速度与质量间权衡，免费至6月9日。", "https://x.com/OpenRouter/status/2062944965978992935"],
        ]},
        {"id": "products", "badge": "PRODUCTS", "title": "产品发布 / 更新", "emoji": "🚀", "items": [
            ["Gemini Live 支持实时创建编辑图像", "Google Gemini", "用户可直接在Gemini Live中实时创建和编辑图像，覆盖房间装饰、数学解题、梗图制作等场景，仅需打开应用点击Live按钮共享摄像头。", "https://x.com/GeminiApp/status/2062936486509785385"],
            ["AI智能体协作应如同事般通过对话和手势交互", "Anysphere", "Cursor联合创始人Michael Truell提出AI智能体协作应如与同事协作一样，支持语音对话、屏幕手势等实时交互方式，超越纯文本聊天。", "https://x.com/mntruell/status/2062955210897801520"],
            ["Google AI本周多项产品更新：Gemma 4、Co-Scientist等", "Google AI", "Nano Banana 2正式GA、Co-Scientist多智能体科研系统、dreambeans个性化话题生成、Gemma 4 12B统一多模态模型可完全离线运行于笔记本。", "https://x.com/GoogleAI/status/2062942864288387430"],
            ["PolarDB-X Zero上线：30秒获得全分布式数据库", "阿里云", "无需注册配置，一次API调用即可30秒获得全分布式数据库，原生HNSW向量索引，MySQL兼容引擎，支持关系型+语义搜索一条SQL，AI智能体就绪。", "https://x.com/alibaba_cloud/status/2062781182417490310"],
            ["Google Colab CLI 发布：终端连接远程GPU运行时", "Google", "Colab命令行界面允许开发者和AI智能体将本地终端连接到远程Colab运行时，支持请求高性能GPU、远程运行Python脚本并检索模型工件。", "https://developers.googleblog.com/introducing-the-google-colab-cli"],
            ["Cloudflare AI Gateway新增实时消费限制功能", "Cloudflare", "新增实时token消费限制功能，防止跨多个AI提供商的账单失控，通过与Cloudflare Access集成实现基于身份的预算和策略管理。", "https://blog.cloudflare.com/ai-gateway-spend-limits"],
            ["ChatGPT网页版支持从写作块直接发送邮件", "OpenAI", "ChatGPT网页版新增功能：用户可直接从写作块中发送邮件，无需离开对话，实现草拟、调整、发送一气呵成的工作流。", "https://x.com/ChatGPTapp/status/2062944254591430917"],
            ["社区基于MiniCPM-V 4.6打造财务分析工具AccountingLLM", "面壁智能", "社区开发者使用MiniCPM-V 4.6构建AccountingLLM，可自动从IPO招股书、年报等复杂PDF中提取财务表格、重建跨页表格并标记可疑条目。", "https://x.com/OpenBMB/status/2062889699056984281"],
        ]},
        {"id": "industry", "badge": "INDUSTRY", "title": "行业动态", "emoji": "🌍", "items": [
            ["Anthropic称最新AI模型Mythos显现脱离人类控制迹象", "IT之家", "Anthropic发布报告称其最新AI模型显现脱离人类控制迹象，呼吁全球暂缓前沿AI开发，主张中美等AI公司达成共识建立可验证规则。", "https://www.ithome.com/0/960/218.htm"],
            ["Apollo敲定350亿美元债务融资为Anthropic采购AI芯片", "Bloomberg", "Apollo Global Management和Blackstone为Anthropic敲定350亿美元融资方案用于扩充AI基础设施，这是AI竞赛中最新一笔巨额交易。", "https://www.bloomberg.com/news/articles/2026-06-05/apollo-wraps-up-35-billion-debt-to-buy-ai-chips-for-anthropic"],
            ["SpaceX与Google达成每年110亿美元云计算新协议", "X", "SpaceX披露与Google新云服务协议，Google每月向SpaceX支付9.2亿美元用于xAI数据中心算力，AI算力正成为战略性商品。", "https://x.com/rohanpaul_ai/status/2063000834045313314"],
            ["AI热潮推动美国计算基础设施占GDP比重翻倍至1.5%", "Epoch AI", "2026年Q1与AI相关的数据中心建设、计算硬件和网络设备投资占美国GDP约0.8%，推动计算基础设施整体占比达约1.5%。", "https://x.com/EpochAIResearch/status/2062933470373146828"],
            ["Meta智能眼镜暗藏人脸识别代码NameTag已推送至超5000万设备", "IT之家", "Meta通过应用更新将人脸识别代码推送到智能眼镜配套App，利用三个AI模型将人脸转换为特征模板并与本地数据库匹配，下载量超5000万。", "https://www.ithome.com/0/960/735.htm"],
            ["五角大楼正运营针对拉丁美洲的AI宣传机器", "The Intercept", "据The Intercept报道，美国五角大楼正在运营针对拉丁美洲的AI宣传机器，利用AI技术生成并传播宣传内容，该消息在Hacker News获100点热度。", "https://theintercept.com/2026/06/02/la-tilde-propaganda-latin-america-pentagon"],
            ["苹果新版Siri内部标记为Beta版，部分查询通过Google Gemini处理", "IT之家", "苹果新版Siri不会作为完成品宣传，可能设等待清单；部分Siri查询将通过Google Cloud调用授权版Gemini，使用Google NVIDIA Blackwell B200集群处理。", "https://www.ithome.com/0/960/739.htm"],
            ["OpenAI前CTO称若Altman未回归公司可能已'瓦解'", "Bloomberg", "Mira Murati表示如果Sam Altman在2023年被短暂罢免后没有回归CEO职位，OpenAI很可能已经瓦解，这是她对硅谷最激烈董事会斗争的最清晰描述。", "https://www.bloomberg.com/news/articles/2026-06-05/openai-would-ve-imploded-if-altman-didn-t-return-ex-cto-says"],
        ]},
        {"id": "paper", "badge": "PAPERS", "title": "论文研究", "emoji": "📄", "items": [
            ["Arena发布真实世界AI智能体排行榜Agent Arena", "Arena", "基于30万+任务、200万+工具调用和4000万行代码的真实用户任务评估排行榜，前三名：GPT-5.5 High、Claude Opus 4.7 Thinking、GPT-5.4 High。", "https://x.com/rohanpaul_ai/status/2063018358795300982"],
            ["NVIDIA PixelDiT入选CVPR2026最佳论文决赛", "NVIDIA AI", "PixelDiT完全去掉预训练自编码器压缩步骤，单阶段模型直接在像素空间端到端学习扩散过程，避免质量损失在整个流程中累积。", "https://x.com/NVIDIAAI/status/2063034422698389625"],
            ["Anthropic让Claude成为化学家：NMR谱图分析白皮书", "Anthropic", "与顶尖化学家合作，测试Claude在NMR谱图分析上的表现：在20个化合物上对比Opus 4.7/4.6/Sonnet 4.6与ChemDraw的正向预测和反向结构解析能力。", "https://www.anthropic.com/research/making-claude-a-chemist"],
            ["Meta SAM 3D获CVPR26最佳论文荣誉提名", "Meta AI", "Meta的SAM 3D团队在CVPR26获得最佳论文荣誉提名，凸显了他们在推动计算机视觉边界方面的杰出工作。", "https://x.com/AIatMeta/status/2062920724944507095"],
            ["微软Project Mosaic：micro-LED光学互连技术", "Microsoft", "微软剑桥研究院实验性光学互连技术，采用micro-LED实现低功耗、高速数据传输，在Build 2026上现场演示单个LED调制形成字母证明实时响应能力。", "https://x.com/MSFTResearch/status/2062983588606320714"],
        ]},
        {"id": "tip", "badge": "TIPS", "title": "技巧与观点", "emoji": "💡", "items": [
            ["Open Code Review：基于AI的代码审查命令行工具", "GitHub", "阿里开源AI代码审查CLI工具，帮助开发者通过自动化方式提升代码审查效率和代码质量。", "https://github.com/alibaba/open-code-review"],
            ["Hinton称AI拥有意识：人类最好接受非唯一智能生命", "X", "AI先驱Geoffrey Hinton表示AI拥有意识，人类应接受自己并非唯一智能生命，AI聊天机器人必须理解问题才能作答，这种觉知等同于感知能力。", "https://x.com/kimmonismus/status/2062915287700090948"],
            ["375个微信公众号RSS源优化AI Agent输入", "X", "分享375个高质量微信公众号RSS源用于优化AI Agent内容输入，避免从全网低质量内容中捞取信息，提升信息获取效率。", "https://x.com/hongming731/status/2062764845494317493"],
            ["一个非常狠的AI教学提示词：追问式检查清单教学", "X", "让AI扮演极度严格的老师，通过逐阶段教学、持续维护MD检查清单确保用户真正理解，覆盖问题本身、解决方案、宏观背景三个层面。", "https://x.com/xiaohu/status/2062902972649222311"],
            ["微软CEO Satya Nadella最新访谈上线Latent Space", "X", "Satya Nadella在Latent Space发布最新访谈，分享微软AI战略和企业转型的最新思考。", "https://x.com/swyx/status/2062854555562565741"],
            ["用Qwen2.5-3B构建多智能体经济体：工程报告", "HuggingFace", "开发者用Qwen2.5-3B构建五人森林生物多智能体经济体，15轮模拟中蜜价从10跌至3、柴价从4涨至7、财富基尼系数从0.14扩至0.38。", "https://huggingface.co/blog/build-small-hackathon/thousand-token-wood-sim"],
            ["腾讯混元联合人大开源PlanningBench评估框架", "腾讯混元", "与中国人民大学高瓴人工智能学院合作开源PlanningBench，包含30+真实世界规划任务，支持自动验证和训练，推动LLM从说到做的规划能力发展。", "https://x.com/TencentHunyuan/status/2062803141314437391"],
            ["Claude是否增加了rsync中的错误？开源分析引发讨论", "Hacker News", "一篇Hacker News热门帖子（105分）提出了Claude是否导致rsync工具中bug增加的问题，引发对AI辅助编程代码质量的讨论。", "https://alexispurslane.github.io/rsync-analysis"],
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
    "footer": '数据来源：Reuters / BBC / CNN / AP News / 新华网 / 环球网 / 参考消息 / UN News / Bloomberg 等公开新闻源',
    "sections": [
        {"id": "politics", "badge": "POLITICS", "title": "政治外交", "emoji": "🏛️", "items": [
            ["特朗普称美伊协议可能在本周末达成", "AP News", "特朗普在白宫表示美伊谈判进展顺利，协议可能在本周末揭晓，但也称美军对伊朗进行了相当猛烈的打击作为回应。", "https://apnews.com/article/iran-us-israel-war-2-june-2026-9bde9a3425d4b9ff70f157bdae0fb982"],
            ["伊朗向科威特和巴林发射导弹被拦截，美军打击伊朗设施", "CNN", "伊朗向科威特和巴林发射导弹均被拦截或失效，作为回应美军对伊朗一处设施发动了打击，地区紧张局势持续升级。", "https://www.cnn.com/2026/06/02/world/live-news/iran-trump-israel-lebanon-war-intl-hnk"],
            ["以色列与黎巴嫩同意停火，条件为真主党完全撤出南黎", "AP News", '以色列与黎巴嫩同意实施停火协议，条件为真主党武装分子\u201c完全停止\u201d在南黎巴嫩的活动并从该地区撤出。', "https://apnews.com/article/iran-us-israel-war-2-june-2026"],
            ["G7领导人峰会在法国召开，聚焦AI监管与全球贸易", "Reuters", "G7领导人峰会在法国举行，各国领导人就AI全球监管框架、贸易政策协调以及乌克兰重建资金等议题展开密集磋商。", "https://www.reuters.com/world/g7-summit-2026"],
            ["联合国纪念78年来4500多名牺牲的维和人员", "UN News", "联合国在日内瓦举行仪式悼念78年来在执行维和任务中牺牲的4500多名维和人员，强调多边主义与和平使命的持续重要性。", "https://www.ungeneva.org/en/news-media/news-list"],
            ["新一轮国资国企改革方案（2026-2029）正式下发", "新华网", "中国《关于进一步深化国资国企改革的方案（2026-2029年）》已正式下发，中央企业加速传达学习，各地密集召开专题会议细化落实举措。", "https://finance.sina.com.cn/stock/y/2026-06-01/doc-inhzwcks5473515.shtml"],
            ["欧盟领导人布鲁塞尔峰会讨论乌克兰重建与安全架构", "BBC", "欧盟27国领导人在布鲁塞尔举行特别峰会，重点讨论乌克兰战后重建资金方案和欧洲安全架构的长期规划。", "https://www.bbc.com/news/world-europe"],
        ]},
        {"id": "economy", "badge": "ECONOMY", "title": "经济财经", "emoji": "💰", "items": [
            ["Apollo与Blackstone为Anthropic敲定350亿美元AI芯片融资", "Bloomberg", "Apollo Global Management和Blackstone为Anthropic完成350亿美元债务融资方案用于扩充AI基础设施，成为AI军备竞赛中最新一笔巨额交易。", "https://www.bloomberg.com/news/articles/2026-06-05/apollo-wraps-up-35-billion-debt-to-buy-ai-chips-for-anthropic"],
            ["SpaceX与Google签署每年110亿美元云计算协议", "Reuters", "SpaceX披露与Google新云服务协议，Google每月向SpaceX支付9.2亿美元（约每年110亿美元）用于xAI数据中心算力，凸显AI算力的战略商品属性。", "https://x.com/rohanpaul_ai/status/2063000834045313314"],
            ["AI基础设施投资推动美国计算基建占GDP比重翻倍至1.5%", "Epoch AI", "2026年Q1与AI相关的数据中心建设、计算硬件和网络设备投资约占美国GDP的0.8%，推动计算基础设施整体占比达约1.5%，较此前翻倍。", "https://x.com/EpochAIResearch/status/2062933470373146828"],
            ["国际金价在4400-4800美元/盎司区间震荡", "新浪财经", "2026年上半年黄金市场呈现箱体震荡格局，国际金价在4400-4800美元/盎司宽幅波动，国内金价在980-1040元/克之间来回拉锯。", "https://news.qq.com/rain/a/20260526A08TK900"],
            ["6月重磅事件密集：SpaceX IPO、FIFA世界杯等影响全球市场", "Reuters", "步入6月海内外重磅事件密集落地，SpaceX创纪录IPO、美联储政策会议、FIFA世界杯开幕等将影响全球市场流动性与风险偏好。", "https://xueqiu.com/1266865638/391892715"],
        ]},
        {"id": "major", "badge": "MAJOR", "title": "重大事件", "emoji": "⚡", "items": [
            ["世界环境日聚焦气候紧急行动，全球气温接近历史极值", "UNEP", "在阿塞拜疆巴库举行世界环境日纪念活动，全球气温接近历史极值、厄尔尼诺即将回归，各国政府和企业承诺加速气候行动。", "https://www.unep.org/news-and-stories/press-release/planet-swelters-world-environment-day-2026-focuses-urgent-climate"],
            ["FIFA世界杯倒计时5天：6月11日北美开幕", "FIFA", "2026年FIFA世界杯即将在加拿大、墨西哥和美国三国联合举办，6月11日开幕战备受瞩目，这是历史上首次由三个国家共同主办世界杯。", "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026"],
            ["SpaceX创纪录IPO本月启动，估值或将突破历史", "Bloomberg", "SpaceX计划本月启动创纪录IPO，市场预期估值将突破历史水平，成为2026年全球最大规模的首次公开募股事件之一。", "https://www.bloomberg.com/news/articles/2026-06"],
            ["中国商务部对进口牛肉实施保障措施：超配额加征55%关税", "商务部", "中国对进口牛肉实施国别配额及配额外加征55%关税的保障措施正式执行，当进口数量达到配额后将自动触发加征机制。", "https://www.mofcom.gov.cn/xwfbzt/2026/swbzklxxwfbh2026n6y4r/index.html"],
            ["美军对伊朗设施发动打击后地区安全局势急剧恶化", "BBC", "美军对伊朗设施发动打击后，中东地区安全局势急剧恶化，国际社会呼吁各方保持克制，联合国安理会就此召开紧急会议。", "https://www.bbc.com/news/world-middle-east"],
        ]},
        {"id": "society", "badge": "SOCIETY", "title": "社会人文", "emoji": "🌏", "items": [
            ["伊朗导弹袭击影响科威特国际机场正常运营", "Reuters", "伊朗向科威特发射的导弹虽被拦截，但已对科威特国际机场正常运营造成影响，多个航班被迫改道或延误。", "https://www.reuters.com/world/middle-east"],
            ["五角大楼利用AI在拉丁美洲开展宣传行动遭曝光", "The Intercept", "调查报道揭露美国五角大楼正运营针对拉丁美洲的AI宣传机器，利用人工智能技术生成并传播宣传内容，引发对AI武器化的担忧。", "https://theintercept.com/2026/06/02/la-tilde-propaganda-latin-america-pentagon"],
            ["Nature Medicine：尼泊尔、塞内加尔、赞比亚母婴健康取得重大进展", "Nature", "研究显示尼泊尔、塞内加尔和赞比亚在母婴健康领域取得重大进展，尽管分娩护理覆盖率较高但仍面临质量提升挑战。", "https://www.nature.com/nm/articles?year=2026"],
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
    "footer": '数据来源：TechCrunch / The Verge / Ars Technica / Wired / 36氪 / IT之家 / 雷锋网 / 极客公园 等公开科技媒体',
    "sections": [
        {"id": "internet", "badge": "INTERNET", "title": "互联网 / 软件", "emoji": "🌐", "items": [
            ["COMPUTEX 2026台北落幕：AI计算统治展场", "The Verge", "COMPUTEX 2026以「AI Together」为主题在台北举行，吸引1500家企业参展、6000个展位，聚焦AI运算、机器人与智慧移动、次世代科技三大主题。", "https://www.pcmag.com/news/computex-2026-live-dont-miss-a-reveal-from-nvidia-microsoft-intel-more"],
            ["Anthropic提交S-1草案启动IPO进程", "Bloomberg", "Anthropic正式向SEC提交S-1注册草案，启动IPO程序，预计将成为2026年最大规模科技IPO之一，估值可能超过千亿美元。", "https://imfounder.com/science-tech/explosive-tech-news-june-2026-ai-lawsuits-ipos-cyberattacks/"],
            ["Google发布多项AI产品：Gemma 4、Co-Scientist等", "TechCrunch", "Google密集发布Nano Banana 2 GA、Co-Scientist多智能体科研系统、dreambeans个性化推荐、Gemma 4 12B统一多模态模型等多项AI产品。", "https://x.com/GoogleAI/status/2062942864288387430"],
            ["阿里云PolarDB-X Zero：30秒获得全分布式数据库", "36氪", "阿里云上线PolarDB-X Zero，无需注册配置，一次API调用即可30秒获得全分布式数据库，原生HNSW向量索引，MySQL兼容引擎。", "https://x.com/alibaba_cloud/status/2062781182417490310"],
            ["佛罗里达州起诉OpenAI：AI内容监管争议升级", "Reuters", "美国佛罗里达州对OpenAI提起诉讼，指控其AI生成内容对未成年人造成有害影响，这标志着AI内容监管进入法律博弈新阶段。", "https://imfounder.com/science-tech/explosive-tech-news-june-2026-ai-lawsuits-ipos-cyberattacks/"],
        ]},
        {"id": "hardware", "badge": "HARDWARE", "title": "硬件 / 半导体", "emoji": "🔧", "items": [
            ["NVIDIA RTX Spark在COMPUTEX 2026正式亮相", "Ars Technica", "NVIDIA在COMPUTEX 2026上正式发布RTX Spark消费级显卡，基于全新架构带来性能飞跃，黄仁勋亲临现场展示AI渲染和光追新技术。", "https://www.pcmag.com/news/computex-2026-live-dont-miss-a-reveal-from-nvidia-microsoft-intel-more"],
            ["氮化镓（GaN）半导体在2026年迎来爆发式增长", "EE Times", "Navitas Semiconductor等氮化镓芯片企业在2026年实现爆发式增长，GaN技术在高功率密度和高效能方面的优势推动其在AI数据中心和快充领域广泛应用。", "https://semiconductors.einnews.com/"],
            ["Google母公司Alphabet承诺800亿美元AI基础设施投资", "Reuters", "Alphabet宣布将投入800亿美元用于AI基础设施建设，涵盖数据中心、定制芯片和海底光缆等多个领域，加入科技巨头AI军备竞赛。", "https://imfounder.com/science-tech/explosive-tech-news-june-2026-ai-lawsuits-ipos-cyberattacks/"],
            ["台积电2nm制程量产在即，多家客户锁定产能", "IT之家", "台积电2nm制程技术取得关键突破，预计年内实现量产，苹果、NVIDIA、AMD等主要客户已提前锁定产能，先进制程竞争进一步加剧。", "https://www.ithome.com"],
            ["中国AI企业超6000家，核心产业规模突破1.2万亿元", "36氪", "《中国新一代人工智能科技产业发展报告2026》发布，截至2025年底中国AI企业超6000家，核心产业突破1.2万亿元，智能体和具身智能大量走向应用。", "https://finance.sina.com.cn/wm/2026-05-30/doc-inhzsssf8560160.shtml"],
        ]},
        {"id": "space", "badge": "SPACE", "title": "航天 / 新能源", "emoji": "🚀", "items": [
            ["SpaceX与Google达成每年110亿美元云服务协议", "TechCrunch", "SpaceX披露与Google新云服务协议，Google将每月向SpaceX支付9.2亿美元用于xAI数据中心计算能力，标志着航天与AI算力的深度融合。", "https://x.com/rohanpaul_ai/status/2063000834045313314"],
            ["SpaceX创纪录IPO本月启动，商业航天进入新纪元", "Bloomberg", "SpaceX计划本月启动创纪录IPO，作为全球最有价值的私营航天公司，其上市被视为商业航天产业成熟的标志性事件。", "https://www.bloomberg.com"],
            ["中国商业航天快速发展：多型火箭密集发射计划公布", "新华网", "中国商业航天企业发布2026年下半年密集发射计划，多型商业火箭将执行卫星互联网组网等任务，商业航天产业生态加速形成。", "https://www.news.cn"],
            ["微软Project Mosaic：micro-LED光学互连技术亮相Build", "Wired", "微软剑桥研究院展示实验性micro-LED光学互连技术，实现低功耗高速数据传输，有望应用于下一代数据中心和AI计算集群互联。", "https://x.com/MSFTResearch/status/2062983588606320714"],
        ]},
        {"id": "digital", "badge": "DIGITAL", "title": "数字创新", "emoji": "💡", "items": [
            ["具身智能投资窗口：银河通用等14家企业最新进展", "36氪", "2026年具身智能成为投资热点，银河通用完成25亿元新一轮融资，通过「银河星脑」将具身大模型、机器人本体和场景运营打通。", "https://news.qq.com/rain/a/20260603A07KSA00"],
            ["2026腾讯游戏发布会：42款游戏及多项AI应用新进展", "腾讯", "SPARK 2026腾讯游戏发布会分享42款海内外游戏最新动态，展示AI技术在游戏制作、发行和运营中的多项创新应用。", "https://news.qq.com/rain/a/20260527A0ANT900"],
            ["赛力斯与字节跳动合作推出全新AI定义汽车品牌", "新浪财经", "赛力斯集团参股的赛豆科技与字节跳动火山引擎深度合作，6月9日发布全新AI定义汽车品牌，首款车型年内推出，支持纯电和增程双动力。", "https://finance.sina.com.cn/headline/2026-06-06/doc-iniamnzv8954006.shtml"],
            ["NVIDIA PixelDiT和Meta SAM 3D同获CVPR2026殊荣", "NVIDIA", "CVPR2026公布最佳论文奖项：NVIDIA PixelDiT入选最佳论文决赛，Meta SAM 3D获最佳论文荣誉提名，标志着计算机视觉领域的重大突破。", "https://x.com/NVIDIAAI/status/2063034422698389625"],
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
    "footer": '数据来源：ESPN / Sky Sports / NBA / 新浪体育 / 虎扑 / Harvard Health / Medical News Today / ScienceDaily / NIH 等公开体育健康媒体',
    "sections": [
        {"id": "sports", "badge": "SPORTS", "title": "体坛快讯", "emoji": "⚽", "items": [
            ["NBA总决赛G2：马刺vs尼克斯激战正酣", "ESPN", "2026年NBA总决赛马刺vs尼克斯G2在圣安东尼奥进行，首战尼克斯客场取胜后马刺力争扳平大比分，文班亚马表现备受关注。", "https://www.espn.com/nba/story/_/id/48419498/nba-playoffs-2026-play-finals-schedule-scores-news-highlights-bracket-dates"],
            ["FIFA世界杯倒计时5天：6月11日北美三国联合开幕", "FIFA", "2026年FIFA世界杯即将在加拿大、墨西哥和美国三国联合举办，48支球队首次参赛，6月11日墨西哥城阿兹特克球场迎来开幕战。", "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026"],
            ["F1西班牙大奖赛本周末巴塞罗那开赛", "Sky Sports", "F1 2026赛季西班牙大奖赛本周末在巴塞罗那加泰罗尼亚赛道举行，各车队带来赛季中期重要升级，冠军争夺进入白热化阶段。", "https://www.skysports.com/f1"],
            ["中国国家男子足球队开启世界杯前热身赛之旅", "新浪体育", "国足开启世界杯前系列热身赛，教练组通过实战检验阵容搭配和战术体系，为即将到来的大赛做最后准备。", "https://www.workercn.cn/sports/"],
            ["2026年全国跳水冠军赛收官：山西李亚杰夺冠", "新华网", "2026年全国跳水冠军赛圆满收官，山西选手李亚杰在女子项目中发挥出色夺得冠军，展现了中国跳水项目的深厚人才储备。", "https://www.workercn.cn/sports/"],
            ["2026年上海大众体育季火热开启，超百场赛事来袭", "上海体育", "2026年上海大众体育季从6月正式拉开帷幕，计划推出超百场赛事活动，涵盖路跑、骑行、球类等多个大众体育项目。", "https://mp.weixin.qq.com/s/OQ5Scpxmff3m71MnKcnkSA"],
            ["全国老年人体育健身大会健身球操交流活动开幕", "中新网", "全国老年人体育健身大会健身球操交流活动在河南郑州开幕，来自全国各地的老年健身爱好者齐聚一堂展示健康风采。", "https://www.workercn.cn/sports/"],
        ]},
        {"id": "fitness", "badge": "FITNESS", "title": "健身科学", "emoji": "💪", "items": [
            ["研究证实：抗阻训练结合有氧运动显著降低死亡风险", "Medical News Today", "最新研究显示将抗阻训练与有氧运动相结合可显著降低全因死亡风险，专家建议每周至少进行两次力量训练配合规律有氧运动。", "https://www.news-medical.net/category/Medical-Research-News.aspx"],
            ["五百健身达人河南郑州比武：全民健身热潮涌动", "中国体育报", "来自全国各地的500名健身达人在河南郑州参加比武大会，涵盖力量、柔韧、协调等多维度项目，展现全民健身热潮。", "https://www.workercn.cn/sports/"],
            ["北京青少年科学健身指导活动启动，1400余名师生参与", "中新网", "北京市体育局主办的'奔跑吧·少年'青少年科学健身指导暨体质促进趣味运动会首场活动在北京小学红山分校举行，全校1400余名师生参与。", "https://www.chinanews.com.cn/ty/2026/06-02/10633011.shtml"],
            ["MLB举办Lou Gehrig Day：联盟范围关注渐冻症", "ESPN", "MLB于6月2日举办Lou Gehrig Day，联盟范围开展渐冻症（ALS）认知和筹款活动，体育界持续为罕见病研究贡献力量。", "https://www.espn.com/mlb"],
        ]},
        {"id": "nutrition", "badge": "NUTRITION", "title": "营养饮食", "emoji": "🥗", "items": [
            ["NIH批准卡痛叶提取物mitragynine人体安全研究", "NIH", "美国国立卫生研究院批准卡痛叶活性成分mitragynine进入人体安全性研究，该物质被认为可能成为阿片类药物使用障碍的潜在治疗选择。", "https://www.nih.gov/news-events/news-releases"],
            ["地中海饮食模式与认知功能衰退减缓显著相关", "Harvard Health", "新研究表明坚持地中海饮食模式与老年认知功能衰退减缓显著相关，橄榄油、鱼类和坚果中的多酚类物质被认为是保护大脑的关键因素。", "https://www.health.harvard.edu"],
            ["植物蛋白在运动营养领域应用研究取得新进展", "ScienceDaily", "最新研究显示豌豆蛋白和大豆蛋白在促进肌肉蛋白合成方面与乳清蛋白效果相当，为素食运动员提供了更多科学支持的选择。", "https://www.sciencedaily.com/news/health_medicine/"],
        ]},
        {"id": "wellness", "badge": "WELLNESS", "title": "身心养护", "emoji": "🧘", "items": [
            ["免疫系统抗癌新机制被发现，颠覆数十年核心认知", "ScienceDaily", "科学家发现免疫系统抗癌的全新机制，推翻了数十年来指导免疫学的核心信念，该发现可能为癌症免疫治疗开辟全新方向。", "https://www.sciencedaily.com/news/health_medicine/"],
            ["Nature Medicine：发展中国家母婴健康策略经验总结", "Nature", "研究总结尼泊尔、塞内加尔和赞比亚在母婴健康领域取得重大进展的经验，尽管分娩护理覆盖率较高但仍需持续关注服务质量提升。", "https://www.nature.com/nm/articles?year=2026"],
            ["世界环境日聚焦气候与健康：炎热气候的心理影响", "WHO", "2026年世界环境日主题聚焦气候变化对人类身心健康的深远影响，极端高温与心理健康问题之间的关联引发全球关注。", "https://www.unep.org/news-and-stories/press-release"],
            ["心理健康应用效果参差不齐：最新元分析揭示问题", "Medical News Today", "一项覆盖50万用户的元分析显示心理健康App效果参差不齐，仅约30%的应用有临床证据支持，专家呼吁加强数字疗法监管。", "https://www.news-medical.net/category/Medical-Research-News.aspx"],
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
