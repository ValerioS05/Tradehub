import gspread
import random
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("market_hub")


def identify_user():
    """
    Get name of the user,
    we will use the name for greetings and store to add name to basket
    """
    while True:
        user_name = input("Welcome to TradeHub, please enter name to start: ")
        if user_name.strip() and user_name.isalpha():
            return user_name
        elif not user_name.strip():
            print("You must enter a username.")
        else:
            print("Invalid name! Please enter a name containing only letters.")


def get_categories():
    """
    Gets the worksheet name from the spreadsheet excluding the basket
    """
    worksheet_objects = SHEET.worksheets()
    category_names = [
        worksheet.title
        for worksheet in worksheet_objects
        if worksheet.title != "Purchases"
    ]
    return category_names


def choose_category(categories):
    """
    let the user choose a category(category = worksheets in spreadsheet)
    """
    while True:
        user_choice = input("Choose a category by entering its number: ")
        try:
            choice_i = int(user_choice) - 1
            if 0 <= choice_i < len(categories):
                return categories[choice_i]
            else:
                print("Invalid choice. Please enter a valid number")
        except ValueError:
            print("Invalid input, plese enter a number")


def choose_item(category):
    """
    user can choose items stored in the worksheets.
    Items are printed with enumeration
    error handling set to accept valid input
    """
    category_sheet = SHEET.worksheet(category)
    items = category_sheet.get_all_values()
    if len(items) <= 1:
        print("No items available in this category.")
        return
    print("Here are the available items:")
    for index, item in enumerate(items[1:], start=1):
        print(f"{index}. {item[0]} - £{item[1]}")
    while True:
        user_choice = input("Choose an item by entering its number: ")
        try:
            choice_index = int(user_choice) - 1
            if 0 <= choice_index < len(items) - 1:
                return items[choice_index + 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_to_basket(basket, item):
    basket.append(item)
    print(f"{item[0]} added to basket.")


def update_headings():
    """
    Update the headings of the Purchases worksheet
    and calculate the starting column for the next purchase.
    """
    purchases_sheet = SHEET.worksheet("Purchases")
    header_row = purchases_sheet.row_values(3)

    if "" not in header_row:
        next_start_column = len(header_row) * 2 + 1
    else:
        last_col_index = header_row.index("")
        next_start_column = 2 * last_col_index + 1

    next_start_column_a1 = gspread.utils.rowcol_to_a1(1, next_start_column)
    return next_start_column_a1


def purchase(basket, user_name, already_used):
    if not basket:
        print("Your basket is empty!")
    else:
        print("You have purchased the following items:")
        for item in basket:
            print(f"{item[0]} - £{item[1]}")
        purchases_sheet = SHEET.worksheet("Purchases")
        last_column = len(purchases_sheet.row_values(1))
        next_column = last_column + 1
        purchases_sheet.update_cell(1, next_column, user_name)
        total_price = 0
        for i, item in enumerate(basket, start=0):
            purchases_sheet.update_cell(3 + i, next_column, item[0])
            purchases_sheet.update_cell(3 + i, next_column + 1, "£" + item[1])
            total_price += float(item[1])

        purchases_sheet.update_cell(3 + len(basket), next_column, "Total £")
        row = 3 + len(basket)
        column = next_column + 1
        total_price_formatted = f"£{total_price:.2f}"

        purchases_sheet.update_cell(row, column, total_price_formatted)

        order_num = order_number(already_used)
        purchases_sheet.update_cell(1, next_column + 1, order_num)

        print(f"Total price: £{total_price:.2f}")
        print(f"Your order number: {order_num}")
        print("Thank you!")
        return order_num


def get_used_orders():
    purchases_sheet = SHEET.worksheet("Purchases")
    order_numbers = purchases_sheet.col_values(2)[1:]
    return set(order_numbers)


def order_number(already_used):
    while True:
        order_number = str(random.randint(00000, 99999))
        if order_number not in already_used:
            already_used.add(order_number)
            return order_number


def display_basket(basket):
    """
    Display the contents of the basket and provide an option to remove items.
    """
    if not basket:
        print("Your basket is empty.")
    else:
        print("Current items in your basket:")
        for index, item in enumerate(basket, start=1):
            print(f"{index}. {item[0]} - £{item[1]}")
        
        while True:
            user_choice = input("Enter the number of the item to remove or '0' to go back: ")
            try:
                choice_index = int(user_choice) - 1
                if user_choice == '0':
                    break
                elif 0 <= choice_index < len(basket):
                    removed_item = basket.pop(choice_index)
                    print(f"Removed {removed_item[0]} from the basket.")
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")


def main():
    user_name = identify_user()
    next_start_column = update_headings()
    used_order_numbers = get_used_orders()
    order_number_result = order_number(used_order_numbers)
    print(f"Hey {user_name}, choose the category that you want to browse")
    basket = []

    while True:
        categories = get_categories()
        for index, category in enumerate(categories, start=1):
            print(f"{index}: {category}")
        print(f"{len(categories) + 1}: View basket")

        chosen_option = input("Choose an option by entering its number: ")

        if chosen_option == str(len(categories) + 1):
            display_basket(basket)
            continue_shopping = True
            while continue_shopping:
                print("\n1 - Continue shopping in the same category?")
                print("2 - Change category")
                print("3 - Finish purchase")
                print("4 - View basket")

                continue_or_finish = input("Insert number for your next step: ")

                if continue_or_finish == "1":
                    continue_shopping = False
                elif continue_or_finish == "2":
                    break
                elif continue_or_finish == "3":
                    purchase(basket, user_name, used_order_numbers)
                    return
                elif continue_or_finish == "4":
                    display_basket(basket)
                else:
                    print("Invalid choice, please enter 1, 2, 3, or 4.")
            continue

        try:
            chosen_category_index = int(chosen_option) - 1
            if 0 <= chosen_category_index < len(categories):
                chosen_category = categories[chosen_category_index]
            else:
                print("Invalid choice. Please enter a valid number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        while True:
            print(f"This is our stock for {chosen_category}:")
            chosen_item = choose_item(chosen_category)
            if chosen_item:
                add_to_basket(basket, chosen_item)

            print("\n1 - Continue shopping in the same category?")
            print("2 - Change category")
            print("3 - Finish purchase")
            print("4 - View basket")

            continue_or_finish = input("Insert number for your next step: ")

            if continue_or_finish == "1":
                continue
            elif continue_or_finish == "2":
                break
            elif continue_or_finish == "3":
                purchase(basket, user_name, used_order_numbers)
                return
            elif continue_or_finish == "4":
                display_basket(basket)
                continue_shopping = True
                while continue_shopping:
                    print("\n1 - Continue shopping in the same category?")
                    print("2 - Change category")
                    print("3 - Finish purchase")
                    print("4 - View basket")

                    continue_or_finish = input("Insert number for your next step: ")

                    if continue_or_finish == "1":
                        continue_shopping = False
                    elif continue_or_finish == "2":
                        break
                    elif continue_or_finish == "3":
                        purchase(basket, user_name, used_order_numbers)
                        return
                    elif continue_or_finish == "4":
                        display_basket(basket)
                    else:
                        print("Invalid choice, please enter 1, 2, 3, or 4.")
                continue
            else:
                print("Invalid choice, please enter 1, 2, 3, or 4.")


main()