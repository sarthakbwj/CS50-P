from project import check_correct_args, select_stream, select_birthyear
import pytest

def test_check_correct_args():
    with pytest.raises(SystemExit):
        check_correct_args()


def test_select_stream():
    assert select_stream("Computer Science") == "Science"
    assert select_stream("Finance") == "Commerce"
    assert select_stream("History") == "Arts"


def test_select_year():
    assert select_birthyear(2005) == "Year 1"
    assert select_birthyear(2002) == "Year 4"
