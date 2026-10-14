import sys      #Access command-line arguments
from collections import Counter      #count occurrences and store it in dictionary
filename = sys.argv[1]        #Get the log in variable filename
position = int(sys.argv[2])
with open(filename) as f:        #Open the log file
    lines = f.readlines()         #Read all lines and store it as list
print("Total lines: ", len(lines))     #print total lines
counts= Counter()
for line in lines:
    fields=line.split()
    if len(fields)>position:
        key = fields[position]
        counts[key] += 1
print("Top 5:")
for item,n in counts.most_common(5):
    print(item,n)