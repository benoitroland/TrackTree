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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/8E769012-A878-E511-96FF-0025905B8606.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/8EA4AF6B-A778-E511-AB43-0025905A612E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/908ABFBD-6179-E511-82BB-002618FDA28E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/90B20CA4-2479-E511-896F-0025905A48EC.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/9225BDAA-A878-E511-99AD-00261894387A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/925851C5-B278-E511-8F2E-0025905A606A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/9406F874-A778-E511-A188-0025905A60BE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/9438F4A9-B278-E511-9529-002618943985.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/947B70D1-AD78-E511-98B3-0026189438E0.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/94D46D8A-B278-E511-BC83-0026189438F5.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias3_RECO_16Oct2015_v1_251721_17.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
