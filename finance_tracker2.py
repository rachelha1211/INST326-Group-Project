"""A personal financial tracker that will display total budget over the week"""

 
from typing import Any

class Expense():
    """A class that stores each expense's data for the week"""
    def __init__(self, date, amount, category):
        """
        Initializes the Expense object
        
        Args:
        - date (str): the date of expense.
        - amount (float): the dollar amount of expense.
        - category (str): the category of the expense.
        """
        self.amount = amount
        self.date = date
        self.category = category
                 
      
class Create_expenses():
    expense_list = []
    """A class that creates and stores all expenses"""
    def __init__(self):
        """
         Initializes the Create_expenses object.
        """ 
    
    def add_expense(self, date, amount, category):
        """add a new expense to the expense list
        
        Args:
            - date(str): the date of the new expense
            - amount(float): the amount of the new expense
            - category(str): the category of the new expense
            
        Side effects:
            modifies the value of expense_list
        """
        self.expense_list.append(Expense(date, float(amount), category))

    def get_expense_list(self):
        """return the expense_list of the classes instance
        
        Returns:
            expense_list (list): the list of expenses added by the user
        """
        return self.expense_list
        

class Results():   
    """A class that organizes the expense entries and calculates the expense total"""    
    def organize_days(expense_list):
        """Organizes the expense entries based on the days of the week.
        
        Args:
            expense_list (list): list of expenses added by the user
            
        Side effects:
            modifies value of sorted_list

        Returns:
            sorted_list (list): a list of the expense entries.
        """
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        sorted_list = []
        if len(expense_list) >= 1:
            sorted_list = sorted(expense_list, key = lambda expense: days.index(expense.date))
        return sorted_list
    
    def calculate_total_week(sorted_list):
        """
        Calculates the total expenses for the week.

        Args:
            sorted_list (list): list of the expense entries
            
        Returns:
            float: The total expenses for the week.
        """
        total = 0
        
        if len(sorted_list) >= 1:
            for expense in sorted_list:
                
                total += expense.amount
            return total    
            
    def calculate_category_total(sorted_list):
        """Calculates the total expenses for a category
        
        Args:
            sorted_list (list): list of the expense entries
        
        Returns:
            dict: A dictionary where the keys are categories and values are total expenses
        """
        category_totals = {}
        for expense in sorted_list:
            category = expense.category
            amount = expense.amount
            category_totals[category] = category_totals.get(category, 0) + amount
        return category_totals

   
class Display(): 
    "A class that prints user directions for the program."   
    def printMenu():
        """Prints the menu options"""
        print("Please choose from one of the following options (1, 2, 3, 4):")
        print("1. Add A New Expense")
        print("2. Remove an Expense")
        print("3. List All Expenses and total budget for the week")
        print("4. Quit Menu")

    def listExpenses(sorted_list):
        """Lists all the expenses for the week
        
        Args: 
            sorted_list (list): list of expense entries
        """
        print("Here is a list of your expenses for the week:")
        print("--------------------------------")
        counter = 0
        for expense in sorted_list:
            print("#", counter, "-","day:", expense.date, "-","$", expense.amount, "-","category:", expense.category)
            counter += 1
        print("\n\n")
        
    def removeExpense(sorted_list):
        """Removes an expense
        
        Args:
            sorted_list (list): list of expense entries
            
        Raises:
            ValueError: invalid user input
            IndexError: index is out of range
        
        Side effects:
            deletes value in sorted_list
        """
        more_expenses = 1

        while ((more_expenses == 1) and (len(sorted_list) > 0)):
            Display.listExpenses(sorted_list)
            print("What expense would you like to remove? (specific #):")
            
            try:
                expenseToRemove = int(input(">"))
                del sorted_list[expenseToRemove]
                print("Expense deleted")
                print("Would you like to delete another expense?\n1. yes\n2. no\nEnter 1 or 2")
                more_expenses = int(input(">"))
            except (ValueError, IndexError):
                print("Invalid input. Please try again.") 
            
            
new_expense_list = Create_expenses()
def main():
    """Initiates options on menu
    
    Raises:
        ValueError: empty list
    """
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
                new_expense_list.add_expense(date, amount, category)
                break
                
        elif(optionSelected == '2'):
            Display.removeExpense(new_expense_list.get_expense_list())
            break
            
        elif(optionSelected == '3'):
            try:
                result = Results.organize_days(new_expense_list.get_expense_list())
                Display.listExpenses(result)
                print(f"Total amount spent for this week: {Results.calculate_total_week(result)}")
                
                i = input("See category total expenses?(yes/no)")
                if i.lower() == "yes":
                    category_totals = Results.calculate_category_total(result)
                    print("Category Total Expenses: ")
                    for category, total in category_totals.items():
                        print(f"{category}: ${total}")
            except ValueError:
                print("Nothing in the list")
                break
                
        elif(optionSelected == '4'):
            quit()
            
        else:
             print("Invalid input. Please try again.")
             Display.printMenu()
        
        print("\n")
        main()

if __name__ == "__main__":
    main()