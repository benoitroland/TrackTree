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
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/70FAC37A-3279-E511-A33D-0025905A6134.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/72D5C96F-0A79-E511-B95B-002618943843.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/7437A17A-0A79-E511-8686-0025905A60CE.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/74E250D8-8D79-E511-B5DA-002618943843.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/766C3DEE-0979-E511-AC17-0025905B8590.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/78187E35-2979-E511-B126-0025905B8596.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/78356D02-0A79-E511-9961-0026189438AA.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/7A161B12-0A79-E511-AAF0-0025905964BA.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/7A9272EE-0979-E511-88B3-0025905A608E.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/16Oct2015-v1/50000/7C7CFA8D-0A79-E511-9998-0025905B85D8.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias1_RECO_16Oct2015_v1_251721_15.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
