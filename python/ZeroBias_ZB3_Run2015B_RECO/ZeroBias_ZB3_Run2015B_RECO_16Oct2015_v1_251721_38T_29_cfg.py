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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/FA7B7CF4-6279-E511-9A4B-002618943919.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/FC4359C9-5F79-E511-B5C6-0025905A610A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/FE24A1C9-B278-E511-BFF2-003048FFD728.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/FE67EAB7-A678-E511-80F2-0025905938B4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/320000/601C9E46-B787-E511-BC48-0025905A6076.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/410000/12291670-E085-E511-AF7C-0CC47A4C8F06.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/410000/2E36E9B7-7084-E511-813D-0025905964BE.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/410000/486C0896-1885-E511-A0CD-0025905A605E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/410000/5C74F950-1985-E511-877C-0CC47A4C8E8A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/410000/C2C5A098-1885-E511-AC01-0025905A6094.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias3_RECO_16Oct2015_v1_251721_29.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
