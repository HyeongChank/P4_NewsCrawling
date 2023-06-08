from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
nltk.data.path.insert(0, "D:\김형찬\1project_ai_tensorflow_collect\2crawling_py\P4Crawling\nltk_data")
from nltk.corpus import stopwords
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import datetime
import csv
from nltk.book import *

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

links = []
titles= []

article_contents = []

# 전체 기사 페이지에서 페이지 내 모든 기사의 링크 및 제목 크롤링
def daum_crawling(url, start_page, end_page):
################
    unique_links = []
    for i in range(start_page, end_page):
        url_for = f'{url}?page={i}'
        print(url_for)
        # 웹 페이지 가져오기
        response = requests.get(url_for)
        html = response.text
        #print('html',html)
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(html, "html.parser")
        # 기사들의 outerHTML 가져오기
        articles = soup.select('.tit_thumb')
        for ar in articles:
            link = ar.find('a')['href']
            links.append(link)
            title = ar.get_text()
            titles.append(title)
    print(len(links))
    unique_links = list(set(links))
    print(len(unique_links))
    print(unique_links)
    unique_titles = list(set(titles))
    print(len(unique_titles))
    word_counts = Counter()
    # 기사 링크 저장
    existing_csv_path = "./data/crawlingdata.csv"
    with open(existing_csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(['links'])
        for link in links:
            writer.writerow([link])
    print(f"데이터를 '{existing_csv_path}' 파일에 업데이트하여 저장했습니다.")
    return unique_links, word_counts

## 기사 링크 크롤링(전 단계) 후 링크마다의 세부기사 내용 크롤링
def content_crawling(unique_links):
    for link_detail in unique_links:
        response = requests.get(link_detail)
        html = response.text
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(html, "html.parser")
        # article_content = soup.select('.article_view')
        # .find('p') p태그로 받으려고 하니까 됐다가 안됐다가 함(크롤링 블록이 있는게 아닐까 함)
        content_text = soup.select('.article_view')
        # print(content_text)
        article_contents.append(content_text)
    # print(article_contents)
    return article_contents

def generate_word(article_contents, word_counts):
    # stop_words = set(stopwords.words('korean'))
    conbined_contents = ''.join([str(x) for x in article_contents])
    words = conbined_contents.split()
    # words = [word for word in words if not word in stop_words]
    print(words)
    # content_without_stopwords = ' '.join(words)
    word_counts.update(words)

    return word_counts, words

def keyword_count(word_counts, keyword1, keyword2, keyword3, keyword4, words):
    # 단어 빈도수를 데이터프레임으로 변환
    top_words = word_counts.most_common(10) 
    print(top_words)

    word_counts_df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['count'])
    word_counts_df.index.name = 'word'
    word_counts_df.reset_index(inplace=True)
    # 검색어 단어들만 추출
    keywords = [keyword1, keyword2, keyword3, keyword4]
    # dataframe
    keywords_counts_df = word_counts_df.loc[word_counts_df['word'].isin(keywords)]
    # dictionary
    #keywords_counts_dict = {keyword: keywords_counts_df.loc[keywords_counts_df['word'] == keyword, 'count'].item() for keyword in keywords}
    keywords_counts_dict = {}
    for keyword in keywords:
        count = keywords_counts_df.loc[keywords_counts_df['word'] == keyword, 'count']
        if count.empty:
            keywords_counts_dict[keyword] = 0
        else:
            keywords_counts_dict[keyword] = count.item()
    keyword_counts1 = keywords_counts_dict[keyword1]
    keyword_counts2 = keywords_counts_dict[keyword2]
    keyword_counts3 = keywords_counts_dict[keyword3]
    keyword_counts4 = keywords_counts_dict[keyword4]
    print('key1', keyword_counts1, 'key2', keyword_counts2, 'key3', keyword_counts3,'key4', keyword_counts4)
    return top_words, keyword_counts1, keyword_counts2, keyword_counts3, keyword_counts4


def generate_wordcloud(top_words):
    
    # wordcloud 한글 깨지는 거 방지 : font_path = 'malgun.ttf'
    wordcloud = WordCloud(font_path='malgun.ttf',width=800, height=800, 
                        background_color='white',
                        min_font_size=10).generate(str(top_words))
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    #plt.show()
    wordcloud.to_file('static/wordcloud.png')
    return top_words




if __name__=='__main__':
    url = "https://news.daum.net/breakingnews/digital"
    start_page = 1
    end_page = 11
    keyword1 = '서비스'
    keyword2 = '미래'
    keyword3 = '브랜드'
    keyword4 = '우주'
    unique_links, word_counts = daum_crawling(url, start_page, end_page)
    article_contents = content_crawling(unique_links)
    word_counts, words = generate_word(article_contents, word_counts)
    top_words, keyword_counts1, keyword_counts2, keyword_counts3, keyword_counts4 = keyword_count(word_counts, keyword1, keyword2, keyword3, keyword4, words)
    generate_wordcloud(top_words)

