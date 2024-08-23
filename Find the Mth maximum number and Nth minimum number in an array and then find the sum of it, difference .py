array = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3
sorted_array = sorted(array)
mth_max = sorted_array[-M]
nth_min = sorted_array[N-1]
sum_result = mth_max + nth_min
difference_result = abs(mth_max - nth_min)
print(f"{M}st Maximum Number = {mth_max} {N}rd Minimum Number = {nth_min} Sum = {sum_result} Difference = {difference_result}")
