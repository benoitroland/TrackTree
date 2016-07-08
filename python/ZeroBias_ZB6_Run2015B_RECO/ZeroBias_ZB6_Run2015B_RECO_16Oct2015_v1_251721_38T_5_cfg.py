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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/2A6D33B4-7A79-E511-816F-0025905B85E8.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/2AA19E9C-7A79-E511-B118-0025905B8586.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/2CD3F1B1-9C79-E511-980D-003048FFCC1E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/2E44F389-9B79-E511-81E9-0025905A606A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/327337FF-2779-E511-A94C-0025905A6092.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/32AFB365-0E79-E511-AC33-0025905B858A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/34816985-1E79-E511-B805-0025905B85D6.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/349C26C5-0179-E511-B6BC-0025905A48BB.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/34A1ABF7-0D79-E511-86B4-003048FFCBA4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/34F7FA35-3479-E511-B382-00261894393A.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias6_RECO_16Oct2015_v1_251721_5.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
