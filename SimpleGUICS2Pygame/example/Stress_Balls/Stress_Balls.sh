#!/bin/sh

python2 Stress_Balls.py --no-plot 2>&1 | tee Stress_Balls.txt
python2 Stress_Balls.py --no-plot --reverse 2>&1 | tee -a Stress_Balls.txt

python3 Stress_Balls.py --no-plot 2>&1 | tee -a Stress_Balls.txt
python3 Stress_Balls.py --no-plot --reverse 2>&1 | tee -a Stress_Balls.txt
