#!/bin/bash
for ((;;)); do
        ./currentinput.sh | tee currentoutput.txt
        sleep 2
done
