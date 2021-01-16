# 외장 함수 ( import 가 필요)

# list of python modules 검색하면 공식 문서 나옴!!

# glob : 경로 내의 폴더 / 파일 목록 조회

# import glob
# print(glob.glob("*.py")) # 확장자가 Py인 모든 파일

# # os : 운영체제에서 제공하는 기본 기능
# import os 
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample.dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir()) # 폴더 리스트 출력

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
import datetime
print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100) # 100 일 저장
print("우리가 만난지 100일은", today + td)