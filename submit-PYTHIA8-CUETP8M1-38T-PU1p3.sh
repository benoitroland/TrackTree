#!/bin/bash

begin=$1
end=$2

echo "$begin - $end"
shfile="PYTHIA8-CUETP8M1-38T-PU1p3_${begin}_${end}.sh"
outputdir="/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/PYTHIA8-CUETP8M1-38T"

if [ -e "$shfile" ] 
then		    
	rm $shfile	    
fi                      

echo "#!/bin/bash" >> $shfile

for i in $(seq $begin $end);
do
    logfile="log_PYTHIA8-CUETP8M1-38T-PU1p3_${i}.txt"
    
    if [ -e "$logfile" ]    
    then		    
    	rm $logfile	    
    fi                  

    outputfile=$outputdir"/PYTHIA8-CUETP8M1-38T-PU1p3_${i}.root"

    if [ -e "$outputfile" ]
    then
	rm $outputfile
    fi

    pythonfile="python/PYTHIA8_CUETP8M1_38T_PU1p3/PYTHIA8_CUETP8M1_38T_PU1p3_${i}_cfg.py"
    echo "nohup cmsRun $pythonfile >> $logfile &" >> $shfile
done

chmod u=rwx $shfile