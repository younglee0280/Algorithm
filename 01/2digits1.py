#2자리 양수 입력받기(10 ~ 99)
print('2자리 양수를 입력하세요.')

while True:
    num = int(input('값을 입력하기. : '))
    if num > 9 and num < 100:
        break
    
print(f'입력받은 양수는 {num}입니다.') 