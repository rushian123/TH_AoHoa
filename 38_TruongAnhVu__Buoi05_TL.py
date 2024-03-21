# Bai 3
class ShoppingCart:
    
    def __init__(self):
       
        self.items = []


    def add(self, new_item):
      
        if not isinstance(new_item, Item):
            raise TypeError("Can only add items of type Item")
        self.items.append(new_item)


    def remove(self, item_name):
        
        for i, item in enumerate(self.items):
            if item.ten == item_name:
                del self.items[i]
                return  
        print(f"Item '{item_name}' not found in the cart.") 


    def calculate_total(self):
        
        total = 0
        for item in self.items:
            total += item.gia
        return total


    def show(self):
     
        if not self.items:
            print("The shopping cart is empty.")
            return

        print("Items in Shopping Cart:")
        for item in self.items:
            print(f"- {item.ten}: {item.gia}")


class Item:
    
    def __init__(self, ten, gia):

        self.ten = ten
        self.gia = gia


i1 = Item("Sua", 111134)
i2 = Item("Banh mi", 222234)
i3 = Item("Banh trang", 23434)

sc = ShoppingCart()
sc.add(i1)
sc.add(i2)
sc.add(i3)

sc.show()
print(f"Total : {sc.calculate_total()}")
sc.remove("Banh mi")
sc.show()



# Bai 4
class Sanpham:
    
    def __init__(self):
        self.so_luong = 200
        self.gia = 35.0
        self.ten_sp = "shoes"
    
    def get_price(self,sl):
        if sl < 10:
            return sl * self.gia
        elif sl < 100:
            return sl * 0.9  * self.gia
        else:
            return sl * 0.8  * self.gia
        
    def make_purchase(self,sl):
        if sl > self.so_luong:
            print("so luong mua lon hon so luong con lai trong kho")
        else:
            self.so_luong = self.so_luong - sl
        return self.so_luong
    
sp = Sanpham()

spm1 = 4
spm2 = 12
spm3 = 112

print(f"cost for {spm1} {sp.ten_sp} = {sp.get_price(spm1)}")
print(f"remaining in stock after buy : {sp.make_purchase(spm1)}\n")

print(f"cost for {spm2} {sp.ten_sp} = {sp.get_price(spm2)}")
print(f"remaining in stock: {sp.make_purchase(spm2)}\n")        
    
print(f"cost for {spm3} {sp.ten_sp} = {sp.get_price(spm3)}")
print(f"remaining in stock: {sp.make_purchase(spm3)}")         
        


# Bai 5
class Wordplay:
    def __init__(self, lst):
        self.lst = lst
        
    def words_with_length(self):
        for item in self.lst:
                print(f"{item}: {len(item)}")
    
    def started_with(self,stw):
        for item in self.lst:
            if item.startswith(stw):
                print(item)
        
    def end_with(self,ew):
        for item in self.lst:
            if item.endswith(ew):
                print(item)
    
    def only(self, o):
        for item in self.lst:
            if o in item:
                print(item)
    
    def avoids(self, a):
        for item in self.lst:
            if a not in item:
                print(item)


words = ["hellw", "yah", "Yeah", "bobs", "Belly", "ubby", "Vu dap chai"]
list = Wordplay(words)

print("Length of words in list:")
list.words_with_length()

s = "y"
print(f"\nStart with {s}:")
list.started_with(s)

e = "y"
print(f"\nEnd with {e}:")
list.end_with(e)

o = "u"
print(f"\nContain {o} in word:")
list.only(o)

a = "u"
print(f"\nNot contain {o} in word:")
list.avoids(a)



# Bai 6
class Pass_manager:
    
    def __init__(self):
        self.oldpw = []
        
    
    def get_password(self):
        return self.oldpw[-1]
    
    def set_password(self,newpw):
        if newpw in self.oldpw:
            return False
        else:
            self.oldpw.append(newpw)
            return True
            
    
    def is_corr(self, ipw):
        return ipw == self.oldpw[-1]
        
pm = Pass_manager()
pm.set_password("changme")        
print(pm.get_password())

pm.set_password("passwordhasbeenchanged")
print(pm.get_password())

a = pm.is_corr("ipw")
print(a)
    
a = pm.is_corr("passwordhasbeenchanged")
print(a)    
  


# Bai 7
class Subs:
    
    def f1(self):
        nums = []
        n = int(input("Enter number elements of list: "))
        for i in range(n):
            print("Enter element:")
            nums.append(int(input()))
        nums.sort()
        self.f2(nums, [])

    def f2(self, nums, current):
        print(current)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.f2(nums[i+1:], current + [nums[i]])

subsets = Subs()
print("Subset: ")
subsets.f1()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
