# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 크롬드라이버 실행
driver = webdriver.Chrome() 

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://page.kakao.com/menu/10011/screen/84?is_complete=false')
time.sleep(0.3)
toScroll = driver.find_element_by_xpath('/html/body')

work = 10000
link = []

# 웹소설의 page의 URL을 가져오는 부분
for i in range(1, work+1):
    if(i % 10 == 1):
        toScroll.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
        
    pt = '//*[@id="__next"]/div/div[2]/div/div[2]/div[1]/div/div[4]/div/div/div/div[{}]/div/a'.format(i)
    ss = driver.find_element_by_xpath(pt)
    link.append(ss.get_attribute("href"))
    
    print("link: %d" %(i))
    
file = open("urls2.txt","w", encoding='utf-8')
file.write('\n'.join(link))
file.close()

# URL을 가지고 웹소설의 정보 가져오기
file = open("urls.txt","r", encoding='utf-8')
data = file.readlines()
file.close()

txt = ""
      
for i in range(0,10000):
    # 작품 선택 + 정보 탭 선택
    path = data[i] + '?tab_type=about'
    driver.get(path)
    time.sleep(0.03)
            
    try:
        # 작품의 조회수
        view = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/a/div/div[1]/div[2]/span').text
        txt+=view
        txt+="\n"

        # 작품의 키워드
        keyword = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]')
        txt+=keyword.text
    
    except:
        continue
    
    finally:
        txt+="\n--------\n"
        print("content: %d" %(i+1))
        

file = open("data.txt","w", encoding='utf-8')
file.write(txt)
file.close()

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(3)