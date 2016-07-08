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
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/686E7A7B-0A79-E511-A328-00261894387E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/687CA209-0A79-E511-B9BA-00261894396B.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/68801C30-0B79-E511-B5EA-0025905A48D0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/6A2C489C-8879-E511-B472-00248C0BE005.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/6A5D26D3-1A79-E511-B9A0-002618943896.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/6A927CD5-BE79-E511-948E-0025905A60F4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/6AB2DB3D-5F79-E511-ABC5-003048FFD71E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/6CAAE3F3-8D79-E511-A6A1-0025905938B4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/701BCAEA-0979-E511-86B7-0025905964B2.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/70DAF891-0679-E511-95E7-00261894385D.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias1_RECO_16Oct2015_v1_251721_14.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
