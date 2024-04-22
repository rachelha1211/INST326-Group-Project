"""A personal financial tracker that will display total budget over the week"""

# 1 method total continuing 
class Expense():
    """A class that stores each expense's data for the week"""
    def __init__(self, date, amount, category):
        """
        Initializes the Expense object
        
        Params:
        - date (str): the date of expense.
        - expense (float): the dollar amount of expense.
        - category (str): the category of the expense.
        """
        self.amount = amount
        self.date = date
        self.category = category
                 

# 2 methods total continuing       
class Create_expenses():
    """A class that creates and Stores all expenses"""
    def __init__(self, date, amount, category):
        """
         Initializes the CreateExpenses object.

        Params:
        - date (str): the date of expense.
        - amount (float): the dollar amount of expense.
        - category (str): the category of the expense.
        """
        self.expense_list = []
        
        self.expense_list.append(Expense(date, float(amount), category))


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
        
        if len(Create_expenses.expense_list) > 1:
            sorted_list = sorted(Create_expenses.expense_list[0], key = days.index)
        return sorted_list
    
    def calculate_total_week(sorted_list):
        """
        Calculates the total expenses for the week.

        Returns:
        - float: The total expenses for the week.
        """
        total = 0
        
        if sorted_list >= 1:
            for expense in sorted_list:
                total += expense
                return total    
            
    def calculate_category_total(sorted_list):
        """
        Calculates the total expenses for a category
        
        Returns:
        - dict: A dictionary where the keys are categories and values are total expenses
        """
        category_totals = {}
        for expense in sorted_list[2]:
            category = expense
            category_totals[category] = category_totals.get(category, 0) + sorted_list[1]
        return category_totals


# 7 methods total continuing    
class Display: 
    "A class that prints user directions for the program."   
    def printMenu():
        """Prints the menu options"""
        print("Please choose from one of the following options (1, 2, 3, 4):")
        print("1. Add A New Expense")
        print("2. Remove an Expense")
        print("3. List All Expenses and total budget for the week")
        print("4. Quit Menu")

    def listExpenses():
        """Lists all the expenses for the week"""
        print("Here is a list of your expenses for the week:")
        print("--------------------------------")
        counter = 0
        for expense in Results.organize_days:
            print("#", counter, "-","day", expense[0], "-","$", expense[1], "-","category", expense[2])
            counter += 1
        print("\n\n")
        
    def removeExpense():
        """Removes an expense."""
        while True:
            Display.listExpenses()
            amount = print("What expense would you like to remove? (specific date, amount, category):")
            
            for expense in Results.organize_days:
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
            print("Enter the date (Monday, Tuesday...): ")
            while True:
                try:
                    date = input(">")
                    break
                except:
                     print("Invalid input. Please try again.")
            
            print("Enter expense amount: ")
            while True:
                try:
                    amount = input("> ")
                    break
                except:
                     print("Invalid input. Please try again.")
                     
            print("Enter category (Food, Housing, Transport, School, Misc:): ")
            while True:
                try:
                    category = input(">")
                except:
                    print("Invalid input. Please try again.")
            
                Create_expenses(date, amount, category)
                break
                
        elif(optionSelected == '2'):
            Display.removeExpense()
            print("Expense has been removed")
            break
            
        elif(optionSelected == '3'):
            try:
                result = Results.organize_days()
                if len(result) >= 1:
                    Display.listExpenses()
                    print(f"Total amount spent for this week: {result.calculate_total_week()}")
                    
                    i = input("See category total expenses?(yes/no)")
                    if i.lower() == "yes":
                        category_totals = Results.calculate_category_total(Create_expenses.expense_list)
                        print("Category Total Expenses: ")
                        for category, total in category_totals.items():
                            print(f"{category}: ${total}")
            except ValueError:
                print("ValueError, list is empty")
                break
                
        elif(optionSelected == '4'):
            quit()
            
        else:
             print("Invalid input. Please try again.")
             Display.printMenu()