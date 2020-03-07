from ROOT import *
import numpy as np

def myText(x,y,text,color=1):
    l = TLatex()
    l.SetTextSize(0.025)
    l.SetNDC()
    l.SetTextColor(color)
    l.DrawLatex(x,y,text)
    pass

var = "ntrk"

file1 = TFile("../root-files/gamma2jet_sherpa_clean.root")
file2 = TFile("../root-files/trijet_sherpa_clean.root")

bin = np.array([0.,50.,100.,150.,200.,300.,400.,500.,600.,800.,1000.,1200.,1500.,2000.])
bin2 = np.array([0.0,0.5,1.0,2.1])

gStyle.SetOptStat(0)
c = TCanvas("","",500,500)
gPad.SetTickx()
gPad.SetTicky()

pt_gamma_quark =  TH1F("pt_gamma_quark","",13,bin)
pt_gamma_gluon =  TH1F("pt_gamma_gluon","",13,bin)
pt_trijet_quark = TH1F("pt_trijet_quark","",13,bin)
pt_trijet_gluon = TH1F("pt_trijet_gluon","",13,bin)
'''
eta_gamma_quark = TH1F("eta_gamma_quark","",3,bin2)
eta_gamma_gluon = TH1F("eta_gamma_gluon","",3,bin2)
eta_trijet_quark = TH1F("eta_trijet","",3,bin2)
eta_trijet_gluon = TH1F("eta_trijet_gluon","",3,bin2)
'''
bin = np.array([0,50,100,150,200,300,400,500,600,800,1000,1200,1500,2000])

fq1_list = np.zeros(12) #these will hold fq values for different pt ranges
fq2_list = np.zeros(12)

for i in range(0,13):
	gamma_quark = file1.Get(str(bin[i])+"_SubJet_Forward_Quark_"+var)
	gamma_gluon = file1.Get(str(bin[i])+"_SubJet_Forward_Gluon_"+var)
	gamma_quark1 = file1.Get(str(bin[i])+"_LeadingJet_Forward_Quark_"+var)
	gamma_gluon1 = file1.Get(str(bin[i])+"_LeadingJet_Forward_Gluon_"+var)

	trijet_quark = file2.Get(str(bin[i])+"_j2_Forward_Quark_"+var)
	trijet_gluon = file2.Get(str(bin[i])+"_j2_Forward_Gluon_"+var)

	if bin[i] >= 400:
		trijet_quark1 = file2.Get(str(bin[i])+"_j1_Forward_Quark_"+var)
		trijet_gluon1 = file2.Get(str(bin[i])+"_j1_Forward_Gluon_"+var)
		trijet_quark.Add(trijet_quark1)
		trijet_gluon.Add(trijet_gluon1)

	if bin[i] < 1000:
		trijet_quark2 = file2.Get(str(bin[i])+"_j3_Forward_Quark_"+var)
		trijet_gluon2 = file2.Get(str(bin[i])+"_j3_Forward_Gluon_"+var)
		trijet_quark.Add(trijet_quark2)
		gamma_quark.Add(gamma_quark1)

	gamma_gluon.Add(gamma_gluon1)
	trijet_gluon.Add(trijet_gluon2)

	tq1 = 0.  #1 refers to gamma eta jet, 2 refers to trijet eta
	tg1 = 0.
	tq2 = 0.
	tg2 = 0.

	var_q1 = 0.
	var_q2 = 0.
	var_g1 = 0.
	var_g2 = 0.

	for j in range(1, gamma_quark.GetNbinsX()+1):
		tq1 += gamma_quark.GetBinContent(j)
		tg1 += gamma_gluon.GetBinContent(j)
		tq2 += trijet_quark.GetBinContent(j)
		tg2 += trijet_gluon.GetBinContent(j)

		var_q1 += (gamma_quark.GetBinError(j)*gamma_quark.GetBinError(j))
		var_q2 += (trijet_quark.GetBinError(j)*trijet_quark.GetBinError(j))
		var_g1 += (gamma_gluon.GetBinError(j)*gamma_gluon.GetBinError(j))
		var_g2 += (trijet_gluon.GetBinError(j)*trijet_gluon.GetBinError(j))

	var_tot_1 = var_q1 + var_g1
	var_tot_2 = var_q2 + var_g2

	fq1 = tq1/(tq1+tg1)
	fq2 = tq2/(tq2+tg2)
	fg1 = tg1/(tq1+tg1)
	fg2 = tg2/(tg2+tq2)

	print(fq1,fq2)

	var_fq1 = fq1*fq1 * ((var_tot_1 / ((tq1+tg1)*(tq1+tg1))) + (var_q1/(tq1*tq1)))
	var_fq2 = fq2*fq2 * ((var_tot_2 / ((tq2+tg2)*(tq2+tg2))) + (var_q2/(tq2*tq2)))
	var_fg1 = fg1*fg1 * ((var_tot_1 / ((tq1+tg1)*(tq1+tg1))) + (var_q1/(tq1*tq1)))
	var_fg2 = fg2*fg2 * ((var_tot_2 / ((tq2+tg2)*(tq2+tg2))) + (var_q2/(tq2*tq2)))

	pt_gamma_quark.SetBinContent(i+1,fq1)
	pt_gamma_gluon.SetBinContent(i+1,fg1)
	pt_trijet_quark.SetBinContent(i+1,fq2)
	pt_trijet_gluon.SetBinContent(i+1,fg2)

	pt_gamma_quark.SetBinError(i+1,np.sqrt(var_fq1))
	pt_gamma_gluon.SetBinError(i+1,np.sqrt(var_fg1))
	pt_trijet_quark.SetBinError(i+1,np.sqrt(var_fq2))
	pt_trijet_gluon.SetBinError(i+1,np.sqrt(var_fg2))

