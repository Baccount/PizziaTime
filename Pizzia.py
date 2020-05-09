from pizzapy import *

store_open = False
active_order = None
menu = None


def ask_user_info():
    first_name = input('Enter your First Name: ')
    last_name = input('Enter your Last Name: ')
    email = input('Enter your Email Address: ')
    phone = input('Enter your Phone Number: ')
    street = input('Enter your street: ')
    city = input('Enter your City: ')
    state = input('Enter your State, Example CA = California: ')
    zip_code = input('Enter your Zip Code: ')
    address = (street + ', ' + city + ', ' + state + ', ' + zip_code)
    current_customer = Customer(first_name, last_name, email, phone, address)
    return current_customer


def checkout():
    card_number = input('Enter your credit card number: ')
    expiration_date = input('Enter your Credit Card expiration date MM/YY: ').replace("/", "")
    security_code = input('Enter your Credit Card Security code: ')
    billing_zip_code = int(input('Enter your Billing Zipcode: '))
    credit_card = CreditCard(card_number, expiration_date, security_code, billing_zip_code)

    active_order.place(credit_card)  # set credit card
    my_local_dominos.place_order(active_order, credit_card)  # place order


new_customer = ask_user_info()  # new_customer is a new Instance of Customer with all the User Infomation entered

try:
    my_local_dominos = StoreLocator.find_closest_store_to_customer(
        new_customer)  # my_local_dominos contains the location of the closest store
    store_open = True  # No error = store located
    menu = my_local_dominos.get_menu()  # get the full menu
    active_order = Order.begin_customer_order(new_customer, my_local_dominos)  # Current order Instance Obj
except:
    store_open = False  # Skip while Loop
    print('No local stores are currently open')

while store_open:
    menu_search = str(input('Search the menu: ').title())  # uppercase first letter
    menu.search(Name=menu_search)  # Show menu results
    print('##Add to order##')
    user_input = input('Enter the code next to the item you want: ')
    try:
        active_order.add_item(user_input)  # use user_input to add to order
        user_input = input('Would you like to order more? Enter : y \nOr Enter n = Check Out: ').lower()
        if user_input == 'y':
            # if user chose y then restart while loop
            continue
        else:
            # stop loop and checkout
            checkout()
            break

    except:
        print('Try a valid order number')
        continue
