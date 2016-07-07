# information about dataset and GT used below
# https://hypernews.cern.ch/HyperNews/CMS/get/relval/3688.html

import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000000))

process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.TrackRefitter.src = 'generalTracks'
process.TrackRefitter.TrajectoryInEvent = True
process.TrackRefitter.TTRHBuilder = "WithAngleAndTemplate"
process.TrackRefitter.NavigationSchool = ""

xrootd = "root://xrootd-cms.infn.it//" 
mcdir = "store/mc/RunIISpring15DR74/ReggeGribovPartonMC_13TeV-EPOS/GEN-SIM-RECODEBUG/PU1p3RealisticRecodebug_castor_741_p1_mcRun2_Realistic_50ns_v0-v2"
directory = xrootd + mcdir

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(directory+'/50000/14F4E60B-536B-E511-94CA-002590D8C68A.root',
                                                              directory+'/50000/167A918A-516B-E511-87FF-20CF3027A5F4.root',
                                                              directory+'/50000/2287A88C-516B-E511-BAD1-00266CF9B86C.root',
                                                              directory+'/50000/281C832A-526B-E511-9E4F-002590D8C77A.root',
                                                              directory+'/50000/2C49C3E5-526B-E511-8AD3-00266CF9B868.root',
                                                              directory+'/50000/36174AEC-516B-E511-8D89-00266CF275E0.root',

                                                              directory+'/50000/3E44F420-576B-E511-AA2C-02163E00CA8C.root',
                                                              directory+'/50000/40ACA59A-536B-E511-8F8B-20CF3027A5FB.root',
                                                              directory+'/50000/4AA35B29-AE6B-E511-8368-B083FED12B5C.root',
                                                              directory+'/50000/4C420DDD-526B-E511-9775-02163E0131E2.root',
                                                              directory+'/50000/4CDF1C84-546B-E511-89C8-02163E00E75B.root',
                                                              directory+'/50000/4EEE7C89-516B-E511-827C-00A0D1EE8A14.root',
                                                              directory+'/50000/52BC5D24-AE6B-E511-BADA-3417EBE705CD.root',
                                                              directory+'/50000/586F0262-546B-E511-89FD-02163E00F4D3.root',
                                                              directory+'/50000/5E51C5E6-516B-E511-961B-02163E016A60.root',
                                                              directory+'/50000/60E10F26-AE6B-E511-8EB7-00266CFAEBF8.root',
                                                              directory+'/50000/6EFBB0D5-586B-E511-B31E-02163E00B11C.root',
                                                              directory+'/50000/700A92EA-516B-E511-91CE-00266CFAE268.root',
                                                              directory+'/50000/744963B2-526B-E511-A5D4-002590D8C72C.root',
                                                              directory+'/50000/7E682E37-526B-E511-B93A-02163E013A6E.root',
                                                              directory+'/50000/822945DA-506B-E511-949B-00266CF20044.root',
                                                              directory+'/50000/88AD6EE4-606B-E511-B793-02163E00E5C1.root',
                                                              directory+'/50000/92B91672-566B-E511-A8B5-00266CFAE1A8.root',
                                                              directory+'/50000/96EDDE5D-516B-E511-AC85-0025903D0B8A.root',
                                                              directory+'/50000/9A7AF68B-576B-E511-85CE-02163E016698.root',
                                                              directory+'/50000/9CBF6CC8-5D6B-E511-B61B-02163E0153D2.root',
                                                              directory+'/50000/A020DFF4-546B-E511-A1C2-00266CF9B86C.root',
                                                              directory+'/50000/A6C7A869-506B-E511-84EA-3417EBE6459A.root',
                                                              directory+'/50000/A8B7614F-516B-E511-8790-00221952AA6A.root',
                                                              directory+'/50000/B02AEEE2-516B-E511-AFD4-20CF3027A5FB.root',
                                                              directory+'/50000/B82DA438-AE6B-E511-9418-02163E016B65.root',
                                                              directory+'/50000/B845CB17-596B-E511-A8E0-02163E00BC3C.root',
                                                              directory+'/50000/BA43A10B-536B-E511-9B70-02163E0148C1.root',
                                                              directory+'/50000/C00C6B9A-536B-E511-8EC9-00266CF9C22C.root',
                                                              directory+'/50000/C497EE36-546B-E511-B05B-002590743042.root',
                                                              directory+'/50000/C60BA5C8-596B-E511-8070-02163E011EB5.root',
                                                              directory+'/50000/D0F55AD8-546B-E511-8DCF-00259073E51E.root',
                                                              directory+'/50000/E07B3BEC-516B-E511-B3B4-00266CF9B86C.root',
                                                              directory+'/50000/E2415AC0-556B-E511-8AC8-FA163EBF4ADD.root',
                                                              directory+'/50000/E40C1C73-5A6B-E511-81D0-02163E00B7E1.root',
                                                              directory+'/50000/E4E083A0-556B-E511-82B3-3417EBE65F65.root',
                                                              directory+'/50000/EA8BD34D-526B-E511-B3A7-00266CF275E0.root',
                                                              directory+'/50000/F06A9381-566B-E511-8A5F-02163E013636.root',
                                                              directory+'/50000/F40B6454-546B-E511-82E4-02163E015559.root',
                                                              directory+'/50000/F8746EE8-526B-E511-A6D2-00266CF275E0.root',
                                                              directory+'/50000/FC4C889B-546B-E511-BD2D-00266CF9BED8.root',
                                                              directory+'/50000/FE65AB9A-536B-E511-9028-02163E014A36.root',
                                                              directory+'/50000/FE79D590-516B-E511-B6BF-00A0D1EE2990.root'
                                                              ))

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.GlobalTag.globaltag = 'MCRUN2_740TV1::All'

process.analysis = cms.EDAnalyzer('TrackTree',
                                  data_type = cms.string('EPOS-38T-PU1p3'), 

                                  L1GT_label = cms.InputTag('gtDigis'),
                                  L1TT_requested = cms.vstring('L1Tech_BSC_minBias_threshold1.v0','L1Tech_BSC_minBias_threshold2.v0',
                                                               'L1Tech_BPTX_plus_AND_minus.v0'),
                                  
                                  HLT_label = cms.InputTag('TriggerResults','','HLT'),
                                  HLT_requested = cms.vstring('HLT_ZeroBias_v1'),
                                  process_label = cms.string('HLT'),
                                  
                                  generaltrack_label = cms.InputTag('TrackRefitter'), # cms.InputTag('generalTracks','','RECO'),
                                  calotower_label = cms.InputTag('towerMaker','', 'RECO'),
                                  genparticle_label = cms.InputTag('genParticles','','HLT'),
                                  recovertex_label = cms.InputTag('offlinePrimaryVertices','','RECO'),
                                  beamspot_label = cms.InputTag('offlineBeamSpot','','RECO'),
                                  hfrechit_label = cms.InputTag('hfreco','','RECO'),
                                  pu_label = cms.InputTag('addPileupInfo','','HLT')
                                  )


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/EPOS-38T/EPOS-38T-PU1p3.root')
                                   )

process.p = cms.Path(process.TrackRefitter*process.analysis)
