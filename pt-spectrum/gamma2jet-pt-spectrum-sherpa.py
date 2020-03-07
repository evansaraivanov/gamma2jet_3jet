#
#	Draw pT spectrum for the sum of leading jet from gamma+2jet
#
###############################################################################

from ROOT import *

def myText(x,y,text,color=1):
    l = TLatex()
    l.SetTextSize(0.025)
    l.SetNDC()
    l.SetTextColor(color)
    l.DrawLatex(x,y,text)
    pass

bin = [0,50,100,150,200,300,400,500,600,800,1000,1200,1500,2000]

f = TFile("../root-files/gamma2jet_sherpa_py.root")

pt_0_q = f.Get("0_LeadingJet_Forward_Quark_pt")
pt_0_g = f.Get("0_LeadingJet_Forward_Gluon_pt")
pt_0_o = f.Get("0_LeadingJet_Forward_Other_pt")

pt_0_q.Add(pt_0_g)
pt_0_q.Add(pt_0_o)

for i in range (1,13):
	print(str(bin[i]))
	pt_q = f.Get(str(bin[i])+"_LeadingJet_Forward_Quark_pt")
	pt_g = f.Get(str(bin[i])+"_LeadingJet_Forward_Gluon_pt")
	pt_o = f.Get(str(bin[i])+"_LeadingJet_Forward_Other_pt")

	pt_0_q.Add(pt_q)
	pt_0_q.Add(pt_g)
	pt_0_q.Add(pt_o)

c = TCanvas("c","c",500,500)
gPad.SetLogy()
gStyle.SetOptStat(0)
c.SetGrid()
gStyle.SetGridStyle(2)
gStyle.SetGridColor(15)
pt_0_q.GetXaxis().SetTitle("p_{T} (GeV)")
pt_0_q.Draw("HIST")

myText(0.48,0.84,'#it{#bf{#scale[1.4]{#bf{ATLAS} Simulation Preliminary}}}')
myText(0.48,0.80,'#bf{#scale[1.2]{#sqrt{s}=13 TeV}}')
myText(0.48,0.76,'#bf{#scale[1.2]{Anti-K_{t} EM+JES R=0.4}}')
myText(0.48,0.72,'#bf{#scale[1.2]{Leading Jet p_{T} Spectrum, Sherpa}}')

c.Print("gamma2jet-pt-sherpa.pdf")
