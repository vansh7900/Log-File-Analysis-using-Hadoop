import sys
from collections import defaultdict

count_dict = defaultdict(int)
for line in sys.stdin:
    ip, count = line.strip().split("\t")
    count_dict[ip] += int(count)

for ip, count in count_dict.items():
    print(f"{ip}\t{count}")
