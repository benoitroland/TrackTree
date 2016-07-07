#!/bin/bash

begin=$1
end=$2

echo "$begin - $end"
shfile="EPOS-38T-PU1p3-v0-v4_${begin}_${end}.sh"
outputdir="/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/EPOS-38T"

if [ -e "$shfile" ] 
then		    
	rm $shfile	    
fi                      

echo "#!/bin/bash" >> $shfile

for i in $(seq $begin $end);
do
    logfile="log_EPOS-38T-PU1p3-v0-v4_${i}.txt"
    
    if [ -e "$logfile" ]    
    then		    
    	rm $logfile	    
    fi                  

    outputfile=$outputdir"/EPOS-38T-PU1p3-v0-v4_${i}.root"

    if [ -e "$outputfile" ]
    then
	rm $outputfile
    fi

    pythonfile="python/EPOS_38T_PU1p3_v0_v4/EPOS_38T_PU1p3_v0_v4_${i}_cfg.py"
    echo "nohup cmsRun $pythonfile >> $logfile &" >> $shfile
done

chmod u=rwx $shfile