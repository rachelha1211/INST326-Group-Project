"""Test units for financial tracker."""
import unittest
import finance_tracker_gui as ft


class Test_create(unittest.TestCase):
    def test_expense(self):
        """Test for creating an expense."""
        expense = ft.Create_expenses()
        expense.add_expense("Monday", 23, "Food")
        exlist = expense.get_expense_list()
        self.assertEqual(exlist[0].date, "Monday") 
        self.assertEqual(exlist[0].amount, 23) 
        self.assertEqual(exlist[0].category, "Food") 

class Test_Results(unittest.TestCase):
    def test_organize_days(self):
        """Test for accurately sorting expenses by day of the week."""
        expense_tracker = ft.Create_expenses()
        expense_one = ft.Expense("Wednesday", 10, "School")
        expense_tracker.add_expense(expense_one.date, expense_one.amount, expense_one.category)
        expense_two = ft.Expense("Monday", 23, "Food")
        expense_tracker.add_expense(expense_two.date, expense_two.amount, expense_two.category)
        list = expense_tracker.get_expense_list()
        sorted_list = ft.Results().organize_days(list)
        self.assertEqual(sorted_list[0].date, "Monday")
        self.assertEqual(sorted_list[0].amount, 23)
        self.assertEqual(sorted_list[0].category, "Food")
    
    def test_calculate_total_week(self):
        """Test for calculating the total amount of all expense amounts in the week."""
        expense_tracker = ft.Create_expenses()
        expense_one = ft.Expense("Wednesday", 10, "School")
        expense_tracker.add_expense(expense_one.date, expense_one.amount, expense_one.category)
        expense_two = ft.Expense("Monday", 23, "Food")
        expense_tracker.add_expense(expense_two.date, expense_two.amount, expense_two.category)
        #list = expense_tracker.get_expense_list()
        #total = ft.Results().calculate_total_week(expense_tracker.get_expense_list())
        total = ft.Results().calculate_total_week([expense_one, expense_two])
        self.assertEqual(total, 33)

class TestCreateExpenses(unittest.TestCase):
    def test_add_expense(self):
        """Test for adding inputted expense into list."""
        expense_tracker = ft.Create_expenses()
        expense_one = ft.Expense("Monday", 23, "Food")
        expense_tracker.add_expense(expense_one.date, expense_one.amount, expense_one.category)
        expense_two = ft.Expense("Wednesday", 10, "School")
        expense_tracker.add_expense(expense_two.date, expense_two.amount, expense_two.category)
        self.assertEqual(len(expense_tracker.get_expense_list()), 2)
        list = expense_tracker.get_expense_list()
        self.assertEqual(list[0].date, "Monday") 
        self.assertEqual(list[0].amount, 23) 
        self.assertEqual(list[0].category, "Food") 
        self.assertEqual(list[1].date, "Wednesday") 
        self.assertEqual(list[1].amount, 10) 
        self.assertEqual(list[1].category, "School") 
        # self.assertEqual(expense_tracker[0], ft.Expense("Monday", 23, "Food"))
        # self.assertEqual(expense_tracker[1], ft.Expense("Wednesday", 10, "School")) 

    def test_get_expense_list(self):
        """Test for ccreating list of expenses."""
        expense_tracker = ft.Create_expenses()
        expense_tracker.add_expense("Monday", 23, "Food")
        exlist = expense_tracker.get_expense_list()
        self.assertTrue(isinstance(exlist, list))

if __name__ == '__main__':
    unittest.main()
        