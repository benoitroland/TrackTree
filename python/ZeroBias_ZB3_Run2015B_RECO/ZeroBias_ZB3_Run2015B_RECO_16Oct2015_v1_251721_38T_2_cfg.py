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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/04B61DE5-A678-E511-BCAA-0025905A612A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/0640FD15-5A79-E511-813A-003048FFD736.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/0676FBC0-A878-E511-990E-0025905B85EE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/06B9AEF0-B478-E511-BD82-0025905A6094.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/08322D99-E578-E511-9AE5-0025905A6068.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/08957081-A778-E511-B4B6-0025905A60B6.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/0E1FF2E6-AD78-E511-8918-0025905B85B2.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/0EC184E4-AD78-E511-AB49-0025905B855E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/10415769-A778-E511-B9C8-0025905A60F4.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias3/RECO/16Oct2015-v1/10000/10F567D8-5E79-E511-AB3B-0025905A60D6.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias3_RECO_16Oct2015_v1_251721_2.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
