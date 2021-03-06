//-- system include files
#include <memory>
#include<iostream>
#include<vector>
#include<cstring>
#include<fstream>

#include "../src/classes.h"

//-- user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"

#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h" 

#include "DataFormats/TrackReco/interface/HitPattern.h"

#include "TrackingTools/Records/interface/TransientRecHitRecord.h"
#include "TrackingTools/TransientTrackingRecHit/interface/TransientTrackingRecHit.h"
#include "TrackingTools/TransientTrackingRecHit/interface/TransientTrackingRecHitBuilder.h"

#include "DataFormats/CaloTowers/interface/CaloTower.h"
#include "DataFormats/CaloTowers/interface/CaloTowerFwd.h"
#include "DataFormats/CaloTowers/interface/CaloTowerDetId.h"

#include "DataFormats/HcalDetId/interface/HcalDetId.h"
#include "DataFormats/HcalDetId/interface/HcalSubdetector.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "DataFormats/L1GlobalTrigger/interface/L1GtFdlWord.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"

#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

#include "CondFormats/L1TObjects/interface/L1GtTriggerMenu.h"
#include "CondFormats/DataRecord/interface/L1GtTriggerMenuRcd.h"

#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalSourcePositionData.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"

#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"

#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "DataFormats/HcalRecHit/interface/HFRecHit.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "DataFormats/SiStripDetId/interface/TIBDetId.h"
#include "DataFormats/SiStripDetId/interface/TOBDetId.h"
#include "DataFormats/SiStripDetId/interface/TIDDetId.h"
#include "DataFormats/SiStripDetId/interface/TECDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXFDetId.h"

#include "TH1.h"
#include "TH2.h"
#include "TMath.h"
#include "TTree.h"
#include "TString.h"

#define debugL1TT 0
#define debugHLT 0
#define debugVertex 0
#define debugGenVertex 0
#define debugTrack 0
#define debugParticle 0
#define debugHFTower 0
#define debugHFRechit 0
#define debugPU 0
#define debugTrackHit 0

//-- class declaration

class TrackTree : public edm::EDAnalyzer {

public:
  explicit TrackTree(const edm::ParameterSet&);
  ~TrackTree();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  virtual void beginJob();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob();
  
  virtual void beginRun(const edm::Run&, const edm::EventSetup&);
  //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

  int Nwritten = 0;

  //-- Event Setup variables

  edm::ESHandle<TrackerGeometry> trackerGeom;
  edm::ESHandle<HcalDbService> hcalConditions;
  edm::ESHandle<CaloGeometry> caloGeom;

  //-- input tag

  edm::InputTag pu_label;
  edm::InputTag generaltrack_label;
  edm::InputTag calotower_label;
  edm::InputTag genparticle_label;
  edm::InputTag recovertex_label;
  edm::InputTag beamspot_label;
  edm::InputTag hfrechit_label;

  edm::InputTag L1GT_label;
  std::vector<std::string> L1TT_requested;

  edm::InputTag HLT_label;
  std::vector<std::string> HLT_requested;
  std::string process_label;

  //-- tree				       
  
  TTree *tTrack;			       
  
  //-- data type 
  
  std::string DataType;
  bool IsData;

  //-- event id

  int Run,Event,LumiSection;
  int Bunch,Orbit;

  //-- pileup information

  int nbxint,nbxearly,nbxlate,nbxtot;
  double PUint,PUearly,PUlate,PUtot;
  double NumInteraction;                  

  //-- track			       
  
  int nTrack,nTrackmax;			       
  
  std::vector<double> TrackPt;		       
  std::vector<double> TrackEta;		       
  std::vector<double> TrackPhi;		       
  
  std::vector<double> TrackPtError;	       
  std::vector<double> TrackEtaError;	       
  std::vector<double> TrackPhiError;	       

  std::vector<double> Trackdxy; 
  std::vector<double> TrackdxyError;

  std::vector<double> Trackdz;
  std::vector<double> TrackdzError;
  
  std::vector<int> TrackCharge;		       

  std::vector<double> Trackchi2;
  std::vector<double> Trackndof;
  std::vector<double> Trackchi2ndof;

  std::vector<int> TrackValidHit;
  std::vector<int> TrackLostHit;

  std::vector<int> TrackQuality;    

  //-- track rechit

  std::vector< std::vector<double> > TrackHitR;	     
  std::vector< std::vector<double> > TrackHitTheta;     
  std::vector< std::vector<double> > TrackHitPhi;	     
  
  std::vector< std::vector<double> > TrackHitEta;	     
  
  std::vector< std::vector<double> > TrackHitX;	     
  std::vector< std::vector<double> > TrackHitY;	     
  std::vector< std::vector<double> > TrackHitZ;         
  
  std::vector< std::vector<int> > TrackHitDet;          
  std::vector< std::vector<int> > TrackHitSubdet;       

  //-- generated particles

  int nParticle,nParticlemax;			  
  
  std::vector<double> ParticleEnergy;
  std::vector<double> ParticlePt;		  
  std::vector<double> ParticleEta;		  
  std::vector<double> ParticlePhi;		  
  
  std::vector<int> ParticleCharge;		  
  std::vector<int> ParticleStatus;
  std::vector<int> ParticleId;

  //-- HF tower 			       
  
  int nHFTower,nHFTowermax;		       
  
  double HFplusTowerLeadingEnergy;
  double HFplusTowerLeadingEta;
  double HFplusTowerLeadingPhi;    

  double HFminusTowerLeadingEnergy; 
  double HFminusTowerLeadingEta;	   
  double HFminusTowerLeadingPhi;    

  double HFTowerEtot;			       
  
  std::vector<double> HFTowerEnergy;	       
  std::vector<double> HFTowerEta;	       
  std::vector<double> HFTowerPhi;	       

  std::vector<bool> HFTowerPlus;
  std::vector<bool> HFTowerMinus;

  //-- HF rechit

  int nHFRechit,nHFRechitmax;

  std::vector<double> HFRechitEnergy;
  std::vector<double> HFRechitEt;
  std::vector<double> HFRechitTime;

  std::vector<int> HFRechitiEta;
  std::vector<int> HFRechitiPhi;
  std::vector<int> HFRechitDepth;

  std::vector<double> HFRechitEta;
  std::vector<double> HFRechitPhi;          

  //-- generated vertex 

  double GenVx;
  double GenVy;
  double GenVz;

  //-- reco vertex

  int nVertex,nVertexmax;
  
  std::vector<double> Vx;
  std::vector<double> Vy;
  std::vector<double> Vz;
  
  std::vector<double> Vrho;

  std::vector<double> VxError;
  std::vector<double> VyError;
  std::vector<double> VzError;
  
  std::vector<double> Vchi2;
  std::vector<double> Vndof;
  std::vector<double> Vchi2ndof;

  std::vector<bool> VisFake;
  std::vector<bool> VisValid;
  std::vector<bool> VisBest;

  std::vector<int> VnTrack;
  std::vector<double> VsumPt;

  std::vector< std::vector<double> > VTrackPt;
  std::vector< std::vector<double> > VTrackEta;
  std::vector< std::vector<double> > VTrackPhi;

  std::vector< std::vector<double> > VTrackPtError; 
  std::vector< std::vector<double> > VTrackEtaError;  
  std::vector< std::vector<double> > VTrackPhiError;  

  std::vector< std::vector<double> > VTrackdxy;    
  std::vector< std::vector<double> > VTrackdxyError;
                                 
  std::vector< std::vector<double> > VTrackdz;	   
  std::vector< std::vector<double> > VTrackdzError;

  std::vector< std::vector<int> > VTrackCharge;	    
                                  
  std::vector< std::vector<double> > VTrackchi2;    
  std::vector< std::vector<double> > VTrackndof;    
  std::vector< std::vector<double> > VTrackchi2ndof;

  std::vector< std::vector<int> > VTrackValidHit; 
  std::vector< std::vector<int> > VTrackLostHit;  

  std::vector< std::vector<int> > VTrackValidPixelHit;
  std::vector< std::vector<int> > VTrackValidStripHit;

  std::vector< std::vector<int> > VTrackQuality;      

  std::vector< std::vector<double> > VTrackWeight;
  
  //-- beamspot

  double BSx,BSy,BSz;
  double BSxError,BSyError,BSzError;

  double BSdxdz,BSdydz;
  double BSdxdzError,BSdydzError;

  double BSwidthX,BSwidthY,BSsigmaZ;
  double BSwidthXError,BSwidthYError,BSsigmaZError;
  
  //-- weight			       
                                             
  double event_weight;			       

  //-- detector level selection

  bool HFAND_reco;
  bool HFOR_reco;
  bool HFXOR_reco;

