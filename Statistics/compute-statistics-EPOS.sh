#!/bin/bash

directory="/afs/desy.de/user/r/roland/MinBiasAnalysis/CMSSW_7_4_2/src/TrackAnalysis/TrackTree"

inputdir1=$directory"/Log_EPOS_38T_PU1p3_v0_v2"
inputfile1=$inputdir1"/log_EPOS-38T-PU1p3-v0-v2_*.txt"

inputdir2=$directory"/Log_EPOS_38T_PU1p3_v0_v4"	     
inputfile2=$inputdir2"/log_EPOS-38T-PU1p3-v0-v4_*.txt"

outputdir="$directory/Statistics"
outputfile="$outputdir/statistics-epos.txt"

numtot=0
nfile=0

if [ -e "$outputfile" ]                               
then                                                 
        rm -rf $outputfile                            
fi          

for file in $inputfile1
do
  
    num=$(less $file | grep "Number of events written in the tree:" | tail -n1)
    num=${num:38}
    echo "$num events in file $file"
    echo "$num events in file $file" >> $outputfile
    (( nfile += 1))
    (( numtot += num ))
done                                                                               

for file in $inputfile2								   
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