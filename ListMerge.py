# 1. There are two lists of different lengths. The first contains keys, and the second contains values.
# Write a function that creates a dictionary from these keys and values.
# If the key did not have enough values, the dictionary should have the value None.
# Values that did not have enough keys should be ignored.
# Write a tests using unittest/pytest.

import logging

# key_list = [1, 2, 3, 4, 5, 6, 7]
key_list = [1, 2, 3, 4, 5]
value_list = ['BMW', 'Toyota', 'Mitsubishi', 'Honda', 'Merc', 'MINI']

logging.basicConfig(level=logging.DEBUG)


class ListMerge:

    def __init__(self):
        self.vlist = []
        self.klist = []
        self.res = {}

    def vlist_setter(self, mylist):
        self.vlist = mylist

    def klist_setter(self, mylist):
        self.klist = mylist

    def res_getter(self):
        return self.res

    def merge_ignore_excess_keys(self):
        while self.vlist:
            self.res.update({self.klist.pop(0): self.vlist.pop(0)})
        while self.klist:
            self.res.update({self.klist.pop(0): 'None'})

        return self.res

    def merge_fill_excess_value(self):
        while self.klist:
            self.res.update({self.klist.pop(0): self.vlist.pop(0)})

        return self.res

    def merge(self):
        if len(self.klist) > len(self.vlist):
            logging.debug('key_list is longer')
            self.merge_ignore_excess_keys()
            logging.debug(self.res_getter())
        else:
            logging.debug('value_list is longer')
            self.merge_fill_excess_value()
            logging.debug(self.res_getter())


def main():
    ml = ListMerge()
    ml.vlist_setter(value_list)
    ml.klist_setter(key_list)
    ml.merge()
    print(ml.res_getter())


if __name__ == "__main__":
    main()
