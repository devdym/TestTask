import pytest
from ListMerge import ListMerge


def test_merge_ignore_excess_keys():
    ml = ListMerge()
    ml.klist_setter([1, 2, 3, 4, 5])
    ml.vlist_setter(['BMW', 'Toyota', 'Mitsubishi', 'Honda', 'Merc', 'MINI'])
    ml.merge()
    assert ml.res_getter() == {1: 'BMW', 2: 'Toyota', 3: 'Mitsubishi', 4: 'Honda', 5: 'Merc'}


def test_merge_fill_excess_value():
    ml = ListMerge()
    ml.klist_setter([1, 2, 3, 4, 5, 6, 7])
    ml.vlist_setter(['BMW', 'Toyota', 'Mitsubishi', 'Honda', 'Merc', 'MINI'])
    ml.merge()
    assert ml.res_getter() == {1: 'BMW', 2: 'Toyota', 3: 'Mitsubishi', 4: 'Honda', 5: 'Merc', 6: 'MINI', 7: 'None'}
