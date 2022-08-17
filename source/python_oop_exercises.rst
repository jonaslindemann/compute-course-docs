Object-oriented Programming
===========================

P.45
----

Use the base classes from the lecture and implement a Rectangle class with the additional attributes
width and height.

Implement a Polyline class that can handle a set of Point derived objects. The class should have methods for adding, removing and clearing the points. It should also have a methods or properties for accessing the Point-objects in the class.

All classes should implement the __str__() method for printing a description of the object.
Write an example tha illustrates the use of your new classes.

Use the code from the lecture as a base for the assignment.

P.46
----

Implement a class, Geyser, which implements the functionality of assignment P.25. The class constructor should have an argument, filename, which is stored as a member variable self.filename. The constructor should also call the read_data() method to read data. read_data() function is implemented as a member function, reading the data and storing the read table as a member variable. The query_data() method takes single argument t (time of eruption) and returns a nested list of the eruptions longer than t.

The class should be able to be used like in the code below:

.. code-block:: Python

    geyser = Geyser("faithful.csv")
    print(geyser.data_table)
    result_table = geyser.query_data(4.5)
    print(result_table)


