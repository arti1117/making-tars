사람 = 30
차 = 40
트럭 = 15

if 차 > 사람:
    print("차를 타야 해요.")
elif 차 < 사람:
    print("차를 안 타야 해요.")
else:
    print("결정할 수 없어요.")


if 트럭 > 차:
    print("트럭이 너무 많아요.")
elif 트럭 <차:
    print("트럭을 탈 수도 있어요.")
else:
    print("아직도 결정할 수 없어요.")


if 사람 > 트럭:
    print("좋아요 트럭을 탑시다.")
else:
    print("좋아요 그럼 집에 있죠.")

