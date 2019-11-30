"""
counting valley:-

mountain : Mountain is steps above sea level.
valley : Valley is below the sea level. 

U - Uphill
D - Downhill

input format = [UDDDDUUDDUUDUUDDUU]

___/\            _    ___
     \          / \  /
      \  /\  /\/   \/
       \/  \/         

Task : Count the number of valleys Gary Travelled.

Input format : 
    n - number of steps in Gary's hike.
    s - path(U,D) of his hike.

TimeComplexity : O(n)
"""
def countingValleys(steps, path):
    valleys = 0
    level = 0

    for step in path:
        if (step == 'U'):
            level += 1
        if (step == 'D'):
            level -= 1
        if (level == 0) and (step == 'U'):
            valleys += 1
    
    return valleys