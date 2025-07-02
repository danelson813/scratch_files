'''
Installing icecream
To use ic(), first install the icecream library:

pip install icecream
Then, import it into your script:

from icecream import ic
Now, let’s see how it works!

Example 1: Automatic Variable Names and Values
With print(), debugging is manual and repetitive:

x = 42
y = x * 2
print("y:", y) # We have to manually type "y:"
With ic(), debugging is automatic and cleaner:

from icecream import ic

x = 42
y = x * 2
ic(y)
Output:

ic| y: 84
No need to manually type "y:"—ic() does it for you!




'''