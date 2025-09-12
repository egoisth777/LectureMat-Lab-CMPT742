# Function to merge two sorted lists into one sorted list
def merge_sorted_lists(list1, list2):
    # TODO: Implement the merging logic
    merged_list = []
    ind1, ind2 = 0, 0
    while ind1 < len(list1) or ind2 < len(list2):
        if ind1 < len(list1):
            a = list1[ind1]
        else:
            a = 1e10
        if ind2 < len(list2):
            b = list2[ind2]
        else:
            b = 1e10

        if a < b:
            merged_list.append(a)
            ind1 += 1
        else:
            merged_list.append(b)
            ind2 += 1
    return merged_list


# Define main function
def main():
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    print(merge_sorted_lists(list1, list2))  #


if __name__ == "__main__":
    main()