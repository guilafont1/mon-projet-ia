import pytest
from predict import predict_message

def test_spam():
    assert predict_message("Win a free ticket now!!!") == "Spam"

def test_ham():
    assert predict_message("Hey, are we still meeting today?") == "Ham"

def test_empty():
    assert predict_message("") in ["Spam", "Ham"]

def test_special_characters():
    assert predict_message("$$$!!!***") in ["Spam", "Ham"]
