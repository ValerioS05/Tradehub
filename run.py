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
    user_name = input("Welcome to TradeHub, please enter a username to start: ")
    return usern_name


def get_categories():
    """
    Gets the worksheet name from the spreadsheet excluding the basket
    """
    worksheet_objects = SHEET.worksheets()
    category_names = [worksheet.title for worksheet in worksheet_objects if worksheet.title != "Basket"]
    return category_names


# Call the test_get_categories function to test the get_categories function
test_get_categories()
def choose_category():
    pass




def choose_item():
    pass





def add_to_basket():
    pass





def purchase():
    pass




def main():
    pass