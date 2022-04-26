class 방(object):

    def __init__(self, 이름, 설명):
        self.이름 = 이름
        self.설명 = 설명
        self.길들 = {}

    def 이동(self, 방향):
        return self.길들.get(방향, None)

    def 길_추가(self, 길들):
        self.길들.update(길들)
