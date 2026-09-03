from expense import Expense

def main():
    
    expense = user_expense()
    print(expense)
    
    save_expense_to_file()
    
    summerize_expense()

def user_expense():
    
    expense_name = input("Enter the name of expense: ")
    expense_amount = float(input("Enter the expense amount: "))
    
    expense_category = ["🍕Food", "🏚️Home", "💼Work", "🎉Fun", "✨Miscellaneous"]

    while True:
        
        print("Select a Category")

        for i, categroy_name in enumerate(expense_category):
            
            print(f"{i + 1}. {categroy_name}")
        
        
            
        selected_index = int(input("Enter the category [1-5]: ")) - 1
        
        if selected_index in range(len(expense_category)):
            
            selected_category = expense_category[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount = expense_amount)
            return new_expense
            
        else:
            print("Invalid Input")
            

def save_expense_to_file():
    
    pass

def summerize_expense():

    pass

if __name__ == "__main__":
    
    main()