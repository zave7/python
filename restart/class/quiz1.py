# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print("위치:{0}\t타입:{1}\t매매유형:{2}\t가격:{3}\t준공년도:{4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
        print("위치:{location}\t타입:{house_type}\t매매유형:{deal_type}\t가격:{price}\t준공년도:{completion_year}".format(location=self.location, house_type=self.house_type, deal_type=self.deal_type, price=self.price, completion_year=self.completion_year))

h1 = House("강남", "아파트", "매매", "10억", 2010)
h2 = House("마포", "오피스텔", "전세", "5억", 2007)
h3 = House("송파", "빌라", "월세", "500/50", 2000)

houseList = [h1,h2,h3]
houseList.append(h1)
houseList.append(h2)
houseList.append(h3)

for house in houseList:
    house.show_detail()