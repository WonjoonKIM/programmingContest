a= int(input("얼마를 만들어 볼까요?"))

c500=0
c100=0
c50=0
c10=0
c5=0
c1=0

rest=a%500
c500++
if rest==0:
    print(c500+'개 필요')

rest=rest%100
c100++
if rest==0:
    print("500원%d개, 100원 %개 필요", c500, c100)
        
rest=rest%50
c50++
if rest==0:
    print("500원%d개, 100원 %개, 50원 %개 필요", c500, c100, c50)

rest=rest%10
c10++
if rest==0:
    print("500원%d개, 100원 %개, 50원 %개, 10원 %d개 필요"
              ,c500, c100, c50, c10)

rest=rest%5
c5++
if rest==0:
    print("500원%d개, 100원 %개, 50원 %개, 10원 %d개, 5원 %d개 필요"
              ,c500, c100, c50, c10, c5)

rest=rest%1
c1++
if rest==0:
    print("500원%d개, 100원 %개, 50원 %개, 10원 %d개, 5원 %d개, 1원 %개 필요"
              ,c500, c100, c50, c10, c5, c1)
