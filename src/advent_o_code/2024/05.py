import re
import os

def mul(x, y):
    return x * y

if __name__ == "__main__":
    filepath = os.path.join("data", "memory.txt")
    matcher = r"mul\(\d+,\d+\)"
    with open(filepath, "r") as file:
        memory_code = file.read()
    matches = re.findall(matcher, memory_code)
    total = 0
    for match in matches:
        total += eval(match)
    print(total)