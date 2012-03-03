#!/usr/bin/env python
#include"helper.h"
from ctypes import *
c=CDLL("libhelper.so.1")
libc=CDLL("libc.so.6")
c.helper_init()
"""the init function opens display and places pointer at 0,0
a.k.a. top left corner of screen"""
libc.sleep(2)
c.helper_mov_absxy(1024,768)
"""Move to co-ordinate 1024 768 abs displacement"""
libc.sleep(2)
c.helper_mov_relxy(-1024,-768)
"""Again move to exact place"""
c.helper_mov_relxy(15,200)
libc.sleep(2)
c.helper_press()
c.helper_release()
