# LeetCode Daily Report


Daily record for LeetCode solution using Python 3. 


### July 2, 2017
1. Two sum(1) - easy
    - Hash table using Dictionary
  
### July 3, 2017
1. Longest Common Prefix (14) - easy
    - set()
    - zip()
    - min()
    - enumerate()
### July 4, 2017
1. Reverse Integer (7) - easy
    * if result.bit_length() < 32 else 0
    * using % module.
2. Roman to Integer (13) - easy
    * [:]
    * set()
    * sorted()
    * List indexing
        * https://www.programiz.com/python-programming/list
### July 5, 2017
1. Remove element (27) - easy
2. Climbing stairs (70) - easy
    * Fibonacci numbers (dynamic programming)
3. Delete duplicates (83) - easy
4. Symmetric Tree (101) - easy
    * consider root as two roots. each take cares of right side and left side.
    * recursive
### July 7, 2017
1. Best time to buy and sell stock (121) - easy
2. Best time to buy and sell stock2 (122) - easy
3. Linked list cycle (141) - easy
    * cycle detection (Tortoise and hare)
4. Intersection of two linked lists (160) - easy
    * only 2 ways to get out of the loop, they meet or the both hit the end=None 
    the idea is if you switch head, the possible difference between length would be countered. 
    On the second traversal, they either hit or miss. 
    if they meet, pa or pb would be the node we are looking for, 
    if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
5. Two sum 2 - Input array is sorted (167) - easy
    * two pointers
    * dictionary
    * binary search
    
### July 10, 2017
1. Rotate array (189) - easy
    * List indexing
    * nums[:] = nums[length-k:]+nums[:length-k]
2. Number of 1 bits (191) - easy
    * bin(): convert an integer number to a binary string
3. House Robber(198) - easy
    * xrange() and range() difference: xrange not supported in Python 3 any longer
    * dynamic programming
    * 
    ```
    f(0) = nums[0]
    f(1) = max(num[0], num[1])
    f(k) = max( f(k-2) + nums[k], f(k-1) )
    ```

