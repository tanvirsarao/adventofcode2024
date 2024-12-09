day = 2
rows = []
unsafe_rows = []

with open('input.txt', 'r') as file:
    for line in file:
        rows.append(list(map(int, line.split())))

def is_safe(row):
    for i in range(len(row) - 1):
        if not (1 <= abs(row[i] - row[i + 1]) <= 3):
            return False
    safe = all((row[i] < row[i + 1]) for i in range(len(row) - 1)) or all((row[i] > row[i + 1]) for i in range(len(row) - 1))
    return safe

safe_count = sum(1 for i in rows if is_safe(i))
unsafe_rows = [i for i in rows if not is_safe(i)]

result_part_1 = safe_count

def safe_now(row):
    for i in range (len(row)):
        new_row = row[:i] + row[i + 1:]
        if is_safe(new_row):
            return True
    return False

safe_count_new = safe_count
safe_count_new += sum(1 for i in unsafe_rows if safe_now(i))

result_part_2 = safe_count_new

print(f"--- Day {day}: ---") #2
print(f"Part 1: {result_part_1}") #218
print(f"Part 2: {result_part_2}") #290