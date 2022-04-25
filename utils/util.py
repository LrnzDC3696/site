def to_matrix(one_d_list, x):
    return [one_d_list[i:i+x] for i in range(0, len(one_d_list), x)]
