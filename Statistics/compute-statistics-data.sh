#!/bin/bash

directory="/afs/desy.de/user/r/roland/MinBiasAnalysis/CMSSW_7_4_2/src/TrackAnalysis/TrackTree"

inputdirZB1=$directory"/Log_ZeroBias_ZB1_Run2015B_RECO"
inputfileZB1=$inputdirZB1"/log_ZeroBias_ZB1_Run2015B_RECO_16Oct2015_v1_251721_38T_*.txt"

inputdirZB2=$directory"/Log_ZeroBias_ZB2_Run2015B_RECO"					
inputfileZB2=$inputdirZB2"/log_ZeroBias_ZB2_Run2015B_RECO_16Oct2015_v1_251721_38T_*.txt"

inputdirZB3=$directory"/Log_ZeroBias_ZB3_Run2015B_RECO"					
inputfileZB3=$inputdirZB3"/log_ZeroBias_ZB3_Run2015B_RECO_16Oct2015_v1_251721_38T_*.txt"

inputdirZB4=$directory"/Log_ZeroBias_ZB4_Run2015B_RECO"					
inputfileZB4=$inputdirZB4"/log_ZeroBias_ZB4_Run2015B_RECO_16Oct2015_v1_251721_38T_*.txt"

inputdirZB5=$directory"/Log_ZeroBias_ZB5_Run2015B_RECO"					
inputfileZB5=$inputdirZB5"/log_ZeroBias_ZB5_Run2015B_RECO_16Oct2015_v1_251721_38T_*.txt"

inputdirZB6=$directory"/Log_ZeroBias_ZB6_Run2015B_RECO"					
inputfileZB6=$inputdirZB6"/log_ZeroBias_ZB6_Run2015B_RECO_16Oct2015_v1_251721_38T_*.txt"

outputdir="$directory/Statistics"
outputfile="$outputdir/statistics-data.txt"

numtot=0
nfile=0

numtotZB1=0
nfileZB1=0

numtotZB2=0
nfileZB2=0

numtotZB3=0
nfileZB3=0

if [ -e "$outputfile" ]                               
then                                                 
        rm -rf $outputfile                            
fi          

for file in $inputfileZB1
do
  
    num=$(less $file | grep "Number of events written in the tree:" | tail -n1)
    num=${num:38}
    echo "$num events in file $file"
    echo "$num events in file $file" >> $outputfile
    (( nfileZB1 += 1))
    (( numtotZB1 += num ))
    (( nfile += 1))	  
    (( numtot += num ))
done                                                                                     

for file in $inputfileZB2								 
do											 
  											 
    num=$(less $file | grep "Number of events written in the tree:" | tail -n1)		 
    num=${num:38}									 
    echo "$num events in file $file"							 
    echo "$num events in file $file" >> $outputfile					 
    (( nfileZB2 += 1))									 
    (( numtotZB2 += num ))									 
    (( nfile += 1))									 	 
    (( numtot += num ))									 
done                                                                                      

for file in $inputfileZB3								  
do											  
  											  
    num=$(less $file | grep "Number of events written in the tree:" | tail -n1)		  
    num=${num:38}									  
    echo "$num events in file $file"							  
    echo "$num events in file $file" >> $outputfile					  
    (( nfileZB3 += 1))									  
    (( numtotZB3 += num ))								  
    (( nfile += 1))									  
    (( numtot += num ))									  
done                                                                                      

for file in $inputfileZB4								  
do											  
  											  
    num=$(less $file | grep "Number of events written in the tree:" | tail -n1)		  
    num=${num:38}									  
    echo "$num events in file $file"							  
    echo "$num events in file $file" >> $outputfile					  
    (( nfileZB4 += 1))									  
    (( numtotZB4 += num ))								  
    (( nfile += 1))									  
    (( numtot += num ))									  
done                                                                                      


for file in $inputfileZB5								  
do											  
  											  
    num=$(less $file | grep "Number of events written in the tree:" | tail -n1)		  
    num=${num:38}									  
    echo "$num events in file $file"							  
    echo "$num events in file $file" >> $outputfile					  
    (( nfileZB5 += 1))									  
    (( numtotZB5 += num ))								  
    (( nfile += 1))									  
    (( numtot += num ))									  
done                                                                                      

for file in $inputfileZB6
do

    num=$(less $file | grep "Number of events written in the tree:" | tail -n1)
    num=${num:38}
    echo "$num events in file $file"
    echo "$num events in file $file" >> $outputfile
    (( nfileZB6 += 1))
    (( numtotZB6 += num ))
    (( nfile += 1))
    (( numtot += num ))
done

echo ""
echo "total number of ZB1 files: $nfileZB1"
echo "total number of ZB2 files: $nfileZB2"
echo "total number of ZB3 files: $nfileZB3"
echo "total number of ZB4 files: $nfileZB4"
echo "total number of ZB5 files: $nfileZB5"
echo "total number of ZB6 files: $nfileZB6"
echo "total number of files: $nfile"
echo ""
echo "total number of events in ZB1: $numtotZB1"
echo "total number of events in ZB2: $numtotZB2"
echo "total number of events in ZB3: $numtotZB3"
echo "total number of events in ZB4: $numtotZB4"
echo "total number of events in ZB5: $numtotZB5"
echo "total number of events in ZB6: $numtotZB6"
echo "total number of events: $numtot"
echo ""                                  

echo ""	>> $outputfile				 
echo "total number of files in ZB1: $nfileZB1" >> $outputfile
echo "total number of files in ZB2: $nfileZB2" >> $outputfile
echo "total number of files in ZB3: $nfileZB3" >> $outputfile
echo "total number of files in ZB4: $nfileZB4" >> $outputfile
echo "total number of files in ZB5: $nfileZB5" >> $outputfile
echo "total number of files in ZB6: $nfileZB6" >> $outputfile
echo "total number of files: $nfile" >> $outputfile
echo "" >> $outputfile					 
echo "total number of events in ZB1: $numtotZB1" >> $outputfile
echo "total number of events in ZB2: $numtotZB2" >> $outputfile
echo "total number of events in ZB3: $numtotZB3" >> $outputfile
echo "total number of events in ZB4: $numtotZB4" >> $outputfile
echo "total number of events in ZB5: $numtotZB5" >> $outputfile
echo "total number of events in ZB6: $numtotZB6" >> $outputfile
echo "total number of events: $numtot"	>> $outputfile
echo ""                                  