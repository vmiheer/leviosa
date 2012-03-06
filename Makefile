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
libhelper.so.1.0.1: helper.o
	gcc -shared -Wl,-fPIC,-soname,libhelper.so.1 -o libhelper.so.1.0.1 helper.o -lc -lXtst -lc -fPIC
helper.o:
	gcc -shared helper.c -fPIC -c -g -Wall 
clean: 
	rm -rf *.o *.so.*
install:
	ldconfig -n .
