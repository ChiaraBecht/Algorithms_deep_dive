"""
__author__ = Chiara
credits: Michelle Lawson
"""

def conduct_merge_sort(data):
    # dividing
    if len(data) > 1:
        # find middle index
        middle_index = len(data) // 2

        # split list
        left_list = data[:middle_index]
        right_list = data[middle_index:]

        # recursively sort the left and right halves:
        conduct_merge_sort(left_list)
        conduct_merge_sort(right_list)

        # merge sorted halves back
        merged_list = merging(left=left_list, right=right_list)

        for i in range(len(data)):
            data[i] = merged_list[i]
    
        return merged_list


def merging(left, right):

    #left and right are sorted lists
    
    result = []
    i = 0
    j = 0

    # while there are elements in both sublists:
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j+=1
    
    return result


if __name__ == "__main__":
    res = merging(left=[2, 3, 5], right=[1, 4, 6])
    print(res)

    # try merge_sort
    unsorted = [6, 4, 5, 1, 2, 3]
    sorted = conduct_merge_sort(unsorted)
    print(sorted)