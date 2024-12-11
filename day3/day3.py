import re
day = 3

with open('input.txt', 'r') as file:
    input = file.read()

#expression pattern for this library to match instructions of form mul(x, y) where x and y are integers from 1 to 999
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

#re.findall finds all occurrences of the matter defined, in the input string
#each match is a tuple of the two numbers (x, y)
matches = re.findall(pattern, input)

#converts the strings into integers and calculates the sum of the products of all items which matched previous instructions
total_sum = sum( int(x) * int(y) for x, y in matches)

result_part_1 = total_sum


#new pattern for re library to match "do()" and "don't()" control instructions
controls_pattern = r"do\(\)|don't\(\)"

#splits the input string into a list of substrings which break at occurances of mul(x, y), do() or don't()
info = re.split(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", input)

bool = True
new_sum = 0
print(info) #example
for i in info: #to interate through each substring in the split list info
    if not i.strip(): #skips empty strings
        continue
    if re.match(controls_pattern, i): #checks if the current substring matches control instructions; if so, the boolean is enabled according to given instructions
        if i == "do()":
            bool = True
        elif i == "don't()":
            bool = False
    elif re.match(pattern, i): #checks if the current substring matches mult instructions
        #if so, ONLY if the boolean is enabled, it extracts numbers x and y from the instruction, converts to integer, and adds sum of product
        if bool:
            x, y = map(int, re.findall(r"\d+", i))
            new_sum += x * y

result_part_2 = new_sum



print(f"--- Day {day}: ---") #3
print(f"Part 1: {result_part_1}") #190604937
print(f"Part 2: {result_part_2}") #82857512