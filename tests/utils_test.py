
# this is the tests_utils.py file 

from app.utils import to_usd


def test_to_usd():
    assert to_usd(0.45555) == "$0.46"
    assert to_usd(12500.90) == "$12,500.90"