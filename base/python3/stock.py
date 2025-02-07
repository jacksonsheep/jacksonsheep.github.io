import requests 
from json import loads
from sys import argv
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

def stock_infomations():
    '''
    https://push2his.eastmoney.com/api/qt/stock/kline/get 是东方财富网用于获取股票K线数据的API，以下是对其常见参数含义的详细解释：
    fields1

    含义：指定获取的基础行情字段。这些字段通常包含股票的基本交易信息。
    示例值及意义：例如 f1,f2,f3,f4,f5,f6，其中可能 f1 代表开盘价，f2 代表收盘价，f3 代表最高价，f4 代表最低价，f5 代表成交量，f6 代表成交额 。不过实际含义可能需要参考东方财富网的详细文档，不同版本可能有细微差异。

    fields2

    含义：指定获取的扩展行情字段。这些字段包含更多关于股票交易的详细信息，可能涉及盘口数据、技术指标等方面。
    示例值及意义：f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61 等，这些字段可能代表诸如委买委卖数据、大单交易情况等，同样具体含义需参考官方文档。

    klt

    含义：K线类型，用于指定要获取的K线周期。
    常见取值及意义：
    1：表示1分钟K线。
    5：表示5分钟K线。
    15：表示15分钟K线。
    30：表示30分钟K线。
    60：表示60分钟K线。
    101：表示日K线。
    102：表示周K线。
    103：表示月K线。



    fqt

    含义：复权类型。用于指定是否对K线数据进行复权处理以及复权的方式。
    常见取值及意义：
    0：不复权。
    1：前复权，以当前股价为基准，将历史股价进行调整，使图形更加连贯，便于分析长期趋势。
    2：后复权，以最初股价为基准，将后续股价进行调整，可直观看到股票从上市以来的累计涨幅。



    beg

    含义：开始日期，用于指定要获取的K线数据的起始时间。
    格式要求：格式为 YYYYMMDD，例如 20230101 表示2023年1月1日。

    end

    含义：结束日期，用于指定要获取的K线数据的截止时间。
    格式要求：与 beg 格式相同，为 YYYYMMDD，例如 20240101 表示2024年1月1日。

    secid

    含义：证券ID，用于唯一标识要获取数据的证券（股票、基金等）。
    格式要求：格式为 市场标识.证券代码，例如对于深交所上市的浪潮信息（股票代码000977），secid 为 0.000977；上交所上市的股票，市场标识可能为 1 。具体市场标识对应关系也需参考东方财富网文档说明.
    '''
    pass

def get_stock_days(stock='0.000977', k_time=5, days=9):
    current_date = datetime.now().date();
    week_date = current_date+ timedelta(days=-9)
    end_date = datetime.strftime(current_date, "%Y%m%d")
    start_date = end_date if k_time < 100 else datetime.strftime(week_date, "%Y%m%d")
    url = 'https://push2his.eastmoney.com/api/qt/stock/kline/get'
    params = {
        'fields1': 'f1,f2,f3,f4,f5,f6',
        'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
        'klt': k_time,
        'fqt': 0,
        'beg': start_date,
        'end': end_date,
        'secid': stock
    }
    # print(params)
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = loads(response.text)
        # print(data)
        kline_data = data['data']['klines']
        redis = pydb.connect_to_redis()
        print('[start,\tend,\tmax,\tmin,\tcount,\tsum]')
        for day in kline_data:
            day_result = [item.strip() for item in day.split(",")]
            day_result[0] = stock+':'+day_result[0]
            if k_time == 101 :
                redis.set(day_result[0], '-'.join(day_result[1:]))
            print(day_result)
    else:
        print(f"request error code is: {response.status_code}")

def get_stock_news():
    response = api_request(request_type='get',url="http://eastmoney.com",headers=headers)
    if response:
        soup = BeautifulSoup(response, 'html.parser')
        # news_list = soup.find('div', class_='nmlist').find_all('a')
        # news_list = soup.find('div',class_='news_kuaixun').find_all('a')
        # news_list = soup.find('div', class_='hsgs_news').find_all('a')
        # news_list = soup.find('div', class_='news_l2_b').find_all('a')
        news_list = soup.find('div', class_='cjdd_tab_c').find_all('a')
        for item in news_list:
            print(item.get_text(strip=True)+'\t'+item.get('href'))

# TODO fund info search
def get_fund_days():
    pass
    # with open('./test.html', 'r', encoding='utf-8') as file:
    #     response = file.read()
    
# TODO find stock by name， return id
def search_stocks(name):
    # with open('./test.html', 'r', encoding='utf-8') as file:
    #     response = file.read()
    # params = {'keyword': name}
    response = api_request(request_type='get', url='https://stock.eastmoney.com/', headers=headers)
    soup = BeautifulSoup(response, 'html.parser')
    
    print(soup)
    # 找到股票列表的表格
    # stock_table = soup.find('table', {'id': ' QUOTE_TABLE'})
    # if not stock_table:
    #     print('没有找到相关股票。')
    #     return
    
    # # 遍历表格中的行
    # for row in stock_table.find_all('tr')[1:]:  # 跳过标题行
    #     cols = row.find_all('td')
    #     if len(cols) > 1:  # 确保有足够的数据列
    #         stock_id = cols[0].text.strip()
    #         stock_name = cols[1].text.strip()
    #         print(f'股票ID: {stock_id}, 股票名称: {stock_name}')

if __name__ == "__main__":
    # print(argv)
    if len(argv) < 2:
        print("invalid args to found")
    else:
        match argv[1]:
            case 'stock':  # 0.000977 1.600756 0.159934
              code = input('code[0.000977 1.600756 0.159934]:').strip()
              k = input('k:').strip()
              day = input('days:').strip()
              code = code if code else '0.000977'
              k = int(k) if k else 5
              day = int(day) if day else -9
              get_stock_days(stock = code, k_time = k, days = day)
            case 'top': 
              get_stock_news() 
            case 'search':
                search_stocks('茅台')

