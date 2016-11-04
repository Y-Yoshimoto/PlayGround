#!/bin/sh
#ファイルを連番の名前に変更
for i in *.png ; do
let a="${a}+1"
s=$(printf "IMG%02d.png" $a)
echo $s
mv $i $s
done
