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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/ECA82E86-1E79-E511-90B0-0025905B85EE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/EEBC3F74-2779-E511-BEA2-0025905B8610.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/F0B55A1E-0379-E511-9D4F-0025905A48D0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/F2A10AE6-0787-E511-BA2D-0025905A6118.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/F40B0510-0379-E511-8BAE-002618943843.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/F446A60B-0379-E511-AE60-002618943948.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/F4A40179-2279-E511-9999-002590596468.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/F4AF2AD6-2779-E511-B9CA-00261894393F.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/F63C7385-1E79-E511-967B-003048FFD796.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias6/RECO/16Oct2015-v1/80000/F6522A5A-1379-E511-8387-00261894393D.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias6_RECO_16Oct2015_v1_251721_29.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
