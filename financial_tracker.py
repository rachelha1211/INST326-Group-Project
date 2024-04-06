"""A personal financial tracker that will display total budget over the week"""

class Category():
    """A class for defining the name of a category
    
    Attributes:
        name (str): name of the category
    """
    def __init__(self, name):
        """Initializes category_name object
        
        Args: 
            name (str): see class documentation
        """
        self.category_name = name

expenses = []
        
def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

def printMenu():
    print("Please choose from one of the following options...")
    print("1. Add A New Expense")
    print("2. Remove an Expense")
    print("3. List All Expenses")

def listExpenses():
    print("\Here is a list of your expenses")
    print("--------------------------------")
    counter = 0 
    for expense in expenses:
        print("#", counter, "-", expense['amount'], "-", expense['category'])
