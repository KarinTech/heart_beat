from address import extract_city, extract_state, extract_zipcode
import pytest


def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("456, White Finch St, North Augusta, SC 29860") == "North Augusta"
    assert extract_city("85, Bradford Lane, Vincentown, NJ 08120") == "Vincentown"


def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("456, White Finch St, North Augusta, SC 29860") == "SC"
    assert extract_state("85, Bradford Lane, Vincentown, NJ 08120") == "NJ"


def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("456, White Finch St, North Augusta, SC 29860") == "29860"
    assert extract_zipcode("85, Bradford Lane, Vincentown, NJ 08120") == "08120"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
