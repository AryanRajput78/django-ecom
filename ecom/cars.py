# read values from file
input_file = open("inputPS9.txt", "r")
out_file = open('outputPS9.txt','a')
out_file.truncate(0)
n = int(input_file.readline())

# here we are handling error , if no of cars less than 1 it’ll give an error
if n >= 1 :
    speed = list(map(int, (input_file.readline()).strip().split(" ")))
    position = list(map(int, (input_file.readline()).strip().split(" ")))
else :
    raise Exception("No of cars should be >= 1")

# here we declare count variable which stores no of overlaps
count = 0

#  here we sorted both list in decreasing order
# we using sorting so our time complexity is O(nlogn)
# instead of sorting we can use 2 for loops but it'll take higher time complexity O(n^2)
sorted_pairs = sorted(zip(speed, position), reverse=True)
speed_new, position_new = zip(*sorted_pairs)
speed_new, position_new = list(speed_new), list(position_new)

# here we are checking if ith car's speed is greater than position (as per condition given in problem), then we increase count by 1
for i in range(n):
    if speed_new[i] > position_new[i]:
        count += 1
        
# here we send final count to output file
out_file.write(str(count) + '\n')