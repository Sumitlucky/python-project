#define the menu of resturant

menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,
    'tea':20,
    'water':30,
    'chicken roll':100,
    'egg roll':70,
    'momos':100

}
print("welcome to sumit resturant")
print(input("enter your name : "))
print(input("enter your address :"))
print(input("enter your pincode :"))
print(input("enter your phn number :"))
print("pizza:Rs40\npasta:Rs50\nburger:Rs60\nsalad:Rs70\ncoffee:Rs80\ntea:Rs20\nwater:Rs30\nchicken roll:Rs100\negg roll:Rs70\nmomos:Rs100")

order_total = 0
item_1 = input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print(f"Order item {item_1} is not available yet")

another_order = input("do you want to add another item? (yes/no):")
if another_order == "yes":
    item_2 = input("enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2] 
        print(f"item {item_2} has been adddded to order")
    else:
        print(f"Ordered item {item_2} is not available!")


another_order = input("do you want to add another item? (yes/no):")
if another_order == "yes":
    item_3 = input("enter the name of third item = ")
    if item_3 in menu:
        order_total += menu[item_3] 
        print(f"item {item_3} has been adddded to order")
    else:
        print(f"Ordered item {item_3} is not available!")


another_order = input("do you want to add another item? (yes/no):")
if another_order == "yes":
    item_4 = input("enter the name of fourth item = ")
    if item_4 in menu:
        order_total += menu[item_4] 
        print(f"item {item_4} has been adddded to order")
    else:
        print(f"Ordered item {item_4} is not available!")

print(f"the total amount of item to pay is {order_total} ")             

