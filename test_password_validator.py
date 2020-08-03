import pytest
from PasswordValidator import PasswordValidator

valid_passwords = ['dSA43ds-.a', 'ddf43ds-.a', 'dSA43ds']
invalid_passwords = ['fdsgfdgDS*', 'fdsgfdgDS.', 'fdsgfdgDS.-']


@pytest.mark.parametrize("val_pass", valid_passwords)
def test_slow_validator_true(val_pass):
    vl = PasswordValidator()
    vl.slow_validator(val_pass)
    assert vl.isvalid is True

@pytest.mark.parametrize("val_pass", invalid_passwords)
def test_slow_validator_false(val_pass):
    vl = PasswordValidator()
    vl.slow_validator(val_pass)
    assert vl.isvalid is False

@pytest.mark.parametrize("val_pass", valid_passwords)
def test_fast_validator_true(val_pass):
    vl = PasswordValidator()
    vl.slow_validator(val_pass)
    assert vl.isvalid is True


@pytest.mark.parametrize("val_pass", invalid_passwords)
def test_fast_validator_false(val_pass):
    vl = PasswordValidator()
    vl.slow_validator(val_pass)
    assert vl.isvalid is False
