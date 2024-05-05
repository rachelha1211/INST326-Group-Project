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
        
class Test_Display():
    def test_printMenu(self, capsys):
        ft.Display.printMenu()
        captured = capsys.readouterr()
        assert "Please choose from one of the following options" in captured.out
    
    
    def test_listExpenses(self, capsys):
        expenses = [ft.Expense("Monday", 23, "Food"), ft.Expense("Wednesday", 10, "School")]
        ft.Display.listExpenses(expenses)
        captured = capsys.readouterr()
        assert "Monday" in captured.out
        assert "Food" in captured.out
        assert "Wednesday" in captured.out
        assert "School" in captured.out
    
    def test_removeExpense(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '0\n2\n')
        expenses = [ft.Expense("Monday", 23, "Food"), ft.Expense("Wednesday", 10, "School")]
        ft.Display.removeExpense(expenses)
        assert len(expenses) == 1
        assert expenses[0].date == "Wednesday"
        
class Test_main():
    def test_quit_program(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '4\n')
        with pytest.raises(SystemExit):
            ft.main()
            
class Test_invalid_inputs():
    def test_invalid_option(self, capsys, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'invalid\n4\n')
        ft.main()
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out

    def test_invalid_remove_input(self, capsys, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'a\n2\n')
        expenses = [ft.Expense("Monday", 23, "Food"), ft.Expense("Wednesday", 10, "School")]
        ft.Display.removeExpense(expenses)
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out