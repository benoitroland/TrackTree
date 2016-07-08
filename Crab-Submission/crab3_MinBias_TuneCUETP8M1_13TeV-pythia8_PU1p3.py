from WMCore.Configuration import Configuration
config = Configuration()

config.section_("User")
config.User.voGroup = 'dcms'

config.section_("General")
config.General.requestName = 'MinBias_TuneCUETP8M1_13TeV-pythia8_PU1p3'
config.General.workArea = 'MinBias_TuneCUETP8M1_13TeV-pythia8_PU1p3'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'MinBias_TuneCUETP8M1_13TeV-pythia8_PU1p3.py'

config.section_("Data")
config.Data.inputDataset = '/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-PU1p3RealisticRecodebug_741_p1_mcRun2_Realistic_50ns_v0-v2/GEN-SIM-RECODEBUG'
config.Data.splitting = 'EventAwareLumiBased' 
config.Data.unitsPerJob = 100
config.Data.totalUnits = 1000

config.section_("Site")
config.Site.storageSite = "T2_DE_DESY"

