#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)
Because the while loop is n^3, and inside the while loop, the Big O relevant
variables are n^2; if you divide the n^3 by n^2, you are left with one n.
This means that the runtime of this code snippit will grow approximately
linearly as n grows.

b)
O(n log n)
The initial n in the Big O notation represents the for loop with range n - 
meaning the the loop will run n times. The log n in the Big O notation
represents the while loop; because j grows exponentially while n remains
constant with each iteration of the while loop, the while loop runtime
will grow at a slightly lower rate as n grows. Combining the the for loop
and while loop, the runtime of this code snippet will grow at a slightly
faster rate as n increases.

c)
O(n)
Because n, or bunnies, is decremented by 1 with each iteration, and the base case
is bunnies, or n, equals 0; this recursive funtion will run n times before it reaches 
the base case, making the rate the runtime grows linear relative to the growth of n, 
or bunnies.


## Exercise II

Initially, let n = the top floor, and let 0 equal the bottom floor.

The initial middle floor is found by dividing n by 2.

Drop an egg from the middle floor.

If the egg breaks, drop an egg from the floor lower to see if it breaks. 
If the egg does not break, the floor above it is floor f.
If the egg dropped from the current middle floor minus 1 also breaks, divide the 
(middle floor - 1) by 2, and set that number as the new middle floor. Set the
new top floor as the middle floor - 1, and repeat the process starting at line 36
until floor f is identified.

If the egg dropped from the current middle floor does not break, drop an egg
from the floor above. If this egg breaks, this floor is floor f. If it does not: 
Divide (top floor - (the middle floor plus 1)) by 2, and add that number to the 
middle floor plus 1. The resulting number is the new middle floor, and the new 
bottom floor is the middle floor plus 1. Repeat the process starting at line 36 
until floor f is identified.




