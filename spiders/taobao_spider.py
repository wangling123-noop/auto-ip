import requests
from bs4 import BeautifulSoup
from proxy_pool.proxy_pool import get_random_proxy
from utils.headers import get_random_headers

def crawl_taobao_price(book_name):
    url = f"https://s.taobao.com/search?q={book_name}"
    try:
        proxy = get_random_proxy()
        resp = requests.get(url, headers=get_random_headers(), proxies={"http": proxy, "https": proxy}, timeout=10)
        soup = BeautifulSoup(resp.text, 'lxml')
        price = soup.select_one('.price strong')
        return f"¥{price.text.strip()}" if price else "未找到价格"
    except Exception as e:
        return f"请求失败: {e}"
