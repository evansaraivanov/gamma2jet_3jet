from ROOT import *

def myText(x,y,text,color=1):
    l = TLatex()
    l.SetTextSize(0.025)
    l.SetNDC()
    l.SetTextColor(color)
    l.DrawLatex(x,y,text)
    pass

f1 = TFile.Open("dijet-pythia-bdt-pt-2.root")
c = TCanvas("c","c",500,500)

j0 = f1.Get("hj0")
j1 = f1.Get("hj1")
j2 = f1.Get("hj2")
j3 = f1.Get("hj3")
j4 = f1.Get("hj4")
j5 = f1.Get("hj5")
j6 = f1.Get("hj6")
j7 = f1.Get("hj7")
j8 = f1.Get("hj8")
j9 = f1.Get("hj9")

jsum = j0.Clone("")
jsum.Add(j1)
jsum.Add(j2)
jsum.Add(j3)
jsum.Add(j4)
jsum.Add(j5)
jsum.Add(j6)
jsum.Add(j7)
jsum.Add(j8)
jsum.Add(j9)

gPad.SetLogy()
gStyle.SetOptStat(0)
j1.SetLineColor(3)
j2.SetLineColor(4)
j3.SetLineColor(2)
j4.SetLineColor(8)
j5.SetLineColor(7)
j6.SetLineColor(6)
j7.SetLineColor(9)
j8.SetLineColor(31)
j9.SetLineColor(41)
jsum.SetLineColor(1)

leg = TLegend(0.75,0.3,0.89,0.7)
leg.SetBorderSize(0)
leg.AddEntry(j0,"J0","l")
leg.AddEntry(j1,"J1","l")
leg.AddEntry(j2,"J2","l")
leg.AddEntry(j3,"J3","l")
leg.AddEntry(j4,"J4","l")
leg.AddEntry(j5,"J5","l")
leg.AddEntry(j6,"J6","l")
leg.AddEntry(j7,"J7","l")
leg.AddEntry(j8,"J8","l")
leg.AddEntry(j9,"J9","l")
leg.AddEntry(jsum,"SUM","l")


jsum.Draw("HIST")
j0.Draw("HIST same")
j1.Draw("HIST same")
j2.Draw("HIST same")
j3.Draw("HIST same")
j4.Draw("HIST same")
j5.Draw("HIST same")
j6.Draw("HIST same")
j7.Draw("HIST same")
j8.Draw("HIST same")
j9.Draw("HIST same")
leg.Draw("")

myText(0.48,0.84,"#it{#bf{#scale[1.4]{#bf{ATLAS} Simulation Preliminary}}}");
myText(0.48,0.80,"#bf{#scale[1.2]{#sqrt{s} = 13 TeV}}");
myText(0.48,0.76,"#bf{#scale[1.2]{Anti-K_{t} EM+JES R=0.4}}");
myText(0.48,0.72,"#bf{#scale[1.2]{Leading Jet p_{T} Spectrum, Pythia}}");

c.Print("pt-test.pdf")
