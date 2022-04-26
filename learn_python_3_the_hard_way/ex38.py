열_가지 = "사과 귤 까마귀 전화기 빛 설탕 물"

print("잠깐 아직 목록에 10개가 들어있지 않으니 한 번 고쳐봅시다.")

물건 = 열_가지.split(' ')
다른_물건 = ["낯", "밤", "노래", "부메랑"
                ,"옥수수", "바나나", "아이", "어른"]

while len(물건) != 10:
    next_one = 다른_물건.pop()
    print("추가: ", next_one)
    물건.append(next_one)
    print(f"이제 {len(물건)} 항목이 있습니다.")


print("한 번 볼까요! ", 물건)

print("이걸로 무언가 해봅시다.")

print(물건[1])
print(물건[-1])
print(len(물건))
print(물건.pop())
print(len(물건))

print(' '.join(물건))
print('#'.join(물건[3:5]))
