#!/usr/bin/env python
# coding: utf-8

# ### requests, BeautifulSoup 만 사용했을 때의 한계
#  - "자바스크립트로 동적으로 생성된 정보는 가져올 수 없다는 것"

# ### Selenium
#  : 동적인 페이지를 제어하고 내용을 가져오기 위한 라이브러리
#  : 웹 자동화 테스트 도구
#  : 브라우저 제어 - 키보드 입력, 클릭, 스크롤, 이전 페이지 이동 등등
#  
# #### 셀레니움의 필요성
#  - 1. 자바스크립트가 동적으로 만든 데이터를 크롤링하기
#  - 2. 사이트의 다양한 html요소에 클릭, 키보드 입력 등 이벤트 주기, 데이터도 추출할 수 있음
# 
# #### 사용하기 위한 환경 구축
#  - 1. 셀레니움 라이브러리 설치
#  - 2. webdriver 파일 설치 -> 현재 크롤링 폴더에 저장
#  - 웹 드라이버를 설치할 때, 크롬 버전과 동일해야 함
#  - 버전 확인 방법 : 크롬 브라우저 설정 > 크롬 정보 메뉴 > 버전 확인

# In[1]:


get_ipython().system('pip install selenium')


# #### Selenium 사용하기

# In[6]:


# 도구 임폴트
# chromedriver.exe 를 제어 및 실행시켜주는 라이브러리
from selenium import webdriver as wb

# 키보드의 값(enter, space, ctrl, a키보드 값)을 제어할 수 있는 라이브러리
from selenium.webdriver.common.keys import Keys

# html요소를 접근하는 방식을 제공하는 라이브러리
# css선택자 : 태그이름접근, 클래스접근, 아이디 접근
from selenium.webdriver.common.by import By


# #### 페이지 요청

# In[12]:


# wb.Chrome(chromedriver.exe 경로 설정)
# driver = wb.Chrome('./chromedriver.exe') 같은 경로에 있으면 생략 가능
url = "https://www.naver.com/"
# 크롬 브라우저 연결 설정
# 제어할 수 있는 브라우저 실행, 브라우저를 제어하고 접근하기 위해서 driver라는 변수에 저장해서 사용한다

driver = wb.Chrome()

# url주소에 해당하는 웹 페이지를 요청하는 함수
driver.get(url)


# #### 특정 html요소 접근(1개)
#  - find_element(어떤 선택자 종류, value='밸류값')

# In[9]:


# driver.find_element(): 웹 문서에서 특정 html요소 1개에 접근하는 함수
# 검색창(input) 요소 접근하기
driver.find_element(by='id', value = 'query')


# In[10]:


# 검색방법 1
# by, value 활용한 html요소 접근
# 검색창에 키보드 입력값 보내기
# enter 기능
driver.find_element(by='id', value = 'query').send_keys('치즈돈까스\n')


# In[11]:


# 검색방법 2
# BY.ID를 활용한 html 요소 접근
driver.find_element(By.ID, value = 'query').send_keys('치즈돈까스\n')


# In[13]:


# 검색방법 3
# BY.CSS_SELECTOR --> id값에 접근
driver.find_element(By.CSS_SELECTOR, value = "#query") .send_keys('치즈돈까스\n')


# In[20]:


# 검색방법 3
# BY.CSS_SELECTOR --> id값에 접근
driver.find_element(By.CSS_SELECTOR, value = "#query").send_keys('치즈돈까스')
# 검색버튼 요소 접근하기
driver.find_element(By.CSS_SELECTOR, value = "#search_btn").click()


# #### 해당 태그의 여러 요소를 접근하는 함수(여러개)
#  - find_elements()

# In[24]:


# 치즈돈까스 상품명에 접근해보기
products = driver.find_elements(By.CSS_SELECTOR, value = 'a.title')
products[0].text 
# webelement.text : html 객체 내의 텍스트 내용을 접근 -> str


# In[28]:


for i in products:
    print(i.text)


# In[30]:


# 페이지 스크롤 내리기! --> Keys 활용
# 스크롤 내리는 방법 : 
# ARROW_UP(조금씩 내리기)
# PAGE_DOWN(보여지는 페이지에서 다음 페이지로 다운)
# END(제일 하단까지 스크롤 내리기)
# 스크롤 적용할 대상 : body
# 스크롤 적용하는 방법: send_keys(Keys.스크롤내리는방법)
driver.find_element(By.TAG_NAME, value = 'body').send_keys(Keys.END)


# In[101]:


driver.find_element(By.TAG_NAME, value = 'body').send_keys(Keys.ARROW_UP)


# In[102]:


# 크롬 브라우저 창 끄기
driver.close()


# In[ ]:





# In[ ]:





# In[ ]:




