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
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/50000/ACBCE05B-1379-E511-BCC9-002618943974.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/50000/ACC64C60-1B79-E511-9B84-0025905B8576.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/50000/AE084249-AD79-E511-B7C5-0025905B85D8.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/50000/AE80A61F-9B79-E511-8931-0025905B855C.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/50000/B43F636A-AB79-E511-A422-0025905AA9CC.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/50000/B6209A39-1D79-E511-A814-0025905A612A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/50000/B64D87E8-9979-E511-A619-0025905938D4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/50000/B828FCE1-9979-E511-97D7-0025905A6060.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/50000/B856D5C6-9979-E511-B01D-00259059642E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/50000/B8950372-8B79-E511-B854-0025905A612C.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias4_RECO_16Oct2015_v1_251721_23.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
