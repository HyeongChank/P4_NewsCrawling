
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql

# 그래프 그리기
def content_keyword(word, count, keywords_counts_df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=word, y=count, data=keywords_counts_df, palette='Set2')
    plt.xlabel("Keywords")
    plt.ylabel("Counts")
    plt.title("Keyword Counts")
    plt.savefig('static/barplot.png')
    #plt.show()
content_keyword()


def connect_db():
    conn = pymysql.connect(host='localhost', user='musthave', password='jsk281988', db='member', charset='utf8')
    cur = conn.cursor()
    sql = 'insert into goodsinfo(goodscd, goodsname, unitcd, unitprice, stat) values(%s, %s, %s, %d, %s)'
    vals = ('GDS07', 'book', '03', '5000', 'Y')
    cur.execute(sql, vals)
    conn.commit()
    conn.close()
