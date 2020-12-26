gun = 10

def checkpoint(soldiers):
    global gun  # 전역 변수 사용 선언
    # gun = 20 # 지역 변수 선언
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0} ".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun) )