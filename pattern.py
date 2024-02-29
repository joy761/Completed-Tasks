#write code to output the star pattern with row_count(5), using an if-else statement with a combination of a single for loop

row_count = 5
start = 1
end = (2 * row_count) + 1

for row_number in range(start, end):
    star_count = row_number if row_number <= row_count else end - row_number
    print("*" * star_count)
    
