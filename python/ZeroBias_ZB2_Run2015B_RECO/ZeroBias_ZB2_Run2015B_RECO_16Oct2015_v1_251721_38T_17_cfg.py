import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 2000
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000000))

process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.TrackRefitter.src = 'generalTracks'
process.TrackRefitter.TrajectoryInEvent = True
process.TrackRefitter.TTRHBuilder = "WithAngleAndTemplate"
process.TrackRefitter.NavigationSchool = ""

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/92576572-A278-E511-868B-0025905A60D2.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/92FF47CB-9178-E511-BC8F-0025905A6126.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/94F6A671-A278-E511-B5D3-0025905A60CE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/94F730A4-4379-E511-A77D-0025905B8562.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/96A9BDB7-9078-E511-8E5C-0025905B858C.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/96B51863-A678-E511-8A74-0025905A60F2.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/96E00F34-3F79-E511-A211-0025905A608C.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/98198494-4379-E511-B5D1-0025905938D4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/983DA59C-A678-E511-B027-00261894391B.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/988C060C-C878-E511-8C15-0026189438B1.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias2_RECO_16Oct2015_v1_251721_17.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
