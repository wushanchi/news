# 项目记忆

## 项目概述
每日晨报自动化——每天 08:50 自动生成四个日报 HTML，推送至 GitHub `wushanchi/news` 仓库。

## 日报类型
| 日报 | 文件名模板 | 主题色 | 数据源 |
|---|---|---|---|
| AI 晨报 | ai-morning-{date}.html | 橙红 #ff6a3d | AI HOT API |
| 国际焦点 | world-news-{date}.html | 蓝色 #3b82f6 | WebSearch 公开新闻 |
| 科技日报 | tech-news-{date}.html | 绿色 #10b981 | WebSearch 科技媒体 |
| 运动健康 | sports-health-{date}.html | 金色 #f59e0b | WebSearch 体育健康 |

## 技术约定
- 纯 HTML/CSS/JS 单文件，内联所有资源，零外部依赖
- 系统字体栈、CSS 变量、响应式布局、IntersectionObserver 动画
- 文件名使用 YYYY-MM-DD 日期格式
- 全局编号贯穿全文，每个版块不重新计数
- 原文链接使用 target="_blank" rel="noopener noreferrer"
- 时间转北京时间人话格式
- GitHub 仓库：wushanchi/news（Public）

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
