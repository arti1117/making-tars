print("모든 것을 연습해봅시다.")
print("\\를 이용해 \n 새줄이나 \t 탭을 하는 탈출 문자열에 대해 \'알아야만\' 합니다.")

시 = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("----------")
print(시)
print("----------")

다섯 = 10 - 2 + 3 - 6
print(f"이 값은 다섯입니다: {다섯}")

def 비밀_공식(시작):
    젤리알 = 시작 * 500
    그릇 = 젤리알 / 1000
    상자 = 그릇 / 100
    return 젤리알, 그릇, 상자

시작점 = 10000
젤리, 그릇, 상자 = 비밀_공식(시작점)

# 문자열을 포맷하는 다른 방법이었습니다
print("시작점: {}".format(시작점))

# f"" 문자열을 쓰는 것과 같지요
print(f"젤리 {젤리}알, {그릇}그릇, {상자}상자가 있습니다.")

시작점 = 시작점 / 10

print("이렇게 할 수도 있습니다.")
공식 = 비밀_공식(시작점)

# 리스트를 포맷 문자열에 적용하기 쉬운 방법이지요
print("젤리 {}알, {}그릇, {}상자가 있습니다.".format(*공식))


