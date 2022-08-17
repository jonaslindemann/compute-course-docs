General
=======

P.1
---

Given the following list:

.. code-block:: Python

    l = ['a', 2, 7, 3.0, 4.5]

Using the print()-statement på print out the last item in the list without directly giving the last index in
the list.

P.2
---

Given the following list:

.. code-block:: Python

    l = [1, 2, 3, 4, 5, 6, 7]

Assign a new list l2 that contains all values except the first value in the list. The answer should be able to
be applied to arbitrary lists. Print the response using print().

P.3
---

Given the list:

.. code-block:: Python

    l = [67, 87, 34, 67, 99]

Assign a new list l2 that contains all items except the last and first values from L. Print the list with the print()-statement.

P.4
---

Given the list:

.. code-block:: Python

    l = [67, 87, 34, 67, 99]

Add the value 100 to the last in the list.

P.5
---

Given the list:

.. code-block:: Python

    l = [67, 87, 34, 67, 99]

Insert the value 52 first in the list.

P.6
---

Given the list:

.. code-block:: Python

    l = [67, 87, 34, 67, 99]

Insert the value -27 between 87 and 34.

P.7
---

Given the list:

.. code-block:: Python

    l = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]

Remove first occurrence of "Per".

P.8
---

Given the list:

.. code-block:: Python

    l = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]

Use the del function to remove "Sven".

P.9
---

Given the following list:

.. code-block:: Python

    l = ["Arne", "Per", "Sven", "Nils", "Bill", "Per"]

Delete the first two names in the list.

P.10
----

Create a nested list of five rows and six columns where all items have a value of 42. Use print() to print the value of the position (2,2).

P.11
----

Create a dictionary, phone_book, with the following keys and values:

.. code-block::

    Arne, 47329823
    Bengt, 91238129
    Stina, 1928319
    Lena, 98129312

P.12
----

Enter the range() statement for the sequence 2, 5, 8

P.13
----

Type a for statement that iterates over the l:

.. code-block:: Python

    l = [45, 78, 90, 34, 23]

Without using a range()-statement. Print each value in the list.

P.14
----

Create a for statement to iterate over the list in 13, but use a for loop with a range() function.

P.15
----

Write a for-statement that iterates over every other value in the list in task 13.

P.16
----

Write a program that summarizes values from the lists, a, and b. The sum from the lists shall be assigned to list c, which shall be the same length as a and b at the end of the programme. Print the list c.

.. code-block:: Python

    a = [3, 6, 8, 10, 34, 32]
    b = [76, 45, 10, 6, 89, 11]

Tip: Use the zip()-function.

P.17
----

Write a program that iterates and prints all the elements in the following nested list:
nested_list = [[1, 2, 3], [4, 5, 6, 7, 8, 9], [10, 11]]

P.18
----

Write a program that iterates from 2 to 100 and for each number in the series and prints if it is a prime number or not.

If a number n is a prime number, it can be determined by dividing this by all numbers from 2 to sqrt (n). If any remnant of the division becomes 0, n is not a prime number. The remainder of a division can be determined using the modulo operator, %, in Python. Use break to cancel a loop when the rest becomes 0.

P.19
----

Convert the program in P. 18 to use a function that returns True if n is a prime number; otherwise False. Also, write code to calculate the prime numbers between 2 to 100 by iterating and calling the function.

P.20
----

Write a function that assigns all values in a list 0 if these are less than 0. To test the function, the following code can create a list of random numbers:

.. code-block:: Python

    from random import randint
    l = [randint(-100,101) for i in range(100)]

The randint(a, b)-function returns a random number k between a < = k < b.
The list provided as an argument should be modified in place. The function should not return a new list.

P.21*
-----

Functions can be given as an argument just like any other datatype in Python. Implement a function to differentiate numerically according to the formula:

The function should take a function as input and the parameters x and h. Write a main application that calls the function with f(x)=sin(x) and calculates f’(x) when x=2.0.

P.22*
-----

Implement a function to create function tables of a particular function. The function shall, as input parameters, take the starting and ending values, stride length and the function to be plotted. An example of printing is shown below for the function f(x) = sin(x):

.. code-block:: 

    x f(x)
    -6.2832 0.0000
    -6.1832 0.0998
    -6.0832 0.1987
    -5.9832 0.2955

Use the .format()-function to print the formatting.

P.23*
-----

Write the following list to file:

.. code-block:: Python

    l = [
        [45, 78, 56, 34],
        [9, 23, 23],
        [34, 87],
        [12, 19, 78, 56, 45]
    ]

Each nested list should be written to a separate line, i.e. The final file must contain:

.. code-block:: 

    45 78 56 34
    9 23 23
    34 87
    12 19 78 56 45

Use the with statement to ensure that .close() is called. Be aware that values must be converted to
strings before they are written to the file. This can be done using the str()-function. A new line is obtained by using the. Write ("\n") method on the Object object.

P.24*
-----

Write a program that loads the file from P.23 and stores the values in a list with the same structure. Text strings can be split with respect to spaces by using the method .split() method. Values stored in strings can be converted to values by using the int()-function.

P.25
----

In this example, we will open and read a CSV file with the outbreak data from a geyser. The file can be downloaded from:

https://github.com/jonaslindemann/guide_to_python/blob/master/exercises/faithful.csv.

The file begins with a "header" line and is followed by the data separated by commas into three columns according to:

.. code-block:: 

    "Index", "Eruption length (mins)","Eruption wait (mins)"
    1, 3.600, 79
    2, 1.800, 54
    3, 3.333, 74
    ...

Type a function read_data(filename) that loads the CSV file and converts it into a nested list, where each row consists of a list of three values corresponding to the columns contained in the file. The function should return the header line and a list of the loaded data.

Type a function query_data(table, t), which extracts all rows in the table list that exceed T minutes in the outbreak time. The function returns a new list with the rows that exceed t; otherwise, the format is the same as the loaded list.

Type a function write_data(header, table, filename) that writes a new CSV file with the same structure as the loaded file.

Type a main program that loads faithful.csv, extracts outbreaks above 4.5 degrees, and writes the results to the faithful_max_4_5.csv file.

P.26
----

Add error handling routines to task P.24 and P.25.


