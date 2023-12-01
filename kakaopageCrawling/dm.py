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

txt = ""
      
# def func(txt):
work = 10000
link = []
for i in range(1, work+1):
    # print(i)
    if(i % 10 == 1):
        toScroll.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
    
        
    pt = '//*[@id="__next"]/div/div[2]/div/div[2]/div[1]/div/div[4]/div/div/div/div[{}]/div/a'.format(i)
    ss = driver.find_element_by_xpath(pt)
    link.append(ss.get_attribute("href"))
    print("link: %d" %(i))
    # print("count %d : %s" %(i, ss.get_attribute("href")))
    # t = "count {}\n{}\n".format(i,ss.text)
    # txt+=t
    

file = open("urls.txt","w", encoding='utf-8')
file.write('\n'.join(link))
file.close()

for i in range(0,work):
    # print(link[i])
    # 작품 선택 + 정보 탭 선택
    path = link[i] + '?tab_type=about'
    driver.get(path)
    time.sleep(0.3)
            
    try:
        subject = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/a/div').text
        # print("제목 : " + subject)
        txt+="제목 : {} ".format(i+1) + subject
        txt+="\n\n"
    # # 작품의 정보 탭 선택
    # inf = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/a/div')
    # inf.click()
    # time.sleep(0.3)

        # 작품의 줄거리 텍스트
        summary = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]')
        # print(summary.text)
        txt+=summary.text
        txt+="\n\n"

        # 작품의 키워드
        keyword = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]')
        # print(keyword.text)
        txt+=keyword.text
        # print()
    
    except:
        continue
    
    finally:
        txt+="\n\n\n"
        txt+="-------------------------------------------------------------------\n"
        print("content: %d" %(i+1))
        


# func(txt)
# print(txt)
file = open("data.txt","w", encoding='utf-8')
file.write(txt)
file.close()

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(3)