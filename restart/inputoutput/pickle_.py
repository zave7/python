# pickle : 프로그램 상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장

import pickle
# profile_file = open("profile.pickle", "wb") # b는 바이너리 타입을 뜻함 ( pickle에서는 무조건 바이너리로 지정해줘야한다 )
# profile = {"이름" : "박명수", "나이":30, "취미" : ["축구","야구"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()