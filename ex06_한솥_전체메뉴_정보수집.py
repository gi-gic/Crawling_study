#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 도구 불러오기
import pandas as pd
import time # 실행에 대한 딜레이를 줄이기 위한 라이브러리
from selenium import webdriver as wb
from selenium.webdriver.common.by import By


# In[2]:


# url정의
url = 'https://www.hsd.co.kr/menu/menu_list'
driver = wb.Chrome()
driver.get(url)


# 1. '더보기' html요소 접근하기
# 2. '더보기' 요소 클릭하기(while)
# 3. 클릭을 완료했을 때, 모든 메뉴 정보가 브라우저에 출력되어야 한다.
# 4. 메뉴명, 가격 정보를 수집한다
# 5. 메뉴명, 가격 정보의 텍스트 내용만 가져온 후 리스트에 저장한다
# 6. 각 리스트를 이용하여 딕셔너리로 정리 -> DataFrame으로 생성한다

# ### '더보기' html 요소 접근하기

# In[3]:


# driver.find_element(By.CSS_SELECTOR, value = ('.btn_more a'))
driver.find_element(By.CSS_SELECTOR, value = '.c_05')


# ### '더보기' 요소 클릭하기(while)

# ### 클릭을 완료했을 때, 모든 메뉴 정보가 브라우저에 출력되어야 한다.

# In[4]:


# 2~3 : 예외처리(try~except문법)


# In[6]:


try:
    while True:
        driver.find_element(By.CSS_SELECTOR, value = '.c_05').click()
        # 클릭한 후 1초 뒤에 동작
        # -> 네트워크 속도에 따라서 컨텐츠가 보여지는 로딩 시간이 다름
        # sleep() : 딜레이를 적용할 때 적용
        # 2~5초 사이로 설정
        time.sleep(1)
except:
    print('더 보기 클릭 완료')


# ### 메뉴명, 가격 정보를 수집한다

# In[23]:


driver.find_elements(By.CSS_SELECTOR, value = '.item-text>h4')


# In[9]:


driver.find_elements(By.CSS_SELECTOR, value = '.item-price>strong')


# ### 메뉴명, 가격 정보의 텍스트 내용만 가져온 후 리스트에 저장한다

# In[24]:


menu_lst = driver.find_elements(By.CSS_SELECTOR, value = '.item-text>h4')
price_lst = driver.find_elements(By.CSS_SELECTOR, value = '.item-price>strong')
# text로 변환
# 요소.text
# [요소1, 요소2, ..., 요소91].text -> 불가

for i in range(0, len(menu_lst), 1):
    print(menu_lst[i].text, price_lst[i].text)


# In[25]:


menu_txt_lst = []
price_txt_lst = []
for i in range(0, len(menu_lst), 1):
    menu_txt_lst.append(menu_lst[i].text)
    price_txt_lst.append(price_lst[i].text)


# ### 각 리스트를 이용하여 딕셔너리로 정리 -> DataFrame으로 생성한다

# In[29]:


hsd_dic = {'메뉴명':menu_txt_lst, '가격':price_txt_lst}


# In[30]:


hsd_df = pd.DataFrame(hsd_dic)
hsd_df


# In[65]:


# 한솥 전체 메뉴 중에서 5000원 이하인 메뉴는 몇 개 있을까?
# 그 메뉴의 이름은 뭘까?
# 1. 콤마를 제거 -> 가격 컬럼 데이터 타입 변환
# 컬럼인덱싱 하는 방법 df['컬럼명'], df.loc[:,'컬럼영'], df.iloc[:1]
hsd_df['가격'] = hsd_df['가격'].str.replace(',', '').astype('int64')


# In[74]:


hsd_df[hsd_df['가격']<=5000].shape[0]


# In[71]:


len(hsd_df[hsd_df['가격']<=5000])


# In[76]:


hsd_df[hsd_df['가격']<=5000]['메뉴명']


# In[ ]:




