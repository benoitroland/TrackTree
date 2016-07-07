#!/bin/bash

begin=$1
end=$2

echo "$begin - $end"
shfile="ZeroBias_ZB1_Run2015B_Prompt_v2_251721_38T_HFRereco_${begin}_${end}.sh"
outputdir="/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-HFRereco-38T"

if [ -e "$shfile" ] 
then		    
	rm $shfile	    
fi                      

echo "#!/bin/bash" >> $shfile

for i in $(seq $begin $end);
do
    logfile="log_ZeroBias_ZB1_Run2015B_Prompt_v2_251721_38T_HFRereco_${i}.txt"
    
    if [ -e "$logfile" ]    
    then		    
    	rm $logfile	    
    fi                  

    outputfile=$outputdir"/data_Run2015B_ZeroBias1_Prompt_v2_251721_HFRereco_${i}.root"

    if [ -e "$outputfile" ]
    then
	rm $outputfile
    fi

    pythonfile="python/ZeroBias_ZB1_Run2015B_HFRereco_RECO/ZeroBias_ZB1_Run2015B_Prompt_v2_251721_38T_HFRereco_${i}_cfg.py"
    echo "nohup cmsRun $pythonfile >> $logfile &" >> $shfile
done

chmod u=rwx $shfile