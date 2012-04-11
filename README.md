This project focuses on controlling the [Pymol](http://www.pymol.org) UI using kinect gestures.

## Software Used

* [libfreenect](http://openkinect.org) (library for accessing the Microsoft Kinect USB camera)
* [OpenNI](http://openni.org/) (Natural Interface library that interprets the kinect data)
* [PyOpenNI](https://github.com/jmendeth/PyOpenNI) (python bindings for OpenNI)
* [Pymol](http://www.pymol.org/) (molecular viewer with python scripting)

Make sure to use the unstable branch of OpenNI.

## Usage

Start pymol, load a molecule of your choosing and set the view as you like.
Run the script inside pymol and calibrate with the 'Psi' position.
Which is something like this:  
```
| o |  
 \|/  
  |  
 / \  
 | |  
```
When the calibration is done you can turn the molecule along the z and y axis.


## More Info
http://wiki.techinc.nl/index.php?title=Pymol-Kinect
