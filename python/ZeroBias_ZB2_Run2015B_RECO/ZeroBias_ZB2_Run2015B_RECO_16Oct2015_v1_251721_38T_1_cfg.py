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
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/00B2ACA6-9078-E511-B2CC-0025905A610A.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/02B2C157-9178-E511-8445-0025905B858E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/048582A5-4379-E511-BC4A-0025905B8576.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/04ECB0AA-9078-E511-A418-0025905B8596.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/06410C9E-9078-E511-A736-0025905A48EC.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/06AE6AED-C578-E511-8C11-00259059642A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/06DC88A5-4379-E511-9203-00261894380B.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/06E6A534-3D79-E511-94A4-0025905A6066.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/0836DAB5-9078-E511-A920-0025905A610A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias2/RECO/16Oct2015-v1/10000/08DC5668-A278-E511-9365-0025905B8586.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias2_RECO_16Oct2015_v1_251721_1.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
