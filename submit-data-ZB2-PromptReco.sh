#!/bin/bash

begin=$1
end=$2

echo "$begin - $end"
shfile="ZeroBias_ZB2_Run2015B_PromptReco-v1_251721_38T_${begin}_${end}.sh"
outputdir="/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-PromptReco-38T"

if [ -e "$shfile" ] 
then		    
	rm $shfile	    
fi                      

echo "#!/bin/bash" >> $shfile

for i in $(seq $begin $end);
do
    logfile="log_ZeroBias_ZB2_Run2015B_PromptReco-v1_251721_38T_${i}.txt"
    
    if [ -e "$logfile" ]    
    then		    
    	rm $logfile	    
    fi                  

    outputfile=$outputdir"/data_Run2015B_ZeroBias2_PromptReco-v1_251721_${i}.root"

    if [ -e "$outputfile" ]
    then
	rm $outputfile
    fi

    pythonfile="python/ZeroBias_ZB2_Run2015B_PromptReco/ZeroBias_ZB2_Run2015B_PromptReco-v1_251721_38T_${i}_cfg.py"
    echo "nohup cmsRun $pythonfile >> $logfile &" >> $shfile
done

chmod u=rwx $shfile