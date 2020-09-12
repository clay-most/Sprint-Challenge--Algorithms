#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
This is o(n) becuse when the input number gets larger the steps to finish increase proportionately.


b)
o(N^2) becuse the for-loop is linear but so is the nested while.

c)
o(N) because it will only run as many steps as the bunnies it's given 


## Exercise II


I would use a binary search to find the max floor to drop an egg without breaking it. Starting in the middle when the egg is dropped if it breaks we know we are too high and we can move down to the top of lowest quarter and try again discarding the topmost half. And repeat until only one possible floor remains. 

Binary searches have a runtime complexity of o(log n)