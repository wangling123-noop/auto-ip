from flask import Flask, request, jsonify
from spiders.taobao_spider import crawl_taobao_price
from spiders.jd_spider import crawl_jd_price
from spiders.dangdang_spider import crawl_dangdang_price

app = Flask(__name__)

@app.route('/get_price', methods=['POST'])
def get_price():
    data = request.get_json()
    book_name = data.get('book_name')
    if not book_name:
        return jsonify({"error": "缺少书名参数"}), 400

    return jsonify({
        "book_name": book_name,
        "prices": {
            "淘宝": crawl_taobao_price(book_name),
            "京东": crawl_jd_price(book_name),
            "当当": crawl_dangdang_price(book_name)
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
