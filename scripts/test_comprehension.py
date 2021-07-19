import pytest
import os

from bs4_to_csv import filter
from make_dir import create_dir
from mwd import normalize


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

def test_create_dir():
    parent = os.path.dirname(os.getcwd())
    path = os.path.join(parent, "Adam")
    assert create_dir("Adam") == path
    os.rmdir(path)

def test_normalize():
    phrase = "{bc}a round fruit with red, yellow, or green skin and firm white flesh "
    assert normalize(phrase) == "a round fruit with red, yellow, or green skin and firm white flesh "
