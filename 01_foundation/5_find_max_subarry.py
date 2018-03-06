def find_max_crossing_subarry(A,low,mid,high):
    left_sum = -1000
    left = 0
    for i in range(mid,low-1,-1):
        left += A[i]
        if left > left_sum:
            left_sum = left
            max_left = i

    right_sum = -1000
    right = 0
    for j in range(mid+1,high+1):
        right += A[j]
        if right > right_sum:
            right_sum = right
            max_right = j

    return (max_left,max_right,left_sum + right_sum)

def find_maximum_subarry(A,low,high):
    if high == low:
        return (low,high,A[low])
    else:
        mid = int(0.5*(low + high))
        (left_low, left_high, left_sum) = find_maximum_subarry(A,low,mid)
        (right_low,right_high, right_sum) = find_maximum_subarry(A,mid+1,high)
        (cross_low,cross_high,cross_sum) = find_max_crossing_subarry(A,low,mid,high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)


if __name__ == '__main__':
    A = [-8,-2,-3,-4,-7]
    print(find_maximum_subarry(A,0,len(A)-1))