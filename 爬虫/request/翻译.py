import requests
import time
import random
import hashlib
import json
from urllib.parse import quote


def translate_word(word):
    url = "https://dict.youdao.com/suggest"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.youdao.com/",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;",
    }

    params = {
        "num": "5",
        "ver": "3.0",
        "doctype": "json",
        "cache": "false",
        "le": "en",
        "q": word
    }

    try:
        # 添加随机延时
        time.sleep(random.uniform(0.5, 1.5))

        response = requests.get(url, params=params, headers=headers)
        result = response.json()

        if 'result' in result and 'entries' in result['result']:
            print("\n翻译结果：")
            for entry in result['result']['entries']:
                if 'explain' in entry:
                    print(f"- {entry['entry']}: {entry['explain']}")
        else:
            print("未找到翻译结果")

    except requests.RequestException as e:
        print(f"请求出错：{e}")
    except ValueError as e:
        print(f"解析响应失败：{e}")


def main():
    print("欢迎使用有道翻译！")
    while True:
        word = input("\n请输入要翻译的单词（按 q 退出）：").strip()
        if word.lower() == 'q':
            print("感谢使用！")
            break
        if word:
            translate_word(word)
        else:
            print("请输入有效的单词")


if __name__ == "__main__":
    main()