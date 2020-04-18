#!/bin/bash
rm -rf *.log *.csv
cp /home/pi/*.log .
cp /home/pi/*.csv .
git add -A
git commit -m "update"
git push
