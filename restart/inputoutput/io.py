# score_file = open("score.txt", "w", encoding="utf8") # 파일이름, 동작, 인코딩 / w인 경우 덮어쓰기
# print("수학 : 0", file=score_file) # 자동 줄바꿈이 됨
# print("영어 : 50", file=score_file)
# score_file.close() # 파일을 사용하면 항상 닫아줘야한다

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()