  //-- hadron level selection

  bool HFAND_gen;
  bool HFOR_gen;
  bool HFXOR_gen;

  //-- L1 Trigger

  std::vector<std::string> L1TTname;
  std::vector<int> L1TTbit;
  std::vector<bool> L1TTdecision;

  //-- HLT Trigger

  HLTConfigProvider HLTconfig;

  std::vector<std::string> HLTname;
  std::vector<unsigned int> HLTindex;
  std::vector<double> HLTprescale;
  std::vector<double> L1prescale;
  std::vector<bool> HLTdecision;
};

//-- constants, enums and typedefs

//-- static data member definitions

//-- constructors and destructor

TrackTree::TrackTree(const edm::ParameterSet& iConfig) {

  //-- initialization 

  IsData = false;
  DataType = iConfig.getParameter<std::string>("data_type");
  if(DataType.compare("data-0T")==0) IsData = true;   
  if(DataType.compare("data-38T")==0) IsData = true;
  if(DataType.compare("data-HFRereco-38T")==0) IsData = true;
  if(DataType.compare("data-PromptReco-38T")==0) IsData = true;

  pu_label = iConfig.getParameter<edm::InputTag>("pu_label");
  generaltrack_label = iConfig.getParameter<edm::InputTag>("generaltrack_label");
  calotower_label = iConfig.getParameter<edm::InputTag>("calotower_label");
  if(!IsData) genparticle_label = iConfig.getParameter<edm::InputTag>("genparticle_label");
  recovertex_label = iConfig.getParameter<edm::InputTag>("recovertex_label");
  beamspot_label = iConfig.getParameter<edm::InputTag>("beamspot_label");
  hfrechit_label = iConfig.getParameter<edm::InputTag>("hfrechit_label");

  if(IsData) {
    L1GT_label = iConfig.getParameter<edm::InputTag>("L1GT_label");
    L1TT_requested = iConfig.getParameter<std::vector<std::string> >("L1TT_requested");

    HLT_label = iConfig.getParameter<edm::InputTag>("HLT_label");
    HLT_requested  = iConfig.getParameter<std::vector<std::string> >("HLT_requested");
    process_label = iConfig.getParameter<std::string>("process_label");
  }

  edm::Service<TFileService> fs;

  //-- tree

  tTrack = fs->make<TTree>("TrackAnalysis","TrackAnalysis");

  //-- data type

  tTrack->Branch("IsData",&IsData,"IsData/O");
  tTrack->Branch("DataType",&DataType,"DataType/C");

  //-- event id

  tTrack->Branch("Run",&Run,"Run/I");
  tTrack->Branch("Event",&Event,"Event/I");
  tTrack->Branch("LumiSection",&LumiSection,"LumiSection/I");
  
  tTrack->Branch("Bunch",&Bunch,"Bunch/I");
  tTrack->Branch("Orbit",&Orbit,"Orbit/I");
  
  //-- pileup information		  
    
  if(!IsData) {

    tTrack->Branch("nbxint",&nbxint,"nbxint/I");				  
    tTrack->Branch("nbxearly",&nbxearly,"nbxearly/I");				  
    tTrack->Branch("nbxlate",&nbxlate,"nbxlate/I");				  
    tTrack->Branch("nbxtot",&nbxtot,"nbxtot/I");				  
    
    tTrack->Branch("PUint",&PUint,"PUint/D");		
    tTrack->Branch("PUearly",&PUearly,"PUearly/D");	
    tTrack->Branch("PUlate",&PUlate,"PUlate/D");	
    tTrack->Branch("PUtot",&PUtot,"PUtot/D");	
    
    tTrack->Branch("NumInteraction",&NumInteraction,"NumInteraction/D");              
  }

  //-- track

  tTrack->Branch("nTrack",&nTrack,"nTrack/I");

  tTrack->Branch("TrackPt",&TrackPt);
  tTrack->Branch("TrackEta",&TrackEta);
  tTrack->Branch("TrackPhi",&TrackPhi);
  
  tTrack->Branch("TrackPtError",&TrackPtError);  
  tTrack->Branch("TrackEtaError",&TrackEtaError);
  tTrack->Branch("TrackPhiError",&TrackPhiError);

  tTrack->Branch("Trackdxy",&Trackdxy);
  tTrack->Branch("TrackdxyError",&TrackdxyError);

  tTrack->Branch("Trackdz",&Trackdz);		 
  tTrack->Branch("TrackdzError",&TrackdzError);

  tTrack->Branch("TrackCharge",&TrackCharge);

  tTrack->Branch("Trackchi2",&Trackchi2);
  tTrack->Branch("Trackndof",&Trackndof);
  tTrack->Branch("Trackchi2ndof",&Trackchi2ndof);
  
  tTrack->Branch("TrackValidHit",&TrackValidHit);
  tTrack->Branch("TrackLostHit",&TrackLostHit);

  tTrack->Branch("TrackQuality",&TrackQuality);

  //-- track rechit

  tTrack->Branch("TrackHitR",&TrackHitR);	      
  tTrack->Branch("TrackHitTheta",&TrackHitTheta);      
  tTrack->Branch("TrackHitPhi",&TrackHitPhi);	      
                                                       
  tTrack->Branch("TrackHitEta",&TrackHitEta);	      
							      
  tTrack->Branch("TrackHitX",&TrackHitX);	      
  tTrack->Branch("TrackHitY",&TrackHitY);	      
  tTrack->Branch("TrackHitZ",&TrackHitZ);       	      
							      
  tTrack->Branch("TrackHitDet",&TrackHitDet);	      
  tTrack->Branch("TrackHitSubdet",&TrackHitSubdet);    
  
  //-- generated particles

  if(!IsData) {
    tTrack->Branch("nParticle",&nParticle,"nParticle/I");

    tTrack->Branch("ParticleEnergy",&ParticleEnergy);
    tTrack->Branch("ParticlePt",&ParticlePt);  
    tTrack->Branch("ParticleEta",&ParticleEta);
    tTrack->Branch("ParticlePhi",&ParticlePhi);
    
    tTrack->Branch("ParticleCharge",&ParticleCharge);
    tTrack->Branch("ParticleStatus",&ParticleStatus);
    tTrack->Branch("ParticleId",&ParticleId);
  }

  //-- HF tower

  tTrack->Branch("nHFTower",&nHFTower,"nHFTower/I");
  tTrack->Branch("HFTowerEtot",&HFTowerEtot,"HFTowerEtot/D");
  
  tTrack->Branch("HFplusTowerLeadingEnergy",&HFplusTowerLeadingEnergy,"HFplusTowerLeadingEnergy/D");
  tTrack->Branch("HFplusTowerLeadingEta",&HFplusTowerLeadingEta,"HFplusTowerLeadingEta/D");
  tTrack->Branch("HFplusTowerLeadingPhi",&HFplusTowerLeadingPhi,"HFplusTowerLeadingPhi/D");

  tTrack->Branch("HFminusTowerLeadingEnergy",&HFminusTowerLeadingEnergy,"HFminusTowerLeadingEnergy/D");
  tTrack->Branch("HFminusTowerLeadingEta",&HFminusTowerLeadingEta,"HFminusTowerLeadingEta/D");
  tTrack->Branch("HFminusTowerLeadingPhi",&HFminusTowerLeadingPhi,"HFminusTowerLeadingPhi/D");

  tTrack->Branch("HFTowerEnergy",&HFTowerEnergy);
  tTrack->Branch("HFTowerEta",&HFTowerEta);
  tTrack->Branch("HFTowerPhi",&HFTowerPhi);      

  tTrack->Branch("HFTowerPlus",&HFTowerPlus);
  tTrack->Branch("HFTowerMinus",&HFTowerMinus);
  
  //-- HF rechit			    
  
  tTrack->Branch("nHFRechit",&nHFRechit,"nHFRechit/I");

  tTrack->Branch("HFRechitEnergy",&HFRechitEnergy); 	    
  tTrack->Branch("HFRechitEt",&HFRechitEt);	  
  tTrack->Branch("HFRechitTime",&HFRechitTime);	  

  tTrack->Branch("HFRechitiEta",&HFRechitiEta);	  
  tTrack->Branch("HFRechitiPhi",&HFRechitiPhi);	  
  tTrack->Branch("HFRechitDepth",&HFRechitDepth); 	    

  tTrack->Branch("HFRechitEta",&HFRechitEta);	  
  tTrack->Branch("HFRechitPhi",&HFRechitPhi);        

  //-- generated vertex 

  if(!IsData) {
    tTrack->Branch("GenVx",&GenVx,"GenVx/D");
    tTrack->Branch("GenVy",&GenVy,"GenVy/D");
    tTrack->Branch("GenVz",&GenVz,"GenVz/D");
  }

  //-- reco vertex		 

  tTrack->Branch("nVertex",&nVertex,"nVertex/I");
  
  tTrack->Branch("Vx",&Vx);
  tTrack->Branch("Vy",&Vy);
  tTrack->Branch("Vz",&Vz);

  tTrack->Branch("Vrho",&Vrho);

  tTrack->Branch("VxError",&VxError);
  tTrack->Branch("VyError",&VyError);
  tTrack->Branch("VzError",&VzError);
  
  tTrack->Branch("Vchi2",&Vchi2);
  tTrack->Branch("Vndof",&Vndof);
  tTrack->Branch("Vchi2ndof",&Vchi2ndof);

  tTrack->Branch("VisFake",&VisFake);
  tTrack->Branch("VisValid",&VisValid);
  tTrack->Branch("VisBest",&VisBest);

  tTrack->Branch("VnTrack",&VnTrack);
  tTrack->Branch("VsumPt",&VsumPt);

  tTrack->Branch("VTrackPt",&VTrackPt);
  tTrack->Branch("VTrackEta",&VTrackEta);
  tTrack->Branch("VTrackPhi",&VTrackPhi);

  tTrack->Branch("VTrackPtError",&VTrackPtError);	 
  tTrack->Branch("VTrackEtaError",&VTrackEtaError);
  tTrack->Branch("VTrackPhiError",&VTrackPhiError);

  tTrack->Branch("VTrackdxy",&VTrackdxy);
  tTrack->Branch("VTrackdxyError",&VTrackdxyError);

  tTrack->Branch("VTrackdz",&VTrackdz);	   
  tTrack->Branch("VTrackdzError",&VTrackdzError);

  tTrack->Branch("VTrackCharge",&VTrackCharge);

  tTrack->Branch("VTrackchi2",&VTrackchi2);
  tTrack->Branch("VTrackndof",&VTrackndof);
  tTrack->Branch("VTrackchi2ndof",&VTrackchi2ndof);
  
  tTrack->Branch("VTrackValidHit",&VTrackValidHit);
  tTrack->Branch("VTrackLostHit",&VTrackLostHit);

  tTrack->Branch("VTrackValidPixelHit",&VTrackValidPixelHit);
  tTrack->Branch("VTrackValidStripHit",&VTrackValidStripHit);

  tTrack->Branch("VTrackQuality",&VTrackQuality);

  tTrack->Branch("VTrackWeight",&VTrackWeight);

  //-- beamspot

  tTrack->Branch("BSx",&BSx,"BSx/D");
  tTrack->Branch("BSy",&BSy,"BSy/D");
  tTrack->Branch("BSz",&BSz,"BSz/D");
  
  tTrack->Branch("BSxError",&BSxError,"BSxError/D");
  tTrack->Branch("BSyError",&BSyError,"BSyError/D");
  tTrack->Branch("BSzError",&BSzError,"BSzError/D");

  tTrack->Branch("BSdxdz",&BSdxdz,"BSdxdz/D");
  tTrack->Branch("BSdydz",&BSdydz,"BSdydz/D");
  
  tTrack->Branch("BSdxdzError",&BSdxdzError,"BSdxdzError/D");
  tTrack->Branch("BSdydzError",&BSdydzError,"BSdydzError/D");

  tTrack->Branch("BSwidthX",&BSwidthX,"BSwidthX/D");
  tTrack->Branch("BSwidthY",&BSwidthY,"BSwidthY/D");
  tTrack->Branch("BSsigmaZ",&BSsigmaZ,"BSsigmaZ/D");

  tTrack->Branch("BSwidthXError",&BSwidthXError,"BSwidthXError/D");
  tTrack->Branch("BSwidthYError",&BSwidthYError,"BSwidthYError/D");
  tTrack->Branch("BSsigmaZError",&BSsigmaZError,"BSsigmaZError/D");
  
  //-- weight

  tTrack->Branch("event_weight",&event_weight,"event_weight/D");

  //-- detector level selection

  tTrack->Branch("HFAND_reco",&HFAND_reco,"HFAND_reco/O");
  tTrack->Branch("HFOR_reco",&HFOR_reco,"HFOR_reco/O");
  tTrack->Branch("HFXOR_reco",&HFXOR_reco,"HFXOR_reco/O");
  
  //-- hadron level selection

  if(!IsData) {
    tTrack->Branch("HFAND_gen",&HFAND_gen,"HFAND_gen/O");
    tTrack->Branch("HFOR_gen",&HFOR_gen,"HFOR_gen/O");
    tTrack->Branch("HFXOR_gen",&HFXOR_gen,"HFXOR_gen/O");
  }

  //-- L1 Trigger
  
  if(IsData) {
    tTrack->Branch("L1TTname",&L1TTname);
    tTrack->Branch("L1TTbit",&L1TTbit);
    tTrack->Branch("L1TTdecision",&L1TTdecision);
  }

  //-- HLT Trigger
  
  if(IsData) {
    tTrack->Branch("HLTname",&HLTname);
    tTrack->Branch("HLTindex",&HLTindex);
    tTrack->Branch("HLTprescale",&HLTprescale);
    tTrack->Branch("L1prescale",&L1prescale);
    tTrack->Branch("HLTdecision",&HLTdecision);
  }
}


