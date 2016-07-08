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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/6601B800-A878-E511-A77B-0025905964BA.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/66809147-0879-E511-A2BF-0025905A60A8.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/66C09EFB-057A-E511-9515-0025905B8576.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/6A17B615-A878-E511-950A-0025905A6134.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/6A6E6D27-5A79-E511-84A0-0025905A6092.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/6AB497FF-B278-E511-8FB0-002618943947.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/6CA71CE0-AD78-E511-8099-0025905964C4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/6E123CFE-AD78-E511-BC5D-0025905A60DE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/6EDAC10B-A878-E511-9911-0025905B8592.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/6EDFF1E4-AD78-E511-8172-0025905A6056.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias3_RECO_16Oct2015_v1_251721_13.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
