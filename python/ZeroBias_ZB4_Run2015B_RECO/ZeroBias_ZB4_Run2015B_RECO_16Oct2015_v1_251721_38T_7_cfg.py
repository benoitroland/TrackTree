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
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/40000/FEAFB5D3-2179-E511-B097-0025905A48BB.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/410000/08713F3C-7C84-E511-BE22-0025905A60D6.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/410000/1401DAD3-6086-E511-956C-0025905A606A.root',
#'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/410000/20C65454-7D84-E511-A010-0025905A6090.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/410000/585E7DFC-FE84-E511-9BDB-002590593902.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/410000/5E022CB7-2B86-E511-80E0-0025905B858A.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/410000/5EA56F93-1985-E511-994F-002618943985.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/410000/764E4EC8-7C84-E511-BE07-0025905A611C.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/410000/78373ABC-7A84-E511-8A2A-0025905A612E.root',
'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias4/RECO/16Oct2015-v1/410000/8C22A743-2B86-E511-8BC0-0025905B8592.root'
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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias4_RECO_16Oct2015_v1_251721_7.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
