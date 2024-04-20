"""A personal financial tracker that will display total budget over the week"""

# 1 method total continuing 
class Expense():
    """A class that stores each expense's data for the week"""
    def __init__(self, date, expense, category):
        """
        Initializes the Expense object
        
        Params:
        - date (str): the date of expense.
        - expense (float): the dollar amount of expense.
        - category (str): the category of the expense.
        """
        self.expense = expense
        self.date = float(date)
        self.category = category
             

# 2 methods total continuing       
class Create_expenses():
    """A class that creates and Stores all expenses"""
    def __init__(self, date, expense, category):
        """
         Initializes the CreateExpenses object.

        Params:
        - date (str): the date of expense.
        - expense (float): the dollar amount of expense.
        - category (str): the category of the expense.
        """
        self.expense_list = []
        
        self.expense_list.append(Expense(date, expense, category))


# 4 methods total continuing 
class Results:   
    """A class that organizes the expense entries and calculates the expense total"""            
    def organize_days():
        """
        Organizes the expense entries based on the days of the week.

        Returns:
        - list: a list of the expense entries.
        """
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        if Create_expenses.expense_list > 1:
            sorted(Create_expenses.expense_list[0], key = days.index)
        return Create_expenses.expense_list
    
    def calculate_total_week():
        """
        Calculates the total expenses for the week.

        Returns:
        - float: The total expenses for the week.
        """
        total = 0
        
        if Create_expenses.expense_list > 1:
            for expense in Create_expenses.expense_list[1]:
                total += expense
                return total    
            
    def calculate_category_total(expense_list):
        category_totals = {}
        for expense in expense_list:
            category = expense.category
            category_totals[category] = category_totals.get(category, 0) + expense.expense
        return category_totals


            

# 7 methods total continuing    
class Display: 
    "A class that prints user directions for the program."   
    def printMenu():
        """Prints the menu options"""
        print("Please choose from one of the following options (1, 2, 3):")
        print("1. Add A New Expense")
        print("2. Remove an Expense")
        print("3. List All Expenses and total budget for the week")

    def listExpenses():
        """Lists all the expenses for the week"""
        print("Here is a list of your expenses for the week:")
        list = Results.organize_days()
        print(list)
        
    def removeExpense():
        """Removes an expense."""
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
            
            i = input("See category total expenses?(yes/no)")
            if i.lower() == "yes":
                category_totals = Results.calculate_category_total(Create_expenses.expense_list)
                print("Category Total Expenses: ")
                for category, total in category_totals.items():
                    print(f"{category}: ${total}")
        else:
             print("Invalid input. Please try again.")
             Display.printMenu()