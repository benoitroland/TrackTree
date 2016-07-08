# !/bin/bash

inputfile=$1
outputfile="${inputfile::38}_251721.txt"
pattern="251/721"

echo ""
echo "looking for $pattern"
echo "in $inputfile"
echo "to $outputfile"

for line in $(cat $inputfile); do
    if [[ $line = *$pattern* ]]
    then
        echo $line >> $outputfile
    fi
done

echo ""
num="$(less $inputfile | wc -l)"
echo "$num files in $inputfile"

numsel="$(less $outputfile | wc -l)"
echo "$numsel files in $outputfile"
echo ""