# Assignments
Weekly Assignments of Programming, Data Structures And Algorithms Using Python (NPTEL  course)

# Week 2

1.  A positive integer m can be expresseed as the sum of three squares if it is of the form p + q + r where p, q, r ≥ 0, and p, q, r are all perfect squares. For instance, 2 can be written as 0+1+1 but 7 cannot be expressed as the sum of three squares. The first numbers that cannot be expressed as the sum of three squares are 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, … (see Legendre's three-square theorem).

Write a Python function threesquares(m) that takes an integer m as input and returns True if m can be expressed as the sum of three squares and False otherwise. (If m is not positive, your function should return False.)

     Here are some examples of how your function should work.
>>> threesquares(6)           True

>>> threesquares(188)         False

>>> threesquares(1000)        True


2.  Write a function repfree(s) that takes as input a string s and checks whether any character appears more than once. The function should return True if there are no repetitions and False otherwise.

     Here are some examples to show how your function should work.
     
>>> repfree("zb%78")          True

>>> repfree("(7)(a")          False

>>> repfree("a)*(?")          True

>>> repfree("abracadabra")    False


3.  A list of numbers is said to be a hill if it consists of an ascending sequence followed by a descending sequence, where each of the sequences is of range at least two. Similarly, a list of numbers is said to be a valley hill if it consists of an descending sequence followed by an ascending sequence. You can assume that consecutive numbers in the input sequence are always different from each other.

Write a Python function hillvalley(l) that takes a list l of integers and returns True if it is a hill or a valley, and False otherwise.

     Here are some examples to show how your function should work.

>>> hillvalley([1,2,3,5,4])               True

>>> hillvalley([1,2,3,4,5])               False

>>> hillvalley([5,4,1,2,3])               True

>>> hillvalley([5,4,3,2,1])               False

>>> hillvalley([1,2,3,4,5,3,2,4,5,3,2,1]) False


# Week 3

1.  Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the first occurrence of each number.

>>> print(remdup([3,1,3,5]))

[3, 1, 5]

>>> print(remdup([7,3,-1,-5]))

[7, 3, -1, -5]

>>> print(remdup([3,5,7,5,3,7,10])) 

[3, 5, 7, 10]


2.  Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.

Here are some examples to show how your function should work.

>>> print(sumsquare([1,3,5]))

[35, 0]

>>> print(sumsquare([2,4,6]))

[0, 56]

>>> print(sumsquare([-1,-2,3,7]))

[59, 4]



3.  A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

1  2  3  4

5  6  7  8

would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].

The transpose of a matrix converts each row into a column. The transpose of the matrix above is:

1  5

2  6

3  7

4  8

which would be represented as [[1, 5], [2, 6], [3, 7], [4, 8]].

Write a Python function transpose(m) that takes as input a two dimensional matrix m and returns the transpose of m. The argument m should remain undisturbed by the function. Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

>>> print(transpose([[1,2,3],[4,5,6]]))

[[1, 4], [2, 5], [3, 6]]

>>> print(transpose([[1],[2],[3]]))

[[1, 2, 3]]

>>> print(transpose([[3]]))

[[3]]

# Week 4

1.  We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:

   { 'match1':{'player1': 57, 'player2': 38},
     'match2':{'player3': 9 , 'player1': 42},
     'match3':{'player2': 41, 'player4': 63 , 'player3': 91 }

Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not fixed (here they are 'match1', 'match2', 'match3'), nor are the names of the players. A player need not have a score recorded in all matches. Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, and topscore is an integer, the total score of playername. The input will be such that there are never any ties for highest total score.
     
     For instance:

>>> orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})

('player3', 100)

>>> orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'Ashwin':59, 'Pujara':42}})

('Ashwin', 143)


2.  Let us consider polynomials in a single variable x with integer coefficients.
     
     For instance:
     
3x4 - 17x2 - 3x + 5

Each term of the polynomial can be represented as a pair of integers (coefficient,exponent). The polynomial itself is then a list of such pairs.

We have the following constraints to guarantee that each polynomial has a unique representation:
     1. Terms are sorted in descending order of exponent
     2. No term has a zero cofficient
     3. No two terms have the same exponent
     4. Exponents are always nonnegative

For example, the polynomial introduced earlier is represented as:

