def find_max_crossing_subarray(alist,low,mid,high):
    left_sum = -1000
    sum_sub = 0
    max_left = -1
    max_right = 1000
    for i in range(mid,low-1,-1):
        sum_sub = sum_sub + alist[i]
        if sum_sub > left_sum:
            left_sum = sum_sub
            max_left = i
    right_sum = -1000
    sum_sub = 0
    for j in range(mid+1,high+1):
        sum_sub = sum_sub + alist[j]
        if sum_sub > right_sum:
            right_sum = sum_sub
            max_right =  j
    return (max_left,max_right,left_sum + right_sum)

def find_maximum_subarray(alist,low,high):
    if high == low:
        return (low, high, alist[low])
    else:
        mid = int(0.5*(low+high))
        (left_low,left_high,left_sum) = find_maximum_subarray(alist,low,mid)
        (right_low,right_high,right_sum) = find_maximum_subarray(alist,mid+1,high)
        (cross_low,cross_high,cross_sum) = find_max_crossing_subarray(alist,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)

if __name__ == '__main__':
    alist = [12,-8,-9,3,4,5,6,2,1,19,-1,35,26]
    print(find_maximum_subarray(alist,0,len(alist)-1))