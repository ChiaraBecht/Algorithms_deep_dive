"""
__author__ = Chiara Becht
credits: Michelle Lawson
"""

def conduct_bubble_sort(data):
    """
    :params:
        data: list to be sorted
    :returns:
        data: sorted list
    """
    if type(data) == list:
        print(data)
        data_len = len(data)
        for i in range(data_len - 1): # skip last pass where we only look on the first element
            print("pass:", i)
            swap = {"yes": 0, "no": 0}
            for j in range(0, data_len - i - 1): # shortening the comparisons omitting the last elements that where sorted already
                print("j, j+1", j, j+1)
                print("list items", data[j], data[j+1])
                if data[j] > data[j+1]:
                    swap["yes"] += 1
                    data[j], data[j+1] = data[j+1], data[j]
                else:
                    swap["no"] += 1
            if swap["yes"] == 0:
                print(data)
                return data
        print(data)
        return data
    else:
        return "data must be of type list"

if __name__ == "__main__":
    test_list = [34, 12, 45, 32, 10, 6]
    sorted_list = conduct_bubble_sort(data=test_list)
    test_list_2 = [6, 8, 9, 10, 34]
    conduct_bubble_sort(test_list_2)
    test_list_3 = [20, 1, 19, 17, 2, 5, 18]
    conduct_bubble_sort(test_list_3)