pt_gamma_quark.SetMaximum(1.)
pt_gamma_quark.SetMinimum(0.)
pt_gamma_quark.GetYaxis().SetTitle("Fraction")
pt_gamma_quark.GetXaxis().SetTitle("p_{T} (GeV)")

pt_gamma_quark.SetLineColor(28)
pt_gamma_gluon.SetLineColor(6)
pt_trijet_quark.SetLineColor(4)
pt_trijet_gluon.SetLineColor(8)

pt_gamma_quark.SetLineWidth(2)
pt_gamma_gluon.SetLineWidth(2)
pt_trijet_quark.SetLineWidth(2)
pt_trijet_gluon.SetLineWidth(2)

leg1 = TLegend(.15,0.15,0.45,0.3)
leg1.SetNColumns(2)
leg1.AddEntry(pt_gamma_quark,"f_{\gamma+2jet,Q}","l")
leg1.AddEntry(pt_gamma_gluon,"f_{\gamma+2jet,G}","l")
leg1.AddEntry(pt_trijet_quark,"f_{3jet,Q}","l")
leg1.AddEntry(pt_trijet_gluon,"f_{3jet,G}","l")
leg1.SetBorderSize(0)
leg1.SetFillStyle(0)

line = TLine(0.,0.5,2000.,0.5)
line.SetLineColor(1)
line.SetLineWidth(2)

pt_gamma_quark.Draw("HIST")
pt_gamma_gluon.Draw("HIST same")
pt_trijet_quark.Draw("HIST same")
pt_trijet_gluon.Draw("HIST same")
line.Draw("same")
leg1.Draw("same")

myText(0.14,0.84,'#it{#bf{#scale[1.4]{#bf{ATLAS} Simulation Preliminary}}}')
myText(0.14,0.80,'#bf{#scale[1.2]{#sqrt{s}=13 TeV}}')
myText(0.14,0.76,'#bf{#scale[1.2]{Anti-K_{t} EM+JES R=0.4}}')

