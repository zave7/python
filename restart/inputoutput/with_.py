# import pickle
# # 열었던 파일에대해 close를 따로 해줄 필요가 없다
# with open("profile.pickle", "rb") as profile_file: # profile_file이라는 변수에 저장
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
#     print(study_file)

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
print(study_file.read()) # with 구문을 빠져나오는 순간 이미 close 되었기 때문에 에러 발생