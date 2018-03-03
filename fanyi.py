import requests
import sys
import json


class BaiduTranslate(object):
    def __init__(self, query_string):
        self.query_string = query_string
        self.basetrans_url = "http://fanyi.baidu.com/basetrans"
        self.langdetect_url = "http://fanyi.baidu.com/langdetect"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"}

    def parse_url(self, url, data):  # 发送请求,获取响应
        response = requests.post(url, headers=self.headers, data=data)
        return json.loads(response.content.decode())

    def prepare_data(self):
        data = {"query": self.query_string}  # 语言检测 post数据
        dict_ret = self.parse_url(self.langdetect_url, data)
        if dict_ret['lan'] == "zh":
            post_data = {
                "query": query_string,
                "from": "zh",
                "to": "en",
            }
        else:
            post_data = {
                "query": query_string,
                "from": "en",
                "to": "zh",
            }
        return post_data

    def run(self):
        # 1 语言检测
            # 1.1 准备post数据 url data
            # 1.2 发送语言检测的请求 获取响应
        # 2 准备待翻译的请求数据
        post_data = self.prepare_data()
        # 3 发送post请求获取响应
        tran_dict = self.parse_url(self.basetrans_url, post_data)
        # 4 提取数据
        ret = tran_dict["trans"][0]["dst"]
        print("<{}>的翻译结果是:{}".format(self.query_string, ret))


if __name__ == '__main__':
    query_string = sys.argv[1]
    trans = BaiduTranslate(query_string)
    trans.run()
