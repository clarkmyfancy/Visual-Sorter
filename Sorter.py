from ListGenerator import Generator

class Sorter:
    def __init__(self):
        self.list_factory = Generator(20, 10)

    def sort(self, choice):
        if choice == 'rs':
            return self.recursive_selection_sort()
        elif choice == 'is':
            return self.iterative_selection_sort()

    def recursive_selection_sort(self):
        _list = self.list_factory.generate_random_list()
        print()
        print(_list)
        startIndexOfUnsortedList = 0
        for x in range(startIndexOfUnsortedList, len(_list)):
            smallestVal = _list[x]
            smallestValIndex = -1
            smallestValWasChanged = False
            for y in range(startIndexOfUnsortedList + 1, len(_list)):
                if _list[y] < smallestVal:
                    smallestVal = _list[y]
                    smallestValWasChanged = True
                    smallestValIndex = y
            if smallestValWasChanged:
                tempValue = _list[x]
                _list[x] = smallestVal
                _list[smallestValIndex] = tempValue
            startIndexOfUnsortedList += 1
        return _list

    def iterative_selection_sort(self):
        _list = self.list_factory.generate_random_list()
        print()
        print(_list)
        self.s_sort(_list)
        return _list

    def s_sort(self, _list, first = 0):
        length = len(_list)
        if first == length:
            return -1
        candidate_smallest = self.findMinIndex(_list, first, length - 1)
        if candidate_smallest != first:
            _list[candidate_smallest], _list[first] = _list[first], _list[candidate_smallest]
        return self.s_sort(_list, first + 1)

    def findMinIndex(self, _list, first, last):
        if first == last:
            return first
        smallest_index = self.findMinIndex(_list, first + 1, last)
        return first if _list[first] < _list[smallest_index] else smallest_index