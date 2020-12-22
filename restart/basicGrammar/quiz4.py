# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추천 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가넝
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용


from random import *

id_list = list(range(1, 21))
print(id_list)
shuffle(id_list)
print(id_list)
result = sample(4, id_list)
print(id_list)
print("치킨 당첨자 아이디 : {0}".format(result[0]))
print("커피 쿠폰 당첨자 아이디 : {0}".format(result[1:]))