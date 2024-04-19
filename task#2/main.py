import types


def flat_generator(list_of_lists):
    index = 0
    while index < len(list_of_lists):
        index_index = 0
        a_list = list_of_lists[index]
        while index_index < len(a_list):
            a_value = a_list[index_index]
            yield a_value
            index_index += 1
        index += 1


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    print(list(flat_generator(list_of_lists_1)))

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
