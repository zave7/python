# def profile(name, age, lang1, lang2, lang3):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end 키워드를 사용하면 print 사용 시 한줄을 띄우지 않고 출력함
#     print(lang1, lang2, lang3)


# 가변인자 !!!
def profile(name, age, *langs):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end 키워드를 사용하면 print 사용 시 한줄을 띄우지 않고 출력함
    for lang in langs:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "c", "c++", "c#")
profile("김태호", 23, "python", "java")