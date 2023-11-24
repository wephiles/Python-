# 普通冒泡排序，最普通的那种
def bubble_sort(sort_list: [int]) -> list[int]:
    """这是一个普通的不能再普通的冒泡排序算法。

    example：
    you can do like this:
    print(bubble_sort([98, 94, 2, -12, 4, 19, 50, 48, -100, -10]))

    output:
    [-100, -12, -10, 2, 4, 19, 48, 50, 94, 98]
    """
    if len(sort_list) == 0:
        return []
    length = len(sort_list)
    for i in range(0, len(sort_list)):
        for j in range(0, len(sort_list) - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list