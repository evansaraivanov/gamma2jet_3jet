from ROOT import *
import numpy as np

var1 = "ntrk" #name of variable as shown in .root file
VAR1 = "n_{Track}" #this is how the variable will be displayed on the graph using LATEX

sample = ["gamma","trijet"]
higherGraph = []

def myText(x,y,text, color=1):
    l = TLatex()
    l.SetTextSize(0.025)
    l.SetNDC()
    l.SetTextColor(color)
    l.DrawLatex(x,y,text)
    pass

for j in sample:
	higherGraph = []
	if(j == "trijet"):
		bin = [400,600,800,1000,1500,2000]
		varmc = TFile("../root-files/trijet-sherpa-py-nancheck.root")
	if(j == "gamma"):
		bin = [0,200,500,800,1500,2000]
		varmc = TFile("../root-files/gamma2jet_sherpa_py.root")

	for i in range(0,len(bin)-1):
		if(j == "gamma"):
		    higherQuark = varmc.Get(str(bin[i])+"_LeadingJet_Forward_Quark_"+var1+";1")
		    higherGluon = varmc.Get(str(bin[i])+"_LeadingJet_Forward_Gluon_"+var1+";1")
		if(j == "trijet"):
		    higherQuark = varmc.Get(str(bin[i])+"_j1_Central_Quark_"+var1+";1")
		    higherGluon = varmc.Get(str(bin[i])+"_j1_Central_Gluon_"+var1+";1")

	    #Normalize histograms
		if(higherQuark.Integral() != 0):
		    higherQuark.Scale(1./higherQuark.Integral())
		if(higherGluon.Integral() != 0):
		    higherGluon.Scale(1./higherGluon.Integral())

		x = np.empty(60)
		y = np.empty(60)

		for l in range(60):
		    x[l] = (higherQuark.Integral(0,l))
		    y[l] = (1. - higherGluon.Integral(0,l))

		higherGraph.append(x)
		higherGraph.append(y)

	a = np.array([0.0000001,0.9999999])
	b = np.array([0.9999999,0.0000001])

	c1 = TCanvas("c1","c1",500,500)
	c1.SetGrid()

	gr1 = TGraph(60,higherGraph[0],higherGraph[1])
	gr2 = TGraph(60,higherGraph[2],higherGraph[3])
	gr3 = TGraph(60,higherGraph[4],higherGraph[5])
	gr4 = TGraph(60,higherGraph[6],higherGraph[7])
	gr6 = TGraph(60,higherGraph[8],higherGraph[9])
	gr5 = TGraph(2,a,b)

	gr1.SetLineColor(8)
	gr2.SetLineColor(6)
	gr3.SetLineColor(4)
	gr4.SetLineColor(2)
	gr5.SetLineStyle(2)

	gr5.GetXaxis().SetTitle("Quark Efficiency")
	gr5.GetYaxis().SetTitle("Gluon Rejection")

	gr5.GetXaxis().SetLimits(0.,1.)
	gr5.SetMinimum(0.)
	gr5.SetMaximum(1.)

	gr5.GetXaxis().SetLimits(0.,1.)
	gr5.SetMinimum(0.)
	gr5.SetMaximum(1.)

	gPad.SetTickx()
	gPad.SetTicky()
	gStyle.SetGridStyle(2)
	gStyle.SetGridColor(15)
	gr5.SetLineStyle(2)

	leg1 = TLegend(0.14,0.42,0.38,0.6)
	leg1.SetBorderSize(0)
	leg1.SetFillStyle(0)
	leg1.AddEntry("","Quark Jet Tagging, "+VAR1+" < X","")

	if(j == "trijet"):
		leg1.AddEntry(gr1,"400 < p_{T} < 500 GeV","L")
		leg1.AddEntry(gr2,"600 < p_{T} < 800 GeV","L")
		leg1.AddEntry(gr3,"800 < p_{T} < 1000 GeV","L")
		leg1.AddEntry(gr4,"1000 < p_{T} < 1200 GeV","L")
		leg1.AddEntry(gr6,"1500 < p_{T} < 2000 GeV","L")
	if(j == "gamma"):
		leg1.AddEntry(gr1,"0 < p_{T} < 50 GeV","L")
		leg1.AddEntry(gr2,"200 < p_{T} < 300 GeV","L")
		leg1.AddEntry(gr3,"500 < p_{T} < 600 GeV","L")
		leg1.AddEntry(gr4,"800 < p_{T} < 1000 GeV","L")
		leg1.AddEntry(gr6,"1500 < p_{T} < 2000 GeV","L")

	gr5.SetTitle("")

	gr5.Draw("AL")
	gr1.Draw("same")
	gr2.Draw("same")
	gr3.Draw("same")
	gr4.Draw("same")
	gr6.Draw("same")
	leg1.Draw("same")

	myText(0.13,0.30,'#it{#bf{#scale[1.4]{#bf{ATLAS} Simulation Preliminary}}}')
	myText(0.13,0.26,'#bf{#scale[1.2]{#sqrt{s}=13 GeV}}')
	myText(0.13,0.22,'#bf{#scale[1.2]{Anti-K_{t} EM+JES R=0.4}}')
	if(j == "gamma"):
		myText(0.13,0.18,'#bf{#scale[1.2]{\gamma + dijet}}')
	if(j == "trijet"):
		myText(0.13,0.18,'#bf{#scale[1.2]{Trijet}}')

	c1.Print("./roc-range/"+j+"-"+var1+"-ROC.pdf")
