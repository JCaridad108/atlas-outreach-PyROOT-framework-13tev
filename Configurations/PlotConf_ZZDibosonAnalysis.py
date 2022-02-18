config = {
#"Luminosity": 547, #period A
#"Luminosity": 1949, #period B
#"Luminosity": 2884, #period C
#"Luminosity": 4684, #period D
"Luminosity": 10064, #period A-D
"InputDirectory": "resultsZZDiboson",

"Histograms" : {
    #"mass_four_lep_ext"       : {},
    "invMassZ1"       : {"rebin" : 2},
    "invMassZ2"       : {"rebin" : 2},
    "lep_n"           : {"y_margin" : 0.4},
    "lep_pt"          : {"y_margin" : 0.4, "rebin" : 4},
    "lep_eta"         : {"y_margin" : 0.5, "rebin" : 3},
    "lep_E"           : {"rebin" : 3},
    "lep_phi"         : {"y_margin" : 0.6, "rebin" : 4,},
    "lep_charge"      : {"y_margin" : 0.6},
    "lep_type"        : {"y_margin" : 0.5,},
    "lep_ptconerel30" : {"y_margin" : 0.3, "rebin" : 4},
    "lep_etconerel20" : {"y_margin" : 0.3, "rebin" : 4},

},

"Paintables": {
    "Stack": {
        "Order": ["ZZ", "Background"],#, "Other"],#,"HZZ"],
        "Processes" : {  
            #"HZZ" : {
            #    "Color" : "#ff0000",
            #    "Contributions" : ["ggH125_ZZ4lep","VBFH125_ZZ4lep","WH125_ZZ4lep","ZH125_ZZ4lep"]},

              
            "ZZ" : {
                "Color"         : "#ffcd00",#"#00cdff",
                "Contributions" : ["llll"
                                   #,"ZqqZll"
                                   #,"llvv"
                                  ]},
			"Background" : {
				"Color"			: "#6b59d3",
				"Contributions"	: ["ZqqZll","WqqZll","WpqqWmlv","WplvWmqq","WlvZqq",
								  "lllv","llvv","lvvv", "single_top_tchan", "single_antitop_tchan",
								  "single_top_wtchan","single_antitop_wtchan","single_top_schan",
								  "single_antitop_schan","ttbar_lep"
								  ]},
            #"Other": {       
            #    "Color"         : "#6b59d3",
            #    "Contributions" : ["Zee", "Zmumu"
            #                       #, "WqqZll", "lllv"
            #                       #, "ttbar_lep"]},
			#					   ]},

        }
    },

    "data" : {
        "Contributions": ["data_A", "data_B", "data_C", "data_D"]}
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
