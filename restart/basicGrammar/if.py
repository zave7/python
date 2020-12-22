# weather = input("오늘 날씨는 어때요? ")

# if weather == "비" or weather == '눈':
#     print("우산을 챙겨!!")
# elif weather == "미세먼지":
#     print("마스크를 챙겨!!")
# else:
#     print("날씨는 맑아")

temp = int(input("현재 기온은? "))
if 30 <= temp:
    print('덥네여')
elif 10 <= temp < 30:
    print("적당해여")
else:
    print("쌀쌀 하네여")