import sys
from collections import Counter

books = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))]
name_cnt_list = sorted(Counter(books).most_common(), key=lambda x: (-x[1], x[0]))
print(name_cnt_list[0][0])




