"""
    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
"""
import sys

# tup_list = ["14 17", "-8 -5", "26 29", "-20 -15", "12 15", "2 3",
#             "-10 -7", "25 30", "2 4", "-21 -16", "13 18", "22 27",
#             "-6 -3", "3 6", "-25 -14"]

tup_list = ["14 17", "12 15", "10 20"]

tuples_list = []
for m_tuple in tup_list:
    tup = m_tuple.split()
    tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

# print(tuples_list)

def merge_tuples (tuples_list):
    """Merge the tuples"""
    tuple_merged = []
    for i in range(len(tuples_list) - 1):
        for j in range(i + 1, len(tuples_list)):
            if (tuples_list[i][0] > tuples_list[j][0]):
                    pass

    return tuple_merged # Replace this 

print(merge_tuples(tuples_list))

def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """

    # Add Your Code HERE ... AND REMOVE THIS Line

    return None # Replace this.



def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    # sys.stdin.readline()

    tup_list = ["14 17", "-8 -5", "26 29", "-20 -15", "12 15", "2 3",
                "-10 -7", "25 30", "2 4", "-21 -16", "13 18", "22 27",
                "-6 -3", "3 6", "-25 -14"]
    # tup_list = sys.stdin.readlines()

    # Editing this for now just to manually input tuple pairs
    # tuples_list = []
    # for m_tuple in tup_list:
    #     tup = m_tuple.split()
    #     tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # print(tuples_list)
    # merge the list of tuples
    # merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    # sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    # print(merged)
    # print(sorted_merge)

if __name__ == "__main__":
    main()
