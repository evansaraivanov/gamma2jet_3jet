from ROOT import *

var = "ntrk" #analysis variable,pick from  ntrk, bdt

#varData = TFile("dijet_data_py.root")
f1 = TFile("../root-files/gamma2jet_sherpa_py.root")
f2 = TFile("../root-files/trijet-sherpa-py-nancheck.root")

bin = [0,50,100,150,200,300,400,500,600,800,1000,1200,1500]

def myText(x,y,text, color=1):
    l= TLatex()
    l.SetTextSize(0.025)
    l.SetNDC()
    l.SetTextColor(color)
    l.DrawLatex(x,y,text)


for i in bin:
	leadingQuark = f1.Get(str(i)+"_LeadingJet_Forward_Quark_"+var+";1")
	if i > 400:
		leadingQuark2 = f2.Get(str(i)+"_j1_Central_Quark_"+var+";1")
		leadingQuark.Add(leadingQuark2)

	leadingGluon = f1.Get(str(i)+"_LeadingJet_Forward_Gluon_"+var+";1")
	if i > 400:
		leadingGluon2 = f2.Get(str(i)+"_j1_Central_Gluon_"+var+";1")
		leadingGluon.Add(leadingGluon2)

    #Normalize histograms
	if(leadingQuark.Integral() != 0):
		leadingQuark.Scale(1./leadingQuark.Integral())
	if(leadingGluon.Integral() != 0):
		leadingGluon.Scale(1./leadingGluon.Integral())

	if(var == "bdt" or var == "ntrk" or var == "c1" or var == "width"):
		if(i == 50):
			higherQuark50 = leadingQuark
			higherGluon50 = leadingGluon
		if(i == 200):
			higherQuark200 = leadingQuark
			higherGluon200 = leadingGluon
		if(i == 500):
			higherQuark500 = leadingQuark
			higherGluon500 = leadingGluon
		if(i == 1000):
			higherQuark1000 = leadingQuark
			higherGluon1000 = leadingGluon
		if(i == 1500):
			higherQuark1500 = leadingQuark
			higherGluon1500 = leadingGluon
	else:
		if(i == 0):
			higherQuark0 = leadingQuark
			higherGluon0 = leadingGluon
		if(i == 50):
			higherQuark50 = leadingQuark
			higherGluon50 = leadingGluon
		if(i == 100):
			higherQuark100 = leadingQuark
			higherGluon100 = leadingGluon
		if(i == 150):
			higherQuark150 = leadingQuark
			higherGluon150 = leadingGluon
		if(i == 200):
			higherQuark200 = leadingQuark
			higherGluon200 = leadingGluon
		if(i == 300):
			higherQuark300 = leadingQuark
			higherGluon300 = leadingGluon
		if(i == 400):
			higherQuark400 = leadingQuark
			higherGluon400 = leadingGluon
		if(i == 500):
			higherQuark500 = leadingQuark
			higherGluon500 = leadingGluon
		if(i == 600):
			higherQuark600 = leadingQuark
			higherGluon600 = leadingGluon
		if(i == 800):
			higherQuark800 = leadingQuark
			higherGluon800 = leadingGluon
		if(i == 1000):
			higherQuark1000 = leadingQuark
			higherGluon1000 = leadingGluon
		if(i == 1200):
			higherQuark1200 = leadingQuark
			higherGluon1200 = leadingGluon
		if(i == 1500):
			higherQuark1500 = leadingQuark
			higherGluon1500 = leadingGluon

#Create plots
c1 = TCanvas("c1","c1",500,500)

higherQuark500.GetYaxis().SetTitle("Normalized")
higherQuark500.GetYaxis().SetLabelSize(0.025)

gStyle.SetOptStat(0)
gPad.SetTickx()
gPad.SetTicky()

if(var == "bdt"):
    higherQuark500.GetYaxis().SetRangeUser(0,0.2)
    higherQuark500.GetXaxis().SetTitle("BDT")
if(var == "ntrk"):
    higherQuark500.GetYaxis().SetRangeUser(0,.23)
    higherQuark500.GetXaxis().SetTitle("n_{track}")
if(var == "c1"):
    higherQuark500.GetYaxis().SetRangeUser(0,0.1)
    higherQuark500.GetXaxis().SetTitle("C1")
if(var == "width"):
    higherQuark500.GetYaxis().SetRangeUser(0,0.24)
    higherQuark500.GetXaxis().SetTitle("Track width")
if(var == "eta"):
    higherQuark500.GetYaxis().SetRangeUser(0,0.1)
    higherQuark500.GetXaxis().SetTitle("|\eta|")
if(var == "pt"):
    higherQuark500.GetYaxis().SetRangeUser(0,0.6)
    higherQuark500.GetXaxis().SetTitle("p_{T}")

higherQuark50.SetLineColor(9)
higherQuark50.SetLineStyle(1)
higherGluon50.SetLineColor(9)
higherGluon50.SetLineStyle(2)

higherQuark500.SetLineColor(1)
higherQuark500.SetLineStyle(1)
higherGluon500.SetLineColor(1)
higherGluon500.SetLineStyle(2)

