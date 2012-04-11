#!/usr/bin/python
## The equivalent of:
##  "Working with the Skeleton"
## in the OpenNI user guide.

"""
This shows how to identify when a new user is detected, look for a pose for
that user, calibrate the users when they are in the pose, and track them.

Specifically, it prints out the location of the users' head,
as they are tracked.
"""

# Pose to use to calibrate the user
pose_to_use = 'Psi'


from openni import *
from math import *
import time
from pymol import cmd


#cmd.load('01-reference.mol2')


ctx = Context()
ctx.init()

# Create the user generator
user = UserGenerator()
user.create(ctx)

# Obtain the skeleton & pose detection capabilities
skel_cap = user.skeleton_cap
pose_cap = user.pose_detection_cap

# Declare the callbacks
def new_user(src, id):
    print "1/4 User {} detected. Looking for pose..." .format(id)
    pose_cap.start_detection(pose_to_use, id)

def pose_detected(src, pose, id):
    print "2/4 Detected pose {} on user {}. Requesting calibration..." .format(pose,id)
    pose_cap.stop_detection(id)
    skel_cap.request_calibration(id, True)

def calibration_start(src, id):
    print "3/4 Calibration started for user {}." .format(id)

def calibration_complete(src, id, status):
    if status == CALIBRATION_STATUS_OK:
        print "4/4 User {} calibrated successfully! Starting to track." .format(id)
        skel_cap.start_tracking(id)
    else:
        print "ERR User {} failed to calibrate. Restarting process." .format(id)
        new_user(user, id)

def lost_user(src, id):
    print "--- User {} lost." .format(id)

# Register them
user.register_user_cb(new_user, lost_user)
pose_cap.register_pose_detected_cb(pose_detected)
skel_cap.register_c_start_cb(calibration_start)
skel_cap.register_c_complete_cb(calibration_complete)

# Set the profile
skel_cap.set_profile(SKEL_PROFILE_ALL)

# Start generating
ctx.start_generating_all()
print "0/4 Starting to detect users. Press Ctrl-C to exit."

# Accumulated angles
acchor=0
accver=0

while True:
    # Update to next frame
    ctx.wait_and_update_all()

    # Extract head position of each tracked user
    for id in user.users:
        if skel_cap.is_tracking(id):
            lhand = skel_cap.get_joint_position(id, SKEL_LEFT_HAND)
	    rhand = skel_cap.get_joint_position(id, SKEL_RIGHT_HAND)
	    
	    lloc=lhand.point
	    rloc=rhand.point

	    # Distance between hands on each axis
            x=lloc[0]-rloc[0]
            y=lloc[1]-rloc[1]
            z=lloc[2]-rloc[2]

	    # Degrees to turn horizontally or vertically
	    hor=degrees(round(atan2(z, x), 2))-acchor
	    ver=degrees(round(atan2(x, y), 2))-accver
	    acchor+=hor
	    accver+=ver

	    cmd.turn('y', hor)
	    cmd.turn('z', ver)

	    # Refresh screen and wait for next iteration
	    cmd.refresh()
	    time.sleep(0.05)

#	    print "x={0}, y={1}, z={2}" .format(x, y, z)

