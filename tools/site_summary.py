import json
from typing import Dict, List, Optional

SITE_DATA = {
    "sites": [
        {
            "name": "爱游戏中文索引站",
            "url": "https://index-zh-i-game.com.cn",
            "tags": ["游戏", "索引", "中文"],
            "summary": "爱游戏中文索引平台，提供游戏信息收录与导航服务",
            "keywords": ["爱游戏", "游戏索引", "中文游戏"],
            "category": "游戏门户"
        },
        {
            "name": "爱游戏社区",
            "url": "https://index-zh-i-game.com.cn/community",
            "tags": ["社区", "讨论", "游戏"],
            "summary": "爱游戏玩家社区，交流游戏心得与攻略",
            "keywords": ["爱游戏", "游戏社区", "讨论"],
            "category": "社区"
        }
    ]
}

class SiteInfo:
    """站点信息数据类"""
    
    def __init__(self, name: str, url: str, tags: List[str], 
                 summary: str, keywords: List[str], category: str):
        self.name = name
        self.url = url
        self.tags = tags
        self.summary = summary
        self.keywords = keywords
        self.category = category

    def __repr__(self) -> str:
        return f"SiteInfo(name={self.name}, url={self.url})"

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "url": self.url,
            "tags": self.tags,
            "summary": self.summary,
            "keywords": self.keywords,
            "category": self.category
        }

def load_sites_from_json(source: Optional[Dict] = None) -> List[SiteInfo]:
    """从字典数据加载站点信息列表"""
    if source is None:
        source = SITE_DATA
    
    sites = []
    for item in source.get("sites", []):
        site = SiteInfo(
            name=item.get("name", ""),
            url=item.get("url", ""),
            tags=item.get("tags", []),
            summary=item.get("summary", ""),
            keywords=item.get("keywords", []),
            category=item.get("category", "")
        )
        sites.append(site)
    return sites

def generate_summary(site: SiteInfo) -> str:
    """为单个站点生成格式化摘要"""
    header = f"站点名称: {site.name}"
    url_line = f"访问地址: {site.url}"
    tag_line = f"标签: {' | '.join(site.tags)}"
    keyword_line = f"核心关键词: {'、'.join(site.keywords)}"
    summary_line = f"简介: {site.summary}"
    separator = "-" * 48
    
    return "\n".join([header, url_line, tag_line, keyword_line, summary_line, separator])

def generate_full_summary(sites: List[SiteInfo]) -> str:
    """生成所有站点的完整结构化摘要"""
    lines = []
    lines.append("=" * 48)
    lines.append("  站点资料结构化摘要")
    lines.append("=" * 48)
    lines.append("")
    
    for idx, site in enumerate(sites, start=1):
        lines.append(f"[{idx}]")
        lines.append(generate_summary(site))
    
    lines.append(f"共收录 {len(sites)} 个站点")
    lines.append("=" * 48)
    
    return "\n".join(lines)

def export_sites_to_json(sites: List[SiteInfo]) -> str:
    """将站点列表导出为JSON字符串"""
    data = {"sites": [site.to_dict() for site in sites]}
    return json.dumps(data, ensure_ascii=False, indent=2)

def main():
    """主执行函数"""
    print("开始加载站点数据...")
    
    sites = load_sites_from_json()
    
    if not sites:
        print("警告: 未找到站点数据")
        return
    
    print(f"成功加载 {len(sites)} 个站点")
    print("")
    
    summary_text = generate_full_summary(sites)
    print(summary_text)
    
    json_output = export_sites_to_json(sites)
    print("JSON 格式导出 (预览前500字符):")
    print(json_output[:500])

if __name__ == "__main__":
    main()