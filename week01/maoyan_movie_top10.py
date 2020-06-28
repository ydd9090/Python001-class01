from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd
'''
作业一：
爬取猫眼top10电影信息

Beautiful Soup 官方文档：
https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
'''

URL= "https://maoyan.com/films?showType=3"


def get_html(url:str):
    try:
        headers = dict(user-agnet="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")
        resp = get(url,headers=headers)
    except Exception:
        return None
    if resp.status_code == 200:
        return resp.text    # 网页编码情况
    return None

def parse_html(html:str):
    movie_list = []
    bs_info = bs(html,'html.parse')
    if tags_list := bs_info.find_all('div',attrs={'class': 'movie-item film-channel'}):  # 海象运算符
        for index,tags in enumerate(tags_list):
            if index >9:
                break
            #电影名称
            movie_title = tags.find('span', attrs={'class': 'name'}).text
            hover_tags = tags.find_all('span', attrs={'class': 'hover-tag'})
            #电影类型
            movie_type = hover_tags[0].next_sibling.strip()
            #上映日期
            movie_date = hover_tags[2].next_sibling.strip()
            movie_list.append(movie_title,movie_type,movie_date)
    return movie_list





def write_cvs_file(data:list,file_name:str):
    movies = pd.DataFrame(data=data)
    movies.to_csv(filename,encoding='utf-8',index=False,header=False)
    


if __name__ == "__main__":
    if html := get_html(URL): #python3.8 海象运算符
        if movie_list := parse_html(html):
            write_cvs_file(movie_list,".\movies.csv")
        else:
            print("解析网页信息失败...")
    else:
        print("获取网页信息失败...")