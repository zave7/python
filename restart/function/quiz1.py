# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)

# 남자 : 키(m) x 키(m) x x 22
# 여자 : 키(m) x 키(m) x x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키 (height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# 출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

gender = input("성별을 입력해주세요 : ")
height = 175

def std_weight(height, gender):
    print(height)
    result = 0
    if(gender=="남자"):
        result = weight_cal(height, 22, 2)
    else:
        result = weight_cal(height, 21, 2)
    print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, result))

def weight_cal(height, val, round1): # 파이썬에서 함수 파라미터에 키워드 사용 불가능!!!
    print(( height * height ) * val)
    return round(( height * height ) * val, round1)

std_weight(height / 100, gender)