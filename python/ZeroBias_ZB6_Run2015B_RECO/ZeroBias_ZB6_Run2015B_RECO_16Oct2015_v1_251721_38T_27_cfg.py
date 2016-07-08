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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/DC49C27B-2279-E511-9AF0-0025905A6132.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/DCBB406D-1379-E511-B757-0025905A6136.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/E02C1723-0379-E511-BCF8-0025905A608A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/E0598940-0A79-E511-B00E-0025905A60BC.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/E0640B96-3B79-E511-B93B-0025905A613C.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/E0ECD11B-0379-E511-91BE-002618943869.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/E243AE84-1E79-E511-BA1C-0025905B8562.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/E25AD681-1E79-E511-ADDF-0025905B860C.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/E25C32FE-8E79-E511-84A6-0025905A608C.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/E272A218-0379-E511-AE55-00261894396D.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias6_RECO_16Oct2015_v1_251721_27.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
