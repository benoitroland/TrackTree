import FWCore.ParameterSet.Config as cms

process = cms.Process("TrackAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/00F336E7-3F2C-E511-912B-02163E0139B0.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/0A227A7F-3F2C-E511-871E-02163E011D30.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/14137011-3F2C-E511-A743-02163E01420D.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/164E302C-402C-E511-A760-02163E011F52.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/168CE2A5-3F2C-E511-9EC2-02163E0136A2.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/187FF5AD-3E2C-E511-B997-02163E0139A9.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/1A32F390-3A2C-E511-964F-02163E014527.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/1CF059BE-3B2C-E511-B4C1-02163E012B10.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/1EA8EDB6-452C-E511-8A42-02163E0125C8.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/229843B6-422C-E511-94A3-02163E0133D0.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/26CC6C91-3D2C-E511-BF18-02163E014576.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/34810F68-3D2C-E511-B7E7-02163E0121A1.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/36279E9B-412C-E511-9632-02163E0126D2.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/3AACBA2E-402C-E511-8C83-02163E012377.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/3EA49168-3D2C-E511-8F3F-02163E012620.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/4013E38A-3F2C-E511-99D7-02163E014181.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/40BA5695-422C-E511-B3DC-02163E01364E.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/42EFECB2-3E2C-E511-A7E8-02163E011C0F.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/461FD988-3E2C-E511-B103-02163E0133DE.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/4E1F836A-3C2C-E511-BEFC-02163E014558.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/540275C7-402C-E511-A530-02163E0136A2.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/54B1764C-422C-E511-9C6B-02163E0117FF.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/54C45121-3E2C-E511-AEC0-02163E0127D3.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/56CF95B8-3C2C-E511-8341-02163E013481.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/5EE8D4F5-3A2C-E511-8ACB-02163E012044.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/84349C6F-3C2C-E511-B1EF-02163E0118F0.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/848FEFEC-3D2C-E511-879B-02163E011C0F.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/88296829-3B2C-E511-8598-02163E011D23.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/8AAF7777-3C2C-E511-81C2-02163E011836.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/908635FA-3C2C-E511-BD05-02163E014272.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/90D54424-3C2C-E511-ADC9-02163E014254.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/920F94A8-402C-E511-843C-02163E013436.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/928E21F7-3A2C-E511-B4BE-02163E012377.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/969C91A7-3F2C-E511-A020-02163E013896.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/9CFBFBD8-3E2C-E511-A5FB-02163E014272.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/AC8D0C69-3D2C-E511-8FFD-02163E0126D2.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/B493D34E-412C-E511-99AE-02163E01206A.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/B87AF221-3C2C-E511-A686-02163E014629.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/BAD3DCCC-3C2C-E511-BFFE-02163E0133D0.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/C6A27770-3C2C-E511-976F-02163E0135F3.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/C8B44D67-3D2C-E511-952A-02163E01364E.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/D0B77A19-442C-E511-8055-02163E013599.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/D4096F34-3E2C-E511-98B0-02163E01250C.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/D4E5E73B-412C-E511-84F6-02163E011A29.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/D8399BC2-3B2C-E511-8657-02163E013770.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/D87CA098-3B2C-E511-BF16-02163E013436.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/DA7E648A-402C-E511-9582-02163E01250C.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/DE1670B7-3E2C-E511-9268-02163E0124CC.root'
        ,'root://xrootd-cms.infn.it//store/data/Run2015B/ZeroBias1/RECO/PromptReco-v1/000/251/721/00000/E630A804-3D2C-E511-A818-02163E0128F0.root'
        ,'root://xrootd-cms.infn.it//store/data/run2015b/zerobias1/reco/promptreco-v1/000/251/721/00000/ea953290-3b2c-e511-a49a-02163e01441a.root'
        ,'root://xrootd-cms.infn.it//store/data/run2015b/zerobias1/reco/promptreco-v1/000/251/721/00000/ee22ebcc-3c2c-e511-bc93-02163e011d30.root'
        ,'root://xrootd-cms.infn.it//store/data/run2015b/zerobias1/reco/promptreco-v1/000/251/721/00000/f876f115-3f2c-e511-86c9-02163e011948.root'
        ,'root://xrootd-cms.infn.it//store/data/run2015b/zerobias1/reco/promptreco-v1/000/251/721/00000/f883047d-3f2c-e511-8c86-02163e0135f3.root'
        ,'root://xrootd-cms.infn.it//store/data/run2015b/zerobias1/reco/promptreco-v1/000/251/721/00000/fa074469-3d2c-e511-aefc-02163e0139d5.root'
        ,'root://xrootd-cms.infn.it//store/data/run2015b/zerobias1/reco/promptreco-v1/000/251/721/00000/fef6a457-3c2c-e511-acc4-02163e011a5a.root'
        ),lumisToProcess = cms.untracked.VLuminosityBlockRange('251721:90-251721:max'))
                            
process.load('Configuration.StandardSequences.Services_cff')
# process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v0' # 'GR_P_V56::All'

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
                                  generaltrack_label = cms.InputTag('generalTracks','','RECO'),
                                  calotower_label = cms.InputTag('towerMaker','', 'RECO'),
                                  genparticle_label = cms.InputTag('genParticles','','HLT'),
                                  recovertex_label = cms.InputTag('offlinePrimaryVertices','','RECO'),
                                  beamspot_label = cms.InputTag('offlineBeamSpot','','RECO'),
                                  hfrechit_label = cms.InputTag('hfreco','','RECO'),
                                  pu_label = cms.InputTag('addPileupInfo','','HLT')
                                  )


process.TFileService = cms.Service("TFileService",
             fileName = cms.string('/nfs/dust/cms/user/roland/TrackAnalysis/OutputTree/data-38T/data_Run2015B_ZeroBias1_PromptReco_251721.root')
)

process.p = cms.Path(process.analysis)
