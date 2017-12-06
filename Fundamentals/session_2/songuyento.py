n = int(input("number?"))
for i in range(2,n):
    if i%n == 0:
        print("ko phai so nguyen to")
        break
    else:
        print("so nguyen to")
