def sum_number():
    arr = []
    for i in range(34,40):
        arr.append(i + 140)
    return arr

def even_number(start,end):
    for i in range(start,end+1):
        if i % 2 == 0:
            print(i,end="  ")
    print()

def largest_number(num):
    return max(num)

def frequency_count():
    strings = 'gehjfdisfndosgfwqhasreuwqrwanrewaus'
    # from a - z are 26 characters
    arr = [0]*26
    for i in range(len(strings)):
        n = ord(strings[i]) - ord('a')
        arr[n] = arr[n] + 1
    return arr

print(frequency_count())

print(largest_number(sum_number()))
even_number(1,20)
print(sum_number())
