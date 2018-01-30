import pandas as pd

def max_subarray(alist):
    alist = pd.Series(alist)
    max_alist = -1000
    max_right = -1
    for i in range(1,len(alist)+1):
        alist_ri = alist.rolling(i).sum()
        max_alist_ri = max(alist_ri[i-1:])
        if max_alist_ri > max_alist:
            max_alist = max_alist_ri
            max_right = alist_ri[alist_ri == max_alist_ri].index
            max_left = max_right - i + 1
        else:
            pass
    return max_left, max_right, max_alist


if __name__ == 'main':
    alist = [1,2,3,45,-4,-7,9,-12]
    print(max_subarray(alist))