TrackTree::~TrackTree(){
  //-- do anything here that needs to be done at desctruction time
  //-- e.g. close files, deallocate resources etc.
}

//-- member functions


//-- method called for each event
void TrackTree::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup){
  
  using namespace edm;
  using namespace std;
  using namespace reco; 

  //-- event id
  
  Run = iEvent.id().run();   
  Event = iEvent.id().event();
  LumiSection = iEvent.luminosityBlock();

  Bunch = iEvent.bunchCrossing();
  Orbit = iEvent.orbitNumber();
  
  //-- cout<<"Lumi Section = "<<LumiSection<<endl;

  //-- weight			                                                      
  event_weight = 1;

  //-- HF rechit
  
  //-- for eta and phi information
  
  //-- edm::ESHandle<HcalDbService> hcalConditions;
  //-- iSetup.get < HcalDbRecord > ().get(hcalConditions);

  //-- edm::ESHandle < CaloGeometry > caloGeom;
  //-- iSetup.get < CaloGeometryRecord > ().get(caloGeom);
  
  const CaloGeometry* fGeo = caloGeom.product();
     
  edm::Handle<HFRecHitCollection> hfrechitcollection;
  iEvent.getByLabel(hfrechit_label,hfrechitcollection);

  HFRecHitCollection::const_iterator hfrechit;

  nHFRechit = 0;

  HFRechitEnergy.clear();	
  HFRechitEt.clear();	    	
  HFRechitTime.clear();	    	

  HFRechitiEta.clear();	    	
  HFRechitiPhi.clear();	    	
  HFRechitDepth.clear();	

  HFRechitEta.clear();	    	
  HFRechitPhi.clear();          

  for(hfrechit = hfrechitcollection->begin(); hfrechit != hfrechitcollection->end(); hfrechit++) {
    if (hfrechit->id().subdet() == HcalForward) {
      nHFRechit++;
      
      GlobalPoint fPos = fGeo->getPosition(hfrechit->id()); //-- for eta and phi information

      HFRechitEnergy.push_back(hfrechit->energy());	
      HFRechitEt.push_back(hfrechit->energy()/TMath::CosH(fPos.eta()));	    	
      HFRechitTime.push_back(hfrechit->time());	    	

      HFRechitiEta.push_back(hfrechit->id().ieta());	    	
      HFRechitiPhi.push_back(hfrechit->id().iphi());	    	
      HFRechitDepth.push_back(hfrechit->id().depth());	

      HFRechitEta.push_back(fPos.eta());	    	
      HFRechitPhi.push_back(fPos.phi());          
    }
  }
  
  if(nHFRechit > nHFRechitmax) nHFRechitmax = nHFRechit;       		

  if(debugHFRechit) {
    cout<<"n HF Rechit = "<<nHFRechit<<endl<<endl;
    getchar();

    for(int irh = 0; irh < nHFRechit; ++irh) {
      
      cout<<"HF Rechit "<<irh+1<<":"<<endl<<endl;
      
      cout<<"Energy = "<<HFRechitEnergy.at(irh)<<endl; 	    
      cout<<"Et = "<<HFRechitEt.at(irh)<<endl;       
      cout<<"Time = "<<HFRechitTime.at(irh)<<endl<<endl;     
      
      cout<<"iEta = "<<HFRechitiEta.at(irh)<<endl;     
      cout<<"iPhi = "<<HFRechitiPhi.at(irh)<<endl;     
      cout<<"Depth = "<<HFRechitDepth.at(irh)<<endl<<endl;    
      
      cout<<"Eta = "<<HFRechitEta.at(irh)<<endl;      
      cout<<"Phi = "<<HFRechitPhi.at(irh)<<endl<<endl;       
    }
    cout<<endl<<endl;
    getchar();
  }

  //-- HF tower
  edm::Handle<CaloTowerCollection> calotowercollection;
  iEvent.getByLabel(calotower_label,calotowercollection);
  
  CaloTowerCollection::const_iterator calotower; 

  nHFTower = 0;	                           
  HFTowerEtot = 0;      
     
  HFplusTowerLeadingEnergy = 0;
  HFplusTowerLeadingEta = 0;
  HFplusTowerLeadingPhi = 0;

  HFminusTowerLeadingEnergy = 0;
  HFminusTowerLeadingEta = 0;
  HFminusTowerLeadingPhi = 0;
  
  HFTowerEnergy.clear();
  HFTowerEta.clear();   
  HFTowerPhi.clear();   
  
  HFTowerPlus.clear(); 
  HFTowerMinus.clear();

  //-- HF reco level selection
  double EHFcut_reco = 5;
  bool HFPlusSel_reco = false;
  bool HFMinusSel_reco = false;
  
  HFAND_reco = false;
  HFOR_reco = false;
  HFXOR_reco = false;
 
  for(calotower = calotowercollection->begin(); calotower != calotowercollection->end(); ++calotower)
    {
      bool isHFPlus = false; 
      bool isHFMinus = false;
      
      //-- loop over CaloTower constituents
      for(size_t iconst = 0; iconst < calotower->constituentsSize(); iconst++) {
	DetId detId = calotower->constituent(iconst);
	
	if(detId.det() == DetId::Hcal) {
	  HcalDetId hcalDetId(detId);
	  
	  if(hcalDetId.subdet() == HcalForward && calotower->eta() > 0) isHFPlus = true;
	  if(hcalDetId.subdet() == HcalForward && calotower->eta() < 0) isHFMinus = true;
	} 
      }

      //-- keep information about HF Tower
      if(!isHFPlus && !isHFMinus) continue;

      HFTowerPlus.push_back(isHFPlus);	
      HFTowerMinus.push_back(isHFMinus);
			   										     
      HFTowerEnergy.push_back(calotower->energy());								   
      HFTowerEta.push_back(calotower->eta());									   
      HFTowerPhi.push_back(calotower->phi());									   
	
      nHFTower++;												  
      HFTowerEtot+=calotower->energy();									   
      
      if(calotower->eta() > 0 && calotower->energy() > HFplusTowerLeadingEnergy) {
	HFplusTowerLeadingEnergy = calotower->energy();
	HFplusTowerLeadingEta = calotower->eta();
	HFplusTowerLeadingPhi = calotower->phi();
      }
      
      if(calotower->eta() < 0 && calotower->energy() > HFminusTowerLeadingEnergy) {
	HFminusTowerLeadingEnergy = calotower->energy();
	HFminusTowerLeadingEta = calotower->eta();
	HFminusTowerLeadingPhi = calotower->phi();
      }

      //-- detector level selection
      if(calotower->energy() > EHFcut_reco && isHFPlus) HFPlusSel_reco = true;
      if(calotower->energy() > EHFcut_reco && isHFMinus) HFMinusSel_reco = true;
  
    } //-- end loop over calotower
  
  if(HFPlusSel_reco && HFMinusSel_reco) HFAND_reco = true;
  if(HFPlusSel_reco || HFMinusSel_reco) HFOR_reco = true;
  if((HFPlusSel_reco && !HFMinusSel_reco) || (HFMinusSel_reco && !HFPlusSel_reco)) HFXOR_reco = true;
  
  if(nHFTower > nHFTowermax) nHFTowermax = nHFTower;       		
  
  if(debugHFTower) {								
    cout<<"n HF Tower = "<<nHFTower<<endl;				
    cout<<"HF Tower E tot = "<<HFTowerEtot<<endl<<endl;			
    
    cout<<"HF plus Tower Leading Energy = "<<HFplusTowerLeadingEnergy<<endl;									
    cout<<"HF plus Tower Leading Eta = "<<HFplusTowerLeadingEta<<endl;									
    cout<<"HF plus Tower Leading Phi = "<<HFplusTowerLeadingPhi<<endl<<endl;									
    
    cout<<"HF minus Tower Leading Energy = "<<HFminusTowerLeadingEnergy<<endl;									
    cout<<"HF minus Tower Leading Eta = "<<HFminusTowerLeadingEta<<endl;									
    cout<<"HF minus Tower Leading Phi = "<<HFminusTowerLeadingPhi<<endl<<endl;

    getchar();

    for(int itower = 0; itower < nHFTower; ++itower) {			
      cout<<"HF Tower "<<itower+1<<")"<<endl;				
      cout<<"HF Tower Energy = "<<HFTowerEnergy.at(itower)<<endl;	
      cout<<"HF Tower Eta = "<<HFTowerEta.at(itower)<<endl;		
      cout<<"HF Tower Phi = "<<HFTowerPhi.at(itower)<<endl;	
      cout<<"HF Tower Plus = "<<HFTowerPlus.at(itower)<<endl;
      cout<<"HF Tower Minus = "<<HFTowerMinus.at(itower)<<endl<<endl;
    }
  }                                                                    
  
  //-- generated particles
  if(!IsData) {
    
    edm::Handle<reco::GenParticleCollection> genparticlecollection;
    iEvent.getByLabel(genparticle_label,genparticlecollection);
    
    GenParticleCollection::const_iterator genparticle;
    
    nParticle = 0;							
    
    ParticleEnergy.clear();						
    ParticlePt.clear();		  				
    ParticleEta.clear();		  				
    ParticlePhi.clear();		  				
    
    ParticleCharge.clear();		  				
    ParticleStatus.clear();						
    ParticleId.clear();						

    //-- HF gen level selection
    double EHFcut_gen = 5;
    bool HFPlusSel_gen = false;
    bool HFMinusSel_gen = false;
    
    HFAND_gen = false;
    HFOR_gen = false;
    HFXOR_gen = false;
    
    for(genparticle = genparticlecollection->begin(); genparticle != genparticlecollection->end() ; ++genparticle) {	  
                                                                                                                      
      if(genparticle->status() != 1) continue;								
		  
      int part_id = abs(genparticle->pdgId());								     

      if(part_id == 12 || part_id == 14 || part_id == 16) continue; //-- do not take into account neutrinos  
      if(part_id == 13) continue; //-- do not take into account muons                                        
															  
      ParticleEnergy.push_back(genparticle->energy());									  
      ParticlePt.push_back(genparticle->pt());	      									  
      ParticleEta.push_back(genparticle->eta());      									  
      ParticlePhi.push_back(genparticle->phi());      									  
  															  
      ParticleCharge.push_back(genparticle->charge());									  
      ParticleStatus.push_back(genparticle->status());									  
      ParticleId.push_back(genparticle->pdgId());									  
  															  
      nParticle++;                                                                                                        

      if(genparticle->energy() > EHFcut_gen && genparticle->eta() > 3 && genparticle->eta() < 5) HFPlusSel_gen = true;
      if(genparticle->energy() > EHFcut_gen && genparticle->eta() > -5 && genparticle->eta() < -3) HFMinusSel_gen = true;
    
    } //-- end loop over gen particles
    
    if(HFPlusSel_gen && HFMinusSel_gen) HFAND_gen = true;
    if(HFPlusSel_gen || HFMinusSel_gen) HFOR_gen = true;
    if((HFPlusSel_gen && !HFMinusSel_gen) || (HFMinusSel_gen && !HFPlusSel_gen)) HFXOR_gen = true;
    
    if(nParticle > nParticlemax) nParticlemax = nParticle;
    
    if(debugParticle) {
      
      cout<<"n Particle = "<<nParticle<<endl<<endl;
      
      for(int ipart = 0; ipart < nParticle; ++ipart) {
	cout<<"Particle "<<ipart+1<<")"<<endl;
	cout<<"Particle Energy = "<<ParticleEnergy.at(ipart)<<endl;
	cout<<"Particle Pt = "<<ParticlePt.at(ipart)<<endl;
	cout<<"Particle Eta = "<<ParticleEta.at(ipart)<<endl;
	cout<<"Particle Phi = "<<ParticlePhi.at(ipart)<<endl<<endl;
	
	cout<<"Particle Charge = "<<ParticleCharge.at(ipart)<<endl;
	cout<<"Particle Status = "<<ParticleStatus.at(ipart)<<endl;
	cout<<"Particle Id = "<<ParticleId.at(ipart)<<endl<<endl;;
      }
      getchar();
    }
    
    //-- generated vertex 
    
    math::XYZPoint GVertex = (*genparticlecollection)[2].vertex();
    GenVx = GVertex.X();
    GenVy = GVertex.Y();
    GenVz = GVertex.Z();
    
    if(debugGenVertex) {
      cout<<"generated vertex x = "<<GenVx<<endl;
      cout<<"generated vertex y = "<<GenVy<<endl;
      cout<<"generated vertex z = "<<GenVz<<endl;
      getchar();
    }
  } //-- end monte carlo only

  //-- beamspot

  edm::Handle<reco::BeamSpot> BSpot;
  iEvent.getByLabel(beamspot_label,BSpot);

  BSx = BSpot.product()->position().x();    
  BSy = BSpot.product()->position().y();    
  BSz = BSpot.product()->position().z();    

  BSxError = BSpot.product()->x0Error();
  BSyError = BSpot.product()->y0Error();
  BSzError = BSpot.product()->z0Error();
  
  BSdxdz = BSpot.product()->dxdz();
  BSdydz = BSpot.product()->dydz();

  BSdxdzError = BSpot.product()->dxdzError();
  BSdydzError = BSpot.product()->dydzError();

  BSwidthX = BSpot.product()->BeamWidthX();
  BSwidthY = BSpot.product()->BeamWidthY();
  BSsigmaZ = BSpot.product()->sigmaZ();

  BSwidthXError = BSpot.product()->BeamWidthXError();
  BSwidthYError = BSpot.product()->BeamWidthYError();
  BSsigmaZError = BSpot.product()->sigmaZ0Error();

  //-- reco vertex
  
  nVertex = 0;
  
  Vx.clear();
  Vy.clear();
  Vz.clear();

  Vrho.clear();

  VxError.clear();
  VyError.clear();
  VzError.clear();
  
  Vchi2.clear();
  Vndof.clear();
  Vchi2ndof.clear();

  VisFake.clear();
  VisValid.clear();
  VisBest.clear();

  VnTrack.clear();
  VsumPt.clear();

  VTrackPt.clear();
  VTrackEta.clear();
  VTrackPhi.clear();

  VTrackPtError.clear(); 	
  VTrackEtaError.clear();  
  VTrackPhiError.clear();  
                 
  VTrackdxy.clear();    	
  VTrackdxyError.clear();	
  
  VTrackdz.clear();	
  VTrackdzError.clear();	
  
  VTrackCharge.clear();	
  
  VTrackchi2.clear();    	
  VTrackndof.clear();    	
  VTrackchi2ndof.clear();	
  
  VTrackValidHit.clear(); 	
  VTrackLostHit.clear();  	

  VTrackValidPixelHit.clear();
  VTrackValidStripHit.clear();  

  VTrackQuality.clear();      
  
  VTrackWeight.clear();

  edm::Handle<reco::VertexCollection> vertexcollection; 
  iEvent.getByLabel(recovertex_label,vertexcollection);

  nVertex = vertexcollection->size();
  if(nVertex > nVertexmax) nVertexmax = nVertex;

  reco::VertexCollection::const_iterator vertex;

  double sumPtmax = 0;
  int best_vertex = -1;
  int nTrack_all_vertex = 0;

  //-- begin loop over vertices
  for(vertex = vertexcollection->begin(); vertex != vertexcollection->end(); ++vertex) {
    
    Vx.push_back(vertex->x());
    Vy.push_back(vertex->y());
    Vz.push_back(vertex->z());
    
    Vrho.push_back(sqrt(vertex->x()*vertex->x() + vertex->y()*vertex->y()));

    VxError.push_back(vertex->xError());
    VyError.push_back(vertex->yError());
    VzError.push_back(vertex->zError());
    
    Vchi2.push_back(vertex->chi2());
    Vndof.push_back(vertex->ndof());
    if(vertex->ndof()!=0) Vchi2ndof.push_back(vertex->chi2()/vertex->ndof());
    else Vchi2ndof.push_back(0);

    VisFake.push_back(vertex->isFake());
    VisValid.push_back(vertex->isValid());

    //-- tracks associated to the vertices
    reco::Vertex::trackRef_iterator itrack; 
    std::vector<reco::TrackBaseRef>::const_iterator itrack_base;

    double sumPt = 0;
    int ntrack_vertex = 0;

    vector<double> temp_VTrackPt;
    vector<double> temp_VTrackEta;
    vector<double> temp_VTrackPhi;

    vector<double> temp_VTrackPtError; 	
    vector<double> temp_VTrackEtaError;  
    vector<double> temp_VTrackPhiError;  
    
    vector<double> temp_VTrackdxy;    	
    vector<double> temp_VTrackdxyError;	
    
    vector<double> temp_VTrackdz;	
    vector<double> temp_VTrackdzError;	
    
    vector<int> temp_VTrackCharge;	
    
    vector<double> temp_VTrackchi2;    	
    vector<double> temp_VTrackndof;    	
    vector<double> temp_VTrackchi2ndof;	
    
    vector<int> temp_VTrackValidHit; 	
    vector<int> temp_VTrackLostHit;  	
    
    vector<int> temp_VTrackValidPixelHit;
    vector<int> temp_VTrackValidStripHit;

    vector<int> temp_VTrackQuality;      

    vector<double> temp_VTrackWeight;
    
    for(itrack_base = vertex->tracks_begin(); itrack_base != vertex->tracks_end();++itrack_base) 
      temp_VTrackWeight.push_back(vertex->trackWeight(*itrack_base));

    //-- begin loop over tracks associated to the vertices
    for (itrack = vertex->tracks_begin(); itrack != vertex->tracks_end();++itrack) {
      sumPt+=(*itrack)->pt();
      ntrack_vertex++;

      temp_VTrackPt.push_back((*itrack)->pt());
      temp_VTrackEta.push_back((*itrack)->eta());
      temp_VTrackPhi.push_back((*itrack)->phi());

      temp_VTrackPtError.push_back((*itrack)->ptError());   
      temp_VTrackEtaError.push_back((*itrack)->etaError());  
      temp_VTrackPhiError.push_back((*itrack)->phiError());  
      
      temp_VTrackdxy.push_back((*itrack)->dxy(vertex->position()));       
      temp_VTrackdxyError.push_back((*itrack)->dxyError());  
      
      
      temp_VTrackdz.push_back((*itrack)->dz(vertex->position()));	   
      temp_VTrackdzError.push_back((*itrack)->dzError());   
      
      temp_VTrackCharge.push_back((*itrack)->charge());	   
      
      temp_VTrackchi2.push_back((*itrack)->chi2());      
      temp_VTrackndof.push_back((*itrack)->ndof());      
      if((*itrack)->ndof()!=0) temp_VTrackchi2ndof.push_back((*itrack)->chi2()/(*itrack)->ndof());  
      else temp_VTrackchi2ndof.push_back(0);

      temp_VTrackValidHit.push_back((*itrack)->numberOfValidHits()); 	   
      temp_VTrackLostHit.push_back((*itrack)->numberOfLostHits());  	   
      
      const reco::HitPattern & hp = (*itrack)->hitPattern();
      temp_VTrackValidPixelHit.push_back(hp.numberOfValidPixelHits());
      temp_VTrackValidStripHit.push_back(hp.numberOfValidStripHits());

      if((*itrack)->quality(reco::TrackBase::highPurity)) temp_VTrackQuality.push_back(2);
      else if((*itrack)->quality(reco::TrackBase::tight)) temp_VTrackQuality.push_back(1);
      else if((*itrack)->quality(reco::TrackBase::loose)) temp_VTrackQuality.push_back(0);     

    } //-- end loop over tracks associated to the vertices

    if(sumPt > sumPtmax) sumPtmax = sumPt;

    VnTrack.push_back(ntrack_vertex);
    VsumPt.push_back(sumPt);

    VTrackPt.push_back(temp_VTrackPt);
    VTrackEta.push_back(temp_VTrackEta);
    VTrackPhi.push_back(temp_VTrackPhi);

    VTrackPtError.push_back(temp_VTrackPtError);   
    VTrackEtaError.push_back(temp_VTrackEtaError); 
    VTrackPhiError.push_back(temp_VTrackPhiError); 
    		      		    
    VTrackdxy.push_back(temp_VTrackdxy);      
    VTrackdxyError.push_back(temp_VTrackdxyError); 
    		      		    
    VTrackdz.push_back(temp_VTrackdz);	    
    VTrackdzError.push_back(temp_VTrackdzError);  
                                                    
    VTrackCharge.push_back(temp_VTrackCharge);	      
                                		      
    VTrackchi2.push_back(temp_VTrackchi2);      
    VTrackndof.push_back(temp_VTrackndof);    
    VTrackchi2ndof.push_back(temp_VTrackchi2ndof);
                                                    
    VTrackValidHit.push_back(temp_VTrackValidHit);     
    VTrackLostHit.push_back(temp_VTrackLostHit);     
	
    VTrackValidPixelHit.push_back(temp_VTrackValidPixelHit);
    VTrackValidStripHit.push_back(temp_VTrackValidStripHit);
					      
    VTrackQuality.push_back(temp_VTrackQuality);       

    VTrackWeight.push_back(temp_VTrackWeight);

    nTrack_all_vertex+=ntrack_vertex;

  } //-- end loop over vertices

  for(unsigned int ivertex =0; ivertex < vertexcollection->size(); ++ivertex) {
    if(VsumPt.at(ivertex) == sumPtmax) {
      VisBest.push_back(true);
      best_vertex = ivertex;
    }
    else VisBest.push_back(false);
  }
  
  if(debugVertex && nVertex > 1) {    
    
    cout<<"N vertex = "<<nVertex<<endl<<endl;

    for(unsigned int ivertex =0; ivertex < vertexcollection->size(); ++ivertex) {
    
      cout<<"vertex "<<ivertex+1<<endl<<endl;

      cout<<"Vx = "<<Vx.at(ivertex)<<endl;
      cout<<"Vy = "<<Vy.at(ivertex)<<endl;
      cout<<"Vz = "<<Vz.at(ivertex)<<endl<<endl;

      cout<<"Vrho = "<<Vrho.at(ivertex)<<endl<<endl;

      cout<<"Vx error = "<<VxError.at(ivertex)<<endl;
      cout<<"Vy error = "<<VyError.at(ivertex)<<endl;      
      cout<<"Vz error = "<<VzError.at(ivertex)<<endl<<endl;
    
      cout<<"V chi2 = "<<Vchi2.at(ivertex)<<endl;
      cout<<"V ndof = "<<Vndof.at(ivertex)<<endl;
      cout<<"V chi2/ndof = "<<Vchi2ndof.at(ivertex)<<endl<<endl;

      cout<<"V ntracks = "<<VnTrack.at(ivertex)<<endl;
      cout<<"V sumPt = "<<VsumPt.at(ivertex)<<endl<<endl;

      cout<<"V is Fake = "<<VisFake.at(ivertex)<<endl;
      cout<<"V is Valid = "<<VisValid.at(ivertex)<<endl;
      cout<<"V is Best = "<<VisBest.at(ivertex)<<endl<<endl;

      for(unsigned int itrack = 0; itrack < VTrackPt.at(ivertex).size(); ++itrack) {
	cout<<"associated track "<<itrack+1<<")"<<endl;
	cout<<"Pt = "<<VTrackPt.at(ivertex).at(itrack)
	    <<", eta = "<<VTrackEta.at(ivertex).at(itrack)<<", phi = "<<VTrackPhi.at(ivertex).at(itrack)<<endl;
	cout<<"Pt error = "<<VTrackPtError.at(ivertex).at(itrack)<<", eta error = "<<VTrackEtaError.at(ivertex).at(itrack)
	    <<", phi error = "<<VTrackPhiError.at(ivertex).at(itrack)<<endl;
	cout<<"dxy = "<<VTrackdxy.at(ivertex).at(itrack)<<", dxy error = "<<VTrackdxyError.at(ivertex).at(itrack)<<endl;    		      
	cout<<"dz = "<<VTrackdz.at(ivertex).at(itrack)<<", dz error = "<<VTrackdzError.at(ivertex).at(itrack)<<endl;  	    
	cout<<"charge = "<<VTrackCharge.at(ivertex).at(itrack)<<endl;
	cout<<"chi2 = "<<VTrackchi2.at(ivertex).at(itrack)<<", ndof = "<<VTrackndof.at(ivertex).at(itrack)
	    <<", chi2/ndof = "<<VTrackchi2ndof.at(ivertex).at(itrack)<<endl;
	cout<<"valid hits = "<<VTrackValidHit.at(ivertex).at(itrack)<<", lost hits = "<<VTrackLostHit.at(ivertex).at(itrack)<<endl;
	cout<<"valid pixel hits = "<<VTrackValidPixelHit.at(ivertex).at(itrack)<<endl;
	cout<<"valid strip hits = "<<VTrackValidStripHit.at(ivertex).at(itrack)<<endl;
	cout<<"quality = "<<VTrackQuality.at(ivertex).at(itrack)<<endl;	
	cout<<"weight = "<<VTrackWeight.at(ivertex).at(itrack)<<endl<<endl;
      } //-- end track
      cout<<endl;
      getchar();
    } //-- end vertex
  } //-- end debug
  
  //-- pileup information
  
  nbxint = 0;
  nbxearly = 0;
  nbxlate = 0;
  nbxtot = 0;

  PUint = 0;
  PUearly = 0;
  PUlate = 0;
  PUtot = 0;

  NumInteraction = 0;    

  if(debugPU) cout<<endl;					 
  if(debugPU) cout<<" -- pile up information -- "<<endl<<endl;

  if(!IsData) {

    edm::Handle<std::vector<PileupSummaryInfo> > pucollection;
    iEvent.getByLabel(pu_label,pucollection);
  
    nbxtot = pucollection->size();
    
    std::vector<PileupSummaryInfo>::const_iterator pu;
    
    for(pu = pucollection->begin(); pu != pucollection->end(); ++pu) {

      int npu = pu->getPU_NumInteractions();
      
      if(pu->getBunchCrossing() < 0) {
	PUearly+=npu;
	nbxearly++;
      }

      if(pu->getBunchCrossing() > 0) {
	PUlate+=npu;
	nbxlate++;
      }

      if(pu->getBunchCrossing() == 0) {
        PUint+=npu;
	nbxint++;
        NumInteraction = pu->getTrueNumInteractions();
       }

      PUtot+=npu;

      if(!debugPU) continue;
      if(npu > 0 && pu->getBunchCrossing() == 0) cout<<"bx = "<<pu->getBunchCrossing()<<" has "<<npu<<" PU in time"<<endl;
      if(npu > 0 && pu->getBunchCrossing() < 0)  cout<<"bx = "<<pu->getBunchCrossing()<<" has "<<npu<<" PU early"<<endl;
      if(npu > 0 && pu->getBunchCrossing() > 0)  cout<<"bx = "<<pu->getBunchCrossing()<<" has "<<npu<<" PU late"<<endl;
      if(npu == 0) cout<<"bx = "<<pu->getBunchCrossing()<<" has no PU"<<endl;
    } //-- end loop over pileup

    PUint/=nbxint;
    PUearly/=nbxearly;
    PUlate/=nbxlate;
    PUtot/=nbxtot;

    if(debugPU) {
      cout<<endl;
      cout<<"number of bunch crossings = "<<nbxtot<<endl<<endl;
      cout<<"number of PU in time = "<<PUint<<endl;
      cout<<"number of PU early = "<<PUearly<<endl;
      cout<<"number of PU late = "<<PUlate<<endl;
      cout<<"total number of PU = "<<PUtot<<endl<<endl;
      cout<<"true number of interactions = "<<NumInteraction<<endl<<endl;
      getchar();
    }
  
  } //-- end pileup information

  //-- track
   
  nTrack = 0;

  TrackPt.clear();
  TrackEta.clear();
  TrackPhi.clear();

  TrackPtError.clear(); 
  TrackEtaError.clear();
  TrackPhiError.clear();

  Trackdxy.clear();    
  TrackdxyError.clear();
             
  Trackdz.clear();	   
  TrackdzError.clear(); 
 
  TrackCharge.clear();
  
  Trackchi2.clear();
  Trackndof.clear();
  Trackchi2ndof.clear();

  TrackValidHit.clear();
  TrackLostHit.clear();

  TrackQuality.clear();

  //-- track rechit

  TrackHitR.clear();     
  TrackHitTheta.clear(); 
  TrackHitPhi.clear();   
		       
  TrackHitEta.clear();   
		       
  TrackHitX.clear();     
  TrackHitY.clear();     
  TrackHitZ.clear();     
                       
  TrackHitDet.clear();   
  TrackHitSubdet.clear();

  Handle<reco::TrackCollection> trackcollection;
  iEvent.getByLabel(generaltrack_label,trackcollection);

  nTrack = trackcollection->size();
  if(nTrack > nTrackmax) nTrackmax = nTrack;

  reco::TrackCollection::const_iterator track;
  
  //--begin loop over tracks
  for(track = trackcollection->begin(); track != trackcollection->end(); ++track) {
    
    //-- track rechits 
    trackingRecHit_iterator ihit;  
    
    vector<double> HitR;	 
    vector<double> HitTheta;	 
    vector<double> HitPhi;	 
		    			 
    vector<double> HitEta;	 
		    			 
    vector<double> HitX;	 
    vector<double> HitY;	 
    vector<double> HitZ;       
    
    vector<int> HitDet;
    vector<int> HitSubdet;

    //-- begin loop over rechits associated to the tracks
    for(ihit = track->recHitsBegin(); ihit != track->recHitsEnd();++ihit) {
      
      if(!(*ihit)->isValid()) continue;
      
      DetId hitId = (*ihit)->geographicalId();
      
      LocalPoint hitLocalPosition = (*ihit)->localPosition();
      GlobalPoint hitGlobalPosition = (*ihit)->globalPosition();
      
      //-- cout<<"hit local position = "<<hitLocalPosition<<" - hit global position = "<<hitGlobalPosition<<endl;
      //-- getchar();
      
      HitR.push_back(hitGlobalPosition.perp());
      HitTheta.push_back(hitGlobalPosition.theta());
      HitPhi.push_back(hitGlobalPosition.phi());
      
      HitEta.push_back(hitGlobalPosition.eta());
      
      HitX.push_back(hitGlobalPosition.x());
      HitY.push_back(hitGlobalPosition.y());
      HitZ.push_back(hitGlobalPosition.z());
      
      if(!(hitId.det() == DetId::Tracker)) continue;
      
      //-- PXB = 1 - PXF = 2 - TIB = 3 - TID = 4 - TOB = 5 - TEC = 6
      HitDet.push_back(hitId.subdetId()); 
      
      if(hitId.subdetId() == (int) PixelSubdetector::PixelBarrel)  
	//--  cout<<"hit subdetector = PXB = "<<hitId.subdetId()<<" - layer = "<<PXBDetId(hitId).layer()<<endl;  
	HitSubdet.push_back(PXBDetId(hitId).layer());
      
      
      else if(hitId.subdetId() == (int) PixelSubdetector::PixelEndcap) 
	//--  cout<<"hit subdetector = PXF = "<<hitId.subdetId()<<" - disk = "<<PXFDetId(hitId).disk()<<endl;   
	HitSubdet.push_back(PXFDetId(hitId).disk());
      
      else if(hitId.subdetId() == StripSubdetector::TIB) 
	//--  cout<<"hit subdetector = TIB = "<<hitId.subdetId()<<" - layer = "<<TIBDetId(hitId).layer()<<endl;
	HitSubdet.push_back(TIBDetId(hitId).layer());
      
      else if(hitId.subdetId() == StripSubdetector::TID) 				       
	//--  cout<<"hit subdetector = TID = "<<hitId.subdetId()<<" - wheel = "<<TIDDetId(hitId).wheel()<<endl;  
	HitSubdet.push_back(TIDDetId(hitId).wheel());
      
      else if(hitId.subdetId() == StripSubdetector::TOB) 
	//--  cout<<"hit subdetector = TOB = "<<hitId.subdetId()<<" - layer = "<<TOBDetId(hitId).layer()<<endl;
	HitSubdet.push_back(TOBDetId(hitId).layer());
      
      else if(hitId.subdetId() == StripSubdetector::TEC) 
	//--  cout<<"hit subdetector = TEC = "<<hitId.subdetId()<<" - wheel = "<<TECDetId(hitId).wheel()<<endl;
	HitSubdet.push_back(TECDetId(hitId).wheel());
      
    } //-- end loop over rechits associated to the tracks
      
    TrackPt.push_back(track->pt());
    TrackEta.push_back(track->eta());
    TrackPhi.push_back(track->phi());
    
    TrackPtError.push_back(track->ptError());  
    TrackEtaError.push_back(track->etaError());
    TrackPhiError.push_back(track->phiError());
    
    if(best_vertex < 0) Trackdxy.push_back(track->dxy(BSpot.product()->position()));   
    else Trackdxy.push_back(track->dxy(vertexcollection->at(best_vertex).position()));
    TrackdxyError.push_back(track->dxyError());
    
    if(best_vertex < 0) Trackdz.push_back(track->dz(BSpot.product()->position()));	
    else Trackdz.push_back(track->dz(vertexcollection->at(best_vertex).position()));	
    TrackdzError.push_back(track->dzError());
    
    TrackCharge.push_back(track->charge());
    
    Trackchi2.push_back(track->chi2());
    Trackndof.push_back(track->ndof());
    if(track->ndof()!=0) Trackchi2ndof.push_back(track->chi2()/track->ndof());
    else Trackchi2ndof.push_back(0);
    
    TrackValidHit.push_back(track->numberOfValidHits());
    TrackLostHit.push_back(track->numberOfLostHits());
    
    if(track->quality(reco::TrackBase::highPurity)) TrackQuality.push_back(2);         
    else if(track->quality(reco::TrackBase::tight)) TrackQuality.push_back(1);     
    else if(track->quality(reco::TrackBase::loose)) TrackQuality.push_back(0);     

    TrackHitR.push_back(HitR);	   
    TrackHitTheta.push_back(HitTheta);   
    TrackHitPhi.push_back(HitPhi);       
    
    TrackHitEta.push_back(HitEta);     
    
    TrackHitX.push_back(HitX);	      
    TrackHitY.push_back(HitY);	      
    TrackHitZ.push_back(HitZ);          
    
    TrackHitDet.push_back(HitDet);
    TrackHitSubdet.push_back(HitSubdet);

  } //-- end loop over tracks

  if(debugVertex && nVertex > 1) {
    cout<<endl<<"N track from all vertices = "<<nTrack_all_vertex<<endl;
    cout<<"N track from general track collection = "<<nTrack<<endl<<endl;
    getchar();
  }

  if(debugTrackHit) {
  
    cout<<endl;
    cout<<"track rechit information"<<endl;
    cout<<endl;

    cout<<"N vertex = "<<nVertex<<endl;
    cout<<"N track = "<<nTrack<<endl<<endl;

    //-- loop over tracks
    for(int itrack = 0; itrack < nTrack; ++itrack) {

      getchar();
      cout<<"-- track "<<itrack+1<<" --"<<endl;
      cout<<"N hits associated to the track = "<<TrackHitR.at(itrack).size()<<endl<<endl;
      getchar();

      //-- loop over rechits 
      for(unsigned int irec = 0; irec < TrackHitR.at(itrack).size(); ++irec) {
	cout<<"-- hit "<<irec+1<<" --"<<endl;
	cout<<"hit R = "<<TrackHitR.at(itrack).at(irec)<<endl;
	cout<<"hit theta = "<<TrackHitTheta.at(itrack).at(irec)<<endl;
	cout<<"hit phi = "<<TrackHitPhi.at(itrack).at(irec)<<endl;

	  cout<<"hit eta = "<<TrackHitEta.at(itrack).at(irec)<<endl;
 			     			   
	  cout<<"hit x = "<<TrackHitX.at(itrack).at(irec)<<endl;
	  cout<<"hit y = "<<TrackHitY.at(itrack).at(irec)<<endl;
	  cout<<"hit z = "<<TrackHitZ.at(itrack).at(irec)<<endl;

	  cout<<"hit detector = "<<TrackHitDet.at(itrack).at(irec)<<endl;
	  cout<<"hit subdetector = "<<TrackHitSubdet.at(itrack).at(irec)<<endl<<endl;
      } //-- end loop over rechits
    } //-- end loop over tracks
  }
  
  if(debugTrack) {
    
    cout<<"n Tracks = "<<nTrack<<endl<<endl;

    for(unsigned int itrack = 0; itrack < trackcollection->size(); ++itrack) {

      cout<<"track number = "<<itrack+1<<endl<<endl;

      cout<<"Track Pt = "<<TrackPt.at(itrack)<<endl;
      cout<<"Track Eta = "<<TrackEta.at(itrack)<<endl;
      cout<<"Track Phi = "<<TrackPhi.at(itrack)<<endl<<endl;
    
      cout<<"Track Pt error = "<<TrackPtError.at(itrack)<<endl;
      cout<<"Track Eta error = "<<TrackEtaError.at(itrack)<<endl;
      cout<<"Track Phi error = "<<TrackPhiError.at(itrack)<<endl<<endl;

      cout<<"best vertex index = "<<best_vertex<<endl<<endl;

      cout<<"Track dxy = "<<Trackdxy.at(itrack)<<endl;
      cout<<"Track dxy error = "<<TrackdxyError.at(itrack)<<endl<<endl;
           		
      cout<<"Track dz = "<<Trackdz.at(itrack)<<endl;
      cout<<"Track dz error = "<<TrackdzError.at(itrack)<<endl<<endl;
      
      cout<<"Track Charge = "<<TrackCharge.at(itrack)<<endl<<endl;

      cout<<"Track Chi2 = "<<Trackchi2.at(itrack)<<endl;
      cout<<"Track ndof = "<<Trackndof.at(itrack)<<endl;
      cout<<"Track Chi2/ndof = "<<Trackchi2ndof.at(itrack)<<endl<<endl;
	
      cout<<"Track number of valid hits = "<<TrackValidHit.at(itrack)<<endl;
      cout<<"Track number of lost hits = "<<TrackLostHit.at(itrack)<<endl;

      cout<<"Track quality = "<<TrackQuality.at(itrack)<<endl<<endl;
      getchar();
    }
  }          

  if(IsData) {
    //-- L1 Trigger
    
    L1TTdecision.clear();
    
    edm::Handle<L1GlobalTriggerReadoutRecord> gtReadoutRecord;
    iEvent.getByLabel(L1GT_label,gtReadoutRecord);
    
    const TechnicalTriggerWord& technicalTriggerWordBeforeMaskBx0 = gtReadoutRecord->technicalTriggerWord();
    
    for(unsigned int i = 0; i < L1TTbit.size(); ++i){
      int ibit = L1TTbit.at(i);
      L1TTdecision.push_back(technicalTriggerWordBeforeMaskBx0.at(ibit));
    }
    
    if(debugL1TT) {
      for(unsigned int i = 0; i < L1TTbit.size(); ++i) {
	cout<<"element "<<i<<" contains Technical Trigger "<<L1TTname.at(i)<<" with bit number "<<L1TTbit.at(i)
	    <<" and decision "<<L1TTdecision.at(i)<<endl;
      }
      getchar();
    }
  
    //-- HLT Trigger
    
    HLTprescale.clear();
    L1prescale.clear();
    HLTdecision.clear();
    
    edm::Handle<edm::TriggerResults> TrigResult;
    iEvent.getByLabel(HLT_label,TrigResult);
    
    const edm::TriggerNames& TrigName = iEvent.triggerNames(*TrigResult);
    
    for(unsigned int itrig =0; itrig < HLTindex.size(); ++itrig) {
      bool accept = TrigResult->accept(HLTindex.at(itrig));
      HLTdecision.push_back(accept);
      
      //const std::pair<int,int> prescales(HLTconfig.prescaleValues(iEvent,iSetup,HLTname.at(itrig)));
      //L1prescale.push_back(prescales.first);
      //HLTprescale.push_back(prescales.second);      
      L1prescale.push_back(1);
      HLTprescale.push_back(1);
      //HLTprescale.push_back(HLTconfig.prescaleValue(iEvent,iSetup,HLTname.at(itrig)));
    }
    
    if(debugHLT) {
      for(unsigned int itrig =0; itrig < HLTindex.size(); ++itrig) {
	cout<<"HLT name = "<<HLTname.at(itrig)<<endl;
	cout<<"HLT index = "<<HLTindex.at(itrig)<<endl;
	cout<<"HLT prescale = "<<HLTprescale.at(itrig)<<endl;
	cout<<"L1 prescale = "<<L1prescale.at(itrig)<<endl;      
	cout<<"HLT decision = "<<HLTdecision.at(itrig)<<endl;
      }
    }
  } //-- end data only
  
  //-- fill tree
  Nwritten++;
  if(Nwritten%10000 == 0) cout<<"Number of events written in the tree: "<<Nwritten<<endl;
  tTrack->Fill();
}


