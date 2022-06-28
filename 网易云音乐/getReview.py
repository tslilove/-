import requests
import random
from Crypto.Cipher import AES
import base64
from binascii import hexlify


def RandomString(a):
    '''
    随机返回16位字符串 JS代码里面的a(16)
    :param a:
    :return:
    '''
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    randomStr = random.sample(string, a)
    return "".join(randomStr)


def AESEncrypt(text, key):
    '''
    AES加密
    :param text: 需要加密的密文
    :param key: 秘钥
    :return:
    '''
    iv = b'0102030405060708'
    pad = 16 - len(text) % 16
    text = text + chr(2) * pad
    # 创建 AES对象
    encryptor = AES.new(key.encode(), AES.MODE_CBC, iv)
    # AES 进行加密
    encryptor_str = encryptor.encrypt(text.encode())
    result = base64.b64encode(encryptor_str).decode()
    return result


def AES2(text, random_str):
    '''
    第二次AES加密
    :param text: 加密的密文
    :param random_str: 随机16位字符串
    :return:
    '''
    first_aes = AESEncrypt(text, key='0CoJUm6Qyw8W8jud')
    second_aes = AESEncrypt(first_aes, random_str)
    return second_aes


def RSA1(text):
    '''
    RSA加密
    :param text: 需要加密的密文
    :return:
    '''
    f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    e = "010001"
    text = text[::-1]
    # 返回二进制数据的16进制表示
    result = pow(int(hexlify(text.encode()), 16), int(e, 16), int(f, 16))
    return format(result, 'x').zfill(131)
def _token(cookie):
    def token():
        _cookie = cookie#'_ntes_nnid=cf94d70cae5d783294ce4a6ac12ec7cb,1634636238872; UM_distinctid=17c97e9933b797-0c37a94b9fe08b-b7a1438-144000-17c97e9933c9b5; _ntes_nuid=cf94d70cae5d783294ce4a6ac12ec7cb; _iuqxldmzr_=32; NMTID=00O3Ein-SwnXSPQ_ECvi6dNxL8PZKcAAAF8uwJ9Zw; WEVNSM=1.0.0; WNMCID=jyekkl.1635225075130.01.0; WM_TID=ifNl5pqT%2FaxBAUAFBFd%2F9J7bVQyQUPiN; ntes_kaola_ad=1; __root_domain_v=.163.com; _qddaz=QD.157739218739954; WM_NI=HQ9LB1nF3mBOFIrkvr6Rn%2FdRUP%2F3Bl%2BCobXTw%2FZx%2Bx9rCMKOWvVzur5FDCNwVzQae3E5e0FC0LOWcZ4NQJet%2BZGS%2FlOnkVjJrrvszB%2BEIvrl3AvxSHqJZ%2FUNdX5TDaIcTzI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee89c57d899d8fd3f03ef38e8ba7c54b878b8faff425a986888efc6787b9ffd1c22af0fea7c3b92a8c8ff7adc13bae9afd8ec1458697be8cf57af68ea2d0e75a9790e1d4c168e99da183db60b5f19699aa74fbae8daeca4595aa9a9bf87af79a8ca4cd7d96a69f82e83987ebabd1c549f49481b8e252f8929fabe880e98689b4ae688db2a5b7e942b2aeba94f94ae99b8797f168f19fba99d244b39696d0d846a888fbb5c76b8bbd9c9bcc37e2a3; __csrf=207281b7dd563b4bb6bdea4c4f78b152; JSESSIONID-WYYY=oHoNm%5C1vbcFI%2Ftb3lkAK6ScjEKE1RsMueivmYMmvMflbTkT4IfiCHedEe%2B4UTQQO%2Fi3uWtmzbyUYMQ2tDkMBWmZx41XygXp6Vx8ykdVeiAJJ6%2FDtt%2FGC6h1mJjdQIXsG8jXPcaJYnv5ycIt7tmsSHssTz%5CnyAVTpZhct%2FNZ9GbhIeHoT%3A1645276820517'
        z8r = "__csrf"
        vc4g = z8r + "="
        bfi6c = _cookie.index(vc4g)
        if bfi6c < 0:
            return ""
        bfi6c += len(vc4g) - 2
        zk5p = _cookie.find(";", bfi6c)
        if zk5p < 0:
            zk5p = len(_cookie)
        # return
        print(_cookie[bfi6c + 2:zk5p])

