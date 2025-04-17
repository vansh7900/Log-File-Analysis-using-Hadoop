import sys
for line in sys.stdin:
    parts = line.split(" ")
    if len(parts) > 6:
        print(f"{parts[0]}\t1")  # IP Address as key
