import requests
import time

url = 'https://user.lu.com/user/query-pwd-pub-key'

data = {
    "supportPwdEncryptVersion": "V0",
    "_": str(int(time.time()*1000))
}
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_g=n_458310_a587e5c2-d3b7-4666-8096-8edd2d69099a; _g2=n_458310_b333e0c7-0cf6-46f2-a876-72d8ad021e9e; IMVC=d6c0d82a0e294a13a3ea2d546eda258a; Hm_lvt_9842c7dcbbff3109ea37b7407dd0e95c=1649918915; _fp=\"We79c4d57-09c3-45aa-87bc-dc862a6c2a5aLxw=_4nxEVzIwMjEwNzIyMTc1ODM4ODA4MDgw_OcYKNTCI0f5mpgQjUbRzqkZghFgkFqRUMXf4s7PEwvVcZ5eXXwfJsSl2nTbVPiqPK3s=:S7Qyy0oNpyW4XSwDowI99bV0+X8E8ePPn9QM2WbVAqw=\"; __SK_cookieId=1095047864119261649918914742; Hm_lpvt_9842c7dcbbff3109ea37b7407dd0e95c=1649918970",
    "Host": "user.lu.com",
    "Referer": "https://user.lu.com/user/login",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36",
    "X-Requested-With": "XMLHttpRequest"
}
resq = requests.get(url,headers=headers,params=data)
print(resq.json())
