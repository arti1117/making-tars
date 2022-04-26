class 부모(object):

    def 덮어쓰기(self):
        print("부모 덮어쓰기()")

class 자식(부모):

    def 덮어쓰기(self):
        print("자식 덮어쓰기()")

아빠 = 부모()
아들 = 자식()

아빠.덮어쓰기()
아들.덮어쓰기()
