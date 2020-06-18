

def check (list1 : list, list2: list) -> (bool, str) :
    errors = []
    index_to_remove = []

    if len(list1) != len(list2):
        return False, "not same size"

    #  check elements
    for i in range (len(list1)):
        if len(list1[i]) != 4:
            errors.append('wrong length : {}'.format(list1[i]))
            index_to_remove.append(i)
            continue
        if type(list2[i]) != int:
            errors.append('type wrong in {}, input : {}'.format(list1[i],type(list2[i])))
            index_to_remove.append(i)
            continue

    #  remove corrupted elements
    for i in range (len(index_to_remove)):
        list1.pop(index_to_remove[i]-i)
        list2.pop(index_to_remove[i]-i)

    #.... use non corrupted elements
    if not errors:
        return True, "added : {}".format(list1)
    else:
        return False, "added : {} but you need to verify the following errors : \n{}".format(list1, '\n'.join(errors))


list1 = ['aaa','bbbb', 'cccc', 'd', 'eee', 'ffff','gggg','hhhh','i','jjjj']
list2 = [1,2,3,4,'5',6,7,8,9,'10']
print(check(list1, list2)[1])
    