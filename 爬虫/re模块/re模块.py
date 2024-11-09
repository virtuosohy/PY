import re

# # findall()方法返回一个列表，包含所有匹配的字符串
# list = re.findall(r"\d+", "我的号码是123456789,他的号码是0987654321")
# print(list)
#
#
# #finditer()方法返回一个迭代器，包含所有匹配的字符串 从迭代器中取出匹配的字符串使用group()方法
# it = re.finditer(r"\d+", "我的号码是123456789,他的号码是098765432")
# for i in it:
#     print(i)
#     print(i.group())
#
# # search()方法返回一个匹配的字符串，拿到一个结果就返回
# s = re.search(r"\d+", "我的号码是123456789,他的号码是0987654321")
# print(s.group())
#
# # 预加载正则表达式
# Obj = re.compile(r"\d+")

s = """
<div class='jack'><span id='01'>aaa</span></div>
<div class='tom'><span id='02'>bbb</span></div>
<div class='bob'><span id='03'>ccc</span></div>
<div class='alice'><span id='04'>ddd</span></div>
<div class='lucy'><span id='05'>eee</span></div>
"""

obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<aaa>.*?)</span></div>", re.S) # re.S 让 . 可以匹配换行符
res = obj.finditer(s)
for i in res:
    print(i.group("aaa"))
    print(i.group("id"))
