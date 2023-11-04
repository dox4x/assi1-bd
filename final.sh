#!/bin/bash

cp /home/doc-bd-a1/eda-in-1.txt /home/doc-bd-a1/eda-in-2.txt /home/doc-bd-a1/eda-in-3.txt /home/doc-bd-a1/vis.png /home/doc-bd-a1/k.txt /home/vd2 
PPID=$(ps -p $$ | awk '{print $1}')
kill -KILL $PPID