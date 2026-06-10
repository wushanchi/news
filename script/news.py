import feedparser
import urllib.parse
import json

def build_rss_url(topic_or_query, is_search=False):
    """
    构建中文 Google News RSS 链接
    """
    base_params = "hl=zh-CN&gl=CN&ceid=CN:zh-Hans"
    
    if is_search:
        # 对搜索词进行 URL 编码
        encoded_query = urllib.parse.quote(topic_or_query)
        return f"https://news.google.com/rss/search?q={encoded_query}&{base_params}"
    elif topic_or_query:
        return f"https://news.google.com/rss/headlines/section/topic/{topic_or_query}?{base_params}"
    else:
        # 默认头条
        return f"https://news.google.com/rss?{base_params}"

def fetch_titles_only(url, limit=5):
    """
    抓取 RSS 并只提取指定数量的新闻标题
    """
    feed = feedparser.parse(url)
    # 提取标题，并清理来源后缀 (Google RSS 标题通常自带 "- 来源")
    titles = []
    for entry in feed.entries[:limit]:
        title = entry.title
        # 可选：如果不需要标题末尾的 "- 新华网" 等媒体后缀，可以按 " - " 切割
        clean_title = title.rsplit(' - ', 1)[0] if ' - ' in title else title
        titles.append(clean_title)
    return titles

def generate_news_matrix():
    """
    按照区域和细分板块构建新闻矩阵
    """
    # 定义矩阵配置
    # 规则：如果用标准 topic 则 is_search=False，如果用关键词聚合则 is_search=True
    news_config = {
        "中国": {
            "焦点新闻": {"query": "", "is_search": False},
            "商业": {"query": "BUSINESS", "is_search": False},
            "科技": {"query": "TECHNOLOGY", "is_search": False},
            "运动": {"query": "SPORTS", "is_search": False}
        },
        "美国": {
            "焦点新闻": {"query": "美国", "is_search": True},
            "商业": {"query": "美国 经济 OR 华尔街", "is_search": True},
            "科技": {"query": "美国 科技 OR 硅谷", "is_search": True},
            "运动": {"query": "美国 体育 OR NBA OR NFL", "is_search": True}
        },
        "全球": {
            "焦点新闻": {"query": "WORLD", "is_search": False} # 原生国际版块
            # "商业": {"query": "全球 商业 OR 跨国公司", "is_search": True},
            # "科技": {"query": "全球 科技前沿 OR 国际科技", "is_search": True},
            # "运动": {"query": "国际 体育 OR 奥运 OR 世界杯", "is_search": True}
        }
    }

    result_matrix = {}

    print("开始并行抓取新闻矩阵...")
    for region, categories in news_config.items():
        result_matrix[region] = {}
        for category, params in categories.items():
            url = build_rss_url(params["query"], params["is_search"])
            titles = fetch_titles_only(url, limit=10)
            result_matrix[region][category] = titles
            print(f"已获取: [{region}] - [{category}] ({len(titles)}条)")

    return result_matrix

if __name__ == "__main__":
    # 运行并输出格式化的 JSON 数据
    news_data = generate_news_matrix()
    print("\n最终输出的 JSON 数据结构：")
    print(json.dumps(news_data, indent=2, ensure_ascii=False))