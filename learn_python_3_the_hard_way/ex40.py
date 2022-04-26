class 노래(object):
    def __init__(self, 가사):
        self.가사 = 가사

    def 노래_불러(self):
        for 한줄 in self.가사:
            print(한줄)


생일_축하 = 노래(["생일 축하 합니다~",
                  "고소당하기는 싫으니까",
                  "여기서 이만 할게요"])


bulls_on_parade = 노래(["조개 껍질 한가득 차고",
                        "가장을 위한다지"])


생일_축하.노래_불러()
bulls_on_parade.노래_불러()
