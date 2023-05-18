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





url = 'https://news.daum.net/digital#1'
start_page = 1
end_page = 2
keyword1 = 'it'
keyword2 = 'com'
keyword3 = 'platform'
keyword4 = 'key'

links = []
titles= []
url = "https://news.daum.net/breakingnews/digital"
################
#https://news.daum.net/breakingnews/digital?page=10

# 웹 페이지 가져오기
response = requests.get(url)
html = response.text
#print('html',html)
# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 기사들의 outerHTML 가져오기
articles = soup.select('.tit_thumb')
#print(articles)
for ar in articles:
    #print('ar', ar)
    
    link = ar.find('a')['href']
    links.append(link)
    title = ar.get_text()
    titles.append(title)
# print(links)
# print(titles)


## 세부기사


url2 = 'https://v.daum.net/v/20230518221744630'
response = requests.get(url2)
html = response.text
#print('html',html)
# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, "html.parser")
articless = soup.select('.article_view')
print(articless)
# <div class="news_view fs_type1" data-cloud="article_body" data-cvdc-comp-name="article_body">    
#         <div id="layerTranslateNotice" style="display:none;"> 
#         </div> 
#         <div class="article_view" data-translation-body="true" data-tiara-layer="article_body" data-tiara-action-name="본문이미지확대_클릭"> 
#          <section dmcf-sid="67hugrsbf0">
#           <figure class="figure_frm origin_fig" dmcf-pid="PN9aZ7qkf3" dmcf-ptype="figure">
#            <p class="link_figure"><img alt="윤석열 대통령이 지난 4일 충남 아산 삼성디스플레이를 방문해 OLED 모듈 라인을 시찰하고 있다. /사진=대통령실 제공,뉴시스" class="thumb_g_article" data-org-src="https://t1.daumcdn.net/news/202305/18/moneytoday/20230518163759261tbkc.jpg" data-org-width="1024" dmcf-mid="8SdIBPxv9p" dmcf-mtype="image" height="auto" src="https://img2.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/202305/18/moneytoday/20230518163759261tbkc.jpg" width="658"></p>
#            <figcaption class="txt_caption default_figure">
#             윤석열 대통령이 지난 4일 충남 아산 삼성디스플레이를 방문해 OLED 모듈 라인을 시찰하고 있다. /사진=대통령실 제공,뉴시스
#            </figcaption>
#           </figure>
#           <p dmcf-pid="Qj2N5zBE2F" dmcf-ptype="general">정부가 27일 발표한 디스플레이산업 혁신전략을 두고 국내 디스플레이 업계가 "매우 환영한다"고 밝혔다. 한국과 중국이 글로벌 디스플레이 산업 주도권을 두고 엎치락뒤치락하며 경쟁을 벌이고 있는 가운데 정부가 나서 세계 1위 탈환에 대한 의지를 드러내며 국내 기업들에게 힘을 실어주는 조치를 적기에 취했다는 반응이다. </p>
#           <p dmcf-pid="xepRS5tnqt" dmcf-ptype="general">업계는 특히 정부가 전세계 시장점유율 50% 달성을 목표로, 중국과의 산업 기술력 격차 확대에 대한 의지를 분명히 한 것을 긍정적으로 평가했다. 한국은 2004년 디스플레이 시장점유율 1위를 차지한 후 17년간 왕좌를 지켜왔지만, 2021년 중국에 1위 자리를 내줬다. 시장조사업체 옴디아에 따르면 지난해 국가별 전세계 디스플레이 시장점유율은 중국이 42.5%로 1위, 한국이 36.9%로 2위였다. 중국은 국가 차원의 막대한 보조금 투입과 저렴한 인건비를 바탕으로 저가 물량 공세를 통해 디스플레이 점유율을 무섭게 늘려왔다. 디스플레이 업계 관계자는 "국가적 대응을 하는 중국과 달리 한국 디스플레이 기업들은 오직 자력갱생해왔기에 이미 시작점이 달랐다"며 "최대 25% 세액공제 확대가 중국 기업들과의 경쟁에 실질적 도움이 될 것"이라고 말했다. </p>
#           <div class="ad_body2" id="kakao_ad_EKQqAd" style="text-decoration: none; min-width: 655px; min-height: 120px; width: 655px; height: 120px;"><div data-ad-creative-wrap="outer" class="adfit__banner__outer adfit__debug-toolbar-container" style="position: absolute; inset: 0px;"><div data-ad-creative-wrap="inner" class="adfit__banner__inner" id="0018cbce-ac01-414b-9842-732e71ba44b9"><iframe src="https://t1.daumcdn.net/adfit/adunit_style/1d52674aa0220007881f0531b105924070bcf66d" width="100%" style="position:absolute;top:0;left:0;display:block;border:none;height:100%;width:100%;min-width:655px;min-height:120px;overflow:hidden;padding:0;margin:0 auto" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" name="%5B%7B%22usePrefersColorScheme%22%3A%22N%22%2C%22adunitId%22%3A%22DAN-LMhCax710HKR6iRC%22%2C%22width%22%3A655%2C%22height%22%3A120%2C%22usePreferColorScheme%22%3A%22N%22%2C%22frameId%22%3A%226b8e0b38-2bac-412f-a978-9a4008141e64%22%2C%22frameName%22%3A%226b8e0b38-2bac-412f-a978-9a4008141e64%22%2C%22bidId%22%3A%22ade28ef022a94d1e8888d152bb260a65%22%2C%22safeFrameData%22%3A%7B%22id%22%3A%220018cbce-ac01-414b-9842-732e71ba44b9%22%2C%22meta%22%3A%7B%22shared%22%3A%7B%22sf_ver%22%3A%221-1-0%22%2C%22ck_on%22%3A0%2C%22flash_ver%22%3A0%7D%2C%22nas%22%3A%7B%22enabled%22%3Atrue%7D%7D%2C%22supports%22%3A%7B%22exp-ovr%22%3Atrue%2C%22exp-push%22%3Atrue%2C%22read-cookie%22%3Afalse%2C%22write-cookie%22%3Afalse%7D%2C%22geom%22%3A%7B%22win%22%3A%7B%22t%22%3A247%2C%22b%22%3A897%2C%22l%22%3A779%2C%22r%22%3A1806%2C%22w%22%3A1027%2C%22h%22%3A650%7D%2C%22self%22%3A%7B%22t%22%3A1268.38818359375%2C%22b%22%3A1388.3881912231445%2C%22l%22%3A67.5%2C%22r%22%3A722.5%2C%22w%22%3A655%2C%22h%22%3A120.00000762939453%2C%22xiv%22%3A0%2C%22yiv%22%3A0%2C%22iv%22%3A0%2C%22z%22%3A%22auto%22%7D%2C%22exp%22%3A%7B%22t%22%3A1268.38818359375%2C%22b%22%3A0%2C%22l%22%3A67.5%2C%22r%22%3A286.5%2C%22xs%22%3A0%2C%22ys%22%3A0%7D%7D%2C%22winHasFocus%22%3Atrue%2C%22html%22%3A%22%22%7D%2C%22title%22%3A%22%EC%9C%A0%EB%8B%88%ED%81%B4%EB%A1%9C%20%ED%8B%B0%EC%85%94%EC%B8%A0%20%EC%BB%AC%EB%A0%89%EC%85%98%22%2C%22mainImage%22%3A%7B%22url%22%3A%22https%3A%2F%2Ft1.daumcdn.net%2Fb2%2Fcreative%2F48057%2Fcab7928a6687363943778ec9d0a97813.jpg%22%2C%22width%22%3A1200%2C%22height%22%3A600%7D%2C%22profileName%22%3A%22UNIQLO%22%2C%22adInfoIcon%22%3A%7B%22url%22%3A%22https%3A%2F%2Ft1.daumcdn.net%2Fbiz%2Fui%2Fad%2FADmark%2Fi_mark_200803.png%22%2C%22width%22%3A15%2C%22height%22%3A15%7D%2C%22adInfoUrl%22%3A%22https%3A%2F%2Finfo.ad.daum.net%2Foptout.do%22%2C%22landingUrl%22%3A%22https%3A%2F%2Ftr.ad.daum.net%2Fclk%3Fwa%3DaFKBcGphmyF7d12TPIi4Gg%26enc%3DdoLn_EUVQu0Lc6m_kZoyhgOo3LhOepnhoG5r60XDT0clwSKaZNRhl8XsyY5GtkIy7Jc1s6tmaPKR88YNNDQvdxeRB4ygXAbbPEUFMVc4KdCYt57riYdlEIsYWjhhXYurNLfLcTNYi2TfN0N2AaH5O9t9400C5MTUi7BwMunUcqokdOTZ9dluIfnhPlf8Y04Jw74mX0gl3TdrQ_LD0UKzZDmlo9vUX183AwtXx8ZckdYxWQyocpBPJtjlivpWOp-d0cRyWeIQ2P3yzxujITj5CX7vjYfafAE5vfvkwJfhc_sTI_N7Jug350ksmOuUWA74x1fKfqXG7LnJbEEjC8jtNi2GuyWS0pyPBuuJJC4mHtpzJIbuy2hEjgykBgOW9StgpMbWK6-k5eJlgnM4KN2iDvw7jbAwSvLjh0t7jbmaEpmc_HaY5gR4zpYdZLDHQ32GMK6NlcoOLuKHBjuXRjsuRyuOL6397SCG_UwPSJgPQr6f2j1e8y_oisp8sV-RBoty-P94CiVRJrpzkpZrINQTl0_xH0U4YO5ZyRGmUaJP1coKW35GVUbuH89HXfZOu_5GUbY66TD9usg5IMHzhWBLSAhJcLb_p50f90ZeX0CZHDuS8OaVIOAddNwpicxYNvZPfR7V9hcwLAPVQEvlnRWBKShON21fsYW8VBz6EOoOM0veG0KeOK1L3bRMsVzKOXfSqNs6nMObL1d8CX_s7c2-LkSK6ySKEJKNG1Gprm5ixywi-mBGxkOtphwKa61fTKXv%26signature%3D101b993fef9d4a4f378959531fddab89%26lc%3D1%22%2C%22useAdInfoIcon%22%3Afalse%2C%22useAdInfoUrl%22%3Afalse%2C%22events%22%3A%5B%7B%22type%22%3A%22viewable%22%2C%22url%22%3A%22https%3A%2F%2Ftr.ad.daum.net%2Fvimp%3Fwa%3DaFKBcGphmyF7d12TPIi4Gg%26enc%3DdoLn_EUVQu0Lc6m_kZoyhgOo3LhOepnhoG5r60XDT0clwSKaZNRhl8XsyY5GtkIy7Jc1s6tmaPKR88YNNDQvdxeRB4ygXAbbPEUFMVc4KdCYt57riYdlEIsYWjhhXYurNLfLcTNYi2TfN0N2AaH5O9t9400C5MTUi7BwMunUcqokdOTZ9dluIfnhPlf8Y04Jw74mX0gl3TdrQ_LD0UKzZDmlo9vUX183AwtXx8ZckdYxWQyocpBPJtjlivpWOp-d0cRyWeIQ2P3yzxujITj5CZ8kP5YeJOqYEjBQqMfDAP4ZDug_mhtTpjM1LyI70iHz4LlHbwO6P1BjadGIHGg2mP_fog-WcTzbmIAJnSRqOUHw2s1vWHhwkay6nyQoNBZz%26signature%3D6477b375141a3bb0b7f116b357322edd%26lc%3D1%22%7D%2C%7B%22type%22%3A%22hide%22%2C%22url%22%3A%22https%3A%2F%2Ftr.ad.daum.net%2Fac%3Fwa%3DaFKBcGphmyF7d12TPIi4Gg%26enc%3DdoLn_EUVQu0Lc6m_kZoyhgOo3LhOepnhoG5r60XDT0clwSKaZNRhl8XsyY5GtkIy7Jc1s6tmaPKR88YNNDQvdxeRB4ygXAbbPEUFMVc4KdCYt57riYdlEIsYWjhhXYurNLfLcTNYi2TfN0N2AaH5O9t9400C5MTUi7BwMunUcqokdOTZ9dluIfnhPlf8Y04Jw74mX0gl3TdrQ_LD0UKzZDmlo9vUX183AwtXx8ZckdYxWQyocpBPJtjlivpWOp-d0cRyWeIQ2P3yzxujITj5CZ8kP5YeJOqYEjBQqMfDAP4ZDug_mhtTpjM1LyI70iHz4LlHbwO6P1BjadGIHGg2mP_fog-WcTzbmIAJnSRqOUG8vHmUKGwaDP5-thh9JCCV%26signature%3D4623c68416a6013d918d318831d0646a%26lc%3D1%22%7D%2C%7B%22type%22%3A%22rendered%22%2C%22url%22%3A%22https%3A%2F%2Fserv.ds.kakao.com%2Fdspr%2Fsync%3Fdspr%3DalHgmZ_rq05OpnPWXKqO-R1ac5RlRCnJcXuv3-y0kdqDGGkUR7h1V4WMamfzGqTaMcGM9XKe5pWYzznoIMgoF-owrt3SRVoBqfoEvAxPhdvR_N-zz394CV_L_GDn63ekvPinih1Tc7ZnSqPpDyfPM0ZmSriLUj1oTCbwSwsu9OLayM7lBCqvoqqG1uBFAr-WASSuVhAt8Z1MGw-zJBdoO-G49oSf1WdjcYMeQYqlnijcjCR2aMxW-9JIpicUxewku_dXJxT_N4ghB3VNH_QHZ5-78pDybM_0Rz9fFog1aax_k1IB04kaT-DJRp_gt4sI9wu-R9zdDWAZvNY_PZSDc-b01L_dpa7aPwUs06dVWbqzXqDfZfyYRxCs3f7J0eP7MMfw7OF6tMW4lT8wz2Bzyca3oo-N-sEsIa7DIN0dehwaJJv_09ZzTZCXDsSxrwhRxTEcnpIWtwcqzCVm5WGYz5QqZThCVV9HP_ZQcqqLVNETSBolGiVoq8eKLoj445ZYuCEnyq6dRwEfcAfvHNA6F6NZB5AErr66J9_Jrh2TGRAkP6-WCqMlp8xYue5pXXXLKgtwKKZ_WhW7Fn3Vli_uOvBAK3x5Lhio3arBShRqQKtcGz6tKpzI7eumqMBCrZVhy9TaKykasgxcyu13gy3YJeUwMl9BMNz48ch_S6IIZ1e55lqIeDYWLBCsX75Mo0GjmsXI4J0akiMBjGC_6fgFV_j4uMDttYNgAfri_nWSro9yZi8WYIBS3nPWWUkZr1Bc87a3hx23bf6TqjDTo6CIdvd6B2-GZ4g4xw-_MH3rmbulVjzrWAkWOz8JCNWkt0gq%22%7D%5D%2C%22dspId%22%3A%22MOMENT%22%2C%22altText%22%3A%22%EA%B4%91%EA%B3%A0%20%EC%9C%A0%EB%8B%88%ED%81%B4%EB%A1%9C%20%EA%B4%91%EA%B3%A0%EC%9E%85%EB%8B%88%EB%8B%A4%22%2C%22nasTemplateSeq%22%3A126%2C%22type%22%3A%22native%22%7D%5D" id="6b8e0b38-2bac-412f-a978-9a4008141e64" title="광고"></iframe></div></div>
#             <ins data-ad-unit="DAN-LMhCax710HKR6iRC" data-ad-param-cp="5_pc_media_news" data-ad-param-channel="harmony" data-ad-onfail="removeArticleMiddleAd" data-ad-width="100%">
#             </ins>
#         </div><p dmcf-pid="yGjY6no5f1" dmcf-ptype="general">업계는 특히 전문인력 9000명 양성 계획을 시급한 지원책 중 하나로 꼽았다. 디스플레이 산업은 OLED(유기발광다이오드)와 차세대 무기발광 디스플레이 등 첨단 기술 위주로 재편되고 있다. 신기술 개발을 위해선 전문 연구개발(R&amp;D)인력이 필수적이다. 이공계 기피 현상과 반도체 산업으로의 이탈이 겹치면서 디스플레이 업계는 인력난을 호소해왔다. 또 다른 국내 업체 관계자는 "디스플레이 산업의 중장기적 발전을 위해선 국가적 차원에서의 인력 양성이 꼭 필요하다"고 말했다. </p>
#           <p dmcf-pid="WHAGPLg1K5" dmcf-ptype="general">정부가 이날 발표한 디스플레이 혁신 전략은 2027년 세계 1위를 목표로 민간의 설비와 R&amp;D를 적극 지원하는데 초점을 맞췄다. 최대 25% 세액공제 확대와 전문인력 9000명 양성, 소부장 자립화율 80% 확보를 핵심으로 세계 시장 점유율 50%를 달성하고 경쟁국과 기술격차를 5년 이상으로 벌리겠다는 계획이다. </p>
#           <p dmcf-pid="YHAGPLg1qZ" dmcf-ptype="general">한지연 기자 vividhan@mt.co.kr</p>
#          </section> 
#         </div> 
#         <p data-translation="true">저작권자 ⓒ '돈이 보이는 리얼타임 뉴스' 머니투데이 </p> 
#        </div>
# 기사들의 outerHTML 가져오기