text = '{"rid":"A_PL_0_6895723062","threadId":"A_PL_0_6895723062","pageNo":"4","pageSize":"20","cursor":"1643879884054","offset":"0","orderType":"1","csrf_token":"c1146b59972042e72a4d428b2714eb30"}'
random_str = RandomString(16)
params = AES2(text, random_str)
encSecKey = RSA1(random_str)

cookie = 'wyy_uid=9b506044-5411-45dd-a112-4adbacc0439d; mp_MA-91DF-2127272A00D5_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fm.sf.163.com%2F%22%2C%22updatedTime%22%3A%201633706492051%2C%22sessionStartTime%22%3A%201633706492048%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%202%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22d58f3c3dacf97703a06da837c0dff927c3623166%22%2C%22persistedTime%22%3A%201633706492042%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201633706492051%7D%2C%22sessionUuid%22%3A%20%22a5eaa45da8f373b8b840dc82de7ae4e6e8ae23ae%22%7D; _ga=GA1.2.1774609083.1633706492; _ntes_nnid=a53c74f44a2a7706b4c9955a276a559f,1635518607478; UM_distinctid=17ccc8177178a6-063397d0ca2f79-561a145a-144000-17ccc817718df5; _iuqxldmzr_=32; NMTID=00OrQ-YRA71g1rEA0g7r-OwMmmpotUAAAF8zIXgdg; WEVNSM=1.0.0; WNMCID=xssgzj.1635518900276.01.0; WM_TID=SQx6MKnRRW1EEUFRFQY7tS31s3SGRrls; MUSIC_A_T=1555138451115; MUSIC_U=9de0b492647e46610ebfe82cd5b87833a08ecc221443c8bd8188423e828dd5e5e865e922881deed91d59bda2b01d4b9d57269bcdb85fb02022fac3ef9d6f10fce758fe0f42e01662ad811b647f556b6fd427f2c8160bfdad; MUSIC_R_T=1555138556361; ntes_kaola_ad=1; _ntes_nuid=a53c74f44a2a7706b4c9955a276a559f; P_INFO=yxl20160@126.com|1644916377|1|mail126|00&99|null&null&null#bej&null#10#0#0|&0||yxl20160@126.com; hb_MA-BFF5-63705950A31C_source=link.zhihu.com; hb_MA-BFF5-63705950A31C_u=%7B%22utm_source%22%3A%20%22weixin%22%2C%22utm_medium%22%3A%20%22iphoneShare%22%2C%22utm_campaign%22%3A%20%22share%22%2C%22utm_content%22%3A%20%22%22%2C%22utm_term%22%3A%20%22%22%2C%22promotional_id%22%3A%20%22%22%7D; __csrf=c1146b59972042e72a4d428b2714eb30; WM_NI=iiFrvANwxHceY7omUqWoa3bwusMdzATlOOoisEQUUcf5lp3P7qUVzTIzMQ9X20e3%2B7fk%2BcnKh1ycjh0r2nYC5A0bALc8%2FvROXrSozEFQ1tp%2FJyxk1RHimslZJc%2Bh8YwfU1c%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb2ed69fbeaab9ac460aa8e8eb2c85e869a8fabaa7ba586acb7ca629cb6fdcce82af0fea7c3b92aabb78a93f54b8ea9b8a9e26f9be9a18ed87b95b1afd4e17db7ad8385f94b98b481b0ee63b19b9fb6d869a6eba491b25cf5af9bb7f9608ba683b2bc54f2f0abd4aa3da6b5e584ed41acefb784e964f4aefe8fdc49f79f0083c448a1e8e197d1459cae9d90f94f868fff95f3258aa7b88cb45a8cb7a394ef528abde589bb53b5ba9bd2e237e2a3; JSESSIONID-WYYY=QIQobvj62xsfPsmM8V6K4R46HQWx%2BP1yvBUmkY5Y4VeoAwxkbqunFkKmjBAtNOh%2BoGOHYs86rP17bEhGdwQJGpYr%5CO92psYhe0cQJIma4zbrBEHcglWMlV%2BOE9FHqRfEut%5CpIBq%5CYNOktHNmi3lcJVtISc1tZn09edaONpU98axbU3Ij%3A1645280703411'
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token=%s'%_token(cookie)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'referer': 'https://music.163.com/',
    'cookie': cookie
}
data = {
    'params': params,
    'encSecKey': encSecKey,
}
response = requests.post(url, headers=headers, data=data).json()
comments = response['data']['comments']
# print(comments)
for comment in comments:
    print(comment['content'])
