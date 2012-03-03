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
//	XTestFakeRelativeMotionEvent(dpy,1024,768,CurrentTime);
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
	XTestFakeMotionEvent(dpy,-1,x,y,CurrentTime);
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

