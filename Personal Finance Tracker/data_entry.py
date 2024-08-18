from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}
#get information from the user
#getting the date
def get_date(prompt, allow_default=False):
    #allow default tells value if we should have value for today's date, blank-entering would input today's date
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format) # format to dd-mm-yyyy
    # check if the user inputs a valid date format
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)
    

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Income 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

def get_description():
    return input("Enter a description (optional): ")