print("a" + "b")
print("a", "b")
print("나는 %d 살 입니다" % 10) # %d 는 정수
print("나는 %s를 좋아해요" % "Python") # %s 문자열
print("Apple은 %c로 시작해요" % "A") # %c는 문자

print("나는 %s를 좋아해요" % 1234) # %s 는 모든 값을 출력가능하다

# print ("나는 %s색과 %s색을 좋아해요" % ("파란, 노랑"))

# 방법 2
print("나는 {}색을 좋아해요".format("안늉"))
print("나는 {}색을 {}좋아해요".format("안늉", "참")) # 순서대로
print("나는 {1}색을 {0}좋아해요".format("안늉", "참")) # 인덱스 설정 가능

# 방법 3
print("나는 {color}색을 {oo}좋아해요".format(color = "안늉", oo = "참"))

# 방법 4
color = "파란"
oo = "ㅋㅋ"
print(f"나는 {color}색을 {oo}좋아해요")