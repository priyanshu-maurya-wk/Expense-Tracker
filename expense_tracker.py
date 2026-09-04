from expense import Expense
from pathlib import Path
import datetime
import calendar


def main():
    
    BASE_DIR = Path(__file__).resolve().parent
    expense_file_path = BASE_DIR / "expense.csv"
    budget = 2000
    
    expense = user_expense()
    print(expense)
    
    
    save_expense_to_file(expense, expense_file_path)
    
    summerize_expense(expense_file_path, budget)

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
            

def save_expense_to_file(expense : Expense, expense_file_path):

    with open (expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")
    

def summerize_expense(expense_file_path, budget):

    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding = "utf-8") as f:
        lines = f.readlines()
        

        for line in lines:
            
            expense_name, expense_category, expense_amount = line.strip().split(",")
            
            line_expense = Expense(
                name = expense_name,
                category = expense_category,
                amount = float(expense_amount),
            )

            expenses.append(line_expense)
    
    amount_by_category = {}

    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
            
    print("Expense By Category")
    for key, amount in amount_by_category.items():
        print(f"{key}:  ${amount:.2f}")
        
    total_spent = sum([x.amount for x in expenses])

    print(f"Total amount spent is: ${total_spent:.2f} this month")

    remaining_budget = budget - total_spent

    print(f"You have remaining budget of total: ${remaining_budget:.2f}")
    
    now  = datetime.datetime.now()

    day_in_month = calendar.monthrange(now.year, now.month)[1]

    remaining_days = day_in_month - now.day

    print(f"You have {remaining_days} remaining days in this month")
    
    daily_budget = remaining_budget / remaining_days
    
    print(f"You have daily budget of: ${daily_budget:.2f}")
    
        
if __name__ == "__main__":
    
    main()