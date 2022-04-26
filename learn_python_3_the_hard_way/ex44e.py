class 합성대상(object):

    def 덮어쓰기(self):
        print("합성대상 덮어쓰기()")

    def 묵시적_동작(self):
        print("합성대상 묵시적_동작()")

    def 대체하기(self):
        print("합성대상 대체하기()")


class 자식(object):

    def __init__(self):
        self.합성대상 = 합성대상()

    def 묵시적_동작(self):
        self.합성대상.묵시적_동작()

    def 덮어쓰기(self):
        print("자식 덮어쓰기()")

    def 대체하기(self):
        print("자식, 합성대상 대체하기() 호출 전")
        self.합성대상.대체하기()
        print("자식, 합성대상 대체하기() 호출 후")


아들 = 자식()

아들.묵시적_동작()
아들.덮어쓰기()
아들.대체하기()
