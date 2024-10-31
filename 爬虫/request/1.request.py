import requests
url = "http://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%87%8D%E5%BA%86&fenlei=256&rsv_pq=0xc67666b5000931c2&rsv_t=649e%2FNG1kk9GKLqzn6PcqK0HFTLBXw8r0RHYhQiOWooZqUjhQVxA8AZcfagJ&rqlang=en&rsv_enter=1&rsv_dl=ih_0&rsv_sug3=1&rsv_sug1=1&rsv_sug7=001&rsv_sug2=1&rsv_btype=i&rsp=0&rsv_sug9=es_2_1&rsv_sug4=2415&rsv_sug=9"
response = requests.get(url)
print(response.text)