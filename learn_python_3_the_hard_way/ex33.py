i = 0

숫자들 = []

while i < 6:
    print(f"꼭대기에서 i는 {i}")
    숫자들.append(i)

    i = i + 1
    print("숫자는 이제: ", 숫자들)
    print(f"바닥에서 i는 {i}")


print ("숫자: ")

for 숫자 in 숫자들:
    print(숫자)
