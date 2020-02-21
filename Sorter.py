class Sorter:

    def __init__(self, _list):
        self._list = _list

    def runSelectionSortIteratively(self):
        startIndexOfUnsortedList = 0
        for x in range(startIndexOfUnsortedList, len(self._list)):
            smallestVal = self._list[x]
            smallestValIndex = -1
            smallestValWasChanged = False
            for y in range(startIndexOfUnsortedList + 1, len(self._list)):
                if self._list[y] < smallestVal:
                    smallestVal = self._list[y]
                    smallestValWasChanged = True
                    smallestValIndex = y
            if smallestValWasChanged:
                tempValue = self._list[x]
                self._list[x] = smallestVal
                self._list[smallestValIndex] = tempValue
            startIndexOfUnsortedList += 1
        return self._list

    def runSelectionSortRecursively(self):
        smallestVal = self._list[0]

        return self._list