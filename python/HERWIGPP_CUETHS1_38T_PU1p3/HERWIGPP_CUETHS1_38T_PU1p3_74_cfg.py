# information about dataset and GT used below
# https://hypernews.cern.ch/HyperNews/CMS/get/relval/3688.html
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
'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/MinBias_TuneCUETHS1_13TeV-herwigpp/GEN-SIM-RECODEBUG/PU1p3RealisticRecodebug_castor_741_p1_mcRun2_Realistic_50ns_v0-v2/30000/F8F2BF72-3269-E511-8B30-003048FFD744.root',
'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/MinBias_TuneCUETHS1_13TeV-herwigpp/GEN-SIM-RECODEBUG/PU1p3RealisticRecodebug_castor_741_p1_mcRun2_Realistic_50ns_v0-v2/30000/FA40A9F4-3069-E511-986E-0025905B858A.root',
'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/MinBias_TuneCUETHS1_13TeV-herwigpp/GEN-SIM-RECODEBUG/PU1p3RealisticRecodebug_castor_741_p1_mcRun2_Realistic_50ns_v0-v2/30000/FCCC8975-3269-E511-B27C-0025905B85A2.root',
'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/MinBias_TuneCUETHS1_13TeV-herwigpp/GEN-SIM-RECODEBUG/PU1p3RealisticRecodebug_castor_741_p1_mcRun2_Realistic_50ns_v0-v2/30000/FCFA55BC-2D69-E511-BA4E-0025905A60A0.root',
'root://xrootd-cms.infn.it//store/mc/RunIISpring15DR74/MinBias_TuneCUETHS1_13TeV-herwigpp/GEN-SIM-RECODEBUG/PU1p3RealisticRecodebug_castor_741_p1_mcRun2_Realistic_50ns_v0-v2/30000/FE1B3829-2F69-E511-9648-0025905B858E.root'
))

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.GlobalTag.globaltag = 'MCRUN2_740TV1::All'

process.analysis = cms.EDAnalyzer('TrackTree',
                                  data_type = cms.string('HERWIGPP-CUETHS1-38T-PU1p3'),

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
        fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/HERWIGPP-CUETHS1-38T/HERWIGPP-CUETHS1-38T-PU1p3_74.root'))

process.p = cms.Path(process.TrackRefitter*process.analysis)
