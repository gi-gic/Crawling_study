#!/usr/bin/env python
# coding: utf-8

# ### 네이버 영화 평점 데이터
# - 영화명, 평점
# - 네이버 영화 > 영화랭킹 > 평점순(현재상영영화)

# In[3]:


# 환경세팅
import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}


# In[10]:


url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20221214'
# html 요청
res = req.get(url, headers = header)
# 파이썬 객체 변환
html = bs(res.text, 'lxml')


# In[5]:


# 영화명, 평점 데이터 수집 후 출력해보기
movie_name = html.select('.tit5 > a')
movie_point = html.select('.point')


# In[42]:


# 영화명 넣기
movie_name_lst = []
movie_point_lst = []
rank_lst = []
for i in range(0,len(movie_name),1):
    movie_name_lst.append(movie_name[i].text)
    movie_point_lst.append(movie_point[i].text)
    rank_lst.append(i+1)


# 다른 방법
# 
# List comprehension 문법 -> 리스트 내포
# List의 각 요소를 반복하기 위해 for 루프와 함께 실행되는 표현식
# [i for i in 반복대상]
# 1. 루프보다 시간 효율적, 공간 효율적
# 2. 더 적은 수의 코드로 짤 수 있음(가독성)
# 
# movie_name_lst2 = [i.text for i in movie_name]
# 
# movie_point_lst2 = [i.text for i in movie_point] 

# In[7]:


len(movie_name_lst)


# In[8]:


movie_dict = {'순위':rank_lst,'영화명':movie_name_lst, '평점':movie_point_lst}
movie_df = pd.DataFrame(movie_dict)
movie_df.set_index('순위')


# ### 페이지를 이동하면서 날짜별 영화명, 평점 데이터 수집하기
# - 20221210 - 20221214 (5일) 페이지 접근
# - 각 페이지마다 영화명, 평점데이터 수집
# - 각 페이지에 접근하기 위해서 url을 활용 : 날짜 값을 변경

# In[17]:


# day_list = ['20221210','20221211','20221212','20221213','20221214']
day_lst = pd.date_range(start = '2022-12-10', periods = 5)
day_lst[0].strftime('%Y%m%d') # 문자열 포매팅 %, format(), f-문자열 


# In[19]:


day_lst2 = [i.strftime('%Y%m%d') for i in day_lst]


# In[91]:


# 20221210~ 20221214 (5일) 페이지 접근하는 코드
movie_date_lst2 = []
movie_rank_lst2 = []
movie_name_lst2 = []
movie_point_lst2 = []

for day in day_lst2:
#     url = f'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date={day}'
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur'
    res = req.get(url, headers = header, params = {'date':day})
#     param요소는 object요소에 의해 불러와지는 플러그인을 위한 매개변수를 정의
#     key:values로 이루어져 있음!

    html = bs(res.text, 'lxml')
    
    # 영화명, 평점 데이터 수집
    movie_name = html.select('.tit5 > a')
    movie_point = html.select('.point')
    
    
    for i in range (0, len(movie_name),1):
        movie_date_lst2.append(day) # 날짜 수집 -> 같은 값을 50번씩
        movie_rank_lst2.append(i+1) # 1 ~ 50 순위 수집 -> 같은 값을 5번씩
        movie_name_lst2.append(movie_name[i].text) # 각 날짜별 영화 순위
        movie_point_lst2.append(movie_point[i].text) # ㄴ> 그 영화의 평점


# In[92]:


movie_df2 = pd.DataFrame({'날짜' : movie_date_lst2, '랭킹':movie_rank_lst2
                          ,'영화명':movie_name_lst2, '평점':movie_point_lst2})


# In[93]:


movie_df2


# In[101]:


# 날짜 2022년 12월 12일 날짜에 대한 영화 정보 출력해보기
movie_df2[movie_df2['날짜'] == '20221212'][['영화명']]
movie_df2.loc[movie_df2['날짜'] == '20221212',['영화명']]

