import pytest
from working import convert  

def test_valid_time_with_minutes():
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("12:15 PM to 3:45 PM") == "12:15 to 15:45"
    assert convert("11:30 AM to 12:30 PM") == "11:30 to 12:30"
    assert convert("12:45 AM to 2:00 AM") == "00:45 to 02:00"

def test_valid_time_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 3 PM") == "12:00 to 15:00"
    assert convert("12 AM to 1 AM") == "00:00 to 01:00"

def test_edge_cases():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Invalid separator
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # Invalid hour
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  # Invalid minute
    with pytest.raises(ValueError):
        convert("9 AM to 5")  # Missing AM/PM
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")  # Missing AM/PM

