import builtins
from calculator.repl import run_calculator


def test_exit(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_calculator()
    captured = capsys.readouterr()

    assert "Goodbye!" in captured.out


def test_invalid_operation(monkeypatch, capsys):
    inputs = iter(["bad", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_calculator()
    captured = capsys.readouterr()

    assert "Invalid operation" in captured.out


def test_add(monkeypatch, capsys):
    inputs = iter(["add", "2", "3", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_calculator()
    captured = capsys.readouterr()

    assert "Result: 5.0" in captured.out


def test_divide_by_zero(monkeypatch, capsys):
    inputs = iter(["div", "5", "0", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_calculator()
    captured = capsys.readouterr()

    assert "Division by zero" in captured.out


def test_invalid_number(monkeypatch, capsys):
    inputs = iter(["add", "a", "2", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_calculator()
    captured = capsys.readouterr()

    assert "Invalid number input" in captured.out
