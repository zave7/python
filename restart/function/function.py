
# 함수 정의
def open_account():
    print("새로운 계좌가 개설되었습니다.")

open_account()

# 전달값과 반환값

def deposit(balance, money):
    print("입급이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)