# 爬虫

## HTTP协议

请求：

```python
请求行 -> 请求方式 请求地址 协议
请求头 -> 服务器需要的附加信息
请求体 -> 请求参数
```



相应：

```python
状态行 -> 协议 状态码
响应头 -> 客户端需要使用的附加消息
响应体 -> 服务器返回客户端要用的内容(html,json)
```



请求头里常用的内容

1.User-Age 请求载体的身份标识

2.Referer:防盗链

3.cookie:本地字符串数据信息(用户登录信息，反爬的token)

