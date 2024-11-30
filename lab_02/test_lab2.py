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
    inputs = iter(["Alice"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    test_list = [{"name": "Alice", "phone": "0631112222", "email": "alice@example.com", "address": "321 Cedar St"}]
    deleteElement(test_list)
    assert len(test_list) == 0

def test_updateElement(monkeypatch):
    inputs = iter(["Alice", "0639998888", "alice_new@example.com", "321 New Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    test_list = [{"name": "Alice", "phone": "0631112222", "email": "alice@example.com", "address": "321 Cedar St"}]
    updateElement(test_list)
    assert test_list[0]["phone"] == "0639998888"
    assert test_list[0]["email"] == "alice_new@example.com"
    assert test_list[0]["address"] == "321 New Cedar St"
