def delete(list_, index=None):
    if index is None:
        return list_[:-1]
    first_list = list_[:index]
    second_list = list_[index+1:]
    new_list = first_list + second_list
    return new_list

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
