#!/usr/bin/env python
# coding: utf-8

# ### 네이버 영화 리뷰 문장 수집
# - 하나의 페이지에서 리뷰 데이터 수집
# - 다섯 페이지에서 리뷰 데이터 수집 후 워드클라우드 만들어보기

# In[1]:


import requests as req
from bs4 import BeautifulSoup as bs
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}


# In[9]:


url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=74977&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
# html 정보 요청
res = req.get(url, headers = header)
print(res)
# 파이썬 객체 변환
html = bs(res.text, 'lxml')
html


# In[55]:


# 선택자로 리뷰 문장 접근하기
# 관람객 단어는 제외하기
# select_one() : 제일 처음 등장하는 해당 태그의 값을 접근 추출 -> 요소 1개
# select() : 해당 태그에 모든 값을 접근 추출 -> 요소 여러개
reple = html.select('p > span:last-child') # list
len(reple)
# 0번째->text
reple[0].text.strip()
reple_txt = []
for i in range(0, len(reple), 1):
    # i 인덱스 번호
    reple_txt.append(reple[i].text.strip())
reple_txt


# ### 1~5페이지 리뷰 데이터 수집
#  - 단순 출력해보기
#  - txt 메모장에 저장 : 파일 다루기
#  - 워드클라우드 생성

# In[59]:


# 4번째 페이지 접근하는 코드
# url 주소에 페이지 번호 연결하기
# url~~~~false&page=4
url='https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=74977&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'
res = req.get(url, headers = header, params = {'page':3})
print(res.url)


# In[77]:


# 1~5 리뷰 List
reple_lst = []


# In[78]:


# 1~5페이지 url 접근
for i in range(1,6,1):
    url='https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=74977&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'
    res = req.get(url, headers = header, params = {'page':i})
    # 파이썬 객체 변환
    html = bs(res.text, 'lxml')
#     print('-' * 30+f'페이지 번호 : {i}' +'-'*30)
    print('-' * 30+f'페이지 번호 : '+ str(i) +'-'*30)
    reple = html.select('p > span:last-child')
    for j in range(0, len(reple), 1):
        print(f'{j+1} ' + reple[j].text.strip())
        reple_lst.append(reple[j].text.strip())


# In[79]:


reple_lst


# ### 파일 다루기
# - 파일 읽기
# - 파일 쓰기

# In[80]:


# 쓰기 -> write
# f = open('경로 및 파일 명', '모드설정')
f = open('./test.txt', 'w') # 파일 생성
f.write('★캐치마인드 주인공 박인성★') # 메모장에 적을 내용
f.close()


# In[95]:


# with open: 자동으로 close()
with open('test1.txt','w') as f:
    f.write('신기하네요.')


# In[84]:


# 읽기 -> read
f = open('./test.txt','r')
data = f.readline()
f.close()
print(data)


# In[94]:


with open('test1.txt','r') as f:
    data = f.readline()
print(data)


# In[97]:


# 1~5페이지 url 접근
# txt파일로 저장

# 텍스트 파일 쓰기 모드로 열기
f = open('./reple.txt', 'w')

for i in range(1,6,1):
    url='https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=74977&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'
    res = req.get(url, headers = header, params = {'page':i})
    
    # 파이썬 객체 변환
    html = bs(res.text, 'lxml')
    
    # 리뷰 문장 접근 [요소, 요소, 요소]
    reple = html.select('p > span:last-child')
    
    for j in range(0, len(reple), 1):
        #f.write 메모장에 계속해서 적기!
        # 파일 생성
        f.write(reple[j].text.strip()) # 메모장에 적을 내용
f.close()


# In[99]:


# reple 파일 읽어보기
f = open('./reple.txt','r')
data = f.readline()
f.close()
print(data)


# ### 워드클라우드 그리기
# - 준비해야할 사항 2가지 : matplotlib, wordcloud

# In[100]:


get_ipython().system('pip install wordcloud')


# In[102]:


# 임폴트
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[103]:


# 텍스트데이터(data) -> 단어로 분류 -> 워드클라우드 그리기
# WordCloud(스타일옵션) : 워드 클라우드의 스타일을 지정
# generate(텍스트데이터) : 단어로 분류 후 워드 클라우드 생성

# wc = WordCloud(폰트설정,
#               배경색,
#               글씨색상)

wc = WordCloud(font_path = "C:/Windows/Fonts/malgunbd.ttf",
               background_color = 'white',
               colormap = 'Dark2').generate(data)
# 빈도수가 높은 단어를 제일 크게 표현


# In[109]:


# 그리기
# plt.figure(figsize = (x,y))
plt.figure(figsize = (12,5))
plt.axis('off')
plt.imshow(wc)
# plt.savefig('경로및파일')
plt.savefig('./아바타리뷰.png')


# In[ ]:




