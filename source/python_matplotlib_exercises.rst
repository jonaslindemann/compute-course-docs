Matplotlib exercises
====================

P.40
----

Plot np.sin(x), np.cos(x), np.tan(x) and np.arctan(x) in a single figure using the plt.subplot() command. Set suitable y-limits for the different plots and give each plot its own title.

P.41
----

Square waves can be formed by summing sine waves of odd harmonics. For example:

.. code-block:: python

    t = np.linspace(-2*np.pi, 2*np.pi)
    y = np.sin(t) + np.sin(3*t)/3 + np.sin(5*t)/5 + np.sin(7*t)/7

Or as a sum of

    np.sin(k*t)/k, where k = 1, 3, 5, 7, …

Plot all sums from k = 1 to k = 19 in a single plot
Add labels and titles to the diagram.

P.42
----

Plot the function f(x,y) = sin(x*y/4.0) as a contour plot (plt.contour()) and a filled contour (plt.contourf()) plot in separate figures. Plot range should be from -2*pi to 2*pi in both x and y directions. Each plot should have 10 contour levels. Add labels and titles to the diagram.

P.43
----

Plot the function f(x,y) = sin(x*y/4.0) as a 3D surface. Plot range should be from -2*pi to 2*pi in both x and y directions. 3D surface plots can be created by adding the following imports:

.. code-block:: python

    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt
    from matplotlib import cm

An axes object has to be created to activate 3d-plotting in the current figure.

.. code-block:: python

    fig = plt.figure()
    ax = plt.axes(projection='3d')

The ax.plot_surface() method can the be used to plot the surface. See also lecture slides and the
documentation for plot_surface() in the matplotlib documentation.