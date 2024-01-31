"""
    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
"""
import sys

tup_list = ["14 17", "-8 -5", "26 29", "-20 -15", "12 15", "2 3",
            "-10 -7", "25 30", "2 4", "-21 -16", "13 18", "22 27",
            "-6 -3", "3 6", "-25 -14"]

tuples_list = []
for m_tuple in tup_list:
    tup = m_tuple.split()
    tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

def merge_tuples (tuples_list):
    """Merge the tuples"""        
    sort_list = [list(i) for i in sorted(tuples_list)]
    result = [sort_list.pop(0)]

    sort_iterator = 0
    result_iterator = 0
    while len(sort_list) >= 1:
        # Overlap, where second element ends after the first
        if (result[result_iterator][1] >= sort_list[sort_iterator][0] and
            sort_list[sort_iterator][1] >= result[result_iterator][1]):
            result[result_iterator][1] = sort_list[sort_iterator][1]
            del sort_list[sort_iterator]
        # Complete overlap, where first element completely envelops second element
        elif (result[result_iterator][1] >= sort_list[sort_iterator][1] and
            result[result_iterator][0] <= sort_list[sort_iterator][0]):
            del sort_list[sort_iterator]
        # Overlap, where second element starts before the first
        elif (result[result_iterator][0] >= sort_list[sort_iterator][0] and
            result[result_iterator][1] >= sort_list[sort_iterator][1]):
            result[result_iterator][0] = sort_list[sort_iterator][0]
            del sort_list[sort_iterator]
        # Complete overlap, where second element completely envelops first element
        elif (result[result_iterator][1] <= sort_list[sort_iterator][1] and
              result[result_iterator][0] >= sort_list[sort_iterator][0]):
            result[result_iterator] = sort_list[sort_iterator]
            del sort_list[sort_iterator]
        # No overlap at all
        else:
            result.append(sort_list[sort_iterator])
            result_iterator += 1
            del sort_list[sort_iterator]

    result = [tuple(i) for i in result]

    return result                                 

def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """
    result = merge_tuples(tuples_list)
    sort = result.copy()

    for i in range(len(sort) - 1):
        min_int = i
        for j in range(i + 1, len(sort)):
            if (max(sort[j]) - min(sort[j]) 
                < max(sort[min_int]) - min(sort[min_int])):
                min_int = j

        if min_int != i:
            temp = sort[i]
            sort[i], sort[min_int] = sort[min_int], temp

    return sort

def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = ["14 17", "-8 -5", "26 29", "-20 -15", "12 15", "2 3",
                "-10 -7", "25 30", "2 4", "-21 -16", "13 18", "22 27",
                "-6 -3", "3 6", "-25 -14"]
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    print(tuples_list)
    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
