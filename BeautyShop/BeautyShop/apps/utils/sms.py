import requests

class YunPian(object):
    def __init__(self, api_key):
        self.apikey = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        params = {
            "apikey": self.apikey,
            "mobile": mobile,
            "text": "【完美女孩】您的验证码是{code}，如非本人操作，请忽略本短信".format(code=code)
        }
        response = requests.post(self.single_send_url, data=params)
        import json
        re_dict = json.loads(response.text)
        print re_dict

if __name__ == "__main__":
    yun_pian = YunPian()
