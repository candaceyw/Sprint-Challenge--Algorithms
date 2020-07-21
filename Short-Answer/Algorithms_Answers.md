#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

    a)  a = 0
    while (a < n * n * n):
      a = a + n * n


    O(n) runtime is linear. Because the loop runs through n until finished.


b) 

    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
        
        
    O(n^2) quadratic time because of the nested loop. 
    Outer loop is O(n)
    Inner loop O(n)
    so we get O(n^2)
    
    getting the sum is O(1)
    
    O(n^2) is the worst case.



c)  


    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0
      

        O(n)
        add 2 and perform recursion until the base case is reached.
        A single recursive call not inside of a loop is O(n)

## Exercise II
        
        n = number of stories in building
        f = floor +/- 1 where the egg breaks/doesn't break
        
        Start in middle floor of the building n // 2
        drop egg
        if egg does break then n // 2 - 1 to go down a floor
        or if egg doesn't breaks, then n // 2 + 1 to go up a floor
        drop egg 
        
        continue loop until egg doesn't break between floors.
        if floor above breaks  and floor below doesn't break, then current floor is our winner
        
        runtime would be O(log n) 
        solution takes the number of floors and cut in half each test we make the loop