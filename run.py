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

#def choose_category():
    #while True:
        #user_choise = input("Choose a category by entering its number: ")
        #try:




def choose_item():
    pass





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

main()