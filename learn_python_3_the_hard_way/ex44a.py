class 부모(object):

    def 묵시적_동작(self):
        print("부모 묵시적_동작()")

class 자식(부모):
    pass


아빠 = 부모()
아들 = 자식()

아빠.묵시적_동작()
아들.묵시적_동작()
