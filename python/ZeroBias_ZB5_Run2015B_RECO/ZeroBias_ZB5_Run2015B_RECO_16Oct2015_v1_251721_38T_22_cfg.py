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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/B6010876-0579-E511-B980-0026189438F8.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/B63E28D7-FB78-E511-9412-0025905A610C.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/B6963452-F978-E511-B4A6-0025905A60CA.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/BA20D1A6-FC78-E511-83C5-002618943961.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/BA5A7042-8279-E511-B05F-0025905A609A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/BA8AB248-8279-E511-BB23-0025905938A8.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/BE7F9344-1B79-E511-B642-0025905A60FE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/C071B480-FC78-E511-B5A6-0026189438E0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/C07FE71A-FE78-E511-93D5-0025905B85D0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/C0FA9AC1-FB78-E511-B205-0026189438C9.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias5_RECO_16Oct2015_v1_251721_22.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