# for ar in articless:
#     print('ar', ar)
    
  
#     article_body = ar.find('p')
#     print(article_body)
    # 텍스트 추출
    # text = article.find('a').text
    # print("텍스트:", text)
    
    
# def daum_crawling_news_main():
#     url = f"https://news.daum.net/digital#1"
#     print(url)
#     response = requests.get(url)

#     # BeautifulSoup 객체 생성
#     soup = BeautifulSoup(response.text, 'html.parser')

#     for i in range(1,10):
#         for j in range(1,10):
#             article = soup.select(f'body > div.container-doc.cont-category > main > section > div.main-sub > div:nth-child({i}) > ul > li:nth-child({j}) > div > div > strong > a')
#             # for article in articles:
#             print(article)
#             link = article['href']
#             links.append(link)
#             text = article.get_text()
#             titles.append(text)
#             print(link)
#             print(text)

    # for i in range(1,10):
    #     articles = soup.select(f'body > div.container-doc.cont-category > main > section > div.main-sub > div.box_g.box_news_major > ul > li:nth-child({i}) > strong > a')
    #     for article in articles:
    #         link = article['href']
    #         links.append(link)
    #         text = article.get_text()
    #         titles.append(text)
            
    # for i in range(1,10):
    #     for j in range(1,10):
    #         articles = soup.select(f'body > div.container-doc.cont-category > main > section > div.main-sub > div:nth-child({i}) > ul > li:nth-child({j}) > div > div.cont_thumb > strong > a')
    #         for article in articles:
    #             link = article['href']
    #             links.append(link)
    #             text = article.get_text()
    #             titles.append(text)
                    
    # for page in range(1, 11):  
    #     url = f"https://news.daum.net/digital#{page}"
    #     print(url)
    #     response = requests.get(url)

    #     # BeautifulSoup 객체 생성
    #     soup = BeautifulSoup(response.text, 'html.parser')

    #     for i in range(1,10):
    #         for j in range(1,10):
    #             article = soup.select(f'body > div.container-doc.cont-category > main > section > div.main-sub > div:nth-child({i}) > ul > li:nth-child({j}) > div > div > strong > a')
    #             # for article in articles:
    #             print(article)
                
    #             a_tag = soup.find('a')
    #             link = a_tag['href']
    #             title = a_tag.text
    #             print(link)
    #             print(title)


                # links.append(link)
                # text = article.get_text()
                # print(text)
                # titles.append(text)

  
            
    # print(len(titles))
    # print(len(links))
    # print(titles)
    # print(links)
    
#     return links

# if __name__=='__main__':
#     links = daum_crawling_news_main()


#section_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a
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
#                     # print(article_content)
# print(link_li)


