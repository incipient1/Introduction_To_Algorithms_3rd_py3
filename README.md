# 使用Python3实现[算法导论](https://book.douban.com/subject/20432061/)中的案例、习题
## 01_foundations第一部分&ensp;基础知识
1. 插入排序insert_sort<br>
从将未排序的数（在右边）第一个开始，插入到已经排好序的（在左边）数列中去，形成新的排好序的数列。这个方法被称作**增量**方法
1. 选择排序selection_sort<br>
依次在未排序的数列（在已排序数的右边）中选择最小的数，然后把它放到未排序数的第一个
1. 冒泡排序bubble_sort<br>
反复交换相邻的两个数，然后将较小者挤出去
1. 最大子数组（分治策略）<br>
已实现矩阵的行、列必须是2^n(n为正整数)
## 02_sorting_and_order_statistics第二部分&ensp;排序和顺序统计量
5. 堆排序heap_sort<br>
建立最大堆，把最大元素换到堆的最后一个元素并踢出堆，维护最大堆
6. 快速排序quick_sort
找到一个数，把比它小的放在它前面，比它大的放在它后面，包括：<br>
* 现行版本quick_sort
* 随机化版本randomized_quick_sort
* 最初版本quick_sort_hoare，暂时未处理相同元素的数组
* 针对相同元素的随机化版本randomized_quick_sort_equal
7. 计数排序counting_sort<br>
找到数字排列的位置，然后将其放到相应位置。前提假设：小区间内的非负整数。如果区间过大，排序过程中产生的C中就有很多零，影响效率。
8. 基数排序radix_sort<br>
在元素的每一个位上排序(稳定的)，循环了所有的位后排序完成。其中稳定排序用的是counting_sort。
9. 桶排序bucket_sort<br>
把元素放到不同的桶里，然后在桶里排序后在串起来。前提假设元素是[0,1)上的均匀分布。在桶里的排序用的是insert_sort，也可以用其它原址排序。