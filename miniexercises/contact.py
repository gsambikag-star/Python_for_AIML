contacts={}

while True:
    print("1.Add Contacts")
    print("2.Update Phone number")
    print("3.Delete Contact")
    print("4.Display contacts")
    choice=int(input("Enter your choice:\n"))

    match choice:
        case 1:
            name=input("enter name:\n")
            if name in contacts:
                print("Contact Already exists")
            else:
                phone_no=int(input("enter phone number:\n"))
                contacts[name]=phone_no
                print("Contact added successfully")

        case 2:
            name=input("enter name:\n")
            if name in contacts:
                new_phone_no=int(input("enter new phone number:\n"))
                contacts[name]=new_phone_no
                print("updated phone number successfully")
            else:
                print("no contact found")
        case 3:
            name=input("enter name:\n")
            if name in contacts:
                del contacts[name]
                print("deleted contact successfully")
            else:
                print("no contact found")

        case 4:
            if len(contacts)==0:
                print("no contacts in contact book")
            else:
                print("\ncontacts:\n")
                for x,y in contacts.items():
                    print(x,":",y)
            break
        