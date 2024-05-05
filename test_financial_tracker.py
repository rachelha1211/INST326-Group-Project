"""Test units for financial tracker."""
import pytest
import finance_trackerfinal as ft



class Test_create():
    #fail
    def test_expense(self):
        expense = ft.Create_expenses()
        expense.add_expense("Monday", 23, "Food")
        exlist = expense.get_expense_list(self)
        assert exlist == [ft.Expense("Monday", 23, "Food")]

class Test_Results():
    #fail
    def test_organize_days(self):
        sorted_list = ft.Results.organize_days([ft.Expense("Wednesday", 10, "School"), ft.Expense("Monday", 23, "Food")])
        assert sorted_list == [ft.Expense("Monday", 23, "Food"), ft.Expense("Wednesday", 10, "School")]
    
    #passed    
    def test_calculate_total_week(self):
        total = ft.Results.calculate_total_week([ft.Expense("Monday", 23, "Food"), ft.Expense("Wednesday", 10, "School")])
        assert total == 33
class TestCreateExpenses:
    #fail
    def test_add_expense():
        expense_tracker = ft.Create_expenses
        expense_tracker.add_expense("Monday", 23, "Food")
        exlist = expense_tracker.get_expense_list()
        assert len(exlist) == 3
        assert exlist[0] == ft.Expense("Monday", 23, "Food")
    #fail
    def test_get_expense_list():
        expense_tracker = ft.Create_expenses()
        expense_tracker.add_expense("Monday", 23, "Food")
        exlist = expense_tracker.get_expense_list()
        assert isinstance(exlist, list)
        