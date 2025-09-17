Installing Conda-Forge on macOS
-------------------------------

This document provides a step-by-step guide to installing Conda-Forge on macOS. Conda-Forge is a community-driven collection of conda packages that are built and maintained by the community. 

Step 1: Downloading Conda-Forge installer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Go to the `Conda-Forge page <https://conda-forge.org>`_ and download the Anaconda installer for Windows.

.. image:: images/cf-install-mac-01.png
   :alt: Conda-Forge homepage

Click on the button **Download Installer**.

.. image:: images/cf-install-mac-02.png
   :alt: Conda-Forge homepage

In this step it is important to now if you are using a Intel- or Apple Silicon Mac. If you are using a Intel Mac, click on the **macOS** Button to download the installer for Intel Macs. If you are using an Apple Silicon Mac, click on the **Apple Silicon** Button to download the installer for Apple Silicon Macs.

Step 2: Installing Conda-Forge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the download completed the installation needs to be completed in a Terminal. To open a Terminal, press **Command** + **Space** and type in **Terminal**. This will open the Terminal application.

In the terminal we need to navigate to the folder where the installer was downloaded. By default, this is the **Downloads** folder. To navigate to the Downloads folder, run the following command in the terminal:

.. code-block:: bash

   cd ~/Downloads

We are now ready to start the installer. The installer is a `.sh` file. To start the installation, run the following command in the terminal:

.. code-block:: bash

   sh Miniforge3-MacOSX-arm64.sh

.. image:: images/cf-install-mac-03.png
   :alt: Conda-Forge installer

When the installer starts it shows the license agreement. To accept the license agreement, we need to move down in the text. To do this, press the **Space** key until the end of the license agreement is reached. After that, type in **yes** and press **Enter** to accept the license agreement.

.. image:: images/cf-install-mac-05.png
   :alt: Conda-Forge installer

Next you will be asked where to install Conda-Forge. By default, it will be installed in the home directory under the folder **miniforge3**. To accept the default location, press **Enter**. If you want to change the location, type in the new location and press **Enter**.

.. image:: images/cf-install-mac-06.png
   :alt: Conda-Forge installer

The installer now downloads the required packages. Finally it asks if you would like to configure the shell to use conda by default. This is recommended, so type in **yes** and press **Enter**.

.. image:: images/cf-install-mac-07.png
   :alt: Conda-Forge installer

The installation is now complete. Before we use the Conda-Forge, we need to restart the terminal. To do this, close the terminal and open it again. 

The new terminal should look like this:

.. image:: images/cf-install-mac-08.png
   :alt: Conda-Forge installer

That is there should be a prompt with `(base)` in front of it. This indicates that the Conda-Forge is installed and ready to use.

Step 3: Creating an environment for this course
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the opened terminal we need to create a new environment for this course. An environment is a self contained Python installation with a set of packages. To create a new environment, run the following command in the terminal:

.. code-block:: bash

   conda create -n vsmn20 python=3.11 numpy=1.26 scipy matplotlib qtpy pyqt

This will create a new environment called `vsmn20` with Python 3.12 and the packages `numpy`, `scipy`, `matplotlib`, `qtpy` and `pyqt`. The command will also install all the dependencies required for these packages. 

.. image:: images/cf-install-mac-11.png
   :alt: Conda-Forge installer

At some point during the installation, you will be asked if you want to proceed with the installation. Type in **y** and press **Enter** to proceed with the installation.

When the installation is complete, you will see a message indicating that the environment has been created and how to activate it.

.. image:: images/cf-install-mac-12.png
   :alt: Conda-Forge installer

To continue our installation with the packages required for this course, we need to activate the environment. To do this, run the following command in the terminal:

.. code-block:: bash

   conda activate vsmn20

This will activate the environment and change the prompt to indicate that the environment is active. The prompt should now look like this:

.. code-block:: bash

   (vsmn20) user@computer:~$

In this environment we now have to install CALFEM for Python. We will use a special package manager called pip to install CALFEM. To do this, run the following command in the terminal:

