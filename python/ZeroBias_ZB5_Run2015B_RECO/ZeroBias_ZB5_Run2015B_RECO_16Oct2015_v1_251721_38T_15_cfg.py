import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 5000
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000000))

process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.TrackRefitter.src = 'generalTracks'
process.TrackRefitter.TrajectoryInEvent = True
process.TrackRefitter.TTRHBuilder = "WithAngleAndTemplate"
process.TrackRefitter.NavigationSchool = ""

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/7C429A90-FC78-E511-AA36-0025905A613C.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/7C73FEF3-0D79-E511-BCD4-0025905A60FE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/7E4213A9-9F79-E511-9F4A-002590593920.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/7E427552-2179-E511-A838-0025905A60F2.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/7E92F5C2-FE78-E511-9C6E-0025905A6110.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/7EC021AA-F978-E511-AE2E-00261894383B.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/7EC3B5CC-FE78-E511-8080-0025905A6070.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/826595AB-F978-E511-B845-002618943975.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/8284D4BE-FB78-E511-B085-00261894393D.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/82996489-8179-E511-A6A8-0025905A48BB.root'
),lumisToProcess = cms.untracked.VLuminosityBlockRange('251721:123-251721:244'))

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v0' #'GR_P_V56::All'

process.analysis = cms.EDAnalyzer('TrackTree',
                                  data_type = cms.string('data-38T'),

                                  L1GT_label = cms.InputTag('gtDigis'),
                                  L1TT_requested = cms.vstring('L1Tech_BPTX_plus_AND_minus.v0',
                                                               'L1Tech_BPTX_plus_AND_NOT_minus.v0',
                                                               'L1Tech_BPTX_minus_AND_not_plus.v0',
                                                               'L1Tech_BPTX_quiet.v0'),
                                  HLT_label = cms.InputTag('TriggerResults','','HLT'),
                                  HLT_requested = cms.vstring('HLT_ZeroBias_part0_v1','HLT_ZeroBias_part1_v1','HLT_ZeroBias_part2_v1',
                                                              'HLT_ZeroBias_part3_v1','HLT_ZeroBias_part4_v1','HLT_ZeroBias_part5_v1',
                                                              'HLT_ZeroBias_part6_v1','HLT_ZeroBias_part7_v1',
                                                              'HLT_L1Tech5_BPTX_PlusOnly_v1','HLT_L1Tech6_BPTX_MinusOnly_v1','HLT_L1Tech7_NoBPTX_v1'),
                                  process_label = cms.string('HLT'),
                                  generaltrack_label = cms.InputTag('TrackRefitter'), # cms.InputTag('generalTracks','','RECO'),
                                  calotower_label = cms.InputTag('towerMaker','','RECO'),
                                  genparticle_label = cms.InputTag('genParticles','','HLT'),
                                  recovertex_label = cms.InputTag('offlinePrimaryVertices','','RECO'),
                                  beamspot_label = cms.InputTag('offlineBeamSpot','','RECO'),
                                  hfrechit_label = cms.InputTag('hfreco','','RECO'),
                                  pu_label = cms.InputTag('addPileupInfo','','HLT')
                                 )

process.TFileService = cms.Service("TFileService",
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias5_RECO_16Oct2015_v1_251721_15.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
