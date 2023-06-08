import os
import sys
import urllib.request
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import datetime

import requests
from bs4 import BeautifulSoup
#main_content > div > div._persist > div.section_headline > ul > li:nth-child(2) > div.sh_text > a
#main_content > div > div:nth-child(3) > div > div.cluster_body > ul > li:nth-child(1) > div.cluster_text > a
#section_body > ul.type06_headline > li:nth-child(2) > dl > dt:nth-child(2) > a

titles = []
links = []
article_contents = []
def naver_crawling(url, start_page, end_page):
    for i in range(start_page,end_page):
        url = f'{url}&page={i}'
        html = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(html.text, "html.parser")
        # 헤드라인 뉴스
        # articles = soup.select('.sh_text')
        # print(articles)
        # for ar in articles:
        #     link = ar.find('a')['href']
        #     links.append(link)
        #     title = ar.find('a').text
        #     # print(title)            
        #     titles.append(title)
        # # print(links)
        # # print(titles)
        # # 일반 뉴스
        # articles = soup.select('.cluster_text')
        # # print(articles)
        # for ar in articles:
        #     link = ar.find('a')['href']
        #     links.append(link)
        #     title = ar.find('a').text
        #     # print(title)
#section_body      
#section_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a
#.section_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a
        articles = soup.select('#section_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a')
        print(articles)
        # for ar in articles:
        #     link = ar.select('a')
        #     print(link)
            
# <div class="cluster_text">
#                                         <div class="cluster_text_info" data-comment="{gno:'news001,0013950068',params:{sid1:'105'},nclicks:'cmt.count'}">
#                                             <div class="cluster_text_press">연합뉴스</div>
#                                         </div>
                                        
#                                         <a href="C:\git clone\P_NewsCrawling\P4_NewsCrawling" class="cluster_text_headline nclicks(itn.sera)"> "생쥐 간에 사람 간세포 이식했더니…생체리듬이 변했다"</a>
#                                     </div>
# <a href="https://n.news.naver.com/mnews/hotissue/article/001/0013950068?type=series&amp;cid=1087298" class="cluster_text_headline nclicks(itn.sera)"> "생쥐 간에 사람 간세포 이식했더니…생체리듬이 변했다"</a>
        #     print(articles)
        #     for article in articles:
        #         print(article)
        #         link = article['href']
        #         link_li.append(link)
        #         # 제목
        #         text = article.get_text()
        #         title.append(text)
        #         # 기사 페이지에 접속해서 HTML 파싱
        #         article_html = requests.get(link, headers={'User-Agent':'Mozilla/5.0'})
        #         article_soup = BeautifulSoup(article_html.text, "html.parser")
                
        #         # 기사 내용 가져오기
        #         article_content = article_soup.select("#dic_area")
        #         content_li.append(article_content)
        #         # print(article_content)
        # print(link_li)
        # #section_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a
        # for i in range(1,5):
        #     for j in range(1,5):
        #         for k in range(1,5):
        #             articles = soup.select(f'#section_body > ul:nth-child({i}) > li:nth-child({j}) > dl > dt:nth-child({k}) > a')
        #             for article in articles:
        #                 link = article['href']
        #                 link_li.append(link)
        #                 # 제목
        #                 text = article.get_text()
        #                 title.append(text)
        #                 # 기사 페이지에 접속해서 HTML 파싱
        #                 article_html = requests.get(link, headers={'User-Agent':'Mozilla/5.0'})
        #                 article_soup = BeautifulSoup(article_html.text, "html.parser")
                        
        #                 # 기사 내용 가져오기
        #                 article_content = article_soup.select("#dic_area")
        #                 content_li.append(article_content)
        #                 # print(article_content)
        # print(title)
        # print(len(title))

if __name__=='__main__':
    url = f'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
    start_page = 1
    end_page = 5
    naver_crawling(url, start_page, end_page)