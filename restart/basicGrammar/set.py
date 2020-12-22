# 집합

# 중복되지 않고 순서가 없다

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", '양세형'}

# list를 set으로 변환
python = set(["유재석", "박명수"])

# 교집합 
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 값 추가
python.add("김태호")

# 값 제거
python.remove("김태호")