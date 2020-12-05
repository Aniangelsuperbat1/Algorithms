# Big O Notation:
# -Way to measure how efficient a data structure is structure based on 4 criteria
# -Most common functions from a data structure:
# 	-Accessing elements
# 	-Searching for elements 
# 	-inserting an element 
# 	-deleting an element
# -Time complexity equation works by inserting the size of the data set as an integer N, and returning  the number of operations that need to be conducted by the computer before the function can finish
# -Always use the worst case scenario when judging data structures (what has the most operations)
# -It is called Big O notation because the syntax for the time complexity equations includes a BigO and a set of parenthesis. The Parenthesis houses the functions.
# - Most of the time our integer N is going to have some adverse-effect on how many operations it takes
# -We measure efficiency in # of operations performed because measuring how long the functions take to run would be silly. Measuring by time would be biased towards better hardware. (A super computer would take less time to run code than a laptop)
# 6 most common Time Complexity equations:
# O(1): Constant Time. Best one. No matter the size of your data set task will be completed in a single instruction
# O(Logn):  Second Best. Gets more efficient as the size of the data set increases.
# O(n): Linear time. Decent.  Operations increases as the size of your data set increases. 
# O(nlogn): Number of operations increases faster than Linear time as the size of your data set increases
# O(N2(squared)): Polynomial Algorithm. The larger the data set the more inefficient it will become.
# O(2n(squared)):  Exponential Algorithm. The larger the data set the more inefficient it will become.


