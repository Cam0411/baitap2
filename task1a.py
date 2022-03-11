hoten = input("nhap ho ten:   ")
dodai = len(hoten)
kiemtra = hoten.split()
ho = kiemtra[0:1]
ten = kiemtra[1:10]
print("tong so tu la",dodai)
print("ho la",' '.join(ho))
print("ten la",' '.join(ten))