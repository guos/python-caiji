from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import http.client
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.writer.excel import ExcelWriter
import json
import re
import copy
http.client._MAXHEADERS = 1000

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"}
def down_pic(url, path):
    try:
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req).read()
        with open(path, 'wb') as f:
            f.write(data)
            f.close()
    except Exception as e:
        print(str(e))

def getHtmlFromUrl(url):
	try:
		header_selfdefine={
			 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
			 'Accept': '*/*',
		}

		request_obj=urllib.request.Request(url=url, headers=header_selfdefine)
		response_obj=urllib.request.urlopen(request_obj)
		html_code=response_obj.read().decode('utf-8')
		return html_code
	except:
		print("重试"+url)
		getHtmlFromUrl(url)



def getRenderdHtmlFromUrl1(url):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument("window-size=1024,768")
	chrome_options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
	chrome_options.add_argument("--no-sandbox")
	browser = webdriver.Chrome(chrome_options=chrome_options)
	browser.get(url)
	time.sleep(5)
	return BeautifulSoup(browser.page_source, "html.parser",from_encoding="utf-8")