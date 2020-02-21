from Sorter import Sorter

def main():
    s = Sorter()

    print("Recursive List", end = "")
    recursive_selection_sort = s.sort("rs")
    print(recursive_selection_sort)
    print()

    print("Iterative List", end = "")
    iterative_selection_sort = s.sort("is")
    print(iterative_selection_sort)
    print()
    
if __name__ == "__main__":
    main()