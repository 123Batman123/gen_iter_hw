class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cursor_1 = 0
        self.cursor_2 = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor_2 != len(self.list_of_list[self.cursor_1])-1:
            self.cursor_2 += 1
        else:
            self.cursor_1 += 1
            self.cursor_2 = 0

        if self.cursor_1 == len(self.list_of_list):
            raise StopIteration
        self.item = self.list_of_list[self.cursor_1][self.cursor_2]
        return self.item


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
