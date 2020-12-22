# 리스트 [] : 순서를 가지는 객체의 집합이다

# 지하철 칸별로 10명, 20명, 30명

# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]


# print(subway)
# print(123)

# print("12341234")

subway = ["유재석", "조세호", "박명수"]

print(subway.index("조세호"))

subway.insert(1, "정형돈")

# 끝에 있는 객체를 꺼냄
print(subway.pop()) 

# 끝에 추가
print(subway.append("유재석"))

# 같은 이름의 사람이 몇 명 있는지 확인
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 1, True]
print(mi_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)
