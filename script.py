from Sorter import Sorter

_list = [7,2,6,12,7,1,3,7]

def main():
    sorter = Sorter(_list)
    sortedList = sorter.runSelectionSortIter()
    print(sortedList)
    

if __name__ == "__main__":
    main()