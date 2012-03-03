libhelper.so.1.0.1: helper.o
	gcc -shared -Wl,-soname,libhelper.so.1 -o libhelper.so.1.0.1 helper.o -lc -lXtst -lc
helper.o:
	gcc helper.c -c -g -Wall
clean: 
	rm -rf *.o *.so.*
install:
	ldconfig -n .
