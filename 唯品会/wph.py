import requests
import time
import json

def get_productid(pageOffset):
    url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/search/product/rank'
    data = {
    "callback": "getMerchandiseIds",
    "app_name": "shop_pc",
    "app_version": "4.0",
    "warehouse": "VIP_BJ",
    "fdc_area_id": "101101101",
    "client": "pc",
    "mobile_platform": "1",
    "province_id": "101101",
    "api_key": "70f71280d5d547b2a7bb370a529aeea1",
    "user_id": "",
    "mars_cid": "1635571807910_570ad3c132ce7830b808d613bdab38af",
    "wap_consumer": "a",
    "standby_id": "nature",
    "keyword": "母婴用品",
    "lv3CatIds": "",
    "lv2CatIds": "",
    "lv1CatIds": "",
    "brandStoreSns": "",
    "props": "",
    "priceMin": "",
    "priceMax": "",
    "vipService": "",
    "sort": "0",
    "pageOffset": pageOffset,
    "channelId": "1",
    "gPlatform": "PC",
    "batchSize": "120",
    "_": int(time.time()*1000)
    }
    headers = {
    "accept": "*/*",
    "cookie": "vip_cps_cid=1634701786557_c7639d14a01bd23e11f363090a88ea50; PAPVisitorId=b22dc1e7b4c7afbe55c4da61ae7e3b69; vip_new_old_user=1; mars_pid=0; vip_address=%257B%2522pid%2522%253A%2522101101%2522%252C%2522cid%2522%253A%2522101101101%2522%252C%2522pname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%252C%2522cname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%257D; vip_province=101101; vip_province_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_city_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_city_code=101101101; vip_wh=VIP_BJ; vip_ipver=31; vip_cps_cuid=CU16455854983413ed2fe8309762880d; VipDFT=-1; user_class=a; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A1%7Cul%3A3105; cps_share=cps_share; mars_sid=29ce5de54581e95c5032ac6e0b3ec09f; cps=adp%3AC01V4mkmz1lm9edv%3A%40_%401646302078327%3Amig_code%3A%3Aac014mkmz100003g6l6v2ci718fmysqy; visit_id=BB1B0995741BF096087C1474DB65C1DF; vip_access_times=%7B%22list%22%3A8%2C%22detail%22%3A2%7D; pg_session_no=12; vip_tracker_source_from=; mars_cid=1635571807910_570ad3c132ce7830b808d613bdab38af",
    "referer": "https://category.vip.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    res = requests.get(url,headers=headers,params = data,verify=False)
    json_text = res.text[18:-1]
    productid_list = json.loads(json_text)["data"]["products"]
    productid_list = [id['pid'] for id in productid_list]
    print(productid_list)
    return productid_list
def get_page_data(pageOffset):
    productid_list = get_productid(pageOffset)
    id_list = []
    id_list.append(",".join(productid_list[:50]))
    id_list.append(",".join(productid_list[50:100]))
    id_list.append(",".join(productid_list[100:120]))
    url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2'
    headers = {
    "accept": "*/*",
    "cookie": "vip_cps_cid=1634701786557_c7639d14a01bd23e11f363090a88ea50; PAPVisitorId=b22dc1e7b4c7afbe55c4da61ae7e3b69; vip_new_old_user=1; mars_pid=0; vip_address=%257B%2522pid%2522%253A%2522101101%2522%252C%2522cid%2522%253A%2522101101101%2522%252C%2522pname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%252C%2522cname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%257D; vip_province=101101; vip_province_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_city_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_city_code=101101101; vip_wh=VIP_BJ; vip_ipver=31; vip_cps_cuid=CU16455854983413ed2fe8309762880d; VipDFT=-1; user_class=a; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A1%7Cul%3A3105; cps_share=cps_share; mars_sid=29ce5de54581e95c5032ac6e0b3ec09f; cps=adp%3AC01V4mkmz1lm9edv%3A%40_%401646302078327%3Amig_code%3A%3Aac014mkmz100003g6l6v2ci718fmysqy; visit_id=BB1B0995741BF096087C1474DB65C1DF; pg_session_no=12; vip_tracker_source_from=; mars_cid=1635571807910_570ad3c132ce7830b808d613bdab38af; vip_access_times=%7B%22list%22%3A9%2C%22detail%22%3A2%7D",
    "referer": "https://category.vip.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    dd_list = []
    for id in id_list:
        data = {
        "callback": "getMerchandiseDroplets1",
        "app_name": "shop_pc",
        "app_version": "4.0",
        "warehouse": "VIP_BJ",
        "fdc_area_id": "101101101",
        "client": "pc",
        "mobile_platform": "1",
        "province_id": "101101",
        "api_key": "70f71280d5d547b2a7bb370a529aeea1",
        "user_id": "",
        "mars_cid": "1635571807910_570ad3c132ce7830b808d613bdab38af",
        "wap_consumer": "a",
        "productIds": id+",",
        "scene": "search",
        "standby_id": "nature",
        "extParams": "{\"stdSizeVids\":\"\",\"preheatTipsVer\":\"3\",\"couponVer\":\"v2\",\"exclusivePrice\":\"1\",\"iconSpec\":\"2x\",\"ic2label\":1}",
        "context": "",
        "_": int(time.time()*1000)
        }
        res = requests.get(url,headers=headers,params=data,verify=False)
        json_text = res.text[24:-1]
        data_json = json.loads(json_text)['data']['products']
        dd_list.append(data_json)
        # print(data_json)
    return dd_list

def run():

    for page in range(3):
        pageOffset = page*120
        dd_list = get_page_data(pageOffset)
        print(dd_list)


if __name__ == '__main__':
    # get_page_data(pageOffset)
    run()
