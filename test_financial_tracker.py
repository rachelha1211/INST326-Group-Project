"""Test units for financial tracker."""
import financial_tracker
import unittest

tracker = financial_tracker


class Test(unittest.TestCase):
    def test_add(self):
        """Test adding as if the item added was a $100 
        food expense in the food category"""
        tracker.addExpense(100, "Food")
        temp = ""
        temp += "Here is a list of your expenses\n"
        temp += "--------------------------------\n"
        temp += "# 0 - $ 51.00 - shirt\n\n"
        temp += "# 1 - $ 30 - groceries\n\n"
        temp += "# 2 - $100 - Food"
        self.assertEqual(temp, tracker.listExpenses())

    def test_remove(self):
        """Remove the food expense created in the method above"""
        temp = ""
        temp += "Here is a list of your expenses\n"
        temp += "--------------------------------\n"
        temp += "# 0 - $ 51.00 - shirt\n\n"
        temp += "# 1 - $ 30 - groceries\n\n"
        self.assertEqual(temp, tracker.listExpenses())
