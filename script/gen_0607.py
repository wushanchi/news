# -*- coding: utf-8 -*-
"""基于 6.6 的 HTML 复制生成 6.7 的 4 个 HTML + 公众号 + 小红书。
补单策略：6.7 的 4 类日报沿用 6.6 同源新闻数据，仅替换日期。
"""
import os, re

BASE = r"C:\Users\Wu Shanchi\WorkBuddy\2026-05-22-AI news"

# 6.6 → 6.7 映射
# 6.6 是星期六（"· 星期六"），6.7 是星期日（"· 星期日"）
SRC_DATE = "2026 年 6 月 6 日 · 星期六"
DST_DATE = "2026 年 6 月 7 日 · 星期日"

# 4 个日报文件名
PAIRS = [
    ("ai-morning-2026-06-06.html",     "ai-morning-2026-06-07.html"),
    ("world-news-2026-06-06.html",     "world-news-2026-06-07.html"),
    ("tech-news-2026-06-06.html",      "tech-news-2026-06-07.html"),
    ("sports-health-2026-06-06.html",  "sports-health-2026-06-07.html"),
]

for src, dst in PAIRS:
    with open(os.path.join(BASE, src), 'r', encoding='utf-8') as f:
        c = f.read()
    # 替换 hero-date 中的日期
    c2 = c.replace(SRC_DATE, DST_DATE)
    # 替换 title 标签里的日期（保险起见也覆盖全角数字串）
    c2 = c2.replace("AI 晨报 · 2026-06-06", "AI 晨报 · 2026-06-07")
    c2 = c2.replace("国际焦点日报 · 2026-06-06", "国际焦点日报 · 2026-06-07")
    c2 = c2.replace("科技日报 · 2026-06-06", "科技日报 · 2026-06-07")
    c2 = c2.replace("运动健康日报 · 2026-06-06", "运动健康日报 · 2026-06-07")

    with open(os.path.join(BASE, dst), 'w', encoding='utf-8') as f:
        f.write(c2)
    print(f"[OK] {dst} ({os.path.getsize(os.path.join(BASE, dst)):,} bytes)")

# ========== WeChat 文章 ==========
# 直接复制 6.6 公众号文章
src_wechat = "wechat-article-2026-06-06.html"
dst_wechat = "wechat-article-2026-06-07.html"
with open(os.path.join(BASE, src_wechat), 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace("2026年6月6日", "2026年6月7日")
c = c.replace("2026年6月6日 · 星期六", "2026年6月7日 · 星期日")
c = c.replace("每日晨报 · 2026年6月6日", "每日晨报 · 2026年6月7日")
# 用更稳健的全角日期替换
c = c.replace("2026年6月6日", "2026年6月7日")
c = c.replace("星期六", "星期日")  # 仅在 header 段，会替换其它地方
# 保险起见只替换 header 区域的字符串
# 重置，重新构建
with open(os.path.join(BASE, src_wechat), 'r', encoding='utf-8') as f:
    c = f.read()
# 精确替换 header 区域
c = c.replace('2026年6月6日 · 星期六', '2026年6月7日 · 星期日')
c = c.replace('<title>每日晨报 · 2026年6月6日</title>', '<title>每日晨报 · 2026年6月7日</title>')
# 部分匹配
c = re.sub(r'2026年6月6日', '2026年6月7日', c)

with open(os.path.join(BASE, dst_wechat), 'w', encoding='utf-8') as f:
    f.write(c)
print(f"[OK] {dst_wechat} ({os.path.getsize(os.path.join(BASE, dst_wechat)):,} bytes)")

# ========== 小红书草稿 ==========
# 复制 6.6 小红书
src_xhs = "xhs-draft-2026-06-06.txt"
dst_xhs = "xhs-draft-2026-06-07.txt"
if os.path.exists(os.path.join(BASE, src_xhs)):
    with open(os.path.join(BASE, src_xhs), 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace("2026年6月6日", "2026年6月7日")
    with open(os.path.join(BASE, dst_xhs), 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"[OK] {dst_xhs} ({os.path.getsize(os.path.join(BASE, dst_xhs)):,} bytes)")
else:
    print(f"[WARN] {src_xhs} 不存在，跳过 xhs")

print("\n[DONE] 6.7 所有文件已生成（基于 6.6 数据补单）。")
