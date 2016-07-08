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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/8CF4A84F-F978-E511-BB2E-0025905964B2.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/8EDD13F4-0D79-E511-ACD0-002618943849.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/900E4C44-1B79-E511-BAFA-00261894380D.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/906FBDC9-8179-E511-B833-0025905A6094.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/9090704A-8279-E511-BFE4-0025905964CC.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/921CEFBC-FE78-E511-9480-002618943915.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/9247A504-A379-E511-B0F4-0025905A60D0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/92BA8EBE-FB78-E511-85E3-0026189438DE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/940398DE-0E79-E511-AED5-0025905B8590.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias5/RECO/16Oct2015-v1/40000/94797D42-2779-E511-ADA3-0025905A48D8.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias5_RECO_16Oct2015_v1_251721_17.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
