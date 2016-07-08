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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/6887506E-0A79-E511-B4E3-0025905A6068.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/689936A2-9C79-E511-9138-0025905A60B0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/6C033115-0379-E511-B4FA-002618943962.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/6CD65BEB-4779-E511-9A88-002618943916.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/6CDA34B4-0179-E511-9A9D-00261894384F.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/6E2CC184-1E79-E511-A2CE-0025905B85EE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/6E42D8B7-1379-E511-A11A-0026189438B0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/6E5BF226-0379-E511-86B1-003048FFCB84.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/70222278-BD79-E511-AE88-0025905A6080.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/70222A70-2779-E511-9C33-0025905AA9F0.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias6_RECO_16Oct2015_v1_251721_12.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
