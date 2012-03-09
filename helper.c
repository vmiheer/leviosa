//    			libhelper [leviosa]
//	A wrapper for XTest
//  Copyright (C) 2012  
//  miheer mukund vaidya
//  v.miheer@gmail.com
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.

//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#include"helper.h"
Display *dpy;
void helper_init()
{
	dpy=NULL;
	if(((int)(dpy=XOpenDisplay(NULL)))==NULL)
		printf("Error in opening display\n");
	printf("Inside C\n");
	XTestGrabControl(dpy,True);
//	XTestFakeButtonEvent(dpy,1,True,CurrentTime);
	XTestFakeMotionEvent(dpy,-1,0,0,CurrentTime);
//	XTestFakeButtonEvent(dpy,1,False,CurrentTime);
	XSync(dpy,False);
	XTestGrabControl(dpy,False);
	return;
}
void helper_mov_absxy(int x,int y)
{

	XTestGrabControl(dpy,True);
	XTestFakeMotionEvent(dpy,-1,x,y,CurrentTime);
	XSync(dpy,False);
	XTestGrabControl(dpy,False);
}
void helper_mov_relxy(int x,int y)
{

	XTestGrabControl(dpy,True);
	XTestFakeRelativeMotionEvent(dpy,x,y,CurrentTime);
	XSync(dpy,False);
	XTestGrabControl(dpy,False);
}
void helper_press()
{
	XTestGrabControl(dpy,True);
	XTestFakeButtonEvent(dpy,1,True,CurrentTime);
	XSync(dpy,False);
	XTestGrabControl(dpy,False);
}
void helper_release()
{
	XTestGrabControl(dpy,True);
	XTestFakeButtonEvent(dpy,1,False,CurrentTime);
	XSync(dpy,False);
	XTestGrabControl(dpy,False);
}
