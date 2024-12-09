import pytest
from lab2 import addNewElement, deleteElement, updateElement

def test_addNewElement(monkeypatch):
    inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    test_list = []
    addNewElement(test_list)
    assert len(test_list) == 1
    assert test_list[0]["name"] == "Alice"

def test_deleteElement(monkeypatch):
    add_inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(add_inputs))

    test_list = []
    addNewElement(test_list)
    
    # Перевірка, що елемент доданий правильно
    assert len(test_list) == 1
    assert test_list[0]["name"] == "Alice"
    
    # Імітація вводу користувача для видалення елемента
    delete_inputs = iter(["Alice"])
    monkeypatch.setattr('builtins.input', lambda _: next(delete_inputs))

    deleteElement(test_list)
    
    assert len(test_list) == 0



def test_updateElement(monkeypatch):
    inputs = iter(["Alice", "0639998888", "alice_new@example.com", "321 New Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    test_list = []
    addNewElement(test_list)

    assert len(test_list) == 1
    assert test_list[0]["name"] == "Alice"

    update_inputs = iter(["Alice", "123", "007", "1000"])
    monkeypatch.setattr('builtins.input', lambda _: next(update_inputs))

    updateElement(test_list)

    assert test_list[0]["phone"] == "123"
    assert test_list[0]["email"] == "007"
    assert test_list[0]["address"] == "1000"
