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
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/EEDCE0DF-9178-E511-8D15-003048FFCBB0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/EEEEA6A7-A678-E511-B202-0025905964C0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/F0045BB3-A678-E511-9AD3-0025905A60A6.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/F0290A5E-9178-E511-BACC-0025905B859E.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/F099C5CD-9178-E511-9782-0025905B85B2.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/F0C311A5-4379-E511-9BD5-0025905A6126.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/F0DA04A9-9078-E511-B88C-0025905A48F0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/F0E07F70-A278-E511-BA2A-0025905A6084.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/F0E65036-A678-E511-9523-002618943970.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/F24C8CD9-9178-E511-B3FC-0025905A60D2.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias2_RECO_16Oct2015_v1_251721_27.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
