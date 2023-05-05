#!/usr/bin/env python
# coding: utf-8

# ### 멜론차트 Top100 음원데이터 수집
#  - 가수명, 곡명 데이터 수집
#  - 가수명, 곡명 딕셔너리로 정리
#  - pandas를 이용해서 DataFrame으로 생성
#  - DataFrame 엑셀 파일로 저장
# 

# In[1]:


# 환경세팅
import requests as req # HTML 요청 / 응답
from bs4 import BeautifulSoup as bs # HTML 요청하고 파이썬 객체로 변환
import pandas as pd

# header
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}


# In[2]:


# 멜론 > 멜론 차트 > top100
# url 가져오기
url = 'https://www.melon.com/chart/index.htm'

res = req.get(url, headers = header) # 웹파싱
res


# In[3]:


html = bs(res.text, 'lxml')
html


# In[4]:


# 선택자 접근


# In[5]:


# 페이지 내의 html 태그 및 속성 규칙 확인
# 곡명, 가수 명 데이터 수집
# 100개 개수가 잘 맞게 가져와졌는지 길이 확인
song_txt = []
for i in range(0,len(html.select('.rank01 a')),1):
    song_txt.append(html.select('.rank01 a')[i].text)


# In[6]:


singer_txt = []
rank_lst = []
for i in range(0,len(html.select('.rank02 > .checkEllipsis')),1):
    rank_lst.append(i+1)
    singer_txt.append(html.select('.rank02 > .checkEllipsis')[i].text)


# In[7]:


song = html.select('.ellipsis.rank01 a')
singer = html.select('.checkEllipsis')
print(len(song), len(singer))


# In[8]:


for i in range(len(song)):
    rank_lst.append(i+1)
    song_txt.append(song[i].text)
    singer_txt.append(singer[i].text)


# ### 데이터 프레임 생성

# In[19]:


# 1. 딕셔너리 정리
melon_dict = {'순위': rank_lst, '곡명': song_txt, '가수명': singer_txt}
# 2. pd.DataFrame()
melon_df = pd.DataFrame(melon_dict)
melon_df2 = melon_df.set_index('순위')
# 순위 곡명 가수명


# In[53]:


melon_df2.index # 확인용_ 데이터 타입 int 
# 인덱싱(접근) 숙제
# 순위가 30 ~ 60인 가수 명 출력해보기
melon_df2.iloc[29:60,[1]]


# In[1]:


# 엑셀 저장
# csv로 저장 > df.to_csv('경로및파일명.csv',index =False)
melon_df.to_excel('멜론차트top100.xlsx', index = False)


# In[ ]:




