import requests
from bs4 import BeautifulSoup
import re

def get_download_link(share_url, pwd):
    # 设置headers以模仿浏览器行为
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    session = requests.Session()
    response = session.get(share_url, headers=headers)
    
    if '输入密码' in response.text and pwd:
        data = {
            'pwd': pwd,
            'submit': '访问'
        }
        response = session.post(share_url, data=data, headers=headers)
        
    soup = BeautifulSoup(response.text, 'html.parser')
    # 解析出真实的下载链接（根据实际情况调整）
    print(soup)
    link_tag = soup.find('a', href=re.compile(r'/s/.*'))
    if link_tag:
        return link_tag['href']
    else:
        print("未能找到下载链接")
        return None

def download_file(url, local_path):
    response = requests.get(url, stream=True)
    with open(local_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

if __name__ == "__main__":
    # share_url = input("请输入百度网盘分享链接: ")
    # pwd = input("请输入提取码 (如果有的话): ")
    share_url, pwd = 'https://pan.baidu.com/s/1_kBQa3yYez3g4ptFY31hRw', '2vj9'

    download_link = get_download_link(share_url, pwd)
    if download_link:
        print(f"获取到的下载链接为: {download_link}")
        save_path = "./downloaded_file"
        download_file(download_link, save_path)
        print("下载完成")
    else:
        print("无法获取下载链接，请检查分享链接和提取码是否正确")