higherQuark1000.SetLineColor(2)
higherQuark1000.SetLineStyle(1)
higherGluon1000.SetLineColor(2)
higherGluon1000.SetLineStyle(2)

higherQuark500.Draw("HIST")
higherQuark1000.Draw("HIST same")
#higherQuark1500.Draw("HIST same")
higherQuark50.Draw("HIST same")
higherGluon50.Draw("HIST same")
higherGluon500.Draw("dash same")
higherGluon1000.Draw("HIST same")
#higherGluon1500.Draw("HIST same")

leg1 = TLegend(.55,.6,.82,.82)
leg1.AddEntry(higherQuark500,"Quark Jet","L")
leg1.AddEntry(higherGluon500,"Gluon Jet","L")

if(var == "eta" or var == "pt"):
	higherQuark0.SetLineColor(10)
	higherQuark0.SetLineStyle(1)
	higherGluon0.SetLineColor(10)
	higherGluon0.SetLineStyle(2)
	leg1.AddEntry(higherQuark0,"0<p_{T}<50 GeV","F")
	higherQuark0.Draw("HIST same")
	higherGluon0.Draw("HIST same")

leg1.AddEntry(higherQuark50,"50<pT<100 GeV","F")

if(var == "eta" or var == "pt"):
	higherQuark100.SetLineColor(11)
	higherQuark100.SetLineStyle(1)
	higherGluon100.SetLineColor(11)
	higherGluon100.SetLineStyle(2)
	leg1.AddEntry(higherQuark100,"100<p_{T}<150 GeV","F")
	higherQuark100.Draw("HIST same")
	higherGluon100.Draw("HIST same")

	higherQuark150.SetLineColor(12)
	higherQuark150.SetLineStyle(1)
	higherGluon150.SetLineColor(12)
	higherGluon150.SetLineStyle(2)
	leg1.AddEntry(higherQuark150,"150<p_{T}<200 GeV","F")
	higherQuark150.Draw("HIST same")
	higherGluon150.Draw("HIST same")

higherQuark200.SetLineColor(13)
higherQuark200.SetLineStyle(1)
higherGluon200.SetLineColor(13)
higherGluon200.SetLineStyle(2)
leg1.AddEntry(higherQuark200,"200<p_{T}<300 GeV","F")
higherQuark200.Draw("HIST same")
higherGluon200.Draw("HIST same")

if(var == "eta" or var == "pt"):
	higherQuark300.SetLineColor(14)
	higherQuark300.SetLineStyle(1)
	higherGluon300.SetLineColor(14)
	higherGluon300.SetLineStyle(2)
	leg1.AddEntry(higherQuark300,"300<p_{T}<400 GeV","F")
	higherQuark300.Draw("HIST same")
	higherGluon300.Draw("HIST same")

	higherQuark400.SetLineColor(15)
	higherQuark400.SetLineStyle(1)
	higherGluon400.SetLineColor(15)
	higherGluon400.SetLineStyle(2)
	leg1.AddEntry(higherQuark400,"400<p_{T}<500 GeV","F")
	higherQuark400.Draw("HIST same")
	higherGluon400.Draw("HIST same")

leg1.AddEntry(higherQuark500,"500<p_{T}<600 GeV","F")

if(var == "eta" or var == "pt"):
	higherQuark600.SetLineColor(6)
	higherQuark600.SetLineStyle(1)
	higherGluon600.SetLineColor(6)
	higherGluon600.SetLineStyle(2)
	leg1.AddEntry(higherQuark600,"600<p_{T}<800 GeV","F")
	higherQuark600.Draw("HIST same")
	higherGluon600.Draw("HIST same")

	higherQuark800.SetLineColor(7)
	higherQuark800.SetLineStyle(1)
	higherGluon800.SetLineColor(7)
	higherGluon800.SetLineStyle(2)
	leg1.AddEntry(higherQuark800,"800<p_{T}<1000 GeV","F")
	higherQuark800.Draw("HIST same")
	higherGluon800.Draw("HIST same")

leg1.AddEntry(higherQuark1000,"1000<p_{T}<1200 GeV","F")

if(var == "eta" or var == "pt"):
	higherQuark1200.SetLineColor(8)
	higherQuark1200.SetLineStyle(1)
	higherGluon1200.SetLineColor(8)
	higherGluon1200.SetLineStyle(2)
	leg1.AddEntry(higherQuark1200,"1200<p_{T}<1500 GeV","F")
	higherQuark1200.Draw("HIST same")
	higherGluon1200.Draw("HIST same")

#leg1.AddEntry(higherQuark1500,"1500<p_{T}<2000 GeV","F")
leg1.SetBorderSize(0)
leg1.Draw("same")

myText(0.14,0.84,"#it{#bf{#scale[1.8]{#bf{ATLAS} Simulation Preliminary}}}")
myText(0.14,0.80,"#bf{#scale[1.5]{#sqrt{s}=13 GeV}}")
myText(0.14,0.76,"#bf{#scale[1.5]{Anti-K_{t} EM+JES R=0.4}}")
myText(0.14,0.72,"#bf{#scale[1.5]{|\eta|<2.1}}")

c1.Print("kinematcs-"+var+".pdf")
