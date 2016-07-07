#!/bin/bash

begin=$1
end=$2

echo "$begin - $end"
shfile="HERWIGPP-CUETHS1-38T-PU1p3_${begin}_${end}.sh"
outputdir="/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/HERWIGPP-CUETHS1-38T"

if [ -e "$shfile" ] 
then		    
	rm $shfile	    
fi                      

echo "#!/bin/bash" >> $shfile

for i in $(seq $begin $end);
do
    logfile="log_HERWIGPP-CUETHS1-38T-PU1p3_${i}.txt"
    
    if [ -e "$logfile" ]    
    then		    
    	rm $logfile	    
    fi                  

    outputfile=$outputdir"/HERWIGPP-CUETHS1-38T-PU1p3_${i}.root"

    if [ -e "$outputfile" ]
    then
	rm $outputfile
    fi

    pythonfile="python/HERWIGPP_CUETHS1_38T_PU1p3/HERWIGPP_CUETHS1_38T_PU1p3_${i}_cfg.py"
    echo "nohup cmsRun $pythonfile >> $logfile &" >> $shfile
done

chmod u=rwx $shfile