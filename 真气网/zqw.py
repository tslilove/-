import requests
import execjs

url = 'https://m.zq12369.com/goapi/open/city/24hourdata'

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "UM_distinctid=17d0c79ecff651-072675df95f6e6-57b1a33-144000-17d0c79ed00699; CNZZDATA1254317176=1487340931-1636591314-%7C1647585915; city=%E5%8C%97%E4%BA%AC; SECKEY_ABVK=8vTeMrpraeYqm9TapJJgS32d81Xr+4aN4Rf6aE7EoRk%3D; BMAP_SECKEY=8vTeMrpraeYqm9TapJJgS9WB3COprl6xscMNJnp8aEKxstFIj9CSVOKjxnoctefp4ODFyC--z4EJvHddaKo5mgdatdXZFuj6QyR1dR_Pm39v3lgsuW_uk38ByGeB79qL6gIyYT-vjphJhAo8ROi7DonaiH-YTG1MNr7ByfG5vLnRrSyVONvCdtefVafP6ctm",
    "Host": "m.zq12369.com",
    "Pragma": "no-cache",
    "Referer": "https://m.zq12369.com/cityaqi.php?city=%E6%9D%AD%E5%B7%9E",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

with open("air.js", 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())

params = ctx.call('getParam',{'city': '杭州'})
playload = {'param':params}
# params = params.replace("+", '%2B')
# params = params.encode().decode()
print(params)
resq = requests.get(url,headers=headers,params=playload,verify = False)
encrypted = resq.text
print(encrypted)
data = ctx.call('decryptData',encrypted)
print(data)
