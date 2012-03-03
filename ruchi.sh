#!/bin/bash
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH;
python helpercheck.py;
exit 0
