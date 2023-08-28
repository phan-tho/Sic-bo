import time
from random import randrange
sodu = 1000000
print(f"Số dư hiện tại của bạn là {sodu}")
while True:
    while True:
        a =input("Tài hay Xỉu: ")
        if a == "t":
            check = 1
            break
        elif a == "x":
            check = 0
            break

    b = int(input("Bạn muốn cược nhiêu tiền: "))
    while b > sodu:
        b = int(input("Số dư không đủ vui lòng nhập lại "))

    xx1 = randrange(1,7)
    xx2 = randrange(1,7)
    xx3 = randrange(1,7)
    tong = xx1 + xx2 + xx3
    if tong > 10:
        check2 = 1
    else:
        check2 = 0

    print(xx1)
    time.sleep(0.5)
    print(xx2)
    time.sleep(1)
    print(xx3)

    if check == check2:
        print(f"Tông bằng {tong} ==> Tài")
        print("Quá xuất sắc giá như bạn biết đến tài xỉu sớm hơn")
        sodu = sodu + b
        print(f"Sô dư của bạn là {sodu}")
    else:
        print(f"Tông bằng {tong} ==> Xỉu")
        sodu = sodu - b
        print("Lố ở đâu gấp đôi ở đó")
        print(f"Số dư của bạn là {sodu}")
    
    g = input("Bạn có muốn chơi tiếp không(c/k): ")
    if g == "k":
        print("Có những người từ bỏ khi rất gần với thành công")
        break