//-- method called once each job just before starting event loop
void TrackTree::beginJob() {
  using namespace std;

  nTrackmax = 0;
  nParticlemax = 0;
  nHFTowermax = 0;
  nHFRechitmax = 0;
  nVertexmax = 0;

  //-- data type				    
  cout<<"you are going to run on "<<DataType<<endl<<endl;                          
}

//--- method called once each job just after ending the event loop
void TrackTree::endJob() {
  using namespace std;
  
  cout<<"n track max = "<<nTrackmax<<endl;
  cout<<"n particle max = "<<nParticlemax<<endl;
  cout<<"n HF tower max = "<<nHFTowermax<<endl;
  cout<<"n HF rechit max = "<<nHFRechitmax<<endl;
  cout<<"n vertex max = "<<nVertexmax<<endl;
  cout<<"Number of events written in the tree: "<<Nwritten<<endl;
}

//-- method called when starting to process a run
void  TrackTree::beginRun(const edm::Run& iRun, const edm::EventSetup& iSetup) {
  using namespace std;

  iSetup.get<TrackerDigiGeometryRecord>().get(trackerGeom);
  iSetup.get<HcalDbRecord>().get(hcalConditions);
  iSetup.get<CaloGeometryRecord>().get(caloGeom);
  //iSetup.get<TransientRecHitRecord>().get(TTRHbuilder_label,handleTTRHbuilder);

  if(IsData) {
    //-- Retrieve L1 Trigger menu 
    
    edm::ESHandle< L1GtTriggerMenu > menuRcd;                                                                                           
    iSetup.get< L1GtTriggerMenuRcd >().get(menuRcd);     
    
    const L1GtTriggerMenu* menu = menuRcd.product();
    
    const AlgorithmMap L1TechTrigger(menu->gtTechnicalTriggerMap());
    AlgorithmMap::const_iterator l1tech; //-- typedef std::map<std::string, L1GtAlgorithm> AlgorithmMap;                                         
    
    L1TTname.clear();
    L1TTbit.clear();
    
    for(l1tech = L1TechTrigger.begin(); l1tech != L1TechTrigger.end(); ++l1tech) {	
      cout<<"L1 Technical Trigger "<<(l1tech->second).algoName()<<" is present with bit number "<<(l1tech->second).algoBitNumber()<<endl;
      
      for(unsigned int itrig =0; itrig < L1TT_requested.size(); ++itrig) {
	if((l1tech->second).algoName() == L1TT_requested.at(itrig)) {
	  L1TTname.push_back((l1tech->second).algoName());
	  L1TTbit.push_back((l1tech->second).algoBitNumber());
	}
      }
    }
    
    cout<<endl;
    
    for(unsigned int i = 0; i < L1TTbit.size(); ++i) {
      cout<<"element "<<i<<" contains Technical Trigger "<<L1TTname.at(i)<<" with bit number "<<L1TTbit.at(i)<<endl;
    }
    
    cout<<endl;
    
    //-- HLT Trigger
    
    bool changed = true;
    bool validHLTconfig = false;
    
    validHLTconfig = HLTconfig.init(iRun,iSetup,process_label,changed);
    
    //-- valid HLT configuration
    if(validHLTconfig) {
      
      cout<<"HLT configuration with process name "<<process_label<<" is valid"<<endl;
      
      if(debugHLT) {
	cout << "HLT triggers present in the menu: " << endl;
	HLTconfig.dump("Triggers");
      }
      
      //-- new menu
      if(changed) {
	
	cout<<endl<<"New trigger menu found"<<endl;
	
	HLTname.clear();
	HLTindex.clear();
	
	const unsigned int nHLT(HLTconfig.size());
	
	for(unsigned itrig=0; itrig < HLT_requested.size(); ++itrig) {
	  
	  unsigned int index = HLTconfig.triggerIndex(HLT_requested[itrig]); 
	  
	  cout<<HLT_requested.at(itrig)<<" with index "<<index<<" ";  
	  
	  if(index < nHLT) {
	    cout<<"exists in the current menu"<<endl;
	    HLTname.push_back(HLT_requested.at(itrig));
	    HLTindex.push_back(index);
	  }
	  
	  else	  
	    cout<<"does not exist in the current menu"<<endl;
	}
	cout<<endl;
      } //-- end new menu
      
      //-- same menu
      if(!changed) cout<<"Trigger menu is unchanged"<<endl;
      
    } //-- end valid HLT configuration
    
    //-- no valid HLT configuration
    if(!validHLTconfig) 
      cout<<"HLT configuration with process name "<<process_label<<" is NOT valid"<<endl;
  } //-- end data only
}


//-- method called when ending the processing of a run 
/* void TrackTree::endRun(edm::Run const&, edm::EventSetup const&) {
}
*/

//-- method called when starting to processes a luminosity block
/* void TrackTree::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) {
}
*/

//-- method called when ending the processing of a luminosity block
/* void TrackTree::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) {
}
*/

//-- method fills 'descriptions' with the allowed parameters for the module 
void TrackTree::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TrackTree);
