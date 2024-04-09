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

expense1 = {'amount': '51.00', 'category': 'shirt'}
expenses.append(expense1)
expense2 = {'amount': '30', 'category': 'groceries'}
expenses.append(expense2)


    
def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input(">"))
            del expenses[expenseToRemove]
            print("Expense deleted")
        except:
            print("Invalid input. Please try again.")
       
def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

def printMenu():
    print("Please choose from one of the following options...")
    print("1. Add A New Expense")
    print("2. Remove an Expense")
    print("3. List All Expenses")
    

def listExpenses():
    print("Here is a list of your expenses")
    print("--------------------------------")
    counter = 0 
    for expense in expenses:
        print("#", counter, "-","$", expense['amount'], "-", expense['category'])
        counter += 1
    print("\n\n")

if __name__ == "__main__":
    while True:
        ###Prompt the user
        printMenu()
        optionSelected = input(">")
        
        if (optionSelected == "1"):
            print("How much was this expense?")
            while True:
                try:
                    amountToAdd = input("> ")
                    break
                except:
                     print("Invalid input. Please try again.")
            
            print("What category was this expense?")
            while True:
                try:
                    category = input("> ")
                    break
                except:
                     print("Invalid input. Please try again.")
            addExpense(amountToAdd, category)
        elif(optionSelected == '2'):
            removeExpense()
        elif(optionSelected == '3'):
            listExpenses()
        else:
             print("Invalid input. Please try again.")