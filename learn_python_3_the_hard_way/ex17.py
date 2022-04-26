from sys import argv
from os.path import exists

스크립트, 원본_파일, 복사_파일 = argv

print(f"{원본_파일} 에서 {복사_파일} 로 복사합니다.")

# 이 두 줄은 한 줄로도 쓸 수 있습니다. 어떻게 할까요?
입력_파일 = open(원본_파일, encoding='utf-8')
입력_자료 = 입력_파일.read()

print(f"입력 파일은 {len(입력_자료)}바이트입니다.")

print(f"출력 파일이 존재하나요? {exists(복사_파일)}")
print("준비되었습니다. 계속하려면 리턴을, 취소하려면 CTRL-Z를 누르세요.")
input()

출력_파일 = open(복사_파일, 'w', encoding='utf-8')
출력_파일.write(입력_자료)

print("좋습니다. 모두 완료되었습니다.")

출력_파일.close()
입력_파일.close()
