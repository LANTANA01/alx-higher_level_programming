#!/usr/bin/python3
for i in range(100):
    end_str = "\n" if i == 99 else ", "
    print(f"{i:02}", end=end_str)
