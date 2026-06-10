# 项目记忆

## 项目概述
每日晨报自动化——每天 08:50 自动生成四个日报 HTML，推送至 GitHub `wushanchi/news` 仓库。

## 日报类型
| 日报 | 文件名模板 | 主题色 | 数据获取方式 |
|---|---|---|---|
| AI 晨报 | ai-morning-{date}.html | 橙红 #ff6a3d | AI HOT API (唯一固定源) |
| 国际焦点 | world-news-{date}.html | 蓝色 #3b82f6 | WebSearch 多源轮询 |
| 科技日报 | tech-news-{date}.html | 绿色 #10b981 | WebSearch 多源轮询 |
| 运动健康 | sports-health-{date}.html | 金色 #f59e0b | WebSearch 多源轮询 |

---

## 信息来源清单（用于每日自动化）

### 🌍 国际焦点日报 — 信息来源

**海外主流媒体**（每次选 2-3 个做定向搜索）：
- Google News (news.google.com) — 聚合首页，作为首选起手源
- Reuters (reuters.com/world) — 路透社国际新闻
- BBC News (bbc.com/news) — BBC 国际新闻
- CNN (cnn.com) — CNN 国际版
- Axios (axios.com) — 简洁政治/政策新闻
- Associated Press (apnews.com) — 美联社
- Al Jazeera (aljazeera.com) — 中东/全球视角

**国内新闻媒体**（补充中国视角的国际新闻）：
- 新华网国际频道 (xinhuanet.com/world)
- 环球网 (world.huanqiu.com)
- 参考消息 (cankaoxiaoxi.com)
- 央视网国际 (news.cctv.com/world)

**搜索策略**（每类一条 WebSearch）：
1. `site:news.google.com world news today` → 获取聚合摘要
2. `site:reuters.com OR site:bbc.com OR site:cnn.com world news May` → 主流媒体
3. `site:xinhuanet.com OR site:huanqiu.com 国际新闻 今天` → 国内媒体
4. 合并去重，取 20 条，按 政治外交 / 经济财经 / 重大事件 / 社会人文 分组

### 💻 科技日报 — 信息来源

**海外科技媒体**：
- TechCrunch (techcrunch.com) — 创投/产品
- The Verge (theverge.com) — 消费电子/互联网
- Ars Technica (arstechnica.com) — 硬核技术
- Wired (wired.com) — 科技文化
- ZDNet (zdnet.com) — 企业 IT
- Reuters Technology — 科技产业

**国内科技媒体**：
- 36氪 (36kr.com) — 创投/新经济
- IT之家 (ithome.com) — 消费电子/互联网
- 雷锋网 (leiphone.com) — AI/硬科技
- 极客公园 (geekpark.net) — 产品/创新

**搜索策略**：
1. `site:techcrunch.com OR site:theverge.com OR site:arstechnica.com tech news today` → 海外科技
2. `site:36kr.com OR site:ithome.com OR site:leiphone.com 科技 最新` → 国内科技
3. 合并去重，取 20 条，按 互联网/软件 / 硬件/半导体 / 航天/新能源 / 数字创新 分组

### ⚽ 运动健康日报 — 信息来源

**体育 — 海外**：
- ESPN (espn.com) — 综合体育
- BBC Sport (bbc.com/sport) — 足球/综合
- Sky Sports (skysports.com) — 英超/足球
- NBA.com — 篮球
- UEFA (uefa.com) — 欧洲足球

**体育 — 国内**：
- 新浪体育 (sports.sina.com.cn) — 综合
- 虎扑 (hupu.com) — 篮球/足球社区
- 腾讯体育 (sports.qq.com) — 综合
- 直播吧 (zhibo8.com) — 赛事快讯

**健康 — 海外**：
- Harvard Health (health.harvard.edu) — 医学科普
- Medical News Today (medicalnewstoday.com) — 医学新闻
- WHO News (who.int/news) — 全球卫生
- ScienceDaily Health — 健康科研

**健康 — 国内**：
- 丁香医生 (dxy.cn) — 医学科普
- 生命时报 — 健康生活
- 健康时报 (jkb.com.cn) — 健康新闻

**搜索策略**（体育和健康分开搜）：
1. `site:espn.com OR site:skysports.com OR site:nba.com sports news today` → 海外体育
2. `site:sports.sina.com.cn OR site:hupu.com 体育 最新` → 国内体育
3. `site:harvard.edu OR site:medicalnewstoday.com health research May 2026` → 健康科研
4. 合并去重，取 18 条，按 体坛快讯 / 健身科学 / 营养饮食 / 身心养护 分组

## 技术约定
- 纯 HTML/CSS/JS 单文件，内联所有资源，零外部依赖
- 系统字体栈、CSS 变量、响应式布局、IntersectionObserver 动画
- 文件名使用 YYYY-MM-DD 日期格式
- 全局编号贯穿全文，每个版块不重新计数
- 原文链接使用 target="_blank" rel="noopener noreferrer"
- 时间转北京时间人话格式
- GitHub 仓库：wushanchi/news（Public，默认分支 master）
- GitHub 推送方式：Git 沙箱直连失败时，使用 Python + GitHub REST API (urllib) 上传
  - 上传脚本：script/upload_github.py，通过 GITHUB_TOKEN 环境变量认证

## 自动化
- ID: automation-1779433671122
- 名称: 每日晨报生成 (08:50)
- 调度: 每日 08:50 (FREQ=DAILY;BYHOUR=8;BYMINUTE=50)
- 工作目录: C:\Users\Wu Shanchi\WorkBuddy\2026-05-22-AI news

## 文件结构
```
news/
├── index.html                    # 汇总导航页（日期选择 + 四板块卡片）
├── ai-morning-YYYY-MM-DD.html    # AI 晨报（5版块）
├── world-news-YYYY-MM-DD.html    # 国际焦点（4版块）
├── tech-news-YYYY-MM-DD.html     # 科技日报（4版块）
└── sports-health-YYYY-MM-DD.html # 运动健康（4版块）
```
