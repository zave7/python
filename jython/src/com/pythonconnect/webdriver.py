from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/chromedriver/chromedriver')
# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)
# url에 접근한다.
#driver.get('https://nid.naver.com/nidlogin.login')
# 아이디/비밀번호를 입력해준다.
#driver.find_element_by_name('id').send_keys('zave7')
#driver.find_element_by_name('pw').send_keys('rdc2952!!!')
# 로그인 버튼을 눌러주자.
#driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.get('https://news.naver.com/')
driver.find_element_by_name('query').send_keys('셀레니움')
driver.find_element_by_css_selector('button.btn_search_lnb').click()
html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
notices = soup.select('div.mynews>ul>li>dl>dt>a')
for n in notices:
    print(n.text.strip())