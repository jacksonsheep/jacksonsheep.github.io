import requests
from bs4 import BeautifulSoup

# 澎湃新闻头条的URL
url = "https://www.thepaper.cn/"

# 发送HTTP请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 澎湃新闻的头条通常在具有特定类名的标签中，这里以 'list-title' 为例
    # 你可能需要查看网页的源代码来找到正确的类名
    titles = soup.find_all('a', class_='list-title')

    # 输出所有头条的标题和链接
    for title in titles:
        print(f"标题: {title.text.strip()}")
        print(f"链接: {title['href']}\n")
else:
    print(f"无法获取页面，状态码: {response.status_code}")
