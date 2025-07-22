from flask import Flask, request, jsonify
from spiders.taobao_spider import crawl_taobao_price
from spiders.jd_spider import crawl_jd_price
from spiders.dangdang_spider import crawl_dangdang_price
import os

app = Flask(__name__)

@app.route('/api/price', methods=['POST'])
def get_price():
    data = request.get_json()
    if not data:
        return jsonify({"error": "请求体为空或格式错误"}), 400

    # 兼容传入列表的情况
    if isinstance(data, list):
        data = data[0] if data else {}

    book_name = data.get('book_name')
    if not book_name:
        return jsonify({"error": "缺少书名参数"}), 400

    try:
        prices = {
            "淘宝": crawl_taobao_price(book_name),
            "京东": crawl_jd_price(book_name),
            "当当": crawl_dangdang_price(book_name)
        }
    except Exception as e:
        return jsonify({"error": f"爬虫执行错误: {str(e)}"}), 500

    return jsonify({
        "book_name": book_name,
        "prices": prices
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