[(3,4),(-17,2),(-3,1),(5,0)]

The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.

Write Python functions for the following operations:
addpoly(p1,p2)
multpoly(p1,p2)
that add and multiply two polynomials, respectively.

You may assume that the inputs to these functions follow the representation given above. Correspondingly, the outputs from these functions should also obey the same constraints. You can write auxiliary functions to "clean up" polynomials – e.g., remove zero coefficient terms, combine like terms, sort by exponent etc. Build a library of functions that can be combined to achieve the desired format. You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation, and then convert back.

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



# Week 5


1.  The library at the Hogwarts School of Witchcraft and Wizardry has computerized its book issuing process. The relevant information is provided as text from standard input in three parts: information about books, information about borrowers and information about checkouts. Each part has a specific line format, described below.

     1. Information about books

        Line format: Accession Number~Title

     2. Information about borrowers

        Line format: Username~Full Name

     3. Information about checkouts

        Line format: Username~ Accession Number ~Due Date

        Note: Due Date is in YYYY-MM-DD format.

You may assume that the data is internally consistent. For every checkout, there is a corresponding username and accession number in the input data, and no book is simultaneously checked out by two people.

Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Books. The second section begins with a line containing Borrowers. The third section begins with a line containing Checkouts. The end of the input is marked by a line containing EndOfInput.

Write a Python program to read the data as described above and print out details about books that have been checked out.

Each line should describe to one currently issued book in the following format:

>>> Due Date~Full Name~Accession Number~Title

Your output should be sorted in increasing order of due date.

For books due on the same date, sort in increasing order of full name.

If the due date and full name are both the same, sort based on the accession number, and, finally, the title of the book.


Here is a sample input and its corresponding output.

Test case 1 :


Sample Input

Books

     APM-001~Advanced Potion-Making

     GWG-001~Gadding With Ghouls

     APM-002~Advanced Potion-Making

     DMT-001~Defensive Magical Theory

     DMT-003~Defensive Magical Theory

     GWG-002~Gadding With Ghouls

     DMT-002~Defensive Magical Theory

Borrowers

     SLY2301~Hannah Abbott

     SLY2302~Euan Abercrombie

     SLY2303~Stewart Ackerley

     SLY2304~Bertram Aubrey

     SLY2305~Avery

     SLY2306~Malcolm Baddock

     SLY2307~Marcus Belby

     SLY2308~Katie Bell

     SLY2309~Sirius Orion Black

Checkouts

     SLY2304~DMT-002~2019-03-27

     SLY2301~GWG-001~2019-03-27

     SLY2308~APM-002~2019-03-14

     SLY2303~DMT-001~2019-04-03

     SLY2301~GWG-002~2019-04-03

EndOfInput

Sample Output

     2019-03-14~Katie Bell~APM-002~Advanced Potion-Making

     2019-03-27~Bertram Aubrey~DMT-002~Defensive Magical Theory

     2019-03-27~Hannah Abbott~GWG-001~Gadding With Ghouls

     2019-04-03~Hannah Abbott~GWG-002~Gadding With Ghouls

     2019-04-03~Stewart Ackerley~DMT-001~Defensive Magical Theory



Test case 2 :


Books

     GTF-001~A Beginner's Guide to Transfiguration

     GTF-002~A Beginner's Guide to Transfiguration

     GTF-003~A Beginner's Guide to Transfiguration

     WET-001~Great Wizarding Events of the Twentieth Century

     WET-002~Great Wizarding Events of the Twentieth Century

     WTC-001~Great Wizards of the Twentieth Century

     WTC-002~Great Wizards of the Twentieth Century

     WTC-003~Great Wizards of the Twentieth Century

     WTC-004~Great Wizards of the Twentieth Century

     IBI-001~Invisible Book of Invisibility

     IBI-002~Invisible Book of Invisibility

     JFJ-001~Jinxes for the Jinxed

     JFJ-002~Jinxes for the Jinxed

     LDM-001~Men Who Love Dragons Too Much

     LDM-002~Men Who Love Dragons Too Much

     LDM-003~Men Who Love Dragons Too Much

     NTN-001~New Theory of Numerology

     MFM-001~One Minute Feasts - It's Magic!

     PYN-001~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up

     PYN-002~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up

     PYN-003~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up

     PDM-001~Practical Defensive Magic and Its Use Against the Dark Arts

     PDM-002~Practical Defensive Magic and Its Use Against the Dark Arts

     PDM-003~Practical Defensive Magic and Its Use Against the Dark Arts

     PDM-004~Practical Defensive Magic and Its Use Against the Dark Arts

     QAQ-001~Quintessence: A Quest

     QAQ-002~Quintessence: A Quest

     STS-001~Saucy Tricks for Tricky Sorts

     STS-002~Saucy Tricks for Tricky Sorts

     STS-003~Saucy Tricks for Tricky Sorts

     STS-004~Saucy Tricks for Tricky Sorts

