def merge(list1, list2):
    answer_list = []
    while len(list1) > 0 or len(list2) > 0:
        if len(list1) > 0 and len(list2) > 0:
            if list1[0] <= list2[0]:
                answer_list.append(list1[0])
                list1 = list1[1:]
            else:
                answer_list.append(list2[0])
                list2 = list2[1:]
        elif len(list1) > 0:
            answer_list.append(list1[0])
            list1 = list1[1:]
        elif len(list2) > 0:
            answer_list.append(list2[0])
            list2 = list2[1:]
    
    return answer_list




def merge_sort(list):
    length = len(list)
    mid = length // 2
    if len(list) < 2:
        return list
    else:
        return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))
    


print(merge_sort([1,2, 4, 6, 2, 4, 5]))