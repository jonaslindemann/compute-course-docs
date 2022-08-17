ParaView
========

Datafiles and additional python modules can be found here:

https://github.com/jonaslindemann/compute-course-public/tree/master/dataviz

P.47
----

In this exercise we will generate one scalar and one vector field using perlin noise. The fields can be
created by using the following code:

.. code-block:: Python

    # -*- coding: utf-8 -*-

    import numpy as np
    import matplotlib.pyplot as plt
    import perlin2d as pn
    import pyvtk as vtk

    if __name__ == "__main__":
        noise = pn.generate_perlin_noise_2d((256, 256), (8, 8)).reshape(256*256,)
        noise_x = pn.generate_perlin_noise_2d((256, 256), (8, 8)).reshape(256*256,1)
        noise_y = pn.generate_perlin_noise_2d((256, 256), (8, 8)).reshape(256*256,1)

The perlin2d module is provided in the assignment. The vector field can be created by combining the
noise_x and noise_y using:

.. code-block:: Python

    vectors = np.hstack((noise_x, noise_y, np.zeros((256*256,1))))

Using the pyvtk module to export the numpy arrays as a 256 x 256 structured points field
(vtk.StructuredPoints) with scalars and vector fields attached to the nodes. 

Some useful filters are:

**WarpByScalar** – Warps a 2D field in Z-direction by applying a scale factor.
**Glyph** – Creates a vector field visualization using glyphs.
**ExtractSurface** – Creates a 3D surface from a 2D field.
**GenerateSurfaceNormals** – Calculates Surface normal from a 3D surface.
**Transform** – Translates a node in X, Y, Z direction.
**Contour** - Creates contourlines/surfaces from.

A final visualisation is shown below:

P.48
----

In this exercise we will generate one scalar and one vector field in 3D using perlin noise. The fields can be created by using the following code:

.. code-block:: Python

    # -*- coding: utf-8 -*-

    import numpy as np
    import matplotlib.pyplot as plt
    import perlin3d as pn
    import pyvtk as vtk

    if __name__ == "__main__":
        noise = pn.generate_perlin_noise_3d((64, 64, 64), (8, 8, 8)).reshape(64*64*64,)
        noise_x = pn.generate_perlin_noise_3d((64, 64, 64), (4, 4, 4)).reshape(64*64*64,1)
        noise_y = pn.generate_perlin_noise_3d((64, 64, 64), (4, 4, 4)).reshape(64*64*64,1)
        noise_z = pn.generate_perlin_noise_3d((64, 64, 64), (4, 4, 4)).reshape(64*64*64,1)

The perlin3d module is provided in the assignment. The vector field can be created by combining the
noise_x, noise_z and noise_y using:

.. code-block:: Python

    vectors = np.hstack((noise_x, noise_y, noise_z))

Using the pyvtk module to export the numpy arrays as a 64 x 64 x 64 structured points field
(vtk.StructuredPoints) with scalars and vector fields attached to the nodes. An example visualization is shown in the last section.

Some useful filters are:

**Glyph** – Creates a vector field visualization using glyphs.
**StreamTracer** – Creates stream lines. Use “Seed Type” “Point Source”. Give a radius that covers your data volyme
**Tube** – Attached to a StreamTracer will create solid stream lines, which often look better.
**Clip** - Clips the data volume using a plane. Can be used to see inside.

The final result can look like the following image: