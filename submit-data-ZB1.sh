#!/bin/bash

begin=$1
end=$2

echo "$begin - $end"
shfile="ZeroBias_ZB1_Run2015B_RECO_16Oct2015_v1_251721_38T_${begin}_${end}.sh"
outputdir="/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T"

if [ -e "$shfile" ] 
then		    
	rm $shfile	    
fi                      

echo "#!/bin/bash" >> $shfile

for i in $(seq $begin $end);
do
    logfile="log_ZeroBias_ZB1_Run2015B_RECO_16Oct2015_v1_251721_38T_${i}.txt"
    
    if [ -e "$logfile" ]    
    then		    
    	rm $logfile	    
    fi                  

    outputfile=$outputdir"/data_Run2015B_ZeroBias1_RECO_16Oct2015_v1_251721_${i}.root"

    if [ -e "$outputfile" ]
    then
	rm $outputfile
    fi

    pythonfile="python/ZeroBias_ZB1_Run2015B_RECO/ZeroBias_ZB1_Run2015B_RECO_16Oct2015_v1_251721_38T_${i}_cfg.py"
    echo "nohup cmsRun $pythonfile >> $logfile &" >> $shfile
done

chmod u=rwx $shfile