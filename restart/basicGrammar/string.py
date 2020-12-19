
# 문자열 선언
# sentence = '나는 소년입니다' # '
# print(sentence)
# sentence2 = "파이썬은 쉬워요" # "
# print(sentence2)
# sentence3 = """ 팡썬은
# 쉽나요???
# """ # """
# print( sentence3)

# 문자열 슬라이싱
jumin = "970425-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])

print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤 부터) : " + jumin[-7:])