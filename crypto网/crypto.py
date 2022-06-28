"""
网页链接：https://alternative.me/crypto/fear-and-greed-index/
"""

import requests
import json

url = 'https://alternative.me/api/crypto/fear-and-greed-index/history'

data = {"days":30}#"{\"days\":30}"

headers = {
    "accept": "application/json, text/plain, */*",
    "cookie": "_ga=GA1.2.689203725.1646815575; _gid=GA1.2.1264310184.1646815575; __gads=ID=3be63d46c8c169b9-221bf9bbead00089:T=1646815576:RT=1646815576:S=ALNI_Mbzrmj0xrXhVRIPIvCX784Qvix6zw; dancer.session=OmMJcdjem_6kPy-NBtmGML4k2IR1WvzWw3YZ6-axIhE~1678351627~JpFy-lRJwxLrVQOa53GNKg~PcK3TRspI2nmLuHtl0Z2FgLbMnTRMY5k9E9wyoFgq0Q~2",
    "origin": "https://alternative.me",
    "referer": "https://alternative.me/crypto/fear-and-greed-index/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30"
}

resq = requests.post(url,headers=headers,data=json.dumps(data))
data_json = resq.json()['data']
data = data_json['datasets'][0]['data']
label = data_json['labels']
print(data)
print(label)
