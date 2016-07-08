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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/DC93D19E-AA79-E511-952A-0025905A6068.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/DE681C12-A878-E511-BC3B-0025905A606A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/DEEE2D49-A778-E511-9B32-0025905A48D8.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/DEF86871-A878-E511-BEEE-0025905A607E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/E07F7666-5D79-E511-A6A5-0025905AA9F0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/E08B1413-A878-E511-A99A-0025905A60A6.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/E0D1C9DD-B478-E511-AA23-0025905A608E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/E0D729E8-AD78-E511-9A8D-0025905B8572.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/E2823829-6079-E511-8B7E-0025905A48BC.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/E48A0FBA-A878-E511-B294-00259059642E.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias3_RECO_16Oct2015_v1_251721_26.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
