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
'root://xrootd-cms.infn.it//store/user/hvanhaev/ZeroBias1/Run2015B-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1/151008_130104/0000/output_data_rereco_9.root',
'root://xrootd-cms.infn.it//store/user/hvanhaev/ZeroBias1/Run2015B-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1/151008_130104/0000/output_data_rereco_90.root',
'root://xrootd-cms.infn.it//store/user/hvanhaev/ZeroBias1/Run2015B-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1/151008_130104/0000/output_data_rereco_91.root',
'root://xrootd-cms.infn.it//store/user/hvanhaev/ZeroBias1/Run2015B-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1/151008_130104/0000/output_data_rereco_92.root',
'root://xrootd-cms.infn.it//store/user/hvanhaev/ZeroBias1/Run2015B-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1/151008_130104/0000/output_data_rereco_93.root',
'root://xrootd-cms.infn.it//store/user/hvanhaev/ZeroBias1/Run2015B-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1/151008_130104/0000/output_data_rereco_94.root',
'root://xrootd-cms.infn.it//store/user/hvanhaev/ZeroBias1/Run2015B-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1/151008_130104/0000/output_data_rereco_95.root',
'root://xrootd-cms.infn.it//store/user/hvanhaev/ZeroBias1/Run2015B-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1/151008_130104/0000/output_data_rereco_96.root',
'root://xrootd-cms.infn.it//store/user/hvanhaev/ZeroBias1/Run2015B-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1/151008_130104/0000/output_data_rereco_97.root',
'root://xrootd-cms.infn.it//store/user/hvanhaev/ZeroBias1/Run2015B-v1_LowPU_RERECO_74X_dataRun2_Prompt_v2_withCustomCond-v1/151008_130104/0000/output_data_rereco_98.root '
),lumisToProcess = cms.untracked.VLuminosityBlockRange('251721:90-251721:max'))

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v0' #'GR_P_V56::All'

process.analysis = cms.EDAnalyzer('TrackTree',
                                  data_type = cms.string('data-HFRereco-38T'),

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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-HFRereco-38T/data_Run2015B_ZeroBias1_Prompt_v2_251721_HFRereco_12.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
