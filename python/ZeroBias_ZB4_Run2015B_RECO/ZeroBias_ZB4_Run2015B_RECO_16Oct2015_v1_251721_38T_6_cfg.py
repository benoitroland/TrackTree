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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/DAE9C5D5-2179-E511-AB15-002590596484.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/DC3BDE4F-8E85-E511-ABD9-0025905A60AA.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/DE5F8F9A-1479-E511-99AC-002590596498.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/E23FD700-2879-E511-9045-003048FFD7BE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/E4ADE3D5-2179-E511-A26D-0025905938B4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/F0D83945-1B79-E511-A772-0025905B8576.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/F2B32FD5-2179-E511-B84D-0025905A6136.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/F4746E04-2879-E511-B65B-003048FFD756.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/F8FCF5D3-2179-E511-9D1B-0026189438D6.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/FC5BA0D5-2179-E511-A4BB-0025905B85EE.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias4_RECO_16Oct2015_v1_251721_6.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
