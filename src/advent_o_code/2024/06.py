
import re
import os

def mul(x, y):
    return x * y

if __name__ == "__main__":
    filepath = os.path.join("data", "memory.txt")
    matcher = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
    
    with open(filepath, "r") as file:
        memory_code = file.read()
    matches = re.findall(matcher, memory_code)
    total = 0
    enabled = True
    for match in matches:
        if "don't" in match:
            enabled = False
        elif "do" in match:
            enabled = True
        if enabled and "mul" in match:
            total += eval(match)
    print(total)