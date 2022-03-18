#include <TF1.h>
#include <TFile.h>
#include <TH1F.h>

TH1F* h_background;
TH1F* h_signal;

void histgen() {
	/* Defining linear function */
	TF1 f1("f1", "pol1", 0, 10);
	// Setting y-int=5 slode=-0.5
	f1.SetParameters(5, -0.5);
	// Histo with same distribution
	TH1F bkg("background", "linear background", 100, 0, 10);
	bkg.FillRandom("f1", 10000);

	/* Define gaussian function */
	TF1 f2("f2", "gaus", 0, 10);
	// Set params: norm, mean, std dev
	f2.SetParameters(1.0, 6.0, 0.5);
	TH1F sig("signal", "gaussian signal", 100, 0, 10);
	sig.FillRandom("f2", 2000);

	/* Create data hist */
	TH1F data("data", "signal + background", 100, 0, 10);
	// Fill data with bkg
	data.FillRandom("f1", 10000);
	// Fill data with SOME sig 
	data.FillRandom("f2", 1750);
	
	TFile f("fitExample.root", "RECREATE");
	bkg.Write();
	sig.Write();
	data.Write();
	/* data is combo of bkg & sig.
		we will fit data hist to sum of 
		bkg and sig*C, where C is adjustable 
		scale factor to give best fit to data.
	*/
}

double ftotal(double* x, double* par) {
	/* ftotal must be called by other funct that performs fit */
	double xx = x[0];
	// Get int bin # corresponding to value xx
	int bin = h_background->GetXaxis()->FindBin(xx);
	// Use bin to get data out of sig & bkg hists
	double bkgd = h_background->GetBinContent(bin);
	double scale = par[0];
	double sgnl = (1 + scale) * h_signal->GetBinContent(bin);
	return bkgd + sgnl;
}

void fithist() {
	// Generate histograms
	histgen();

	TFile* f = TFile::Open("fitExample.root", "READONLY");
	h_background = (TH1F*) f->Get("background");
	h_signal = (TH1F*) f->Get("signal");
	TH1F* data = (TH1F*) f->Get("data");

	TF1* ftot = new TF1("ftot", ftotal, 0, 10, 1);
	ftot->SetParameter(0, 0.0); // Start w/ unscaled sig
	ftot->SetParLimits(0, -0.5, 0.5);

	data->Fit("ftot", "b");

}
