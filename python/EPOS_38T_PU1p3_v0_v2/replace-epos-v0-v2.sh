#!/bin/bash

OLD1="'\/store\/mc\/RunIISpring15DR74\/ReggeGribovPartonMC_13TeV-EPOS\/GEN-SIM-RECODEBUG\/"
NEW1=""

#echo "old 1 = $OLD1"
#echo "new 1 = $NEW1"
#echo ""

mc="EPOS_38T_PU1p3_v0_v2"

filein1="initial_input_"$mc".txt"
fileout1="temp-1.txt"
sed -e s/$OLD1/$NEW1/g $filein1 > $fileout1

OLD2="',"
NEW2=""

#echo "old 2 = $OLD2"
#echo "new 2 = $NEW2"
#echo ""

filein2="temp-1.txt"
fileout2="temp-2.txt"
sed -e s/$OLD2/$NEW2/g $filein2 > $fileout2

filein3="temp-2.txt"			   
fileout3="input_"$mc".txt"			   
sed 's/[[:space:]]//g' $filein3 > $fileout3 

rm temp-1.txt
rm temp-2.txt
