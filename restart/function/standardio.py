# # 표준 입출력
# print("Python", "Java", sep=",", end="?") # 문자열을 합칠 때 , 사용 시 sep(seperate) 키워드로 지정해 줄 수 있음
#                                             # end 키워드로 출력의 끝을 지정해 줄 수 있음( 기본은 줄 바꿈 )
# print("무엇이 더 재밌을까요 ? ")

# 표준 입출력

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

# 시험 성적
# scores = {"수학" : 0, "영어" : 50, "코딩" : 14}
# for subject, score in scores.items(): # dictionary 에서 items는 키와 밸류 다 가져온다
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust 총 8개의 공간을 만들고 왼쪽 정렬
                                                    # rjust 오른쪽 정렬


# 대기 순번표
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # zfil 0으로 채운다

answer = input() # input에 문자열을 넣어줘도되고 안넣어줘도 된다
print(type(answer)) # 사용자 입력 함수로 받게 되면 항상 문자열로 받게된다
print("입력하신 값은 " + answer + "입니다")