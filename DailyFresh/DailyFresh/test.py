# def get_consecutive_numbers(arr, n):
#     if n not in arr:
#         return []
#
#     index = arr.index(n)
#     start = max(0, index - 3)
#     end = min(len(arr) - 1, start + 6)
#
#     if start == 0 and end < 6:
#         end = min(len(arr) - 1, end + (6 - end))
#     elif start > 0 and end == len(arr) - 1 and end - start < 6:
#         start = max(0, start - (6 - (end - start)))
#
#     consecutive_numbers = arr[start:end+1]
#     return consecutive_numbers
#
# # 示例用法
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# n = 13
#
# consecutive_arr = get_consecutive_numbers(arr, n)
# print(consecutive_arr)

# def get_consecutive_numbers(range_obj, n,sub_num):
#     arr = list(range_obj)
#
#     if sub_num > len(arr):
#         return arr
#
#     if n not in arr:
#         return []
#
#     index = arr.index(n)
#     start = max(0, index - 3)
#     end = min(len(arr) - 1, start + 6)
#
#     if start == 0 and end < 6:
#         end = min(len(arr) - 1, end + (6 - end))
#     elif start > 0 and end == len(arr) - 1 and end - start < 6:
#         start = max(0, start - (6 - (end - start)))
#
#     consecutive_numbers = arr[start:end+1]
#     return consecutive_numbers
#
# # 示例用法
# range_obj = range(1, 5)
# n = 4
#
# consecutive_arr = get_consecutive_numbers(range_obj, n,2)
# print(consecutive_arr)

def get_consecutive_numbers(range_obj, n, count):
    arr = list(range_obj)

    if n not in arr:
        return []

    index = arr.index(n)
    start = max(0, index - count // 2)
    end = min(len(arr) - 1, start + count - 1)

    if start == 0 and end < count - 1:
        end = min(len(arr) - 1, end + (count - 1 - end))
    elif start > 0 and end == len(arr) - 1 and end - start < count - 1:
        start = max(0, start - (count - 1 - (end - start)))

    consecutive_numbers = arr[start:end+1]
    return consecutive_numbers

# 示例用法
range_obj = range(1, 40)
n = 7
count = 19

consecutive_arr = get_consecutive_numbers(range_obj, n, count)
print(consecutive_arr)
