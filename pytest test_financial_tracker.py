"""Test units for financial tracker."""
import pytest
from finance_trackerfinal import Expense, Create_expenses, Results, Display
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
        
def sample_expenses():
    return [
        Expense("Monday", 50.0, "Food"),
        Expense("Tuesday", 30.0, "Transport"),
        Expense("Friday", 20.0, "Misc")
    ]
        
def test_add_expense(sample_expenses):
    create_expenses = Create_expenses()
    create_expenses.add_expense("Monday", 50.0, "Food")
    assert len(create_expenses.expense_list) == 1
    
def test_get_expense_list(sample_expenses):
    create_expenses = Create_expenses()
    create_expenses.expense_list = sample_expenses
    assert len(create_expenses.get_expense_list()) == 3
    
def test_organize_days(sample_expenses):
    sorted_list = Results.organize_days(sample_expenses)
    assert sorted_list[0].date == "Monday"
    assert sorted_list[1].date == "Tuesday"
    assert sorted_list[2].date == "Friday"
    
def test_calculate_total_week(sample_expenses):
    total = Results.calculate_total_week(sample_expenses)
    assert total == 100.0

def test_calculate_category_total(sample_expenses):
    category_totals = Results.calculate_category_total(sample_expenses)
    assert category_totals["Food"] == 50.0
    assert category_totals["Transport"] == 30.0
    assert category_totals["Misc"] == 20.0