from pyfiglet import Figlet
from termcolor import colored

PRODUCTS = []
print("Loading...")
myfile = open('C:/Users/Rayan Novin/Desktop/tamrin/section6/1.txt', 'r+')
data = myfile.read().lower()
products_list = data.split('\n')
for i in range(len(products_list)):
    products_info = products_list[i].split(',')
    myDictionary = {}
    myDictionary['id'] = products_info[0]
    myDictionary['name'] = products_info[1]
    myDictionary['price'] = products_info[2]
    myDictionary['count'] = products_info[3]
    PRODUCTS.append(myDictionary)

def show_menu():
    print("1- Add product")
    print("2- Edit product")
    print("3- Delete product")
    print("4- Search product")
    print("5- Show All list product")
    print("6- Buy product")
    print("7- Exit")

def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])

def add_new_product():
    while True:
        Add_Request = input("Do You Want Add Product to Database?  y/n: ")
        if(Add_Request == "y"):
            myfile = open('C:/Users/Rayan Novin/Desktop/tamrin/section6/1.txt', 'a')
            myfile.write("\n")
            myfile.write(str(input("please input new ID: ")))
            myfile.write(",")
            myfile.write(str(input("please input name of new product: ")))
            myfile.write(",")
            myfile.write(str(input("please input price of new product: ")))
            myfile.write(",")
            myfile.write(str(input("please input count of product: ")))
            myfile.close()
        elif(Add_Request == "n"):
            break

def edit_product():
    while True:
        myfile = open('C:/Users/Rayan Novin/Desktop/tamrin/section6/1.txt', 'r+')
        Edit_product = input("Do you want to edit the product? if yes please input y else n: ")
        if (Edit_product == "y"):
            print("1- Edit Id product")
            print("2- Edit Name product")
            print("3- Edit Price product")
            print("4- Edit Count product")
            choice_a_number = input("please choose one of the number: ")
            Id_edit = input("Please Enter Product Id: ")
            for i in range(len(PRODUCTS)):
                if(PRODUCTS[i]["id"]) == Id_edit:
                    if (choice_a_number == "1"):
                        PRODUCTS[i]["id"] == myfile.write(str(input("please input new ID as you want: "))) 
                    elif (choice_a_number == "2"):
                        PRODUCTS[i]["name"] == myfile.write(str(input("please input name of new product as you want: ")))
                    elif (choice_a_number == "3"):
                        PRODUCTS[i]["price"] == myfile.write(str(input("please input price of new product as you want: ")))
                    elif (choice_a_number == "4"):
                        PRODUCTS[i]["count"] == myfile.write(str(input("please input count of product as you want: ")))
                    else:
                        print("We don't have this product")
                        break
        elif(Edit_product == "n"):
            break
        

def delete_product():
    while True:
        Delete_product = input("Do you want to remove the product? if yes please input y else n: ")
        if (Delete_product == "y"):
            Id_delete = input("Please Enter Product Id: ")
            for i in range(len(PRODUCTS)):
                if(PRODUCTS[i]["id"]) == Id_delete:
                    PRODUCTS.remove(i)
                    print("product removed")
                else:
                    print("We don't have this product")
                    break
        elif(Delete_product == "n"):
            break

def search_in_list():
    print(PRODUCTS)
    while True:
        Search_product = input("Do you want to search for the product? if yes please input y else n: ")
        if (Search_product == "y"):
            search_name = input("What are you looking for? ")
            for i in range(len(PRODUCTS)):
                if(PRODUCTS[i]["name"] == search_name):
                    print("product founded")
                    for key, value in PRODUCTS["name"]: 
	                    print("Name: {}, Score: {}".format(key, value)) 
                    break
            else:
                print("Not match")
        elif (Search_product == "n"):
            break


def buy_product():
    pass
def exit():
    pass

f = Figlet(font='standard')
print (f.renderText('Store Market'))

show_menu()
choice = int(input("please choose a number: "))

if choice == 1:
    add_new_product()
elif choice == 2:
    edit_product()
elif choice == 3:
    delete_product()
elif choice == 4:
    search_in_list()
elif choice == 5:
    show_list()
elif choice == 6:
    buy_product()
elif choice == 7:
    exit()

show_menu()