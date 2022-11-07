def to_dict_lst(x):
    dict = {}
    for i in x:
        dict[i] = i
    return dict
lst = [1,4,9,'fgh','fghjh']



if __name__ == '__main__':
    print(to_dict_lst(lst))