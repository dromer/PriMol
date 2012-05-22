This project focuses on controlling the [Pymol](http://www.pymol.org) UI using kinect gestures.

## Software Used

* [libfreenect](http://openkinect.org) (library for accessing the Microsoft Kinect USB camera)
* [OpenNI](http://openni.org/) (Natural Interface library that interprets the kinect data)
* [PyOpenNI](https://github.com/jmendeth/PyOpenNI) (python bindings for OpenNI)
* [Pymol](http://www.pymol.org/) (molecular viewer with python scripting)

Make sure to use the unstable branch of OpenNI.

## Usage

Make sure your kinect is working. Try running freenect-glview to see if the kinect can fully see you.

Start pymol, load a molecule of your choosing and set the view as you like.

Run the script inside pymol ( '''pymol> run primol.py''' ) and calibrate with the 'Psi' position. Which looks something like this:

     | O |
      \|/  
       |  
      / \  
      | |  

When the calibration is done you can turn the molecule along the z and y axis by moving your hands.

Moving your hands apart will zoom the molecule.

## More Info

http://wiki.techinc.nl/index.php/PriMol
