"""A personal financial tracker that will display total budget over the week"""

from tkinter import *
from tkinter import ttk
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
    def organize_days(self, expense_list):
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
    
    def calculate_total_week(self, sorted_list):
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
            
    def calculate_category_total(self, sorted_list):
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
    # def printMenu():
    #     pass

    def listExpenses(self, root, sorted_list):
        """Lists all the expenses for the week
        
        Args: 
            sorted_list (list): list of expense entries
        """
        
        root.title("Here is a list of your expenses for the week:")
        
        for counter in range(0, len(sorted_list)):
            expense_text = f"#{counter} - day: {sorted_list[counter].date} - ${sorted_list[counter].amount} - category: {sorted_list[counter].category}\n"
            list_lbl = Label(root, text=expense_text)
            list_lbl.grid(row = counter + 1, column = 0, sticky=W)


    def removeExpense(self, root, sorted_list):
        """Removes an expense
        
        Args:
            sorted_list (list): list of expense entries
            
        Raises:
            ValueError: invalid user input
            IndexError: index is out of range
        
        Side effects:
            deletes value in sorted_list
        """

        def deletion():
            try:
                input_text = input_entry.get()
                input_int = int(input_text)
                del sorted_list[input_int]
                root.destroy()
            except ValueError:
                err_lbl = Label(root, text=f"Invalid input{int(input_entry.get())}")
                err_lbl.grid()
            except IndexError:
                err_lbl = Label(root, text="Index out of range")
                err_lbl.grid()

        self.listExpenses(root, sorted_list)
            
        prompt_lbl = Label(root, text = "Please select an expense # to remove\n")
        prompt_lbl.grid()
            
        input_entry = Entry(root, width = 10)
        input_entry.grid()


        enter_btn = Button(root, text = "Enter", fg = "black", command = deletion)
        enter_btn.grid()



class UI():
    """A class to create a GUI for the finance tracker"""
    def gui(self):
        """Creates the main GUI window using Tkinter with buttons for adding, removing, & listing expenses, & quitting the menu

        Side Effects:
            Creates a root window for the user options to be displayed from and entered into.
        """
        
        root = Tk()
        root.title("Welcome to the Financial Tracker")
        root.geometry('700x400')

        #list the possible options the user can do from the home screen
        btn1 = Button(root, text = "1. Add A New Expense", fg = "black", command = self.add_expense)
        btn1.grid(column=10, row = 5)
        btn2 = Button(root, text = "2. Remove an Expense", fg = "black", command = self.remove_expense)
        btn2.grid(column=10, row = 8)
        btn3 = Button(root, text = "3. List All Expenses and total budget for the week", fg = "black", command = self.list_expenses)
        btn3.grid(column=10, row = 11)
        btn4 = Button(root, text = "4. Quit Menu", fg = "black", command = quit)
        btn4.grid(column=10, row = 14)


        lbl = Label(root, text = "Please choose from one of the following options (1, 2, 3, 4):")

        root.mainloop()

    def add_expense(self):
        """Adds a new expense to the finance tracker in a new window where user can input expense details (date, amount, category)
        """
        def check_entry():
            """Make sure the user's entry is of the correct variable type. If it is, save the new entry and go back to the main window.
            
            Side Effects:
                Appends the new expense to the new_expense_list object if the entries pass the check"""
            amount = amount_txt.get()
            date = date_txt.get()
            category = category_txt.get()
            try:
                amount_float = float(amount)
                new_expense_list.add_expense(date, amount_float, category)
                root.destroy()
            except ValueError:
                err_lbl = Label(root, text="Invalid input")
                err_lbl.grid()

        root = Tk()
        root.title("Enter expense information")
        root.geometry('700x400')

        date_lbl = Label(root, text = "Enter a day (Monday, Tuesday, ...)")
        date_lbl.grid()
        date_txt = Entry(root, width = 20)
        date_txt.grid(column = 1, row = 2)
        
        amount_lbl = Label(root, text = "Enter expense amount: ")
        amount_lbl.grid()
        amount_txt = Entry(root, width = 20)
        amount_txt.grid(column = 1, row = 5)

        category_lbl = Label(root, text = "Enter category (Food, Housing, Transport, School, Misc:): ")
        category_lbl.grid()
        category_txt = Entry(root, width = 20)
        category_txt.grid(column = 1, row = 8)

        confirm_btn = Button(root, text = "Enter", fg = "black", command = check_entry)
        confirm_btn.grid(column = 0, row = 12)

        root.mainloop()



    def remove_expense(self):
        """Removes an existing expense from the finance tracker in a window that displays the list of 
        expenses & provides user the choice of which expense to remove

        Side Effects:
            remove the given expense from the list
        """
        root = Tk()
        root.title("Pick an expense to remove")
        root.geometry('700x400')


        Display.removeExpense(Display(), root, new_expense_list.get_expense_list())


    def list_expenses(self):
        """Lists all expenses (with option to show category totals) in a window
        """
        root = Tk()
        root.title("Here are your expenses:")
        root.geometry('700x400')

        def category_totals():
            """if the user wants to see category totals - display them
            
            Side Effects:
                Once the user pushes no the root is destroyed and the user is returned to the home screen.
                If the user pushes yes a categoried list of expenses is displayed """
            see_totals = category_txt.get()
            if see_totals.lower() == "no":
                root.destroy()
            else:
                category_totals = Results.calculate_category_total(Results(), result)
                for category, total in category_totals.items():
                    category_lbl = Label(root, text = f"Category: {category}, Total: {total}")
                    category_lbl.grid()


        try:
            result = Results.organize_days(Results(), new_expense_list.get_expense_list())
            Display.listExpenses(Display(), root, result)            

            category_lbl = Label(root, text = "Would you like to see the category totals for the week? (yes/no)")
            category_lbl.grid()
            category_txt = Entry(root, width = 10)
            category_txt.grid()

            i = category_txt.get()

            enter_btn = Button(root, text = "Enter", fg = "black", command = category_totals)
            enter_btn.grid()

            if i.lower() == "yes":
                category_totals()


        except ValueError:
            print("Nothing in the list")

            
new_expense_list = Create_expenses()

def main():
    """Creates a new UI object which can call the gui method to create the home screen"""
    main_window = UI()
    main_window.gui()

if __name__ == "__main__":
    main()