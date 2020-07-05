from requests import post
from urllib.parse import urlencode

URL = "https://shimo.im/lizard-api/auth/password/login"
headers = {
           "accept": "*/*",
           "accept-encoding": "gzip, deflate, br",
           "accept-language": "zh-CN,zh;q=0.9",
           "content-length": "45",  # str
           "content-type": "application/x-www-form-urlencoded; charset=utf-8",
           "cookie": "shimo_gatedlaunch=2; shimo_kong=1; shimo_svc_edit=5016; _bl_uid=dskXsazC8gU3e7dt66jd5p67Xvbs; _csrf=WWhLtCLrKFpYRnd7yeTBan5i; deviceId=2b34a21f-d9b4-43e7-ac45-447ae60761d1; deviceIdGenerateTime=1593942231353; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2238987881%22%2C%22%24device_id%22%3A%2217217ff01ed47a-0f2438b6ba5fe9-6701434-2073600-17217ff01ee59b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F18%3Farticle%3D253882%22%2C%22%24latest_referrer_host%22%3A%22u.geekbang.org%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2217217ff01ed47a-0f2438b6ba5fe9-6701434-2073600-17217ff01ee59b%22%7D; sensorsdata2015session=%7B%7D; Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1593942244; anonymousUser=-8159088515; shimo_sid=s%3A7skQku6bV0LqhHyJHnozPa33au6q2S8k.6JZEj3tInrkEiPulVa5LD%2BG6Zwxe4iEkZ7r4rr9IHTM; Hm_lpvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1593942291",
           "origin": "https://shimo.im",
           "referer": "https://shimo.im/login?from=home",
           "sec-fetch-dest": "empty",
           "sec-fetch-mode": "cors",
           "sec-fetch-site": "same-origin",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
           "x-requested-with": "XmlHttpRequest",
           "x-source": "lizard-desktop"}

def login(username:str,password:str):
    data = dict(mobile=username,password=password)
    try:
        resp = post(URL,data=urlencode(data),headers=headers)
    except Exception as e:
        print("请求出错了:{}".format(e))
        return
    if resp.status_code is not 204:
        print("响应码错误：{},\n 返回信息:{}\n".format(resp.status_code,resp.text,resp.headers))
        return
    print(resp.headers)
    

if __name__ == '__main__':
    login("your_mobile","your_password")
        