#
# 	This script reads the .root files generated by ReadingTreeMC, and checks
#	the histograms for NaN bins, and sets them to 0. This is done instead of
#	skipping entire plots.
#
###############################################################################

from ROOT import *
import math
import numpy as np

bins = [0, 50, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1200, 1500]
vars = ["pt","c1","bdt","ntrk","eta","width"]

finput1 = TFile.Open("gamma2jet_sherpa_py.root")
foutput1 = TFile("gamma2jet_sherpa_clean.root","recreate")

for i in bins:
	for var in vars:
		bin = str(i)

		print(i,var)

		ql = finput1.Get(bin+"_LeadingJet_Forward_Quark_"+var)
		gl = finput1.Get(bin+"_LeadingJet_Forward_Gluon_"+var)
		ol = finput1.Get(bin+"_LeadingJet_Forward_Other_"+var)
		qs = finput1.Get(bin+"_SubJet_Forward_Quark_"+var)
		gs = finput1.Get(bin+"_SubJet_Forward_Gluon_"+var)
		os = finput1.Get(bin+"_SubJet_Forward_Other_"+var)

		for k in range(1,ql.GetNbinsX()+1):
			a = ql.GetBinContent(k)
			b = gl.GetBinContent(k)
			c = ol.GetBinContent(k)
			d = qs.GetBinContent(k)
			e = gs.GetBinContent(k)
			f = os.GetBinContent(k)

			if math.isnan(a) == True : ql.SetBinContent(k,0)
			if math.isnan(b) == True : gl.SetBinContent(k,0)
			if math.isnan(c) == True : ol.SetBinContent(k,0)
			if math.isnan(d) == True : qs.SetBinContent(k,0)
			if math.isnan(e) == True : gs.SetBinContent(k,0)
			if math.isnan(f) == True : os.SetBinContent(k,0)
			'''
			if a < 0 : ql.SetBinContent(k,np.abs(a))
			if b < 0 : gl.SetBinContent(k,np.abs(b))
			if c < 0 : ol.SetBinContent(k,np.abs(c))
			if d < 0 : qs.SetBinContent(k,np.abs(d))
			if e < 0 : gs.SetBinContent(k,np.abs(e))
			if f < 0 : os.SetBinContent(k,np.abs(f))
			'''
		ql.Write()
		gl.Write()
		ol.Write()
		qs.Write()
		gs.Write()
		os.Write()

foutput1.Write()
foutput1.Close()
