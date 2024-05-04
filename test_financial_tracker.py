"""Test units for financial tracker."""
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
        
class Test_Display():
    def test_list():
        ft.Display.listExpenses([ft.Expense("Monday", 23, "Food"), ft.Expense("Wednesday", 10, "School")])
        
    def test_removeExpense(self):
        expense_list = [ft.Expense("Monday", 23, "Food"), ft.Expense("Wednesday", 10, "School")]
        ft.Display.removeExpense(expense_list)
        assert len(expense_list == 1)
        
class Test_main():
    def test_invalid_input(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "abc")
        ft.main
        captured = capsys.readouterr()
        assert "invalid input" in captured.out