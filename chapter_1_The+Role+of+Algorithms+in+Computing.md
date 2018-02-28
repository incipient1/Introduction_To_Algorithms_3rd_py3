
# 算法在计算机中作用
## 练习page6
### 1.1-1 给出现实生活中需要排序的例子

取号排队。

同时有两拨人来到餐厅，但是餐厅中已经没有多余座位了，这时他们都需要排队。队伍A有两个人，队伍B有6人，参观需要根据他们的人数安排作为，排队在他们前面的桌数也是不定的。

### 1.1-2除速度外，在真实环境中还可能使用哪些其它有关效率的对量

1. 计算单价

举例：解决1MB数据排序问题时花费的金钱数量

2. 开发速度

设计出算法需要花费的时间

## 练习page7
### 1.2-2插入排序$8n^{2}$步，优于归并排序$64nlgn$
即求解当8n \* n < 64n \* lgn时，n的最大值


```python
import math
n = 2
while n < 8*(math.log(n,2)):
    n += 1

print('当n小于等于{}时，插入排序优于归并排序'.format(n-1))
```

    当n小于等于43时，插入排序优于归并排序
    

### 1.2-3 n的最小值为何值时，运行时间为100$n^{2}$的一个算法在相同机器上快于运行时间为$2^{n}$的另一个算法
即求解100n \* n < $2^{n}$时，n的最小值


```python
n = 2
while 100*n**2 > 2 ** n:
    n += 1
    
print('算法100n*n快于算法2**n时，n的最小值为{}'.format(n-1))
```

    算法100n*n快于算法2**n时，n的最小值为14
    

## 思考题
### 时间t内不同算法运行的最大规模
即求解当f(n) <= t时，n的最大值
设g(n) = $f^{-1}(n)$，即求g(t)


```python
time = {'second':10**3,'minute':6*(10**4),'hour':3.6*10**6,
            'day':8.64*10**7,'month':2.592*10**9,
            'year':3.11*10**10,'century':3.11*10**12}
```


```python
time_list = ['second','minute','hour','day','month','year','century']
```


```python
import math
```


```python
def lgn(t):
    if t <= time['second']:
        return 2 ** t
    elif t <= time['minute']:
        return lgn(time['second']) * (t / time['second'])
    elif t <= time['hour']:
        return lgn(time['minute']) * (t / time['minute'])
    elif t <= time['day']:
        return lgn(time['hour']) * (t / time['hour'])
    elif t <= time['month']:
        return lgn(time['day']) * (t / time['day'])
    elif t <= time['year']:
        return lgn(time['month']) * (t / time['month'])
    elif t <= time['century']:
        return lgn(time['year']) * (t / time['year'])
    else:
        return lgn(time['century']) * (t / time['century'])
```


```python
t = time['month']
fun = [lgn][0]
fun(t)
```




    2.777350309826805e+307




```python
print('在{0}内，算法{1}求解问题最大规模n为：{2:.2e}'.format('1秒钟','lgn',lgn(t)))
```

    在1秒钟内，算法lgn求解问题最大规模n为：2.78e+307
    


```python
for t in time_list:
    print('在1 {0}内，算法{1}求解问题最大规模n为：{2:.2e}'.format(t,'lgn',lgn(time[t])))
```

    在1 second内，算法lgn求解问题最大规模n为：1.07e+301
    在1 minute内，算法lgn求解问题最大规模n为：6.43e+302
    在1 hour内，算法lgn求解问题最大规模n为：3.86e+304
    在1 day内，算法lgn求解问题最大规模n为：9.26e+305
    在1 month内，算法lgn求解问题最大规模n为：2.78e+307
    在1 year内，算法lgn求解问题最大规模n为：inf
    在1 century内，算法lgn求解问题最大规模n为：inf
    


```python
def nsqrt(t):
    return t**2
```


```python
def nlgn(t):
    n = 1
    while n * math.log(n,2) <= t:
        n += 1
    
    return n-1
```


```python
def nsqr(t):
    return t**0.5
```


```python
def ncube(t):
    return t ** (1/3)
```


```python
def n2(t):
    return math.log(t,2)
```


```python
def nfactorial(t):
    n = 1
    while math.factorial(n) <= t:
        n += 1
        
    return n-1
```


```python
functions = [lgn,nsqrt,nlgn,nsqr,ncube,n2,nfactorial]
for func in functions:
    for t in time_list:
        print('在1 {}内，算法{}求解问题最大规模n为：{:.2e}'.format(t,func,func(time[t])))  
    
    print()
```

    在1 second内，算法<function lgn at 0x000001487F9D2BF8>求解问题最大规模n为：1.07e+301
    在1 minute内，算法<function lgn at 0x000001487F9D2BF8>求解问题最大规模n为：6.43e+302
    在1 hour内，算法<function lgn at 0x000001487F9D2BF8>求解问题最大规模n为：3.86e+304
    在1 day内，算法<function lgn at 0x000001487F9D2BF8>求解问题最大规模n为：9.26e+305
    在1 month内，算法<function lgn at 0x000001487F9D2BF8>求解问题最大规模n为：2.78e+307
    在1 year内，算法<function lgn at 0x000001487F9D2BF8>求解问题最大规模n为：inf
    在1 century内，算法<function lgn at 0x000001487F9D2BF8>求解问题最大规模n为：inf
    
    在1 second内，算法<function nsqrt at 0x000001487F9E28C8>求解问题最大规模n为：1.00e+06
    在1 minute内，算法<function nsqrt at 0x000001487F9E28C8>求解问题最大规模n为：3.60e+09
    在1 hour内，算法<function nsqrt at 0x000001487F9E28C8>求解问题最大规模n为：1.30e+13
    在1 day内，算法<function nsqrt at 0x000001487F9E28C8>求解问题最大规模n为：7.46e+15
    在1 month内，算法<function nsqrt at 0x000001487F9E28C8>求解问题最大规模n为：6.72e+18
    在1 year内，算法<function nsqrt at 0x000001487F9E28C8>求解问题最大规模n为：9.67e+20
    在1 century内，算法<function nsqrt at 0x000001487F9E28C8>求解问题最大规模n为：9.67e+24
    
    在1 second内，算法<function nlgn at 0x000001487F9E2B70>求解问题最大规模n为：1.40e+02
    在1 minute内，算法<function nlgn at 0x000001487F9E2B70>求解问题最大规模n为：4.90e+03
    在1 hour内，算法<function nlgn at 0x000001487F9E2B70>求解问题最大规模n为：2.04e+05
    在1 day内，算法<function nlgn at 0x000001487F9E2B70>求解问题最大规模n为：3.94e+06
    在1 month内，算法<function nlgn at 0x000001487F9E2B70>求解问题最大规模n为：9.77e+07
    ......
    

函数|1秒钟|1分钟|1小时|1天|1个月|1年|1世纪
--|--|--|--|--|--|--|--
$\lg n$|1.07e+301||||||
$\sqrt n$|3.60e+09||||||
$n$|e+03||||||
$n\lg n$|1.40e+02||||||
$n^{2}$|3.16e+01||||||
$n^{3}$|1.00e+01||||||
$2^{n}$|9.97e+00||||||
$n!$|6.00e+00||||||
