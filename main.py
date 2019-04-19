fl = 0


def merge_sort(array_unsorted):
    global fl
    new_list = []
    if len(array_unsorted) == 1:
        return array_unsorted
    elif len(array_unsorted) == 2:
        if array_unsorted[0] > array_unsorted[1]:
            fl += 1
            new_list.append(array_unsorted[1])
            new_list.append(array_unsorted[0])
        else:
            new_list.append(array_unsorted[0])
            new_list.append(array_unsorted[1])
        return new_list
    else:
        if len(array_unsorted) % 2 == 0:
            first_half = merge_sort(array_unsorted[:int(len(array_unsorted) / 2)])
        else:
            first_half = merge_sort(array_unsorted[:int(len(array_unsorted) / 2) + 1])
        second_half = merge_sort(array_unsorted[len(array_unsorted) - int(len(array_unsorted) / 2):])
        running = True
        while running:
            if len(first_half) != 0 and len(second_half) != 0:
                if first_half[0] <= second_half[0]:
                    new_list.append(first_half[0])
                    del first_half[0]
                else:
                    fl += len(first_half)
                    new_list.append(second_half[0])
                    del second_half[0]
            elif len(first_half) != 0 and len(second_half) == 0:
                # fl+=1
                new_list.append(first_half[0])
                del first_half[0]
            elif len(first_half) == 0 and len(second_half) != 0:
                # fl+=1
                new_list.append(second_half[0])
                del second_half[0]
            elif len(first_half) == 0 and len(second_half) == 0:
                break
        return new_list


if __name__ == "__main__":

    print("Press q to quit inserting values\n")
    unsorted_array = []
    i = 0
    while True:
        x = input("Input : ")
        if x == "q" or x == "Q":
            break
        else:
            try:
                unsorted_array.insert(i, int(x))
                print("Your input of ", x, "has been added")
                i += 1
            finally:
                print("Couldn't be added")

    if len(unsorted_array) == 0:
        print("\n\nNothing to sort")
        print("Goodbye human")
    else:
        print("Unsorted List : ", end="")
        print(unsorted_array)
        print(" Sorted  List : ", end="")
        print(merge_sort(unsorted_array))
        print("\nInversions Present : ", fl)
        print("\n\n  Goodbye Human")
