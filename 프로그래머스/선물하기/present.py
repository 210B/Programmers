import pandas as pd

def solution(friends, gifts):
    # make present index dictionary
    present_dict = {key: 0 for key in friends}

    # calculate
    present_df = pd.DataFrame(0, columns=friends, index=friends)

    for g in gifts:
        row_name, col_name = g.split()
        present_df.loc[row_name, col_name] += 1

    for key in present_dict:
        present_dict[key] = present_df.loc[key].sum() - present_df[key].sum()
    print(present_dict)

    # compare
    prenum_dict = {key: 0 for key in friends}
    l = len(friends)
    for i in range(0, l):
        for j in range(i+1, l):
            if present_df.iloc[i, j] > present_df.iloc[j,i]:
                prenum_dict[friends[i]] += 1
            elif present_df.iloc[i, j] < present_df.iloc[j, i]:
                prenum_dict[friends[j]] += 1
            elif present_dict[friends[i]] > present_dict[friends[j]]:
                prenum_dict[friends[i]] += 1
            elif present_dict[friends[i]] < present_dict[friends[j]]:
                prenum_dict[friends[j]] += 1

    # get max num
    answer = max(prenum_dict.values())
    return answer