c.Print("pt-fraction.pdf")
'''
#for eta range
for i in range(0,3):
    gamma_quark_eta = file2.Get(str(bin2[i])+"_SubJet_Forward_Quark_"+var)
    gamma_gluon_eta = file2.Get(str(bin2[i])+"_SubJet_Forward_Gluon_"+var)

    if(bin2[i] != 1.0):
        gamma_quark1_eta = file2.Get(str(bin2[i])+"_LeadingJet_Forward_Quark_"+var)
        gamma_gluon1_eta = file2.Get(str(bin2[i])+"_LeadingJet_Forward_Gluon_"+var)

        gamma_quark_eta.Add(gamma_quark1_eta)
        gamma_gluon_eta.Add(gamma_gluon1_eta)

    trijet_quark_eta = file2.Get(str(bin2[i])+"_LeadingJet_Central_Quark_"+var)
    trijet_quark1_eta = file2.Get(str(bin2[i])+"_SubJet_Central_Quark_"+var)
    trijet_gluon_eta = file2.Get(str(bin2[i])+"_LeadingJet_Central_Gluon_"+var)
    trijet_gluon1_eta = file2.Get(str(bin2[i])+"_SubJet_Central_Gluon_"+var)

    trijet_quark_eta.Add(trijet_quark1_eta)
    trijet_gluon_eta.Add(trijet_gluon1_eta)

    tq1 = 0. #1 refers to gamma eta jet, 2 refers to trijet eta
    tg1 = 0.
    tq2 = 0.
    tg2 = 0.

    var_q1 = 0.
    var_q2 = 0.
    var_g1 = 0.
    var_g2 = 0.

    for j in range(1, gamma_quark.GetNbinsX()+1):
        tq1 += gamma_quark_eta.GetBinContent(j)
        tg1 += gamma_gluon_eta.GetBinContent(j)
        tq2 += trijet_quark_eta.GetBinContent(j)
        tg2 += trijet_gluon_eta.GetBinContent(j)

        var_q1 += (gamma_quark.GetBinError(j)*gamma_quark.GetBinError(j))
        var_q2 += (trijet_quark.GetBinError(j)*trijet_quark.GetBinError(j))
        var_g1 += (gamma_gluon.GetBinError(j)*gamma_gluon.GetBinError(j))
        var_g2 += (trijet_gluon.GetBinError(j)*trijet_gluon.GetBinError(j))

    var_tot_1 = var_q1 + var_g1
    var_tot_2 = var_q2 + var_g2

    fq1 = tq1/(tq1+tg1)
    fq2 = tq2/(tq2+tg2)
    fg1 = 1.-fq1
    fg2 = 1.-fq2

    var_fq1 = fq1*fq1 * ((var_tot_1 / ((tq1+tg1)*(tq1+tg1))) + (var_q1/(tq1*tq1)))
    var_fq2 = fq2*fq2 * ((var_tot_2 / ((tq2+tg2)*(tq2+tg2))) + (var_q2/(tq2*tq2)))
    var_fg1 = fg1*fg1 * ((var_tot_1 / ((tq1+tg1)*(tq1+tg1))) + (var_q1/(tq1*tq1)))
    var_fg2 = fg2*fg2 * ((var_tot_2 / ((tq2+tg2)*(tq2+tg2))) + (var_q2/(tq2*tq2)))

    eta_gamma_quark.SetBinContent(i+1,fq1)
    eta_gamma_gluon.SetBinContent(i+1,fg1)
    eta_trijet_quark.SetBinContent(i+1,fq2)
    eta_trijet_gluon.SetBinContent(i+1,fg2)

    eta_gamma_quark.SetBinError(i+1,np.sqrt(var_fq1))
    eta_trijet_quark.SetBinError(i+1,np.sqrt(var_fq2))
    eta_gamma_gluon.SetBinError(i+1,np.sqrt(var_fg1))
    eta_trijet_gluon.SetBinError(i+1,np.sqrt(var_fg2))

eta_gamma_quark.SetMaximum(1.)
eta_gamma_quark.SetMinimum(0.)
eta_gamma_quark.GetYaxis().SetTitle("Fraction")
eta_gamma_quark.GetXaxis().SetTitle("|\eta|")

eta_gamma_quark.SetLineColor(6)
eta_gamma_gluon.SetLineColor(2)
eta_trijet_quark.SetLineColor(4)
eta_trijet_gluon.SetLineColor(8)

eta_gamma_quark.SetLineWidth(2)
eta_gamma_gluon.SetLineWidth(2)
eta_trijet_quark.SetLineWidth(2)
eta_trijet_gluon.SetLineWidth(2)

leg1 = TLegend(.15,0.15,0.45,0.3)
leg1.SetNColumns(2)
leg1.AddEntry(pt_gamma_quark,"f_{H,Q}","l")
leg1.AddEntry(pt_gamma_gluon,"f_{H,G}","l")
leg1.AddEntry(pt_trijet_quark,"f_{L,Q}","l")
leg1.AddEntry(pt_trijet_gluon,"f_{L,G}","l")
leg1.SetBorderSize(0)
leg1.SetFillStyle(0)

line = TLine(0.0,0.5,2.1,0.5)
line.SetLineColor(1)
line.SetLineWidth(2)

eta_gamma_quark.Draw("HIST E")
eta_gamma_gluon.Draw("HIST E same")
eta_trijet_quark.Draw("HIST E same")
eta_trijet_gluon.Draw("HIST E same")
line.Draw("same")
leg1.Draw("same")

myText(0.14,0.84,'#it{#bf{#scale[1.4]{#bf{ATLAS} Simulation Preliminary}}}')
myText(0.14,0.80,'#bf{#scale[1.2]{#sqrt{s}=13 TeV}}')
myText(0.14,0.76,'#bf{#scale[1.2]{Anti-K_{t} EM+JES R=0.4}}')

c.Print("eta-fraction.pdf")
'''
