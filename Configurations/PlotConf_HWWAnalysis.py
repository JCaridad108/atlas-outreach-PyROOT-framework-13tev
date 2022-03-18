config = {
#"Luminosity": 547, #period A
#"Luminosity": 1949, #period B
#"Luminosity": 2884, #period C
#"Luminosity": 4684, #period D
"Luminosity": 10064, #period A-D
"InputDirectory": "resultsHWW",

"Histograms" : {
    "deltaPhi_ll"     : {"y_margin": 0.7, "rebin" : 1},
    "pt_ll"           : {"y_margin": 0.5, "rebin" : 1},
    "mass_WW"         : {"y_margin": 1.5, "rebin" : 1},
    "lep_n"           : {"y_margin" : 0.4},
    "lep_pt"          : {"y_margin" : 0.4, "rebin" : 2},
    "lep_eta"         : {"y_margin" : 0.5, "rebin" : 3},
    "lep_E"           : {"rebin" : 3},
    "lep_phi"         : {"y_margin" : 0.6, "rebin" : 4,},
    "lep_charge"      : {"y_margin" : 0.6},
    "lep_type"        : {"y_margin" : 0.5,},
    "lep_ptconerel30" : {"y_margin" : 0.3, "rebin" : 4},
    "lep_etconerel20" : {"y_margin" : 0.3, "rebin" : 4},
	"lep_z0"		  : {"y_margin" : 0.4, "rebin" : 2},
	"lep_d0"		  : {"y_margin" : 0.4, "rebin" : 2},
	"etmiss"		  : {"y_margin" : 0.4, "rebin" : 1},

},

"Paintables": {
    "Stack": {
        #"Order": ["Higgs", "Diboson", "Z/W+jets", "t\\bar{t}", "Single top"],
		"Order": ["Single top", "t\\bar{t}", "Z/W+jets", "Diboson", "Higgs"],
        "Processes" : {  
			  
            "Higgs" : {
                "Color"         : "#ffcd00",#"#00cdff",
                "Contributions" : ["ggH125_WW2lep","VBFH125_WW2lep"]
				},
			"Diboson" : {
				"Color"			: "#6b59d3",
				"Contributions"	: ["ZqqZll","WqqZll","WpqqWmlv","WplvWmqq","WlvZqq","llll","lllv",
									"llvv","lvvv"]
				},
			"Z/W+jets" : {
				"Color"			: "#00cdff",
				"Contributions"	: ["Zee","Zmumu","Ztautau",
									"Wplusenu","Wplusmunu","Wplustaunu","Wminusenu","Wminusmunu","Wminustaunu"]
				},
			"t\\bar{t}"	: {
				"Color"			: "#c0c0c0",
				"Contributions"	: ["ttbar_lep"]
				},
			"Single top" : {
				"Color"			: "#123456",
				"Contributions" : ["single_top_schan", "single_antitop_schan", "single_top_wtchan",
									"single_antitop_wtchan", "single_top_tchan", "single_antitop_tchan"]
				},
            #"Other": {       
            #    "Color"         : "#6b59d3",
            #    "Contributions" : ["Zee", "Zmumu"
            #                       #, "WqqZll", "lllv"
            #                       #, "ttbar_lep"]},
			#					   ]},

        }
    },

    "data" : {
        "Contributions": ["data_A", "data_C", "data_D"]}
},

"Depictions": {
    "Order": ["Main", "Data/MC"],
    "Definitions" : {
        "Data/MC": {
            "type"       : "Agreement",
            "Paintables" : ["data", "Stack"]
        },
        
        "Main": {
            "type"      : "Main",
            "Paintables": ["Stack", "data"]
        },
    }
},
}