Borrowers

     SLY2301~Hannah Abbott

     SLY2307~Marcus Belby

     SLY2311~Susan Bones

     SLY2313~Eleanor Branstone

     SLY2319~Eddie Carmichael

     GRF3703~Dennis Creevey

     GRF3708~J. Dorny

     GRF3715~Basil Fronsac

     RAV4308~Olive Hornby

     RAV4309~Angelina Johnson

     RAV5902~Isobel MacDougal

     RAV5905~Laura Madley

     RAV5906~Draco Malfoy

     RAV5907~Natalie McDonald

     GRF9104~Lily Moon

     GRF9107~Garrick Ollivander

Checkouts

     RAV5906~GTF-001~2019-03-22

     GRF3708~GTF-002~2019-03-26

     SLY2307~GTF-003~2019-03-01

     GRF3708~WET-001~2019-03-06

     SLY2301~WET-002~2019-03-23

     SLY2307~WTC-001~2019-02-26

     SLY2311~WTC-002~2019-03-12

     SLY2313~WTC-003~2019-03-06

     SLY2301~WTC-004~2019-03-12

     RAV5906~IBI-001~2019-03-12

     SLY2307~IBI-002~2019-03-23

     GRF3715~JFJ-001~2019-03-23

     RAV5905~JFJ-002~2019-03-16

     SLY2311~LDM-001~2019-02-26

     RAV4308~LDM-002~2019-03-20

     SLY2307~LDM-003~2019-03-22

     GRF3703~NTN-001~2019-03-09

     RAV4308~MFM-001~2019-03-07

     SLY2311~PYN-001~2019-03-03

     RAV5902~PYN-002~2019-03-02

     GRF9104~PYN-003~2019-03-16

     GRF3708~PDM-001~2019-03-13

     RAV5907~PDM-002~2019-03-26

     SLY2307~PDM-003~2019-02-26

     SLY2313~PDM-004~2019-03-01

     RAV4309~QAQ-001~2019-03-14

     RAV5907~QAQ-002~2019-03-17

     RAV5905~STS-001~2019-03-12

     SLY2319~STS-002~2019-03-11

     GRF3703~STS-003~2019-03-19

     RAV5907~STS-004~2019-03-17

EndOfInput


