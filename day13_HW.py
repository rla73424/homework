import turtle as t                 #거북이 생성
import random                      # 랜덤 import

t.up()                             #거북이 엎시키기
t.goto(-250,-250)                  #거북이 모퉁이 보내기
t.down()                           #거북이 내리기
for x in range(4):                 #500,500짜리 사각형 만들기
    t.forward(500)
    t.left(90)
t.up()                             #거북이 들기
t.home()                           #거북이 0,0으로 보내기
t.shape("circle")                  #거북이 모양 동그라미로 바꾸기



t.left(random.randint(1,360))      #왼쪽으로 랜덤하게 돌리기
while True:                        #벽 무한으로 벽 튕기기 위해 while함수 
    t.fd(5)                        #5씩 이동시키기
    x=t.xcor()                     # x값 읽기
    y=t.ycor()                     # y값 읽기
    a=t.heading()                  # 거북이 각도 a에 넣기
    if x>=250:                     # 오른쪽 벽에 닿았을때 튕기기
        if a>90:
            t.right(180+2*a)       # 각도는 모두 그냥 계산하였습니다. 손으로
        else:
            t.left(180-2*a)
    if y>=250:                     # 위쪽 벽에 닿았을때 튕기기
        if a>90:
            t.left(-2*a)         
        else:
            t.right(2*a)
    if x<=-250:                    # 왼쪽 벽에 닿았을때 튕기기
        if a>90:
            t.left(180-2*a)
        else:
            t.right(180+2*a)
    if y<=-250:                    # 아래쪽 벽에 닿았을때 튕기기
        if a>90:
            t.right(2*a)
        else:
            t.left(-2*a)
            







    
    
