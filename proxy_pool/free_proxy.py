import requests
from bs4 import BeautifulSoup

def fetch_free_proxies(limit=10):
    """
    抓取免费代理网站上的高匿HTTP代理（西刺代理示例）
    返回格式如 ['http://ip:port', ...]
    """
    proxies = []
    url = "https://www.kuaidaili.com/free/inha/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")
        rows = soup.select("table tbody tr")

        for row in rows[:limit]:
            ip = row.select_one("td[data-title=IP]").text.strip()
            port = row.select_one("td[data-title=PORT]").text.strip()
            proxies.append(f"http://{ip}:{port}")
    except Exception as e:
        print(f"抓取代理失败: {e}")

    return proxies
