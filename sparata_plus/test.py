from datetime import datetime

name = '홍길동'
age ='24'

hello =  '제 이름은 '+name+'이구요'
print(hello)

hellow= f'제 이름은 {name}입니다. 나이는{age}입니다.'
print((hellow))
# f스트링


today = datetime.now()
mytime= today.strftime('%Y년 %m월 %d일 %H시%M분%S초')
print(today)
print(mytime)
