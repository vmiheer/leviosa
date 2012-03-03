#    			[leviosa]
#  Copyright (C) 2012  
#  miheer mukund vaidya
#  jaydev kshirsagar
#  akash agrawaal
#  tejas bubne
#  v.miheer@gmail.com
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

#include "stdafx.h"
#include <stdio.h>
#include <opencv/cv.hpp>
import cv
def GetThresholdedImage(img):
	# Convert the image into an HSV image
	imgHSV = cv.CreateImage(cv.GetSize(img), 8, 3)
	cv.CvtColor(img, imgHSV, cv.CV_BGR2HSV)

	imgThreshed = cv.CreateImage(cv.GetSize(img), 8, 1)

	# Values 20,100,100 to 30,255,255 working perfect for yellow at around 6pm
#	cv.InRangeS(imgHSV, cv.Scalar(112, 100, 100), cv.Scalar(124, 255, 255), imgThreshed)

	cv.InRangeS(imgHSV, cv.Scalar(20, 130, 200), cv.Scalar(40, 200, 255), imgThreshed)
	return imgThreshed


def main():

	# Initialize capturing live feed from the camera
	capture = 0
	capture = cv.CaptureFromCAM(0)

	# Couldn't get a device? Throw an error and quit
	if (not capture):
		print "Could not initialize capturing...\n"
		return -1

	# The two windows we'll be using
	cv.NamedWindow("video")
	cv.NamedWindow("thresh")

	# This image holds the "scribble" data...
	# the tracked positions of the ball
	imgScribble = 0

	# An infinite loop
	while(True):
	
		# Will hold a frame captured from the camera
		frame = 0
		frame = cv.QueryFrame(capture)

		# If we couldn't grab a frame... quit
		if(not frame):
			break
		
		# If this is the first frame, we need to initialize it
		if(imgScribble == 0):
		
			imgScribble = cv.CreateImage(cv.GetSize(frame), 8, 3)
		

		# Holds the yellow thresholded image (yellow = white, rest = black)
		imgYellowThresh = GetThresholdedImage(frame)
		moments=0
		# Calculate the moments to estimate the position of the ball
		moments=cv.Moments(imgYellowThresh)

		# The actual moment values
		moment01 = cv.GetSpatialMoment(moments, 0, 1)
		moment10 = cv.GetSpatialMoment(moments, 1, 0)
		area = cv.GetSpatialMoment(moments, 0, 0)
	#	if area==0: continue
		# Holding the last and current ball positions
		posX = 0
		posY = 0

		lastX = posX
		lastY = posY

		posX = moment10/area
		posY = moment01/area

		# Print it out for debugging purposes
		print "position "+ str(posX)+' '+ str(posY)+'\n'

		# We want to draw a line only if its a valid position
		if(lastX>0 and lastY>0 and posX>0 and posY>0):
		
			# Draw a yellow line from the previous point to the current point
			cv.Line(imgScribble, cv.Point(posX, posY), cv.Point(lastX, lastY), cv.Scalar(0,255,255), 5)
		

		# Add the scribbling image and the frame... and we get a combination of the two
		cv.Add(frame, imgScribble, frame)
		cv.ShowImage("thresh", imgYellowThresh)
		cv.ShowImage("video", frame)

		# Wait for a keypress
		c = cv.WaitKey(10)
		if not (c == -1):
		
			# If pressed, break out of the loop
			break
		

		# Release the thresholded image... we need no memory leaks.. please
		

	# We're done using the camera. Other applications can now use it
	return 0
main()
