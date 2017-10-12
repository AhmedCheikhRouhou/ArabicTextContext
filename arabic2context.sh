#!/bin/bash

file=$1

cat $1  | sed 's/ /|/g' | sed -e 's/\(.\)/\1 /g' | sed 's/  / /g' | sed 's/  / /g' | sed 's/  / /g' > tmp.txt

python run.py -f tmp.txt

sed 's/ //g' tmp.txt.ctx | sed 's/||/|/g' | sed 's/|/ /g' | sed '/^ /s/ //' > $1.tra

./addSpace.py $1.tra | sed 's/| / /g' | sed 's/|\r//g' |  > $1.fin
