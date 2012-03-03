#!/usr/bin/env python
#    			makefile for libhelper [leviosa]
#	A wrapper for XTest
#  Copyright (C) 2012  
#  miheer mukund vaidya
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
