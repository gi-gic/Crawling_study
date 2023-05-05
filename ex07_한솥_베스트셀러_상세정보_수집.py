#!/usr/bin/env python
# coding: utf-8

# ### 한솥의 베스트 셀러 수집하기
#  - 한솥 베스트 셀러 페이지 정보 요청
#  - 한번씩 상세 페이지를 들어갔다가 나오면서(이전페이지) 메뉴명, 가격, 상세정보를 수집하기
# 

# In[89]:


import pandas as pd
import time # 실행에 대한 딜레이를 주기 위한 라이브러리
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# ### 1번째 메뉴 상세페이지 들어가서 수집 후 이전 페이지로 이동

# In[101]:


# 한솥 베스트 셀러 페이지 요청
url = 'https://www.hsd.co.kr/menu/menu_keyword?keyword=1'
# 페이지 요청
driver = wb.Chrome()
driver.get(url)


# In[93]:


# 메뉴 아이템 중에서 1번째 데이터 클릭 --> (상세페이지 들어가기)
# item-cont
# item = driver.find_element(By.CSS_SELECTOR, value = '.item-cont')
# 태그:nth-child(1)
item = driver.find_element(By.CSS_SELECTOR, value = '.menu_cont>.item:nth-child(11)')
item.get_attribute('href') #태그 안에 있는 속성값 확인
item.click() #상세페이지 들어감
# 메뉴 정보들 추출 -> 출력
cat = driver.find_element(By.CSS_SELECTOR, value = '.txt_wrap .dp1').text
name = driver.find_element(By.CSS_SELECTOR, value = '.txt_wrap .dp2').text
cont = driver.find_element(By.CSS_SELECTOR, value = '.txt_wrap .account').text
price = driver.find_element(By.CSS_SELECTOR, value = '#total_price').text
print(cat, name, cont, price)
# time.sleep(1.5)
# driver.back()


# ### 베스트 셀러 모든 메뉴 상세 페이지 들어가서 수집하기
#  - 반복을 몇번해야될지 찾아내기
#  - 첫번째 메뉴 상세페이지 들어갔다가 나와서 두번째 메뉴 클릭
#  - 위의 과정을 마지막 메뉴까지 진행하기

# In[91]:


data_len = len(driver.find_elements(By.CSS_SELECTOR, value = '.menu_cont>.item'))
data_len


# In[100]:


data_lst = [] 
for i in range(1,len(data_range)+1):
    # 1개 메뉴 클릭 -> 상세페이지 넘어감
    driver.find_element(By.CSS_SELECTOR, value = f'.menu_cont > li:nth-child({i})').click()
    # 카테고리명, 메뉴명, 상세정보, 가격-> lst 1개 저장
    cat = driver.find_element(By.CSS_SELECTOR, value = '.he_tit>span:first-child')
    name = driver.find_element(By.CSS_SELECTOR, value = '.he_tit>span:last-child')
    price = driver.find_element(By.CSS_SELECTOR, value = 'p.account')
    cont = driver.find_element(By.CSS_SELECTOR, value = '.fz_01')
    data_lst.append([cat.text, name.text, price.text, cont.text])
    time.sleep(1.5)
    # 추천 메뉴 페이지로 나가기
    driver.back()
driver.close()


# In[96]:


cat_lst = []
name_lst = []
cont_lst = []
price_lst = []
for i in range(1, data_len+1):
    # +1을 붙인 이유 -> 시작할 숫자1 종료할 숫자 11 --> 증감량 1이므로 1부터 10까지 1씩 증가이기 때문에 마지막 항목이 포함되지 않음
    item = driver.find_element(By.CSS_SELECTOR, value = f'.menu_cont>.item:nth-child({i})') # f문자열 포매팅
    item.click()
    cat_lst.append(driver.find_element(By.CSS_SELECTOR, value = '.txt_wrap .dp1').text)
    name_lst.append(driver.find_element(By.CSS_SELECTOR, value = '.txt_wrap .dp2').text)
    cont_lst.append(driver.find_element(By.CSS_SELECTOR, value = '.txt_wrap .account').text)
    price_lst.append(driver.find_element(By.CSS_SELECTOR, value = '#total_price').text)
    time.sleep(1.5)
    driver.back()
driver.close()


# In[97]:


# 데이터 프레임 생성
hsd_best_df = pd.dataFrame(data_lst, colums = ['구분', '메뉴명','메뉴정보','가격'])
hsd_best_df


# In[98]:


data = {'분류':cat_lst,'메뉴이름':name_lst, '메뉴설명':cont_lst, '가격':price_lst}
pd.set_option('display.max_colwidth', None) # 컬럼너비설정


# In[99]:


pd.DataFrame(data)


# In[ ]:




