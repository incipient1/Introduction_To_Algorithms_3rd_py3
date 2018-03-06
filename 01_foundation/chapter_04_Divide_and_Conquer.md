
# 第4章&ensp;分治策略

## 4.1&ensp;最大子数组问题

### 4.1&ensp;练习

#### 4.1-1&ensp;均为负数时最大子数组返回什么？

数组中最大的那个数

#### 4.1-2&ensp;暴力求解最大子数组


```python
def maximum_subarray(A):
    max_sum = -1000
    max_left = -1
    max_right = -1
    for i in range(len(A)):
        key = 0
        for j in range(i,len(A)):
            key = key+A[j]
            if key > max_sum:
                max_sum = key
                max_left = i
                max_right = j
    
    return max_sum, max_left,max_right

A = [8,-3,-1,-4,-7]
print(maximum_subarray(A))
```

    (8, 0, 0)
    

#### 4.1-3&ensp;择优选择暴力解法和递归解法

递归求解最大子数组，运行时间为$\Theta(nlgn)$，暴力求解运行次数为$\Theta(n^{2})$，故当$n>=1$时，递归解法有优势。修改后没有变化。

#### 4.1-4&ensp;允许结果为空子集，和为0

只有一种情况才能导致结果为空子集：即数组中的数都为非正数，返回的结果是其中最大的一个。对应于购买股票，即一旦购买就亏损，所以不够买是优情况。

```
def maximun_subarray_zero(A):
    flag = False
    for i in A:
        if i > 0:
            flag = True
            break
    if flag:
        return find_maximum_subarray(A)
    else:
        return []
```

#### 4.1-5&ensp;非递归、线性时间求最大子数组

## 4.2&ensp;Strassen算法

### 4.2&ensp;练习

#### 4.2-1&ensp;Strassen举例

A11 = [[1]]<br>
A12 = [[3]]<br>
A21 = [[7]]<br>
A22 = [[5]]<br>
B11 = [[6]]<br>
B12 = [[8]]<br>
B21 = [[4]]<br>
B22 = [[2]]<br>
S1 = B12-B22 = [[6]]<br>
S2 = A11+A12 = [[4]]<br>
S3 = A21+A22 = [[12]]<br>
S4 = B21-B11 = [[-2]]<br>
S5 = A11+A22 = [[6]]<br>
S6 = B11+B22 = [[8]]<br>
S7 = A12-A22 = [[-2]]<br>
S8 = B21+B22 = [[6]]<br>
S9 = A11-A21 = [[-6]]<br>
S10 = B11+B12 = [[14]]<br>
P1 = A11\*S1 = [[6]]<br>
P2 = S2\*B22 = [[8]]<br>
P3 = S3\*B11 = [[72]]<br>
P4 = A22\*S4 = [[-10]]<br>
P5 = S5\*S6 = [[48]]<br>
P6 = S7\*S8 = [[-12]]<br>
P7 = S9\*S10 = [[-84]]<br>
C11 = P5 + P4 - P2 + P6 = [[18]]<br>
C12 = P1 + P2 = [[14]]<br>
C21 = P3 + P4 = [[62]]<br>
C22 = P5 + P1 - P3 - P7 = [[66]]<br>
C = [[18,14],[62,66]]

#### 4.2-2&ensp;Strassen算法伪码

## 4.3&ensp;用带入法求解递归式

### 4.3&ensp;练习

#### 4.3-1&ensp;证明T(n)=T(n-1)+n的解为$O(n^2)$

使用带入法求解(这个章节的方法)，猜测其解为$O(n^2)$，恰当选择常数c>0，可有$T(n)\leqslant cn^2$：<br>
$T(n)\leqslant c(n-1)^2+n=cn^2+n(1-2c)+c\leqslant cn^2$，只要最后一步时$c\geqslant\frac{1}{2}$

#### 4.3-9&ensp;求解递归式$T(n)=3T(\sqrt{n})+logn$的解

假设$m=\log_{a}{n}$，则$n=a^m$，$T(a^{m})=3T(a^{m/2}+m$，设$S(m)=T(a^{m})$，则$S(m)=3S(m/2)+m$，猜测解为$\Omega(n^{lg3})$<br>
$S(m)\geqslant 3(c(m/2)^{lg3}+m \geqslant c(m^{lg3})$，舍去低阶项m，保证c>=1即可
