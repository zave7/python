# 사전

# key-value

# 키는 중복되지 않음

cabinet = {3:"유재석", 4:"123"}

# get 값이 없으면 None
print(cabinet.get(3)) 

# 값이 없으면 keyError 발생
print(cabinet[3]) 

# 기본값 지정
print(cabinet.get(5, "사용 가능"))

# 값이 있는지 확인
print(3 in cabinet)

# 같은 키 업데이트
cabinet[3] = "유재석2"
print(cabinet)

# 제거
del cabinet[3]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# 전체 제거
cabinet.clear()
print(cabinet)