import random
from urllib.request import urlopen
import sys

단어_URL = "https://learncodethehardway.org/words.txt"
단어들 = [] 

문장들 = {
    "class %%%(%%%):" :
      "%%% (이)라는 이름의 클래스를 만드는데 %%%의 일종이다. (is-a)",
    "class %%%(object):\n\t def __init__(self, ***)" :
      "클래스 %%% 은/는 self와 *** 매개변수를 받는 __init__을 가졌다. (has-a)",
    "class %%%(object):\n\t def ***(self, @@@)" :
      "클래스 %%% 은/는 self와 @@@ 매개변수를 받는 이름이 *** 인 함수를 가졌다. (has-a)",
    "*** = %%%()" :
      "*** 변수를 %%% 클래스의 인스턴스 하나로 정한다.",
    "***.***(@@@)" :
      "*** 변수에서 *** 함수를 받아와 self, @@@ 매개변수를 넣어 호출한다.",
    "***.*** = '***'" :
      "*** 변수에서 *** 속성을 받아와 *** (으)로 값을 정한다.",
}


# 문장을 먼저 연습하고 싶은가
if len(sys.argv) == 2 and sys.argv[1] == "한국어":
    문장을_앞으로 = True
else:
    문장을_앞으로 = False


# 웹사이트에서 단어를 불러온다
for 단어 in urlopen(단어_URL).readlines():
    단어들.append(str(단어.strip(), encoding='utf-8'))

def 변환(코드조각, 문장):
    클래스_이름들 = [w.capitalize() for w in
                         random.sample(단어들, 코드조각.count("%%%"))]
    다른_이름들 = random.sample(단어들, 코드조각.count("***"))

    결과들 = []
    매개변수_이름들 = []

    for i in range(0, 코드조각.count("@@@")):
        매개변수_수 = random.randint(1, 3)
        매개변수_이름들.append(', '.join(
            random.sample(단어들, 매개변수_수)))

    for 문장 in 코드조각, 문장:
        결과 = 문장

        # 가짜 클래스 이름
        for 단어 in 클래스_이름들:
            결과 = 결과.replace("%%%", 단어, 1)

        # 가짜 나머지 이름
        for 단어 in 다른_이름들:
            결과 = 결과.replace("***", 단어, 1)

        # 가짜 매개변수 목록
        for 단어 in 매개변수_이름들:
            결과 = 결과.replace("@@@", 단어, 1)

        결과들.append(결과)

    return 결과들


# CTRL-D를 누를 때까지 계속한다
try:
    while True:
        코드조각들 = list(문장들.keys())
        random.shuffle(코드조각들)

        for 코드조각 in 코드조각들:
            문장 = 문장들[코드조각]
            질문, 답 = 변환(코드조각, 문장)
            if 문장을_앞으로:
                질문, 답 = 답, 질문

            print(질문)

            input('> ')
            print(f"답: {답}\n\n")

except EOFError:
    print("\n끝")
