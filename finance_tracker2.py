"""A personal financial tracker that will display total budget over the week"""

class Expense():
    """A class that stores each expense's data for the week"""
    def __init__(self, date, expense, category):
        self.expense = expense
        self.date = float(date)
        self.category = category
             
        
class Create_expenses():
    """A class that creates and Stores all expenses"""
    def __init__(self, date, expense, category):
        self.expense_list = []
        
        self.expense_list.append(Expense(date, expense, category))

class Results:   
    """A class that organizes the expense entries and calculates the expense total"""            
    def organize_days():
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        if Create_expenses.expense_list > 1:
            sorted(Create_expenses.expense_list[0], key = days.index)
        return Create_expenses.expense_list
    
    def calculate_total_week():
        total = 0
        
        if Create_expenses.expense_list > 1:
            for expense in Create_expenses.expense_list[1]:
                total += expense
                return total    
    
class Display: 
    "A class that prints user directions for the program."   
    def printMenu():
        print("Please choose from one of the following options (1, 2, 3):")
        print("1. Add A New Expense")
        print("2. Remove an Expense")
        print("3. List All Expenses and total budget for the week")

    def listExpenses():
        print("Here is a list of your expenses for the week:")
        list = Results.organize_days()
        print(list)
        
    def removeExpense():
        while True:
            amount = print("What expense would you like to remove? (specific date, amount, category):")
            
            for expense in Create_expenses.expense_list:
                try:
                    if expense == amount:
                        del(expense)
                except:
                    print("Invalid input. Please try again.")
    

if __name__ == "__main__":
    while True:
        ###Prompt the user
        Display.printMenu()
        optionSelected = input(">")
        
        if (optionSelected == "1"):
            date = input("Enter the date (Monday, Tuesday...): ")
            while True:
                try:
                    amountToAdd = input(">")
                    break
                except:
                     print("Invalid input. Please try again.")
            
            amount = input("Enter expense amount: ")
            while True:
                try:
                    category = input("> ")
                    break
                except:
                     print("Invalid input. Please try again.")
            category = input("Enter category (Food, Housing, Transport, School, Misc:): ")
        
            Create_expenses(date, amount, category)
            
            i = input("Add another expense?(yes/no): ")
            if i == "yes":
                optionSelected == "1"    
            else:
                Display.printMenu()
                
        elif(optionSelected == '2'):
            Display.removeExpense()
            i = input("Delete another expense?: ")
            if i == "yes":
                optionSelected == "2"
            else:
                Display.printMenu()
            
        elif(optionSelected == '3'):
            result = Results()
            
            print(Display.listExpenses())
            print(f"Total amount spent for this week: {result.calculate_total_week()}")
        else:
             print("Invalid input. Please try again.")
             Display.printMenu()