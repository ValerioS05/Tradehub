import gspread
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

tech = SHEET.worksheet("Tech")
data = tech.get_all_values()


def identify_user():
    """
    Get name of the user , we will use the name for greetings and store to add name to basket
    """
    while True:
        user_name = input("Welcome to TradeHub, please enter a username to start: ")
        if user_name.strip() and user_name.isalpha():
            return user_name
        elif not user_name.strip():
            print("You must enter a username.")
        else:
            print("Invalid username! Please enter a username containing only letters.")


def get_categories():
    """
    Gets the worksheet name from the spreadsheet excluding the basket
    """
    worksheet_objects = SHEET.worksheets()
    category_names = [worksheet.title for worksheet in worksheet_objects if worksheet.title != "Basket"]
    return category_names

def choose_category(categories):
    """
    let the user choose a category(category = worksheets in spreadsheet)
    """
    while True:
        user_choice = input("Choose a category by entering its number: ")
        try:
            choice_i = int(user_choice) -1
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




def add_to_basket():
    pass





def purchase():
    pass




def main():
    user_name = identify_user()
    print(f"Hey {user_name} Choose the category that you want to browse inserting the relative number")
    categories = get_categories()
    for index, category in enumerate(categories,start=1):
        print(f"{index}: {category}")
    
    choosen_category = choose_category(categories)
    print(f"This is our stock for {choosen_category}:")

    chosen_item = choose_item(choosen_category)

main()