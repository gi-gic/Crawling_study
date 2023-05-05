#!/usr/bin/env python
# coding: utf-8

# ### requests
# - 웹 문서를 요청/응답할 때 사용하는 라이브러리(모듈)
# - url 주소를 입력하여, 해당 페이지 html 정보를 요청/응답

# In[1]:


import requests as req #res라고 하는 곳도 있음


# In[2]:


url = 'https://www.naver.com/'
# url에 저장되어 있는 웹 문서 요청하기 : get()
# Response[200] : 성공적으로 요청/응답 진행된 상태
res = req.get(url)
res


# In[3]:


# 응답받은 데이터(res)에 웹 문서 접근하기
res.text


# ### BeautifulSoup
# - 웹문서 안에 있는 데이터를 추출할 수 있도록 함수를 제공해주는 모듈
# - 1. req 통해 html정보 (텍스트) --> 파이썬객체로 변환
# - 2. bs 제공하는 함수를 통해 원하는 태그 정보에 접근하여 데이터 추출

# In[4]:


from bs4 import BeautifulSoup as bs


# In[5]:


# req통해 html정보(텍스트) --> 파이썬 객체로 변환(태그 접근)
html = bs(res.text, 'lxml') # 파싱 parsing
html


# In[7]:


# css 선택자를 활용하여 접근할 수 있게 하는 함수
# html.select_one(css선택자) : css 선택자에 맞는 가장 먼저 찾아지는 첫번째 html 객체에 접근
# 태그 선택자 : 태그명
# 아이디 선택자 : #아이디명
# 클래스 선택자 : .클래스명
# 계층 선택자 : 자식(>), 자손(공백), 형제(~), 인접형제(+)
html.select_one('title').text


# In[11]:


# html.select(css선택자) : css선택자에 맞는 html 객체 모두 접근
# 결과가 리스트 형식으로 변환
html.select('title')[0].text


# ### 네이버 통합검색 페이지에서 데이터 수집하기
# - 검색키워드 : 겨울축제

# In[21]:


# 1. url2
url2 = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%A8%EC%9A%B8%EC%B6%95%EC%A0%9C&oquery=%EA%B2%A8%EC%9A%B8.%EC%B6%95%EC%A0%9C&tqi=hHCBisp0J14ssuP9MAGsssssta0-520841'
# 2. get() html 요청
res2 = req.get(url2)
# 3. bs 파이썬 객체 변환 => html 태그값 적근
html2 = bs(res2.text, 'lxml')
# 4. 겨울축제 이름들 추출
html2.select_one('.this_text > a').text


# In[38]:


# 4개 다 가져와서 제목 문자열만 출력해보기
for i in range(0, 4, 1):
    print(html2.select('.this_text > a')[i].text)
#4 대신 len(html2.select('.this_text > a'))


# In[37]:


html2_lst = html2.select('.this_text > a')
# 4개 다 가져와서 제목 문자열만 출력해보기
for data in html2_lst:
    print(data.text)


# In[42]:


# href 속성값 접근
link = html2_lst[0].get('href')
link2 = 'https://search.naver.com/search.naver' + link
print(link2)


# ### 네이버 뉴스 기사 크롤링하기
#  - 뉴스 제목, 내용 수집한 후 출력해보기
#  - 1. 어떤 태그에 있는지
#  - 2. 어떤 클래스 등등 속성으로 이루어져 있는지

# In[45]:


news_url = 'https://n.news.naver.com/article/660/0000023947?cds=news_media_pc&type=editn'
news_res = req.get(news_url)
news_res
# 에러 > 컴퓨터에게 브라우저에서 요청했다는 인식을 설정할 필요가 있음


# In[47]:


# 브라우저 요청 인식 설정
# 모든 페이지를 요청할 때 header값 지정할 것
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
# htmld의 data-useragent


# In[48]:


news_url = 'https://n.news.naver.com/article/660/0000023947?cds=news_media_pc&type=editn'
news_res = req.get(news_url, headers = header)
news_res


# In[50]:


# 파이썬 객체로 변환
news_html = bs(news_res.text, 'lxml')
news_html


# In[80]:


# 제목
title = news_html.select_one('#title_area > span')
print(title.text)

print()

# 내용
content = news_html.select_one('#dic_area')
# strip() 문장 양 옆의 공백 제거
print(content.text.strip())


# In[ ]:





# In[ ]:




