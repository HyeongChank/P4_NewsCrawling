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


# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])

def result():
    platform = request.form['platform']
 
    url = request.form['url']
    start_page = int(request.form['spage'])
    end_page = int(request.form['epage'])

    keyword1 = request.form['keyword1']
    keyword2 = request.form['keyword2']
    keyword3 = request.form['keyword3']
    keyword4 = request.form['keyword4']    
    if platform == 'daum':
        keywords_counts_df, word_counts,counttitle, keyword_counts1, keyword_counts2, keyword_counts3, keyword_counts4, keyword1, keyword2, keyword3, keyword4 = platform_daum(url, start_page, end_page, keyword1, keyword2, keyword3, keyword4)
        print("req pass")
        #그래프 그리고 이미지 저장
        content_keyword(keywords_counts_df)        
        #빈도수 높은 단어 선택, wordcloud 이미지 저장
        top_words = generate_wordcloud(word_counts)

    return render_template('result.html', counttitle=counttitle,top_words=top_words, count1=keyword_counts1, keyword1=keyword1, count2=keyword_counts2, keyword2=keyword2, count3=keyword_counts3, keyword3=keyword3, count4=keyword_counts4, keyword4=keyword4)        


def content_keyword(keywords_counts_df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='word', y='count', data=keywords_counts_df, palette='Set2')
    plt.xlabel("Keywords")
    plt.ylabel("Counts")
    plt.title("Keyword Counts")
    plt.savefig('static/barplot.png')
    #plt.show()

def generate_wordcloud(word_counts):
    #wordcloud를 위한(word_counts(단어,빈도))
    top_words = word_counts.most_common(30)    
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

def generate_word(content, word_counts):
    stop_words = set(stopwords.words('korean'))
    words = content.split()
    words = [word for word in words if not word in stop_words]
    content_without_stopwords = ' '.join(words)

    word_counts.update(content_without_stopwords.split())
    return word_counts

def keyword_count(word_counts, keyword1, keyword2, keyword3, keyword4):
    # 단어 빈도수를 데이터프레임으로 변환
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
    return keywords_counts_df, keyword_counts1, keyword_counts2, keyword_counts3, keyword_counts4

def platform_daum(url, start_page, end_page, keyword1, keyword2, keyword3, keyword4):
    print("daum pass")
    #collections.Counter 함수는 (단어, 빈도수) 나타냄
    #article_titles = []
    article_links = []
    counttitle =0
    word_counts = Counter()
    for page in range(start_page, end_page + 1):
        url = url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for a_tag in soup.select("a.link_txt"):
            link = a_tag.get("href")
            if link.startswith("http"):
                article_links.append(link)
        for link in article_links:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find('div', {'class': 'news_view'})
            counttitle += 1
            if content:
                content = content.get_text()
                # words 는 기사(content) split 한 단어 모음
                generate_word(content, word_counts)

    article_links.clear()
    print(counttitle)

    ## 기사 내용에 keyword 나온 횟수
    keywords_counts_df, keyword_counts1, keyword_counts2, keyword_counts3, keyword_counts4= keyword_count(word_counts, keyword1, keyword2, keyword3, keyword4)

    return keywords_counts_df, word_counts,counttitle, keyword_counts1, keyword_counts2, keyword_counts3, keyword_counts4, keyword1, keyword2, keyword3, keyword4        

# def platform_naver(url, start_page, end_page, keyword1, keyword2, keyword3, keyword4):
#     def load_url():
#         url_naver = url
#         html = requests.get(url_naver, headers={'User-Agent':'Mozilla/5.0'})
#         soup = BeautifulSoup(html.text, "html.parser")
#         return soup

def collect_news(soup):
    title = []
    link_li = []
    content_li= []
    for i in range(1,5):
        for j in range(1,5):
            articles = soup.select(f'#main_content > div > div._persist > div:nth-child(1) > div:nth-child({i}) > div.cluster_body > ul > li:nth-child({j}) > div > a')
            for article in articles:
                link = article['href']
                link_li.append(link)
                # 제목
                text = article.get_text()
                title.append(text)
                # 기사 페이지에 접속해서 HTML 파싱
                article_html = requests.get(link, headers={'User-Agent':'Mozilla/5.0'})
                article_soup = BeautifulSoup(article_html.text, "html.parser")
                
                # 기사 내용 가져오기
                article_content = article_soup.select("#dic_area")
                content_li.append(article_content)
                # print(article_content)
    print(link_li)
    #section_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                articles = soup.select(f'#section_body > ul:nth-child({i}) > li:nth-child({j}) > dl > dt:nth-child({k}) > a')
                for article in articles:
                    link = article['href']
                    link_li.append(link)
                    # 제목
                    text = article.get_text()
                    title.append(text)
                    # 기사 페이지에 접속해서 HTML 파싱
                    article_html = requests.get(link, headers={'User-Agent':'Mozilla/5.0'})
                    article_soup = BeautifulSoup(article_html.text, "html.parser")
                    
                    # 기사 내용 가져오기
                    article_content = article_soup.select("#dic_area")
                    content_li.append(article_content)
                    # print(article_content)



if __name__ == '__main__':
    app.run(debug=True)        


