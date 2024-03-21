from math import pi
from math import sqrt


'''BAI TAP HUONG DAN'''

# Bai 1

class Car:
# Thuoc tinh lop
    loaixe = "Ô tô"
# Thuoc tinh doi tuong
    def __init__(self, tenxe, mausac, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu
       
# instantiate the Car class
toyota = Car("Toyota", "Đỏ", "Điện")
lamborghini = Car("Lamborghini", "Vàng", "Deisel")
porsche = Car("Porsche", "Xanh", "Gas")

# access the class attributes
print("Porsche là {}.".format(porsche.__class__.loaixe))
print("Toyota là {}.".format(toyota.__class__.loaixe))
print("Lamborghini cũng là {}.".format(lamborghini.__class__.loaixe))
# access the instance attributes
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( toyota.tenxe, toyota.mausac,
toyota.nguyenlieu))
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( lamborghini.tenxe,
lamborghini.mausac,lamborghini.nguyenlieu))
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( porsche.tenxe, porsche.mausac,
porsche.nguyenlieu))


# Bai 2
class calculator_implementation():
    def __init__(self, in_1, in_2):
        self.a=in_1
        self.b=in_2
        
        
    def add_vals(self):
        return self.a+self.b
    
    
    def multiply_vals(self):
        return self.a*self.b
    
    
    def divide_vals(self):
        return self.a/self.b
    
    
    def subtract_vals(self):
        return self.a-self.b

input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))
print ("The entered first and second numbers are : ")
print(input_1,input_2)
my_instance=calculator_implementation(input_1,input_2)
choice=1


while choice!=0:
    print("e. Exit")
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Multiplication")
    print("4. Division")
    choice=int(input ("Enter your choice... "))
    if choice ==1:
        print ("The computed addition result 1s : ",my_instance.add_vals())
    elif choice==2:
        print ("The computed subtraction result is : ",my_instance.subtract_vals())
    elif choice==3:
        print ("The computed product result is : ",my_instance.multiply_vals())
    elif choice==4:
        print ("The computed division result is : ",round(my_instance.divide_vals(),2))
    elif choice==0:
        print("Exit")
    else:
        print ("Sorry, invalid choice!")
print()

# Bai 3
class rectangle():
    def __init__ (self, breadth, length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:" ,obj.area())
print()



'''BAI TAP TREN LOP'''
# Bai 1
# Class tinh chu vi dien tich hinh tron
class Bai1:
    # Ham khoi tao
    def __init__(self, bankinh):
        self.bankinh = bankinh
    
    # Phuong thuc tinh chu vi
    def Chuvi(self):
        return 2*pi*self.bankinh
    
    #Phuong thuc tinh dien tich
    def Dientich(self):
        return pi*self.bankinh*self.bankinh
    
print("Nhap vao ban kinh cua hinh tron")
bankinh = float(input())
hinhtron = Bai1(bankinh)
print(f"Chu vi cua hinh tron la: {hinhtron.Chuvi()}")
print(f"Dien tich cua hinh tron la: {hinhtron.Dientich()}")



# Bai 2
class Bai2:
    # Ham khoi tao
    def __init__(self):
        self.x = ''
    
    
    # Phuong thuc nhan chuoi vao
    def get(self):
        print("Nhap chuoi vao: ")
        self.x = input()
    
    
    #Phuong thuc in chuoi ra
    def put(self):
        print("chuoi xuat ra: ")
        print(self.x)


bai2 = Bai2()
bai2.get()
bai2.put()

#Bai3
class Bai3:
    def f1(self):
        nums = []
        n = int(input("Nhập số lượng phần tử của danh sách: "))
        print("Nhập các phần tử của danh sách:")
        for i in range(n):
            nums.append(int(input()))
        nums.sort()
        self.f2(nums, [])


    def f2(self, nums, current):
        print(current)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.f2(nums[i+1:], current + [nums[i]])


subsets = Bai3()
while True:
    print("\nChọn chức năng:")
    print("1. Tạo và in ra tất cả các tập hợp con của một danh sách số nguyên")
    print("2. Thoát")
    choice = int(input())
    if choice == 1:
        subsets.f1()
    elif choice == 2:
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


# Bai 4
class Nhanvien():
    
    
    def inputInfor(self): 
        print("Nhap ten ")
        self.ten = input()
        print("Nhap tuoi ")
        self.tuoi = int(input())
        print("Nhap dia chi ")
        self.diachi = input()
        print("Nhap tien luong ")
        self.tienluong = float(input())
        print("Nhap so gio lam ")
        self.tongsogiolam = float(input())
        
               
    def printInfo(self): 
        print(f"Ten: {self.ten}")
        print(f"Tuoi: {self.tuoi}")
        print(f"Dia chi: {self.diachi}")
        print(f"Tien luong: {self.tienluong}")
        print(f"So gio lam: {self.tongsogiolam}")
        print(f"Tien thuong la: {self.tinhThuong()}")
        
        
    def tinhThuong(self):
        if self.tongsogiolam >= 200:
            return self.tienluong *0.2
        elif 200 > self.tongsogiolam >= 100:
            return self.tienluong * 0.1
        else:
            return 0


nhanvien = Nhanvien()
nhanvien.inputInfor()
nhanvien.printInfo()

'''
# Bai 5
class Sinhvien():
    def __init__(self,mssv, diemtb, tuoi, lop):
        self.mssv = mssv
        self.diemtb = diemtb
        self.tuoi = tuoi
        self.lop = lop
    
    
    def inputInfo(self):
        pass
    
    
    def showInfo(self):
        pass
    
    
    def coHocBong(self):
        if self.diemtb >=8:
            return True
        else:
            return False
        

sinhvien = Sinhvien(mssv, diemtb, tuoi, lop)  
sinhvien.inputInfo()
sinhvien.showInfo()  
'''

#Bai 6
# Xay dung lop tam giac
class Triangle():
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        
    # Nhap vao 3 canh cua tam giac    
    def nhap(self):
        self.a = float(input("Nhap vao a: "))
        self.b = float(input("Nhap vao b: "))
        self.c = float(input("Nhap vao c: "))
        
    # Xac dinh cac loai tam giac    
    def loaitamgiac(self):
        if self.a+ self.b > self.c or self.a+self.c > self.b or self.b+self.c > self.a:
            if self.a * self.a == self.b * self.b +self.c * self.c or self.b * self.b == self.a * self.a + self.c * self.c or self.c * self.c == self.b * self.b + self.a * self.a:
                print("Day la tam giac vuong")
            elif  self.a==self.b==self.c:
                print("Day la tam giac deu")
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                print("Day la tam giac can")
            elif  self.a*self.a>self.b*self.b+self.c*self.c or self.b*self.b>self.a*self.a+self.c*self.c or self.c*self.c >self.a*self.a+self.b*self.b:
                print("Day la tam giac tu")
            else:
                print("Day la tam giac nhon")
        else:
            print("Day khong phai la tam giac")
  
     
    def chuvi(self):
        self.P = self.a + self.b + self.c
        self.p = self.P /2
        return self.P


    def dientich(self):
        return sqrt((self.p * (self.p-self.a) * (self.p-self.b) *(self.p-self.c)))

tri = Triangle()
tri.nhap()
tri.loaitamgiac()
print(f"Chu vi cua tam gia la {tri.chuvi()}")
print(f"Dien tich cua tam gia la {tri.dientich()}")










