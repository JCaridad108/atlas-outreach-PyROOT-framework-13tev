Job = {
    "Batch"           : True,
    "Analysis"        : "ZZDibosonAnalysis",
    "Fraction"        : 1.0,  # set to 1.0 to analyze the full statistics
    "MaxEvents"       : 1234567890,
    "OutputDirectory" : "resultsZZDiboson/"    # by changing this, you can keep multiple versions of the output
                                         # (for instance the 1% sample and the 100% sample)
}

prefix2 = "/Volumes/JMCR_SSD/ATLAS_OpenData_Samples/2lep/" # replace with local data directory
prefix4 = "Input/4lep/" # replace with local data directory

Processes = {

    # H -> ZZ -> 4lep processes
    #"ZH125_ZZ4lep"          : prefix+"MC/mc_341947.ZH125_ZZ4lep.4lep.root",
    #"WH125_ZZ4lep"          : prefix+"MC/mc_341964.WH125_ZZ4lep.4lep.root",
    #"VBFH125_ZZ4lep"        : prefix+"MC/mc_344235.VBFH125_ZZ4lep.4lep.root",
    #"ggH125_ZZ4lep"         : prefix+"MC/mc_345060.ggH125_ZZ4lep.4lep.root",

    # Z + jets processes
    "Zee"                   : prefix4+"MC/mc_361106.Zee.4lep.root",
    "Zmumu"                 : prefix4+"MC/mc_361107.Zmumu.4lep.root",
    "Ztautau"               : prefix4+"MC/mc_361108.Ztautau.4lep.root",

    # Diboson processes
    "ZqqZll"                : prefix4+"MC/mc_363356.ZqqZll.4lep.root",
    "WqqZll"                : prefix2+"MC/mc_363358.WqqZll.2lep.root",
    "WpqqWmlv"              : prefix2+"MC/mc_363359.WpqqWmlv.2lep.root",
    "WplvWmqq"              : prefix2+"MC/mc_363360.WplvWmqq.2lep.root",
    "WlvZqq"                : prefix2+"MC/mc_363489.WlvZqq.2lep.root",
    "llll"                  : prefix4+"MC/mc_363490.llll.4lep.root",
    "lllv"                  : prefix4+"MC/mc_363491.lllv.4lep.root",
    "llvv"                  : prefix4+"MC/mc_363492.llvv.4lep.root",
    "lvvv"                  : prefix2+"MC/mc_363493.lvvv.2lep.root",

    # single top
    "single_top_tchan"      : prefix4+"MC/mc_410011.single_top_tchan.4lep.root",
    "single_antitop_tchan"  : prefix4+"MC/mc_410012.single_antitop_tchan.4lep.root",
    "single_top_wtchan"     : prefix4+"MC/mc_410013.single_top_wtchan.4lep.root",
    "single_antitop_wtchan" : prefix4+"MC/mc_410014.single_antitop_wtchan.4lep.root",
    "single_top_schan"      : prefix4+"MC/mc_410025.single_top_schan.4lep.root",
    "single_antitop_schan"  : prefix4+"MC/mc_410026.single_antitop_schan.4lep.root",
    
    # top pair processes
    "ttbar_lep"             : prefix4+"MC/mc_410000.ttbar_lep.4lep.root",

    # W+jets inclusive
    "Wplusenu"              : prefix2+"MC/mc_361100.Wplusenu.2lep.root",
    "Wplusmunu"             : prefix2+"MC/mc_361101.Wplusmunu.2lep.root",
    "Wplustaunu"            : prefix2+"MC/mc_361102.Wplustaunu.2lep.root",
    "Wminusenu"             : prefix2+"MC/mc_361103.Wminusenu.2lep.root",
    "Wminusmunu"            : prefix2+"MC/mc_361104.Wminusmunu.2lep.root",
    "Wminustaunu"           : prefix2+"MC/mc_361105.Wminustaunu.2lep.root",
    
    # Data
    "data_A"                : prefix4+"Data/data_A.4lep.root",
    "data_B"                : prefix4+"Data/data_B.4lep.root",
    "data_C"                : prefix4+"Data/data_C.4lep.root",
    "data_D"                : prefix4+"Data/data_D.4lep.root",

}
