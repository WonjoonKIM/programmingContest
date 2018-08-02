best1=0
best2=0
best3=0

a=[0]

n=int(input('막대기 몇개?'))

for i in range(0,n):
    In=int(input('막대의 길이를 입력하세요.'))
    a.append(In)    

for i in range(0,n):
    for j in range(i+1,n):
        for n in range(j+1,n):
            if (a[i]*a[i])+(a[j]*a[j])<=a[n]*a[n]:
                best1=a[i]
                best2=a[j]
                best3=a[n]

if best1==0:
    print('가능한 수가 없습니다.', best1)
else:
    print('가능한 가장 큰 수는 %d%d%d로 이뤄진 삼각형입니다.',
                      a[i], a[j], a[n])
