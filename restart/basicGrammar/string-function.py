python = "Python is Amazing"

print( python.lower()) # lower 처리
print( python.upper()) # upper 처리
print( python[1].isupper()) # upper인지 비교
print( len(python)) # 길이 구하기
print( python.replace("Python", "123")) # replace

index = python.index("n") # 특정 문자 위치 반환
print(index)
index = python.index("n", index + 1)
print(index)

print( python.find("is")) # 특정 문자열 시작 위치 반환
print( python.find("java")) # 없으면 -1 반환

print( python.index("Python")) # 특정 문자열 시작 위치 반환
# print( python.index("java")) # 없으면 substring not found 에러

print( python.count("n"))