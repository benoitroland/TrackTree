#!/bin/bash

directory="/afs/desy.de/user/r/roland/MinBiasAnalysis/CMSSW_7_4_2/src/TrackAnalysis/TrackTree"

inputdir=$directory"/Log_HERWIGPP_CUETHS1_38T_PU1p3"
inputfile=$inputdir"/log_HERWIGPP-CUETHS1-38T-PU1p3_*.txt"

outputdir="$directory/Statistics"
outputfile="$outputdir/statistics-herwigpp.txt"

numtot=0
nfile=0

if [ -e "$outputfile" ]                               
then                                                 
        rm -rf $outputfile                            
fi          

for file in $inputfile
do
  
    num=$(less $file | grep "Number of events written in the tree:" | tail -n1)
    num=${num:38}
    echo "$num events in file $file"
    echo "$num events in file $file" >> $outputfile
    (( nfile += 1))
    (( numtot += num ))
done

echo ""
echo "total number of files: $nfile"
echo ""
echo "total number of events: $numtot"
echo ""                                  

echo ""	>> $outputfile				 
echo "total number of files: $nfile" >> $outputfile
echo "" >> $outputfile					 
echo "total number of events: $numtot"	>> $outputfile
echo ""                                  