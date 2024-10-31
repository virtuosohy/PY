import requests

url = "https://fanyi.baidu.com/sug"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

s = input("请输入单词：")
data = {
      "kw": s
        }
res = requests.post(url, data = data , headers = headers)
print(res.json())