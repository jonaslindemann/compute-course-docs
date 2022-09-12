Python extra material
=====================

Installing py5
--------------

**py5** is a package for creative programming in Python. The package has complicated dependencies, so it is recommended to install the package in a Python environment. 

Creating a environment for py5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open an Anaconda prompt and run the following commands:::

    $ conda create -n py5 python=3.10
    Collecting package metadata (current_repodata.json): done
    Solving environment: done

    ...

    xz                 pkgs/main/win-64::xz-5.2.5-h8cc25b3_1
    zlib               pkgs/main/win-64::zlib-1.2.12-h8cc25b3_2


    Proceed ([y]/n)?

Press enter to accept the installation settings. 

Installing py5
^^^^^^^^^^^^^^

Before installing **py5** we have to activate the previously environment:::

    $ conda activate py5

We can now install **py5** using pip:::

    $ pip install py5
    Collecting py5
    ...
    Installing collected packages: wcwidth, pywin32, pytz, pure-eval, pickleshare, line-profiler, executing, backcall, widgetsnbextension, urllib3, traitlets, tornado, toml, stackprinter, six, pyzmq, pyparsing, pygments, pycodestyle, psutil, prompt-toolkit, pillow, parso, numpy, nest-asyncio, jupyterlab-widgets, jpype1, idna, entrypoints, decorator, debugpy, colorama, charset-normalizer, requests, python-dateutil, packaging, matplotlib-inline, jupyter-core, jedi, autopep8, asttokens, stack-data, pandas, jupyter-client, ipython, ipykernel, ipywidgets, py5

Next, we need to install the Java runtime:::

    $ pip install install-jdk
    Collecting install-jdk
      Using cached install_jdk-0.3.0-py3-none-any.whl
    Installing collected packages: install-jdk
    Successfully installed install-jdk-0.3.0
    $ python -c "import jdk; print('Java installed to', jdk.install('17'))"

For this to work you need to set the **JAVA_HOME** environment variable to the location returned from the last command. Restart the terminal and reactivate the **py5** environment to run the examples.

For more informaton on installing **py5**, see:

http://py5.ixora.io/content/install.html#

