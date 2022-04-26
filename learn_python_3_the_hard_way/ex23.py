import sys

스크립트, 입력_인코딩, error = sys.argv

def main(언어_파일, 인코딩, errors):
    줄 = 언어_파일.readline()

    if 줄:
        줄_출력(줄, 인코딩, errors)
        return main(언어_파일, 인코딩, errors)



def 줄_출력(줄, 인코딩, errors):
    다음_언어 = 줄.strip()
    생_바이트열 = 다음_언어.encode(인코딩, errors=errors)
    요리한_문자열 = 생_바이트열.decode(인코딩, errors=errors)

    print(생_바이트열, "<===>", 요리한_문자열)



언어들 = open("languages.txt", encoding="utf-8")

main(언어들, 입력_인코딩, error) 
