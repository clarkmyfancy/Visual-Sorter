from Sorter import Sorter

_list = [7,2,6,12,7,1,3,7]

def main():
    s = Sorter(_list)
    # this is not good because the sort algorithm sorts 'in-place' which changes the 
    # list. the class should have a static list member that is used. when a new sort 
    # algorigm is used the sort function should copy the static list over to a mutatable list
    # and use and eventually return that to the console
    sortedList = s.runSelectionSortIteratively()
    print(sortedList)
    diffMethodSortedList = s.runSelectionSortRecursively()
    print(diffMethodSortedList)
    

if __name__ == "__main__":
    main()