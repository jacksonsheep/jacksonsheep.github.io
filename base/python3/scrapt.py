import requests 
from json import loads
from sys import argv
from urllib.parse import quote
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
import pydb


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8'
}

def api_request(request_type, url, headers, params=None):
    
    if request_type == 'get' or request_type == 'GET' :
        response = requests.get(url, headers=headers, params=params)
    elif request_type == 'post' or request_type == 'POST' :
        response = requests.post(url, headers=headers, data=params)
    else :
        return None

    if response.status_code == 200 :
        return response.content
    else :
        print(f"Failed to retrieve data: {response.status_code}")
        return None

def get_baidu_top():
    url = 'https://top.baidu.com/board?tab=realtime'
   
    response = api_request(request_type='get',url=url, headers=headers)
    
    if response :
        soup = BeautifulSoup(response, 'html.parser')
        hot_search_list = []

        # 查找包含热榜信息的元素
        items = soup.select('.c-single-text-ellipsis')

        for item in items:
            title = item.get_text(strip=True)
            if title:
                hot_search_list.append(title)
                print(title)

        return hot_search_list
    return None

def get_flight_price(way, date):
    if way =='work':
        url = 'https://www.ly.com/flights/itinerary/oneway/URC-TNA?from=%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90&to=%E6%B5%8E%E5%8D%97&date='+date+'&fromairport=&toairport='
    elif way == 'home':
        url = 'https://www.ly.com/flights/itinerary/oneway/URC-TNA?from=%E6%B5%8E%E5%8D%97&to=%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90&date='+date+'&fromairport=&toairport='
    else:
        return 

    response = requests.get( url ,headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 查找所有包含航班信息的元素（假设在一个 div 中）
        # print (soup)
        flight_items = soup.find_all('div', class_='flight-item')
        flight_list = []
        for item in flight_items:
            flight_info = {}
            flight_info['number'] = item.find('p', class_='flight-item-name').get_text(strip=True)
            flight_info['departure'] = item.find('div', class_='f-startTime').find('strong').get_text(strip=True)
            flight_info['arrival'] = item.find('div', class_='f-endTime').find('strong').get_text(strip=True)
            flight_info['price'] = item.find('div', class_='head-prices').find('em').get_text(strip=True)
            flight_list.append(flight_info)
            # print(flight_info)
        sorted_list = sorted(flight_list, key=lambda x: x['price'], reverse=True)
        for item in sorted_list:
            print(item)
        return sorted_list
       
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

def search_baidu(search_query):
    base_url = "https://www.baidu.com/s"
    params = {
        'wd': search_query,  # 搜索关键词
        'rn': 10      # 每页显示的结果数量
    }
  
      # 发送GET请求
    response = api_request('get',base_url, params=params, headers=headers)
    if response :
        soup = BeautifulSoup(response, 'html.parser')
        
        # 找到所有搜索结果项
        for item in soup.find_all('div', class_='c-container'):
            title_tag = item.find('h3')
            link_tag = item.find('a')
            
            if title_tag and link_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag['href']
                
                # 过滤掉百度自身的广告和其他非相关内容
                if not link.startswith('http://www.baidu.com/link?url='):
                    continue
                
                print(f"{idx}. {title}   {link}")

if __name__ == "__main__":
    # print(argv)
    if len(argv) < 2:
        print("invalid args to found")
    else:
        match argv[1]:
            case 'top': get_baidu_top()
            case 'plan': 
                if len(argv) == 4:
                        get_flight_price(argv[2], argv[3])
                else :
                    print('error input')
            case 'search': 
                if len(argv) == 3:
                    search_baidu(argv[2])
                else :
                    print('error input')

