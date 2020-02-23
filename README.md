# Assignments
Weekly Assignments of Programming, Data Structures And Algorithms Using Python (NPTEL  course)

# Week 2
1.¦  A positive integer m can be expresseed as the sum of three squares if it is of the form p + q + r where p, q, r ≥ 0, and p, q, r are all perfect squares.
     For instance, 2 can be written as 0+1+1 but 7 cannot be expressed as the sum of three squares. The first numbers that cannot be expressed as the sum of three 
     squares are 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, … (see Legendre's three-square theorem).
     Write a Python function threesquares(m) that takes an integer m as input and returns True if m can be expressed as the sum of three squares and False otherwise.
     (If m is not positive, your function should return False.)
     Here are some examples of how your function should work.
>>> threesquares(6)           True
>>> threesquares(188)         False
>>> threesquares(1000)        True

2.¦  Write a function repfree(s) that takes as input a string s and checks whether any character appears more than once.
     The function should return True if there are no repetitions and False otherwise.
     Here are some examples to show how your function should work.
>>> repfree("zb%78")          True
>>> repfree("(7)(a")          False
>>> repfree("a)*(?")          True
>>> repfree("abracadabra")    False

3.¦  A list of numbers is said to be a hill if it consists of an ascending sequence followed by a descending sequence, where each of the sequences is of range at least two.
     Similarly, a list of numbers is said to be a valley hill if it consists of an descending sequence followed by an ascending sequence.
     You can assume that consecutive numbers in the input sequence are always different from each other.
     Write a Python function hillvalley(l) that takes a list l of integers and returns True if it is a hill or a valley, and False otherwise.
     Here are some examples to show how your function should work.
>>> hillvalley([1,2,3,5,4])               True
>>> hillvalley([1,2,3,4,5])               False
>>> hillvalley([5,4,1,2,3])               True
>>> hillvalley([5,4,3,2,1])               False
>>> hillvalley([1,2,3,4,5,3,2,4,5,3,2,1]) False


# Week 3
1.¦ Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the first occurrence of each number.
>>> print(remdup([3,1,3,5]))
[3, 1, 5]
>>> print(remdup([7,3,-1,-5]))
[7, 3, -1, -5]
>>> print(remdup([3,5,7,5,3,7,10])) 
[3, 5, 7, 10]


2.¦ Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers
in l and even is the sum of squares of all the even numbers in l.
Here are some examples to show how your function should work.
>>> print(sumsquare([1,3,5]))
[35, 0]
>>> print(sumsquare([2,4,6]))
[0, 56]
>>> print(sumsquare([-1,-2,3,7]))
[59, 4]


3.¦ A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix
1  2  3  4
5  6  7  8
would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].
The transpose of a matrix converts each row into a column. The transpose of the matrix above is:
1  5
2  6
3  7
4  8
which would be represented as [[1, 5], [2, 6], [3, 7], [4, 8]].
Write a Python function transpose(m) that takes as input a two dimensional matrix m and returns the transpose of m.
The argument m should remain undisturbed by the function. Here are some examples to show how your function should work.
You may assume that the input to the function is always a non-empty matrix.
>>> print(transpose([[1,2,3],[4,5,6]]))
[[1, 4], [2, 5], [3, 6]]
>>> print(transpose([[1],[2],[3]]))
[[1, 2, 3]]
>>> print(transpose([[3]]))
[[3]]

# Week 4
1. We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:

   { 'match1':{'player1': 57, 'player2': 38},
     'match2':{'player3': 9 , 'player1': 42},
     'match3':{'player2': 41, 'player4': 63 , 'player3': 91 }

   Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not fixed
   (here they are 'match1', 'match2', 'match3'), nor are the names of the players. A player need not have a score recorded in all matches.
   Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. Your function should return a pair
   (playername,topscore) where playername is a string, the name of the player with the highest score, and topscore is an integer, the total score of playername.
   The input will be such that there are never any ties for highest total score.
   For instance:
>>> orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
    ('player3', 100)
>>> orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'Ashwin':59, 'Pujara':42}})
    ('Ashwin', 143)

2. Let us consider polynomials in a single variable x with integer coefficients. For instance:
   3x4 - 17x2 - 3x + 5
   Each term of the polynomial can be represented as a pair of integers (coefficient,exponent). The polynomial itself is then a list of such pairs.
   We have the following constraints to guarantee that each polynomial has a unique representation:
   Terms are sorted in descending order of exponent
   No term has a zero cofficient
   No two terms have the same exponent
   Exponents are always nonnegative
   For example, the polynomial introduced earlier is represented as:
   [(3,4),(-17,2),(-3,1),(5,0)]
   The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.
   Write Python functions for the following operations:
      addpoly(p1,p2)
      multpoly(p1,p2)
   that add and multiply two polynomials, respectively.

   You may assume that the inputs to these functions follow the representation given above. Correspondingly, the outputs from these functions should also obey the same constraints.
   You can write auxiliary functions to "clean up" polynomials – e.g., remove zero coefficient terms, combine like terms, sort by exponent etc.
   Build a library of functions that can be combined to achieve the desired format.
   You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation, and then convert back.
   Some examples:
  
>>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
   [(2, 1),(3, 0)]
   Explanation: (4x^3 + 3) + (-4x^3 + 2x) = 2x + 3

>>> addpoly([(2,1)],[(-2,1)])
   []
   Explanation: 2x + (-2x) = 0

>>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
   [(1, 3),(-1, 0)]
   Explanation: (x - 1) * (x^2 + x + 1) = x^3 - 1
