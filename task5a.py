nhapgiatri = input("nhap gia trt:  ")
laygiatri = nhapgiatri.split()
print("chu la: ")
for x in laygiatri:
    if x.isalpha():
        print(x,end=" ")
    if x.isdigit():
        print("\n","so la",x)  