import ROOT
import itertools 
import math

#from Analysis import Analysis
import Analysis
#from Analysis import AnalysisHelpers
import AnalysisHelpers
#from Analysis import Constants
import Constants

#======================================================================
        
class HWWAnalysis(Analysis.Analysis):
  """Analysis searching for the pair production of two W bosons decaying to different flavor, opposite sign leptons."""
  def __init__(self, store):
      super(HWWAnalysis, self).__init__(store)

  
  def initialize(self):
      self.deltaPhi_ll         =  self.addHistogram("deltaPhi_ll",           ROOT.TH1D("deltaPhi_ll",     "Azimuthal angle between leptons;#Delta#phi (ll); Events", 20, 0, 3.2))
      self.pt_ll         =  self.addHistogram("pt_ll",           ROOT.TH1D("pt_ll",     "Dilepton transverse momentum;p_{T} [GeV]; Events", 30, 0,200))

      self.mass_WW         =  self.addHistogram("mass_WW",           ROOT.TH1D("mass_WW",     "Transverse Mass of the WW system;M_{T} [GeV]; Events",15,50,200))

      self.hist_leptn        =  self.addStandardHistogram("lep_n")
      self.hist_leptpt       =  self.addStandardHistogram("lep_pt")
      self.hist_lepteta      =  self.addStandardHistogram("lep_eta")
      self.hist_leptE        =  self.addStandardHistogram("lep_E")
      self.hist_leptphi      =  self.addStandardHistogram("lep_phi")
      self.hist_leptch       =  self.addStandardHistogram("lep_charge")
      self.hist_leptID       =  self.addStandardHistogram("lep_type")
      self.hist_leptptc      =  self.addStandardHistogram("lep_ptconerel30")
      self.hist_leptetc      =  self.addStandardHistogram("lep_etconerel20")
      self.hist_lepz0        =  self.addStandardHistogram("lep_z0")
      self.hist_lepd0        =  self.addStandardHistogram("lep_d0")
      self.hist_etmiss       =  self.addStandardHistogram("etmiss")

    
  def analyze(self):
      # retrieving objects
      eventinfo = self.Store.getEventInfo()
      if not (eventinfo.triggeredByElectron() or eventinfo.triggeredByMuon()) : return False
      
      weight = eventinfo.scalefactorHWW()*eventinfo.eventWeight() if not self.getIsData() else 1
      self.countEvent("lepton trigger", weight)
      
      # check missing Et
      self.etmiss = self.Store.getEtMiss()
      # The ATLAS note says this cut is 30 GeV
      # But the c++ example code uses 20 GeV
      if not self.etmiss.et() > 20: return False
      self.countEvent("EtMiss > 20 GeV", weight)
      
      # retrieve Leptons  
      goodLeptons = AnalysisHelpers.selectAndSortContainer(self.Store.getLeptons(), isGoodLepton, lambda p: p.pt())
      if not len(goodLeptons) == 2: return False
      self.countEvent("2 isolated leptons", weight)

      if not goodLeptons[0].pt() > 22: return False
      self.countEvent("Lead lep_pt > 22 GeV", weight)
      
      if not goodLeptons[1].pt() > 15: return False
      self.countEvent("2nd lep_pt > 15 GeV", weight)

      # find WW Candidate
      if not self.WWCandidate(goodLeptons): return False
      self.countEvent("DFOS leptons", weight)
      self.dilep = goodLeptons[0].tlv() + goodLeptons[1].tlv()
 
      # EtMiss/dilep azimuth difference
      self.deltaPhi_et_ll = self.DeltaPhi(self.etmiss.tlv(), self.dilep)
      if not self.deltaPhi_et_ll > math.pi / 2 : return False
      self.countEvent("delta(phi) > pi/2", weight)
      
      # Dilepton pt
      self.dilep.pt = self.dilep.Pt()
      if not self.dilep.pt > 30 : return False
      self.countEvent("Dilepton pt > 30 GeV", weight)
      
      # Dilepton mass
      self.dilep.mass = self.dilep.M()
      if not self.dilep.mass > 10 or not self.dilep.mass < 55: return False
      self.countEvent("10 < m(ll) < 55 GeV", weight)
      
      # Dilepton phi difference
      self.deltaPhi_l_l = self.DeltaPhi(goodLeptons[0].tlv(), goodLeptons[1].tlv())
      if not self.deltaPhi_l_l < 1.8: return False
      self.countEvent("delta(phi_ll) < 1.8", weight)
 
      # retrieve jets
      goodJets =AnalysisHelpers.selectAndSortContainer(self.Store.getJets(), isGoodJet, lambda p: p.pt())
      if not len(goodJets) < 2 : return False
      self.countEvent("At most 1 good jet", weight)
      
      # retrieve B jets
      goodBJets =AnalysisHelpers.selectAndSortContainer(self.Store.getJets(), isGoodBJet, lambda p: p.pt())
      if not len(goodBJets) == 0 : return False
      self.countEvent("No good B jets", weight)
      
      # fill deltaphi(ll), pt(ll), mt(WW) histograms
      self.deltaPhi_ll.Fill(self.deltaPhi_l_l, weight)
      self.pt_ll.Fill(self.dilep.pt, weight)
      self.mass_WW.Fill(TransverseMass(self.dilep, self.etmiss), weight)

      # lepton histograms
      self.hist_leptn.Fill(len(goodLeptons), weight)
      [self.hist_leptpt.Fill(lep.pt(), weight) for lep in goodLeptons]
      [self.hist_lepteta.Fill(lep.eta(), weight) for lep in goodLeptons]
      [self.hist_leptE.Fill(lep.e(), weight) for lep in goodLeptons]
      [self.hist_leptphi.Fill(lep.phi(), weight) for lep in goodLeptons]
      [self.hist_leptch.Fill(lep.charge(), weight) for lep in goodLeptons]
      [self.hist_leptID.Fill(lep.pdgId(), weight) for lep in goodLeptons]
      [self.hist_leptptc.Fill(lep.isoptconerel30(), weight) for lep in goodLeptons]
      [self.hist_leptetc.Fill(lep.isoetconerel20(), weight) for lep in goodLeptons]
      [self.hist_lepz0.Fill(lep.z0(), weight) for lep in goodLeptons]
      [self.hist_lepd0.Fill(lep.d0(), weight) for lep in goodLeptons]
      
      # EtMiss histogram
      self.hist_etmiss.Fill(self.etmiss.et(), weight)
      
      return True
  
  def finalize(self):
      pass
    
  def DeltaPhi(self, tlv1, tlv2):
       return tlv1.DeltaPhi(tlv2)
       
  def WWCandidate(self, leptons):
          if leptons[0].charge()*leptons[1].charge() > 0: return False
          if abs(leptons[0].pdgId()) == abs(leptons[1].pdgId()): return False
          return True
    
def TransverseMass(tlv, met):
    return math.sqrt(2*tlv.Pt()*met.et()*(1-math.cos(tlv.DeltaPhi(met.tlv()))));
 
def isGoodLepton(Lepton):
    if not Lepton.isTightID() : return False
    if not Lepton.isoetconerel20() < 0.1: return False
    if not Lepton.isoptconerel30() < 0.1: return False
    return True;

def isGoodJet(Jet):
    if not Jet.pt() > 30 : return False
    if not abs(Jet.eta()) < 2.5 : return False
    if Jet.pt() < 60 and abs(Jet.eta()) < 2.4 and Jet.jvt() < 0.59 : return False
    return True

def isGoodBJet(Jet):
    if not Jet.pt() > 20 : return False
    if not abs(Jet.eta()) < 2.5 : return False
    if Jet.pt() < 60 and abs(Jet.eta()) < 2.4 and Jet.jvt() < 0.59 : return False
    if not Jet.mv2c10() > 0.1758475 : return False
    return True
