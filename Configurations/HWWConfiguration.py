Job = {
    "Batch"           : True,
    "Analysis"        : "HWWAnalysis",
    "Fraction"        : 1.0,  # set to 1.0 to analyze the full statistics
    "MaxEvents"       : 1234567890,
    "OutputDirectory" : "resultsHWW/"    # by changing this, you can keep multiple versions of the output
                                         # (for instance the 1% sample and the 100% sample)
}

prefix = "/Volumes/JMCR_SSD/ATLAS_OpenData_Samples/2lep/" # replace with local data directory

Processes = {

    # Higgs
    "ggH125_WW2lep"             : prefix+"MC/mc_345324.ggH125_WW2lep.2lep.root",
    "VBFH125_WW2lep"            : prefix+"MC/mc_345323.VBFH125_WW2lep.2lep.root",
    
    # single top
    "single_top_schan"      : prefix+"MC/mc_410025.single_top_schan.2lep.root",
    "single_antitop_schan"  : prefix+"MC/mc_410026.single_antitop_schan.2lep.root",
    "single_top_wtchan"     : prefix+"MC/mc_410013.single_top_wtchan.2lep.root",
    "single_antitop_wtchan" : prefix+"MC/mc_410014.single_antitop_wtchan.2lep.root",
    "single_top_tchan"      : prefix+"MC/mc_410011.single_top_tchan.2lep.root",
    "single_antitop_tchan"  : prefix+"MC/mc_410012.single_antitop_tchan.2lep.root",
    
    # Z + jets processes
    "Zee"                   : prefix+"MC/mc_361106.Zee.2lep.root",
    "Zmumu"                 : prefix+"MC/mc_361107.Zmumu.2lep.root",
    "Ztautau"               : prefix+"MC/mc_361108.Ztautau.2lep.root",

    # Diboson processes
    "ZqqZll"                : prefix+"MC/mc_363356.ZqqZll.2lep.root",
    "WqqZll"                : prefix+"MC/mc_363358.WqqZll.2lep.root",
    "WpqqWmlv"              : prefix+"MC/mc_363359.WpqqWmlv.2lep.root",
    "WplvWmqq"              : prefix+"MC/mc_363360.WplvWmqq.2lep.root",
    "WlvZqq"                : prefix+"MC/mc_363489.WlvZqq.2lep.root",
    "llll"                  : prefix+"MC/mc_363490.llll.2lep.root",
    "lllv"                  : prefix+"MC/mc_363491.lllv.2lep.root",
    "llvv"                  : prefix+"MC/mc_363492.llvv.2lep.root",
    "lvvv"                  : prefix+"MC/mc_363493.lvvv.2lep.root",
    
    # top pair processes
    "ttbar_lep"             : prefix+"MC/mc_410000.ttbar_lep.2lep.root",

    # W + jets
    "Wplusenu"              : prefix + "MC/mc_361100.Wplusenu.2lep.root",
    "Wplusmunu"             : prefix + "MC/mc_361101.Wplusmunu.2lep.root",
    "Wplustaunu"            : prefix + "MC/mc_361102.Wplustaunu.2lep.root",
    "Wminusenu"              : prefix + "MC/mc_361103.Wminusenu.2lep.root",
    "Wminusmunu"             : prefix + "MC/mc_361104.Wminusmunu.2lep.root",
    "Wminustaunu"            : prefix + "MC/mc_361105.Wminustaunu.2lep.root",
    
    # Data
    "data_A"                : prefix+"Data/data_A.2lep.root",
    "data_B"                : prefix+"Data/data_B.2lep.root",
    "data_C"                : prefix+"Data/data_C.2lep.root",
    "data_D"                : prefix+"Data/data_D.2lep.root",

}
