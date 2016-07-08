# information about dataset and GT used below
# https://hypernews.cern.ch/HyperNews/CMS/get/relval/3688.html

import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100000))

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        'file:/nfs/dust/cms/user/roland/MinBias-2015-MonteCarlo-38T/MinBias_TuneCUETP8M1_13TeV_pythia8/MinBias_TuneCUETP8M1_13TeV_pythia8_1.root',
        'file:/nfs/dust/cms/user/roland/MinBias-2015-MonteCarlo-38T/MinBias_TuneCUETP8M1_13TeV_pythia8/MinBias_TuneCUETP8M1_13TeV_pythia8_2.root',
        'file:/nfs/dust/cms/user/roland/MinBias-2015-MonteCarlo-38T/MinBias_TuneCUETP8M1_13TeV_pythia8/MinBias_TuneCUETP8M1_13TeV_pythia8_3.root',
        'file:/nfs/dust/cms/user/roland/MinBias-2015-MonteCarlo-38T/MinBias_TuneCUETP8M1_13TeV_pythia8/MinBias_TuneCUETP8M1_13TeV_pythia8_4.root',
        'file:/nfs/dust/cms/user/roland/MinBias-2015-MonteCarlo-38T/MinBias_TuneCUETP8M1_13TeV_pythia8/MinBias_TuneCUETP8M1_13TeV_pythia8_5.root',
        'file:/nfs/dust/cms/user/roland/MinBias-2015-MonteCarlo-38T/MinBias_TuneCUETP8M1_13TeV_pythia8/MinBias_TuneCUETP8M1_13TeV_pythia8_6.root',
        'file:/nfs/dust/cms/user/roland/MinBias-2015-MonteCarlo-38T/MinBias_TuneCUETP8M1_13TeV_pythia8/MinBias_TuneCUETP8M1_13TeV_pythia8_7.root',
        'file:/nfs/dust/cms/user/roland/MinBias-2015-MonteCarlo-38T/MinBias_TuneCUETP8M1_13TeV_pythia8/MinBias_TuneCUETP8M1_13TeV_pythia8_8.root')
                            )


process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.GlobalTag.globaltag = 'MCRUN2_740TV1::All'

process.analysis = cms.EDAnalyzer('TrackTree',
                                  data_type = cms.string('PYTHIA8-CUETP8M1-38T-PU1p3'), 

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
                                  beamspot_label = cms.InputTag('offlineBeamSpot','','RECO'),
                                  hfrechit_label = cms.InputTag('hfreco','','RECO')
                                  )


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/PYTHIA8-CUETP8M1-38T/PYTHIA8-CUETP8M1-38T-PU1p3.root')
)

process.p = cms.Path(process.analysis)
