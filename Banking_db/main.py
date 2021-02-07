from db_logic import *

def main():

    exit = True
    while exit == True:
        print("Hello Dear, nice to hear from your\n==========================\nHere are the services available on our platform")
        print("1 - Create account with us\n2 - See all user on our platform\n3 - Update your details\n4 - Delete your details from our platform\n5 - Exit from our platform")
        option =  int(input("Enter your option: "))

        if option == 1:
            create_customer()
        elif option == 2:
            print_all_user()
        elif option == 3:
            update_customer()
        elif option == 4:
            delete_customer()
        elif option == 5:
            exit = False
            print("Thanks for using our platform existing now...")
            
        

main()