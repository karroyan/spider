import time
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup

url = 'https://www.16personalities.com/free-personality-test'
response = requests.get(url).text
#print(response)

def main(response):
    soup = BeautifulSoup(response, "lxml")
    q_list = soup.find('quiz').text
    print(q_list)
    for q in list(q_list):
        print(q)

# mbtiURL = 'https://www.16personalities.com/free-personality-test'
# # mbtiURL = 'https://ks.wjx.top/jq/55123312.aspx'

# def parse_text_data(resp):
#     '''
#     爬取题目
#     '''
#     print(resp.html.find('quiz', first=True))
#     questions = resp.html.find('quiz', first=True).text
#     print('***************************************************\n')
#     print(questions)
 
#     for i, q in enumerate(questions):
#         title = q.find(':question', first=True).text
#         print(title)
#         print('***************************************************\n')
#         time.sleep(0.5)



# def main():
#     print('开始爬取问卷内容')
#     print('链接:%s' % mbtiURL)
#     session = HTMLSession()
#     resp = session.get(mbtiURL)
#     parse_text_data(resp)

if __name__ == '__main__':
    main(response)