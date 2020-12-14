def intro():
    print("1. Admin\n2. Exit")
    ch = int(input("Enter Choice From Above\n"))
    if ch == 1:
        admin_pwd()
    if ch == 2:
        exit(0)

def admin_pwd():
    passw = "123"s
    ch = input("Enter Password\n")
    if ch == passw:
        admin()
        else:
            print("Wrong Password")
            print("You Will Have 3 Chances")
            for i in range(3):
                passw = "123"
             ch = input("Enter Password\n")
             if ch == passw:
                 admin()
             else:
                 print("Wrong Password")
        print("You Have Excedded Your Three Chances")
        print("Please Try Later")
        exit(0)
                 
            
def admin():
    print("1. Entry In Database\n2. Read The DataBase\n3. Delete The Database\n4. Exit")
    ch = int(input("Enter Choice From Above\n"))
    if ch == 1:
        entry()
    if ch == 2 :
        read()
    if ch == 3:
        delete()
    if ch == 4:
        exit(0)

def entry():
    a = input("Enter Student's Name\n")
    b = int(input("Enter Student's RollNo.\n"))
    c = int(input("Enter Student's Marks\n"))
    d = " "

    f = open("Database.txt","a")
    f.write(a+d+str(b)+d+str(c)+"\n")
    f.close()
    admin()


def read():
    f = open("Database.txt","r")
    z = f.read()
    f.close()
    print(z)
    admin()

def delete():
    f = open("Database.txt","w")
    f.write(" ")
    f.close()
    print("DATABASE Deleted")
    admin()
 
intro()