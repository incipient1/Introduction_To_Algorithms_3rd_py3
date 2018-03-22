# 使用Python3实现[算法导论](https://book.douban.com/subject/20432061/)中的案例、习题
## 01_foundations第一部分&ensp;基础知识
1. 插入排序insert_sort<br>
&ensp;从将未排序的数（在右边）第一个开始，插入到已经排好序的（在左边）数列中去，形成新的排好序的数列。这个方法被称作**增量**方法
1. 选择排序selection_sort<br>
&ensp;依次在未排序的数列（在已排序数的右边）中选择最小的数，然后把它放到未排序数的第一个
1. 冒泡排序bubble_sort<br>
&ensp;反复交换相邻的两个数，然后将较小者挤出去
1. 最大子数组（分治策略）<br>
&ensp;已实现矩阵的行、列必须是2^n(n为正整数)
## 02_sorting_and_order_statistics第二部分&ensp;排序和顺序统计量
5. 堆排序heap_sort<br>
&ensp;建立最大堆，把最大元素换到堆的最后一个元素并踢出堆，维护最大堆
6. 快速排序quick_sort
&ensp;找到一个数，把比它小的放在它前面，比它大的放在它后面，包括：
&ensp;* 现行版本quick_sort
&ensp;* 随机化版本randomized_quick_sort
&ensp;* 最初版本quick_sort_hoare，暂时未处理相同元素的数组