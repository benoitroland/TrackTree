# information about dataset and GT used below
# https://hypernews.cern.ch/HyperNews/CMS/get/relval/3688.html

import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100000))

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        'root://xrootd-cms.infn.it//store/relval/CMSSW_7_4_4/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_740TV1_0Tv2-v1/00000/18B37DA5-EB07-E511-98E2-0025905A6138.root',
        'root://xrootd-cms.infn.it//store/relval/CMSSW_7_4_4/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_740TV1_0Tv2-v1/00000/40FE47E4-F107-E511-80AC-0025905B860C.root',
        'root://xrootd-cms.infn.it//store/relval/CMSSW_7_4_4/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_740TV1_0Tv2-v1/00000/44C8D48B-EA07-E511-B23A-0025905B8582.root',
        'root://xrootd-cms.infn.it//store/relval/CMSSW_7_4_4/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_740TV1_0Tv2-v1/00000/526E0C31-EB07-E511-9386-0025905A48FC.root',
        'root://xrootd-cms.infn.it//store/relval/CMSSW_7_4_4/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_740TV1_0Tv2-v1/00000/5816BB2F-EA07-E511-BD80-0025905A6056.root',
        'root://xrootd-cms.infn.it//store/relval/CMSSW_7_4_4/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_740TV1_0Tv2-v1/00000/78F988CE-ED07-E511-AA3B-0025905A60F2.root',
        'root://xrootd-cms.infn.it//store/relval/CMSSW_7_4_4/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_740TV1_0Tv2-v1/00000/945CCB30-F207-E511-8B09-003048FF9AC6.root',
        'root://xrootd-cms.infn.it//store/relval/CMSSW_7_4_4/RelValMinBias_13/GEN-SIM-RECO/MCRUN2_740TV1_0Tv2-v1/00000/F0E315A2-E907-E511-9082-0025905A60A0.root')
                            )


process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'MCRUN2_740TV1::All'

process.analysis = cms.EDAnalyzer('TrackTree',
                                  data_type = cms.string('PYTHIA8-CUETP8M1-0T-noPU'), 

                                  L1GT_label = cms.InputTag('gtDigis'),
                                  L1TT_requested = cms.vstring('L1Tech_BSC_minBias_threshold1.v0','L1Tech_BSC_minBias_threshold2.v0',
                                                               'L1Tech_BPTX_plus_AND_minus.v0'),
                                  
                                  HLT_label = cms.InputTag('TriggerResults','','HLT'),
                                  HLT_requested = cms.vstring('HLT_ZeroBias_v1'),
                                  process_label = cms.string('HLT'),
                                  
                                  generaltrack_label = cms.InputTag('generalTracks','','RECO'),
                                  calotower_label = cms.InputTag('towerMaker','', 'RECO'),
                                  genparticle_label = cms.InputTag('genParticles','','HLT'),
                                  recovertex_label = cms.InputTag('offlinePrimaryVertices','','RECO'),
                                  beamspot_label = cms.InputTag('offlineBeamSpot','','RECO')
                                  )


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/PYTHIA8-CUETP8M1-0T/PYTHIA8-CUETP8M1-0T-noPU.root')
)

process.p = cms.Path(process.analysis)
