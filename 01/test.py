a = int(input('숫자 입력하세요. : '))
x = int(input('숫자 입력하세요.(2) : '))
y = int(input('숫자 입력하세요.(3) : '))
c = int(input('숫자 입력하세요.(4) : '))

a = x if x > y else y #a if b else c: b를 평가한 값이 참이면 a, 거짓이면 c
print('c는 0입니다.' if c==0 else 'c는 0이 아닙니다.')