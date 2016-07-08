from WMCore.Configuration import Configuration
config = Configuration()

config.section_("User")
config.User.voGroup = 'dcms'

config.section_("General")
config.General.requestName = 'ZeroBias_Run2015B_PromptReco_v1'
config.General.workArea = 'ZeroBias_Run2015B_PromptReco_v1_TrackTree'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ConfFile_ZeroBias_Run2015B_PromptReco_v1_cfg.py'

config.section_("Data")
config.Data.inputDataset = '/ZeroBias/Run2015B-PromptReco-v1/RECO'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-251642_13TeV_PromptReco_Collisions15_JSON.txt'
config.Data.runRange = '251000-252000' 
config.Data.publishDataName = 'crab3_ZeroBias_Run2015B_PromptReco_v1_TrackTree'

config.section_("Site")
config.Site.storageSite = "T2_DE_DESY"
