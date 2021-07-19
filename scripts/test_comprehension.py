import pytest
import os

from bs4_to_csv import filter, spacy_filter
from make_dir import create_dir
from mwd import normalize


def test_spacy_dn():
    assert str(spacy_filter("hadn")) == "had"

def test_spacy_nt():
    assert str(spacy_filter("wouldn't")) == "would"

def test_spacy_dn2():
    assert str(spacy_filter("hadn'")) == "had"

def test_filter_ve():
    assert str(spacy_filter("could've")) == "could"

def test_filter_empty():
    assert spacy_filter("") == None

def test_filter_starter():
    assert str(spacy_filter("A")) == "a"

def test_filter_plural2():
    assert str(spacy_filter("companies")) == "company"

def test_filter_Name():
    assert str(spacy_filter("Anna")) == ""

def test_filter_filtered():
    assert str(spacy_filter("pass")) == "pass"

def test_filter_plural():
    assert str(spacy_filter("cans")) == "can"

def test_filter_unicode():
    assert spacy_filter("askâ") == "ask"

def test_filter_plural():
    assert str(spacy_filter("cans")) == "can"

def test_filter_keep2():
    assert str(spacy_filter("had")) == "have"

def test_create_dir():
    parent = os.path.dirname(os.getcwd())
    path = os.path.join(parent, "Adam")
    assert create_dir("Adam") == path
    os.rmdir(path)

def test_normalize():
    phrase = "{bc}a round fruit with red, yellow, or green skin and firm white flesh "
    assert normalize(phrase) == "a round fruit with red, yellow, or green skin and firm white flesh "
