import pytest

from bs4_to_csv import filter

def test_filter_ied():
    assert filter("tried") == "try"

def test_filter_empty():
    assert filter("") == ""

def test_filter_Starter():
    assert filter("A") == "A"

def test_filter_Name():
    assert filter("Anna") == ""

def test_filter_dn():
    assert filter("hadn") == "had"

def test_filter_nt():
    assert filter("wouldn't") == "would"

def test_filter_dn2():
    assert filter("hadn'") == "had"

def test_filter_filtered():
    assert filter("pass") == "pass"

def test_filter_plural():
    assert filter("cans") == "can"

def test_filter_ve():
    assert filter("could've") == "could"

def test_filter_unicode():
    assert filter("askâ") == "ask"

def test_filter_keep2():
    assert filter("had") == "had"
