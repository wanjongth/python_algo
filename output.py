# 출력할 변수들
a = 1
b = 2

print(a, b)
print(a)
# print()는 기본적으로 출력 이후 줄 바꿈 수행

# 변수를 문자열로 바꾸어 출력하는 소스코드 예시
answer = 7
print("정답은" + str(answer) + "입니다.")

# 각 변수를 콤마로 구분하여 출력하는 소스코드 예시
# 변수를 문자열로 바꾸어 출력하는 소스코드 예시 - 변수의 값 사이에 의도치 않은 공백이 삽입 될 수 있음
answer = 7
print("정답은", str(answer), "입니다.")

# Python3.6 이상 부터 f-string 사용 가능 - {} 안에 변수를 넣음으로써, 자료형의 변환 없이도 간단히 문자열과 정수를 함께 넣을 수 있다
print(f"정답은 {answer}입니다.")
