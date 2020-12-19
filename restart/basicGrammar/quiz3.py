# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성

# 예) http://naver.com 
# 규칙 1 : http:// 부분은 제외 => naver.com 
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# 예) 생성된 비밀번호 : nav51!

string = "http://naver.com"
string = string.replace("http://", "")
string = string[:string.index(".")]
length = str(len(string))
countE = str(string.count("e"))
result = string[:3] + length + countE + "!"
print("생성된 비밀번호 : " + result)