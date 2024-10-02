import pytest
from numb3rs import validate

def test_validate_numbers():
    assert validate("255.255.255.255") == True
    assert validate("300.300.300.300") == False
    assert validate("150.300.150.150") == False
    assert validate("100.100.350.100") == False
    assert validate("125.1.2.300") == False

def test_validate_letters():
    assert validate("aaa.aa.aa.a") == False

def test_validate_str():
    assert validate("Hello, world") == False

def test_validate_char():
    assert validate("152.152.152.!!!") == False