class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list

    def __iter__(self):
        self.index = 0
        self.index_index = 0

        return self

    def __next__(self):
        if self.index == len(self.list_of_lists):
            raise StopIteration
        a_list = self.list_of_lists[self.index]
        a_value = a_list[self.index_index]
        self.index_index += 1
        if len(a_list) == self.index_index:
            self.index += 1
            self.index_index = 0
        return a_value


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()