from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Eric", "Cartman") == "Cartman; Eric"
    assert make_full_name("Ken-ny", "McCormick") == "McCormick; Ken-ny"
    assert make_full_name("Kyle", "Broflovski") == "Broflovski; Kyle"
    assert make_full_name("Stan", "Marsh") == "Marsh; Stan"


def test_extract_family_name():
    assert extract_family_name("Cartman; Eric")
    assert extract_family_name("McCormick; Kenny")
    assert extract_family_name("Broflovski; Kyle")
    assert extract_family_name("Marsh; Stan")


def test_extract_given_name():
    assert extract_given_name("Cartman; Eric")
    assert extract_given_name("McCormick; Kenny")
    assert extract_given_name("Broflovski; Kyle")
    assert extract_given_name("Marsh; Stan")


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
