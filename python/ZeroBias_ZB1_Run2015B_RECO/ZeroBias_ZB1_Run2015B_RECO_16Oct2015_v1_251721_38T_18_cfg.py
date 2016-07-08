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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/9092047C-5179-E511-8BA3-0025905A6138.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/90A91F0D-A279-E511-9951-0025905A612A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/92B3BD7D-3279-E511-B68A-0025905964A6.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/92C18545-027A-E511-9B70-0025905B8610.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/96A1A279-3279-E511-A950-0025905B85AE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/96ADFD75-5179-E511-B162-0025905A608A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/9816AADB-8D79-E511-93C2-00248C65A3EC.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/984836B5-5F79-E511-A27E-003048FFD720.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/98668E89-5179-E511-B0D2-0025905A6066.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/9A4A2C33-0B79-E511-AAB9-002618943902.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias1_RECO_16Oct2015_v1_251721_18.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
