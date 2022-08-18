NumPy
=====

P.27
----

Create the following one-dimensional arrays in NumPy:

a) Integer array with the following content:

.. code-block:: Python

    [1 2 3]

b) Floating-point array with the following appearance:

.. code-block:: Python

    [1.0 2.0 3.0 4.0 5.0 6.0 7.0]

P.28
----

Create the following two-dimensional arrays in NumPy:

a) Integer array with the following appearance:

.. math::

    \begin{bmatrix}
    1 \\ 
    2 \\
    3 \\
    4 \\
    \end{bmatrix}

b) floating point arry with the following appearance:

.. math::

    \begin{bmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9 \\
    \end{bmatrix}

P.29
----

Write code to print all information about the following array:

.. code-block:: Python

    b = np.array([[1, 2, 3], [4, 5, 6]], float)

P.30
----

Change the shape of the following array to a one-dimensional array:

.. code-block:: Python

    a = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]) 

P.31
----

Create a new array b based on a with the 12 x 12 dimension.

.. code-block:: Python

    a = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

P.32
----

Create a 5 x 5 floating-point array filled with zeros.

P.33
----

Create a 10 x 10 integer array filled with ones.

P.34
----

Create a 10 x 5 integer array in which all elements have a value of 27.

P.35
----

Create the following array by using the np.arange() function:

.. code-block:: Python

    [[ 10 11 12 13 14]
     [ 15 16 17 18 19]
     [ 20 21 22 23 24]
     [ 25 26 27 28 29]
     [ 30 31 32 33 34]
     [ 35 36 37 38 39]
     [ 40 41 42 43 44]
     [ 45 46 47 48 49]
     [ 50 51 52 53 54]
     [ 55 56 57 58 59]
     [ 60 61 62 63 64]
     [ 65 66 67 68 69]
     [ 70 71 72 73 74]
     [ 75 76 77 78 79]
     [ 80 81 82 83 84]
     [ 85 86 87 88 89]
     [ 90 91 92 93 94]
     [ 95 96 97 98 99]
     [100 101 102 103 104]
     [105 106 107 108 109]]

The array can be created with a single statement in NumPy.

P.36
----

Create the following array with a single statement in NumPy.

.. code-block:: Python

    [[1. 0. 0. 0. 0. 0.]
     [0. 1. 0. 0. 0. 0.]
     [0. 0. 1. 0. 0. 0.]
     [0. 0. 0. 1. 0. 0.]
     [0. 0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 0. 1.]] 

P.37*
-----

Create an array of 100 values ranging from –π to π. Start and end values must be included in the array. The value of π can be obtained in NumPy with np.pi. (np is NumPy-import-prefix.)

P.38*
-----

Given the following matrices:

.. code-block:: Python

    A = np.random.randint(0, 100, [5, 5])
    B = np.random.randint(0, 100, [5, 5])

Create a new array, C, which is the matrix multiplication of AB.

P.39*
-----

Given the following array:

    [[ 0 1 2 3 4 5]
     [ 6 7 8 9 10 11]
     [12 13 14 15 16 17]
     [18 19 20 21 22 23]
     [24 25 26 27 28 29]
     [30 31 32 33 34 35]]

    # a = np.arange(36).reshape(6,6)

Write expression that returns:

a) the value of row 2, column 2
b) row 3
c) column 4
d) the last row
e) the last column