Sample Output

     2019-02-26~Marcus Belby~PDM-003~Practical Defensive Magic and Its Use Against the Dark Arts

     2019-02-26~Marcus Belby~WTC-001~Great Wizards of the Twentieth Century

     2019-02-26~Susan Bones~LDM-001~Men Who Love Dragons Too Much

     2019-03-01~Eleanor Branstone~PDM-004~Practical Defensive Magic and Its Use Against the Dark Arts

     2019-03-01~Marcus Belby~GTF-003~A Beginner's Guide to Transfiguration

     2019-03-02~Isobel MacDougal~PYN-002~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up

     2019-03-03~Susan Bones~PYN-001~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up

     2019-03-06~Eleanor Branstone~WTC-003~Great Wizards of the Twentieth Century

     2019-03-06~J. Dorny~WET-001~Great Wizarding Events of the Twentieth Century

     2019-03-07~Olive Hornby~MFM-001~One Minute Feasts - It's Magic!

     2019-03-09~Dennis Creevey~NTN-001~New Theory of Numerology

     2019-03-11~Eddie Carmichael~STS-002~Saucy Tricks for Tricky Sorts

     2019-03-12~Draco Malfoy~IBI-001~Invisible Book of Invisibility

     2019-03-12~Hannah Abbott~WTC-004~Great Wizards of the Twentieth Century

     2019-03-12~Laura Madley~STS-001~Saucy Tricks for Tricky Sorts

     2019-03-12~Susan Bones~WTC-002~Great Wizards of the Twentieth Century

     2019-03-13~J. Dorny~PDM-001~Practical Defensive Magic and Its Use Against the Dark Arts

     2019-03-14~Angelina Johnson~QAQ-001~Quintessence: A Quest

     2019-03-16~Laura Madley~JFJ-002~Jinxes for the Jinxed

     2019-03-16~Lily Moon~PYN-003~Powers You Never Knew You Had and What To Do With Them Now You've Wised Up

     2019-03-17~Natalie McDonald~QAQ-002~Quintessence: A Quest

     2019-03-17~Natalie McDonald~STS-004~Saucy Tricks for Tricky Sorts

     2019-03-19~Dennis Creevey~STS-003~Saucy Tricks for Tricky Sorts

     2019-03-20~Olive Hornby~LDM-002~Men Who Love Dragons Too Much

     2019-03-22~Draco Malfoy~GTF-001~A Beginner's Guide to Transfiguration

     2019-03-22~Marcus Belby~LDM-003~Men Who Love Dragons Too Much

     2019-03-23~Basil Fronsac~JFJ-001~Jinxes for the Jinxed

     2019-03-23~Hannah Abbott~WET-002~Great Wizarding Events of the Twentieth Century

     2019-03-23~Marcus Belby~IBI-002~Invisible Book of Invisibility

     2019-03-26~J. Dorny~GTF-002~A Beginner's Guide to Transfiguration

     2019-03-26~Natalie McDonald~PDM-002~Practical Defensive Magic and Its Use Against the Dark Arts



# Week 8


1. IOI Training Camp 20xx   (INOI 2011)

We are well into the 21st century and school children are taught dynamic programming in class 4. The IOI training camp has degenerated into an endless sequence of tests, with negative marking. At the end of the camp, each student is evaluated based on the sum of the best contiguous segment (i.e., no gaps) of marks in the overall sequence of tests. Students, however, have not changed much over the years and they have asked for some relaxation in the evaluation procedure. As a concession, the camp coordinators have agreed that students are allowed to drop upto a certain number of tests when calculating their best segment. For instance, suppose that Lavanya is a student at the training camp and there have been ten tests, in which her marks are as follows.

Test	  1  	   2  	  3  	   4  	  5  	   6  	   7  	   8  	   9  	  10  

Marks	  6  	  -5  	  3  	  -7  	  6  	  -1  	  10  	  -8  	  -8  	  8  

In this case, without being allowed to drop any tests, the best segment is tests 5–7, which yields a total of 15 marks. If Lavanya is allowed to drop upto 2 tests in a segment, the best segment is tests 1–7, which yields a total of 24 marks after dropping tests 2 and 4. If she is allowed to drop upto 6 tests in a segment, the best total is obtained by taking the entire list and dropping the 5 negative entries to get a total of 33. You will be given a sequence of N test marks and a number K. You have to compute the sum of the best segment in the sequence when upto K marks may be dropped from the segment.

Solution hint

For 1 ≤ i ≤ N, 1 ≤ j ≤ K, let Best[i][j] denote the maximum segment ending at position i with at most j marks dropped. Best[i][0] is the classical maximum subsegment or maximum subarray problem. For j ≥ 1; inductively compute Best[i][j] from Best[i][j-1].

Input format

The first line of input contains two integers N and K, where N is the number of tests for which marks will be provided and K is the limit of how many entries may be dropped from a segment.

This is followed by N lines of input each containing a single integer. The marks for test i, i ∈ {1,2,…,N} are provided in line i+1.

Output format

The output is a single number, the maximum marks that can be obtained from a segment in which upto K values are dropped.

Constraints

You may assume that 1 ≤ N ≤ 104 and 0 ≤ K ≤ 102. The marks for each test lie in the range [-104 … 104]. In 40% of the cases you may assume N ≤ 250.

Example:

We now illustrate the input and output formats using the example described above.

Sample input:
    
    10 2
    
    6
    
    -5
    
    3
    
    -7
    
    6
    
    -1
    
    10
    
    -8
    
    -8
    
    8

Sample output:
    
    24
