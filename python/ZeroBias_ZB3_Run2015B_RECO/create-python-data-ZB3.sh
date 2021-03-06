#!/bin/bash

num1=$1
num2=$2

inputdataset="input_ZeroBias_ZB3_Run2015B_RECO.txt"
outputdir="/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/"

for number in $(seq $num1 $num2);
do
    let "lineMin= 10*number-9"
    let "lineMax= 10*$number"
    
    pyfile="ZeroBias_ZB3_Run2015B_RECO_16Oct2015_v1_251721_38T_${number}_cfg.py"
    echo ""
    echo "create python file: $pyfile"
    echo ""
        
    if [ -e "$pyfile" ] 
    then                
        rm $pyfile          
    fi         
    
    aaa="root://xrootd-cms.infn.it/"
    outputfile="${outputdir}data_Run2015B_ZeroBias3_RECO_16Oct2015_v1_251721_${number}.root"
    
    echo "output file: $outputfile"
    echo ""
    
    echo "import FWCore.ParameterSet.Config as cms" >> $pyfile
    echo "" >> $pyfile
    
    echo "process = cms.Process(\"TrackAnalysis\")" >> $pyfile
    echo "" >> $pyfile
    
    echo "process.load(\"FWCore.MessageService.MessageLogger_cfi\")" >> $pyfile
    echo "process.MessageLogger.cerr.FwkReport.reportEvery = 5000"  >> $pyfile
    echo "process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000000))" >> $pyfile 
    echo "" >> $pyfile
    
    echo "process.load(\"RecoTracker.TrackProducer.TrackRefitters_cff\")" >> $pyfile  
    echo "process.TrackRefitter.src = "\'generalTracks\' >> $pyfile 
    echo "process.TrackRefitter.TrajectoryInEvent = True" >> $pyfile 
    echo "process.TrackRefitter.TTRHBuilder = \"WithAngleAndTemplate\""  >> $pyfile 
    echo "process.TrackRefitter.NavigationSchool = \"\"" >> $pyfile 
    echo "" >> $pyfile 
    
    echo "input files from $lineMin to $lineMax:"
    echo ""
    echo "process.source = cms.Source(\"PoolSource\"," >> $pyfile
    echo "                            fileNames = cms.untracked.vstring(" >> $pyfile
    
    for iline in $(seq $lineMin $lineMax);
    do
	fileroot="`sed -n ${iline}p ${inputdataset}`"
	if [ "$iline" -lt "$lineMax" ] 
	then
	    echo \'$aaa${fileroot}\'"," >> $pyfile 
	    echo "$aaa${fileroot}"
	else
	    echo \'$aaa${fileroot}\' >> $pyfile 
	    echo "$aaa${fileroot}"
	fi
    done
    
    echo        "),lumisToProcess = cms.untracked.VLuminosityBlockRange("\'251721:123-251721:244\'"))" >> $pyfile
    echo "" >> $pyfile
    
    echo "process.load("\'Configuration.StandardSequences.Services_cff\'")" >> $pyfile
    echo "process.load("\'Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff\'")" >> $pyfile
    echo "process.load(\"Configuration.StandardSequences.MagneticField_cff\")" >> $pyfile
    echo "process.load("\'Configuration.Geometry.GeometryExtended2015Reco_cff\'")" >> $pyfile
    echo "process.GlobalTag.globaltag = "\'74X_dataRun2_Prompt_v0\'" #"\'GR_P_V56::All\' >> $pyfile
    echo "" >> $pyfile
    
    HLT0=\'HLT_ZeroBias_part0_v1\'
    HLT1=\'HLT_ZeroBias_part1_v1\'
    HLT2=\'HLT_ZeroBias_part2_v1\'
    HLT3=\'HLT_ZeroBias_part3_v1\'
    HLT4=\'HLT_ZeroBias_part4_v1\'
    HLT5=\'HLT_ZeroBias_part5_v1\'
    HLT6=\'HLT_ZeroBias_part6_v1\'
    HLT7=\'HLT_ZeroBias_part7_v1\'                                           
    BPTXPlusOnly=\'HLT_L1Tech5_BPTX_PlusOnly_v1\'
    BPTXMinusOnly=\'HLT_L1Tech6_BPTX_MinusOnly_v1\'
    noBPTX=\'HLT_L1Tech7_NoBPTX_v1\'
    
    echo "process.analysis = cms.EDAnalyzer("\'TrackTree\'"," >> $pyfile
    echo "                                  data_type = cms.string("\'data-38T\'")," >> $pyfile 
    echo "" >> $pyfile
    echo "                                  L1GT_label = cms.InputTag("\'gtDigis\'")," >> $pyfile
    echo "                                  L1TT_requested = cms.vstring("\'L1Tech_BPTX_plus_AND_minus.v0\'"," >> $pyfile 
    echo "                                                               "\'L1Tech_BPTX_plus_AND_NOT_minus.v0\'"," >> $pyfile 
    echo "                                                               "\'L1Tech_BPTX_minus_AND_not_plus.v0\'"," >> $pyfile 
    echo "                                                               "\'L1Tech_BPTX_quiet.v0\'")," >> $pyfile 
    echo "                                  HLT_label = cms.InputTag("\'TriggerResults\'","\'\'","\'HLT\'")," >> $pyfile
    echo "                                  HLT_requested = cms.vstring("${HLT0}","${HLT1}","${HLT2}"," >> $pyfile
    echo "                                                              "${HLT3}","${HLT4}","${HLT5}"," >> $pyfile
    echo "                                                              "${HLT6}","${HLT7}"," >> $pyfile
    echo "                                                              "${BPTXPlusOnly}","${BPTXMinusOnly}","${noBPTX}")," >> $pyfile
    echo "                                  process_label = cms.string("\'HLT\'")," >> $pyfile                                  
    echo "                                  generaltrack_label = cms.InputTag("\'TrackRefitter\'"), # cms.InputTag("\'generalTracks\'","\'\'","\'RECO\'")," >> $pyfile
    echo "                                  calotower_label = cms.InputTag("\'towerMaker\'","\'\'","\'"RECO"\'")," >> $pyfile
    echo "                                  genparticle_label = cms.InputTag("\'genParticles\'","\'\'","\'HLT\'")," >> $pyfile
    echo "                                  recovertex_label = cms.InputTag("\'offlinePrimaryVertices\'","\'\'","\'RECO\'")," >> $pyfile
    echo "                                  beamspot_label = cms.InputTag("\'offlineBeamSpot\'","\'\'","\'RECO\'")," >> $pyfile
    echo "                                  hfrechit_label = cms.InputTag("\'hfreco\'","\'\'","\'RECO\'")," >> $pyfile
    echo "                                  pu_label = cms.InputTag("\'addPileupInfo\'","\'\'","\'HLT\'")" >> $pyfile
    echo "                                 )" >> $pyfile
    echo "" >> $pyfile
    
    echo "process.TFileService = cms.Service(\"TFileService\"," >> $pyfile
    echo "        fileName = cms.string("\'${outputfile}\'"))" >> $pyfile
    echo "" >> $pyfile
    
    echo "process.p = cms.Path(process.TrackRefitter*process.analysis)" >> $pyfile
    echo ""
done