def find_str_occurence(substring, s):
    idx_list = []
    substr_len = len(substring)

    # iterate through the string to match with substring
    for i in range(len(s)):
        # expression to get substring from each index + length of provided substring to compare with each other
        if s[i: i + substr_len] == substring:
            idx_list.append(i)

    # if idx_list is empty, it must mean that there are no matches
    if len(idx_list) <= 0:
        return "No Matches"

    return idx_list

