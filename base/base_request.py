import os
# 封装域名
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

BASE_URL = "http://192.168.100.202:8083"

# 设置一个变量存储 token
TOKEN = None
def get_token():
    url = BASE_URL + "/login_action/"
    data = {"username" : "zhangpeng",  "password ": "zhangpeng123"}

    headers={'Content-Type': "application/json"}
    # 查询所有 无请求数据
    response = requests.post(url,data=data, headers=headers,  verify=False)
    response.encoding = "utf-8"
    # 3 查看响应结果
    # 3.1 查看状态码
    code = response.status_code
    print(code)
    # 3.2 查看返回结果文本格式  字符串
    text = response.content
    text2 = response.request
    print(text2)
    # token = text["data"]
    # print(token)
    # accessToken = token["accessToken"]
    # print(accessToken)
    # return accessToken


# 获取项目的绝对路径
ABS_PAHT = os.path.abspath(__file__)
print(ABS_PAHT)
ABS_DIR = os.path.dirname(ABS_PAHT)
print(ABS_DIR)

if __name__ == '__main__':
    get_token()