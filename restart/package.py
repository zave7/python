# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# import travel.thailand.ThailandPackage 모듈인 아닌 것은 임포트가 불가능하다
# from travel.thailand import ThailandPackage # from ~ import ~ 구문에서는 가능하다
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import * # travel패키지 안에 있는 모든것을 가져오겠다는 것
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()