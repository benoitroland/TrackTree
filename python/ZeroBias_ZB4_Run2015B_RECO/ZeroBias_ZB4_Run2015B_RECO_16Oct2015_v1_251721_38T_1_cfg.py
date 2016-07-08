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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/10000/28518E20-7779-E511-85F7-0025905964C4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/10000/2AAA326D-7679-E511-A71D-002590596498.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/10000/4A796B68-7679-E511-B990-003048FFD754.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/10000/705C8E64-7679-E511-A0E5-00261894393A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/10000/C0E1EF1D-7779-E511-893F-0025905A48D8.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/10000/C45F686A-7679-E511-857B-0025905A60F4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/320000/BCAC7343-B787-E511-AE63-0025905A6092.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/02676CE5-9D79-E511-A790-0026189438A7.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/064AC101-2879-E511-8064-003048FFCBA4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/0CB40EB6-2479-E511-B0A6-0025905A60B0.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias4_RECO_16Oct2015_v1_251721_1.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
