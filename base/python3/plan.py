import requests
from urllib.parse import quote
import pydb
from bs4 import BeautifulSoup
import json
import sys 

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_baidu_hot_search():
    url = 'https://top.baidu.com/board?tab=realtime'
   
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        hot_search_list = []

        # 查找包含热榜信息的元素
        items = soup.select('.c-single-text-ellipsis')

        for item in items:
            title = item.get_text(strip=True)
            if title:
                hot_search_list.append(title)
                print(title)

        return hot_search_list
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None
 
def api_send_request(method, url, params=None, headers=None):
   '''
   转发请求到目的主机
   @param method str 请求方法
   @param url str 请求地址
   @param params dict 请求参数
   @param headers dict 请求头
   '''
   method = str.upper(method)
   if method == "POST":
       return requests.post(url=url, data=params, headers=headers)
   elif method == "GET":
       return requests.get(url=url, params=params, headers=headers)
   else:
       return None

def get_flight_price(start, end, date):
    url = 'https://www.ly.com/flights/itinerary/oneway?date='+date+'&from='+quote(start)+'&to='+quote(end)+'&fromairport=&toairport=&p=&childticket=0,0'
    url = 'https://www.ly.com/flights/itinerary/oneway/URC-TNA?from=%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90&to=%E6%B5%8E%E5%8D%97&date=2025-02-03&fromairport=&toairport='
    response = requests.get( url ,headers=headers)
    print(url)
    print(response)
    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.text, 'html.parser')

    #     hot_search_list = []
    #     items = soup.select('.c-single-text-ellipsis')

    #     for item in items:
    #         title = item.get_text(strip=True)
    #         if title:
    #             hot_search_list.append(title)

    #     return hot_search_list
    # else:
    #     print(f"Failed to retrieve data: {response.status_code}")
    #     return None

if __name__ == '__main__':
    get_baidu_hot_search()
    # get_flight_price('济南','乌鲁木齐','2025-02-03')
