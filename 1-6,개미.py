L=int(input("막대의 길이를 입력하세요:  "))
n=int(input("개미가 몇 마리인지 입력하세요:  "))
a=list()

for i in range(n):
    x=int(input("개미의 위치를 입력하세요:  "))
    a.append(x)

max1=a[0]
max2=a[0]

for i in range(n):
    if a[i]>5 && a[i]>max1:
        max1=a[i]
    if a[i]<=5 && a[i]<max2:
        max2=a[i]

result_min= max1>max2 ? max1:max2

print(result_min)

mx1=a[0]
mx2=a[0]

for i in range(n):
    if a[i]<=5:
        mx1=L-a[i]
    if a[i]>5:
        mx2=a[i]

result_max= mx1>mx2 ? mx1:mx2
        

#최소= 0이나 10으로 직진, 1~5까지 위치 중 가장 큰 수 max1
#                          6~10위치 중 가장 작은 수 max2
#-> min= max1>max2 ? max1:max2

#최대= 0이나 10이 안되게, 1~5까지는 10으로 증가 가장 큰 수 mx1
#                      6~10까지는 0으로 증가 가장 큰 수 mx2
#-> max= mx1>mx2 ? mx1:mx2