.. code-block:: bash

   pip install calfem-python
   pip install pyvtk
   pip install pyqt6-tools

If all goes well, you should see a message indicating that CALFEM has been installed successfully.

.. image:: images/cf-install-mac-14.png
   :alt: Conda-Forge installer

Step 4: Testing the installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To test the installation, will open a Python interpreter. To do this, run the following command in the terminal:

.. code-block:: bash

   python

This will open the Python interpreter. The prompt should now look like this:

.. code-block:: bash

   >>> 

On this prompt we type in the following command to import CALFEM:

.. code-block:: python

   >>> import calfem.core as cfc
   >>> help(cfc.beam2e)

This should display the following in the terminal:

.. image:: images/cf-install-mac-15.png
   :alt: Conda-Forge installer

To exit out of this help display press **q**. To exit out of the Python interpreter, type in **exit()** and press **Enter**.

Step 5: Installing Visual Studio Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install Visual Studio Code, go to the `Visual Studio Code page <https://code.visualstudio.com>`_ and download the installer for macOS. Clicking on the Mac download button should automatically select the correct version for your system.

The download comes in the form of a `.zip` file. 

.. image:: images/vc-install-mac-01.png
   :alt: Visual Studio Code homepage

Open the **Downloads** folder. It should look like this:

.. image:: images/vc-install-mac-02.png
   :alt: Visual Studio Code homepage

Double click on the downloaded file. This will extract the contents of the zip file. You should see a new icon called **Visual Studio Code**. 

.. image:: images/vc-install-mac-03.png
   :alt: Visual Studio Code homepage

Drag the **Visual Studio Code** icon to the **Applications** folder. This will copy the application to the Applications folder.

To open Visual Studio Code, go to the **Applications** folder and double click on the **Visual Studio Code** icon. You can also search for Visual Studio Code in the **Spotlight** search by pressing **Command** + **Space** and typing in **Visual Studio Code**.

.. image:: images/vc-install-mac-04.png
   :alt: Visual Studio Code homepage

When you open Visual Studio Code for the first time, you will see a welcome screen. You can close this screen by clicking on the **X** in the top right corner.

Step 6: Installing the Python extension for Visual Studio Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I the left toolbar click on the **Extensions** icon. This will open the extensions view.

.. image:: images/vc-install-10.png
   :alt: Visual Studio Code

In the search box enter **Python**. This will show the Python extension for Visual Studio Code.
Click on the **Install** button to install the extension.

.. image:: images/vc-install-11.png
   :alt: Visual Studio Code

Next, create a new file by clicking on the **File/New file...** in the menu. This will open a file type selection dialog.

.. image:: images/vc-install-13.png
   :alt: Visual Studio Code

In the file type selection dialog select **Python**. This will create a new Python file.

In the next step we will need to select the Python interpreter. This is the Python version that will be used to run the code. To select the Python interpreter, click on the **Select interpreter** icon in the bottom right corner of Visual Studio Code.

.. image:: images/vc-install-14.png
   :alt: Visual Studio Code

This will open a list of available Python interpreters. Select the one that corresponds to the `vsmn20` environment we created earlier. This should be something like `C:\Users\YourUsername\Miniforge3\envs\vsmn20\python.exe`.

.. image:: images/vc-install-15.png
   :alt: Visual Studio Code

When this has been done, everytime you open a Python file in Visual Studio Code, it will show a play button in the top right corner. This will run the code in the file using the selected Python interpreter. Below shows what happens when you click on the play button.

.. image:: images/vc-install-16.png
   :alt: Visual Studio Code

Step 7: Running Qt Designer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you haven't installed the pip packages `pyqt6-tools` and `pyqt6`, you can do this by running the following command in the terminal:

.. code-block:: bash

   pip install pyqt6-tools

This will install the Qt Designer application. To run Qt Designer, run the following command in the terminal:

.. code-block:: bash

   pyqt6-tools designer


