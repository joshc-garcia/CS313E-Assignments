"""
    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
"""
import sys

tup_list = ["14 17", "15 -5", "26 29", "-20 -15", "12 15", "2 3",
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

    # print(result[result_iterator][1])
    # print(sort_list[sort_iterator][1] - 1)

    # print(result[result_iterator][1] == (sort_list[sort_iterator][0] - 1))

    # print(sort_list[sort_iterator][0])
    # print(sort_list[sort_iterator][1])

    # print(result[result_iterator][0])
    # print(result[result_iterator][1])
    

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
        # No overlap, but second point of first element and first point of second 
        # element touch
        elif (result[result_iterator][1]) == (sort_list[sort_iterator][0] - 1):
            result[result_iterator][1] = sort_list[sort_iterator][1]
            del sort_list[sort_iterator]



        else:
            result.append(sort_list[sort_iterator])
            result_iterator += 1
            del sort_list[sort_iterator]

    return result


print(merge_tuples(tuples_list))
    



    # for i in range(len(tuples_list) - 1):
    #     temp_tuple_1 = tuples_list[i][0]
    #     temp_tuple_2 = tuples_list[i][1]
    #     for j in range(i + 1, len(tuples_list)):
    #         if (min(tuples_list[i]) > min(tuples_list[j]) and
    #             max(tuples_list[i]) > max(tuples_list[j])):
    #             # tuple_merged.append((min(tuples_list[j]), tuples_list[i][1]))
    #             temp_tuple_1 = min(tuples_list[j])
    #             # tuples_list[i][0] = min(tuples_list[j])
            
    #         elif (max(tuples_list[i]) < max(tuples_list[j]) and
    #             min(tuples_list[i]) < min(tuples_list[j])):
    #             temp_tuple_2 = max(tuples_list[j])
    #             # tuples_list[i][1] = max(tuples_list[i])
                                                  

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
