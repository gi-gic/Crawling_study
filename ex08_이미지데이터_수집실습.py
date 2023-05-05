#!/usr/bin/env python
# coding: utf-8

# ### 네이버 이미지 검색을 통한 이미지 수집
#  1. 이미지 저장할 폴더 정리(os라이브러리)
#  2. 이미지 url활용 수집 후 이미지 파일로 저장해보기(urllib 라이브러리 urlretrieve)
#  3. 한 페이지 내의 고양이(동물) 이미지 수집하기
#  4. 스크롤 다운하여 더 많은 이미지 파일 출력해서 저장하기

# In[1]:


from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 파일 시스템을 다룰 때 사용하는 라이브러리
# 파일 or 폴더를 생성, 삭제, 이동, 파일이나 폴더의 존재여부, 판단 등등..
import os

# 이미지경로를 기반으로 서버에 요청해서 이미지 파일을 저장할 수 있게 하는 라이브러리
from urllib.request import urlretrieve


# In[3]:


url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA0MTlfMTQ5%2FMDAxNjUwMzczMzY2Njk2.Ky7KbVADywB3WN7p7u0bgDv36iNtUW7EyFiLuqD7GIQg.voKR0F7xTO706yd6TFafIPeGV2HuayRkgfcfSpPc1SAg.JPEG.kwo5050%2FIMG_1681.JPG&type=a340'
# urlretrieve(요청할 이미지 경로, 이미지 파일을 저장할 경로)
urlretrieve(url, './농담곰.jpg')


# In[5]:


# 폴더 존재여부 판단하기
# 폴더가 있다면 : True
# 폴더가 없다면 : False
os.path.isdir('./농담곰')


# In[6]:


# 폴더 생성하기
os.mkdir('./농담곰')


# In[7]:


os.path.isdir('./농담곰')


# In[8]:


# 조건
# 해당 폴더가 있으면 폴더 생성 X
# 해당 폴더가 없으면 폴더 생성
if os.path.isdir('./농담곰') == True:
    print('현재 폴더는 있습니다.')
else:
    os.mkdir('./농담곰')


# In[9]:


# 폴더 생성하는 함수 만들기
def create_folder(name): #폴더명
    if os.path.isdir(f'./{name}') == True:
        print('현재 폴더는 있습니다.')
    else:
        os.mkdir(f'./{name}')
        print(f'{name} 폴더가 생성되었습니다.')


# In[10]:


# 함수 호출
create_folder('강아지')


# ### 이미지 url활용 수집 후 이미지 파일로 저장하기

# In[17]:


url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%86%8D%EB%8B%B4%EA%B3%B0+%EC%A7%A4'
# 드라이버 html 요청
driver = wb.Chrome()
driver.get(url)


# In[16]:


# 첫번째 이미지 태그에 접근하기
# first_img = driver.find_element(By.CSS_SELECTOR, value ='.thumb img')
first_img = driver.find_element(By.CSS_SELECTOR, value ='img._image._listImage')
first_url = first_img.get_attribute('src')
# 저장하기
urlretrieve(first_url, './농담곰/농담곰1.jpg')


# ### 스크롤 다운하여 더 많은 이미지 파일 저장하기
# 

# In[38]:


url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%86%8D%EB%8B%B4%EA%B3%B0+%EC%A7%A4'
# 드라이버 html 요청
driver = wb.Chrome()
driver.get(url)

# 로딩시간이 필요함
time.sleep(2)

# 스크롤을 내리기
for i in range(6):
    driver.find_element(By.TAG_NAME, value = 'body').send_keys(Keys.END)
    time.sleep(2)
    
# 이미지 태그 접근
imgs = driver.find_elements(By.CSS_SELECTOR, value ='img._image._listImage')
print(len(imgs))


# In[29]:


src_lst = [] # 올바른 주소 저장하는 리스트
for i in range(len(imgs)):
    src = imgs[i].get_attribute('src')
    if src[:4] != 'data': #올바른 주소
        src_lst.append(src)


# In[ ]:


# 폴더에 이미지 파일 저장하기
for i in range(0,len(src_lst),1):
    urlretrieve(src_lst[i], f'./농담곰/농담곰{i}.jpg')


# #### 강아지

# In[40]:


url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=강아지'
# 드라이버 html 요청
driver = wb.Chrome()
driver.get(url)

# 로딩시간이 필요함
time.sleep(2)

# 스크롤을 내리기
for i in range(6):
    driver.find_element(By.TAG_NAME, value = 'body').send_keys(Keys.END)
    time.sleep(2)
    
# 이미지 태그 접근
dog = driver.find_elements(By.CSS_SELECTOR, value ='img._image._listImage')
print(len(dog))


# In[47]:


dog_lst = [] # 올바른 주소 저장하는 리스트
for i in range(len(dog)):
    src = dog[i].get_attribute('src')
    if src[:4] != 'data': #올바른 주소
        dog_lst.append(src)


# In[42]:


# 폴더에 이미지 파일 저장하기
for i in range(0,len(dog_lst),1):
    urlretrieve(dog_lst[i], f'./강아지/강아지{i+1}.jpg')


# In[ ]:




