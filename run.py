import gspread
import random
import pyfiglet
from colorama import just_fix_windows_console, Fore, Style
from google.oauth2.service_account import Credentials

just_fix_windows_console()

SCOPE = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("market_hub")


def print_art(text, font="standard"):
    """
    Printing ascii art
    text, font parameters
    prints argument when called
    """
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
    except pyfiglet.FontNotFound:
        ascii_art = pyfiglet.figlet_format(text)
    print(Fore.GREEN + ascii_art + Style.RESET_ALL)

def print_green(text):
    """
    Printing text with green background
    """
    print(Fore.GREEN + text + Style.RESET_ALL)


def print_red(text):
    """
    Printing text with green background
    """
    print(Fore.RED + text + Style.RESET_ALL)

def identify_user():
    """
    Get name of the user by input of only alphab.
    return user_name
    """
    while True:
        user_name = input("Welcome to TradeHub, please enter name to start:\n")
        if user_name.strip() and user_name.isalpha():
            print_green(f"Hey {user_name}, let's choose a category\n")
            return user_name
        elif not user_name.strip():
            print_red("You must enter a name.\n")
        else:
            print_red("Invalid name! Please enter a name with only letters.\n")


def get_categories():
    """
    Gets the worksheet names from spreadsheet excluding purchases
    Return category_names
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
    parameter categories
    return chosen category (choice_i)
    """
    while True:
        try:
            user_choice = input("Enter the number of the category:\n")
            choice_i = int(user_choice) - 1
            if 0 <= choice_i < len(categories):
                return categories[choice_i]
            else:
                print_red("Invalid choice. Please enter a valid number\n")
        except ValueError:
            print_red("Invalid input, please enter a number\n")


def get_quantity():
    """
    handles the quantity that user insert
    Function used in choose_item
    """
    while True:
        try:
            quantity = int(input("Enter quantity:\n"))
            if quantity <= 0:
                print_red("Invalid quantity! Enter a number greater than 0.\n")
            elif quantity > 5:
                print_red("Maximum quantity allowed at once is 5.\n")
            else:
                return quantity
        except ValueError:
            print_red("Invalid input. Please enter a number.\n")


def choose_item(category):
    """
    User can choose items stored in the worksheets.
    Items are printed with enumeration.
    parameter category
    """
    category_sheet = SHEET.worksheet(category)
    items = category_sheet.get_all_values()
    if len(items) <= 1:
        print_red("No items available in this category.\n")
        return None

    print_green("Here are the available items:\n")
    for index, item in enumerate(items[1:], start=1):
        print_green(f"{index}. {item[0]} - £{item[1]}")
    while True:
        user_choice = input("\nChoose item by entering number, 0 to go back:\n")
        if user_choice == '0':
            return None
        try:
            choice_index = int(user_choice) - 1
            if 0 <= choice_index < len(items) - 1:
                quantity = get_quantity()
                item = items[choice_index + 1]
                return item[0], item[1], quantity
            else:
                print_red("Invalid choice. Please enter a valid number.\n")
        except ValueError:
            print_red("Invalid input. Please enter a number.\n")


def add_to_basket(basket, item_with_quantity):
    item, price, quantity = item_with_quantity
    for _ in range(quantity):
        basket.append((item, price))
    print_green(f"{quantity}x {item} added to basket.\n")


def display_basket(basket, user_name, used_order_numbers):
    while True:
        if not basket:
            print_red("Your basket is empty.\n")
            return False

        print_green("Current items in your basket:\n")

        item_counts = {}
        for item in basket:
            if item[0] in item_counts:
                item_counts[item[0]]['count'] += 1
            else:
                item_counts[item[0]] = {'price': item[1], 'count': 1}

        
        item_list = list(item_counts.items())
        
        
        for index, (item, stats) in enumerate(item_list, start=1):
            print_green(f"{index}. {item} - £{stats['price']} (x{stats['count']})")

        user_choice = input("Enter item number to remove, 0 to go back, + to purchase:\n")
        if user_choice == '0':
            return False
        elif user_choice == '+':
            print_green("Attempting to finish purchase...\n")
            return purchase(basket, user_name, used_order_numbers)
        try:
            choice_index = int(user_choice) - 1
            if 0 <= choice_index < len(item_list):
                removed_item = item_list[choice_index][0]

                for i in range(len(basket)):
                    if basket[i][0] == removed_item:
                        basket.pop(i)
                        break

                item_counts[removed_item]['count'] -= 1
                if item_counts[removed_item]['count'] == 0:
                    del item_counts[removed_item]

                print_green(f"Removed {removed_item} from the basket.\n")
            else:
                print_red("Invalid choice. Please enter a valid number.\n")
        except ValueError:
            print_red("Invalid input. Please enter a number or +.\n")


def handle_basket(basket, user_name, used_order_numbers):
    while True:
        result = display_basket(basket, user_name, used_order_numbers)
        if result == 'Purchased':
            return "Purchased"
        elif result is False:
            return
        while True:
            print_green("\n1 - Continue shopping in the same category?")
            print_green("2 - Change category")
            print_green("3 - Finish purchase")
            print_green("4 - View basket\n")
            continue_or_finish = input("Insert number for next step:\n")
            if continue_or_finish == "1":
                return False
            elif continue_or_finish == "2":
                return True
            elif continue_or_finish == "3":
                return purchase(basket, user_name, used_order_numbers)
            elif continue_or_finish == "4":
                break
            else:
                print_red("Invalid choice, please enter 1, 2, 3, or 4.\n")

def shop_in_category(chosen_category, basket, user_name, used_order_numbers):
    while True:
        print_green(f"This is our stock for {chosen_category}:")
        chosen_item = choose_item(chosen_category)
        if chosen_item:
            add_to_basket(basket, chosen_item)
        while True:
            print_green("\n1 - Continue shopping in the same category?")
            print_green("2 - Change category")
            print_green("3 - Finish purchase")
            print_green("4 - View basket\n")
            continue_or_finish = input("Insert number for your next step:\n")
            if continue_or_finish == "1":
                break
            elif continue_or_finish == "2":
                return True
            elif continue_or_finish == "3":
                return purchase(basket, user_name, used_order_numbers)
            elif continue_or_finish == "4":
                basket_result = display_basket(basket, user_name, used_order_numbers)
                if basket_result == "Purchased":
                    return "Purchased"
                elif basket_result is False:
                    break
            else:
                print_red("Invalid choice, please enter 1, 2, 3, or 4.\n")


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


def give_feedback(user_name):
    print_green("Please rate TradeHub from 1 to 5:\n")
    print_green("Enter 'skip' to skip giving ratings.\n")

    aspects = [
        "Site design",
        "Product variety",
        "Checkout process",
        "Customer service",
        "Service speed"
    ]
    ratings = []

    for aspect in aspects:
        while True:
            rating_input = input(f"Rate '{aspect}': ").strip().lower()
            if rating_input == 'skip':
                print_red("Skipping ratings.\n")
                return None

            try:
                rating = int(rating_input)
                if 1 <= rating <= 5:
                    ratings.append(rating)
                    break
                else:
                    print_red("Invalid rating! Enter a number between 1 and 5.\n")
            except ValueError:
                print_red("Invalid input! Please enter a number between 1 and 5.\n")

    if not ratings:
        print_green("No ratings provided.\n")
        return None

    avg_rating = sum(ratings) / len(ratings)
    print_green(f"\nThank you for your feedback!\n")
    print_green(f"Your average rating for TradeHub is: {avg_rating:.2f}\n")

    if avg_rating < 3:
        print_red("Sorry to hear that you were not satisfied. We'll improve.\n")
    elif avg_rating >= 4:
        print_green("Thank you for your positive feedback! Glad you had a great experience.\n")
    else:
        print_green("We appreciate your feedback. We'll use it to enhance your experience.\n")
    return avg_rating


def purchase(basket, user_name, already_used):
    if not basket:
        print_red("Your basket is empty!\n")
        return "No items"

    print_green("You have purchased the following items:\n")
    for item in basket:
        print_green(f"{item[0]} - £{item[1]}\n")

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

    print_green(f"Total price: £{total_price:.2f}\n")
    print_green(f"Your order number: {order_num}\n")
    print_green(f"Thank you {user_name}!\n")

    avg_rating = give_feedback(user_name)
    purchases_sheet.update_cell(row + 1, next_column, "Rating")
    purchases_sheet.update_cell(row + 1, column, avg_rating)
    return "Purchased"


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







def main():
    print_art("TradeHub", font="standard")
    user_name = identify_user()
    update_headings()
    used_order_numbers = get_used_orders()
    basket = []
    while True:
        categories = get_categories()
        for index, category in enumerate(categories, start=1):
            print_green(f"{index}: {category}")
        print_green(f"{len(categories) + 1}: View basket\n")
        chosen_option = input("Choose an option by entering its number:\n")
        if chosen_option == str(len(categories) + 1) or chosen_option == "+":
            result = handle_basket(basket, user_name, used_order_numbers)
            if result == "empty":
                print_green("Redirecting to categories...\n")
                continue
            elif result == "Purchased":
                print_green("Purchase completed successfully.\n")
                print_green("Exiting program.")
                print_art("Have a great day!", font="standard")
                break
        else:
            try:
                chosen_category_index = int(chosen_option) - 1
                if 0 <= chosen_category_index < len(categories):
                    chosen_category = categories[chosen_category_index]
                    shop_result = shop_in_category(chosen_category, basket, user_name, used_order_numbers)
                    if shop_result == "Purchased":
                        print_green("Purchase completed successfully.\n")
                        print_art("Goodbye", font="standard")
                        break
                    else:
                        continue
                else:
                    print_red("Invalid choice. Enter a valid number.\n")
            except ValueError:
                print_red("Invalid input. Please enter a number.\n")

main()
