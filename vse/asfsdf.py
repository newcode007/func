def sum_range(start, end):
    return sum(range(min(start, end),max(start, end)+1,1))









print(sum_range(2, 12))
print(sum_range(-4, 4))
print(sum_range(3, 2))