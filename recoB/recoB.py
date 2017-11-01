from basf2 import *
from modularAnalysis import *
from stdCharged import *

inputMdst('default',sys.argv[1])
path = analysis_main

# list final state particles
fillParticleList("K+:loose",'Kid > 0.1 and chiProb > 0.001 and pt < 10 and -1. < dr < 1. and -5. < dz < 5.', True, path)
fillParticleList('pi-:all','chiProb > 0.001 and pt < 10 and -1. < dr < 1. and -5. < dz < 5.', True, path)
fillParticleList('e+:loose','eid > 0.1 and chiProb > 0.001 and pt < 10 and -1. < dr < 1. and -5. < dz < 5.', True, path)
fillParticleList('mu+:loose','muid > 0.1 and chiProb > 0.001 and pt < 10 and -1. < dr < 1. and -5. < dz < 5.', True, path)

#fillParticleList("e+:all",'eid > 0.1')
# stdLooseK() # instead of using fillParticleList, this function can be used ... (but how to include charged track cut?)
#stdLooseE()
# stdPi('all') # to list all pi+(-). Basically, fillParticleList('pi+:all','pt < 10 and -1. < dr < 1. and -5. < dz < 5.', True, path)

#reco K_S0 for f.s.p.
reconstructDecay('K_S0:all -> pi-:all pi+:all', '0.4<M<0.6', 1, True, path)
applyCuts('K_S0:all','0.477614<M<0.517614')

#reco for pi0 -> gamma gamma
fillParticleList("gamma:pi0highE",'E > 0.030',True,path)
reconstructDecay("pi0:loose -> gamma:pi0highE gamma:pi0highE",'0.115<M<0.153', 1, True, path)

reconstructDecay("K*0:kpiminus -> K+:loose pi-:all","0.6<M<1.4", 1,True, path)
reconstructDecay("K*0:kpi0 -> K_S0:all pi0:loose","0.6<M<1.4",1,True,path)
reconstructDecay("K*+:kpi0 -> K+:loose pi0:loose","0.6<M<1.4",1,True,path)
reconstructDecay("K*+:kpiplus -> K_S0:all pi+:all","0.6<M<1.4",1,True,path)

matchMCTruth('K*0:kpiminus')

reconstructDecay("B0:kee -> K*0:kpiminus e+:loose e-:loose","5.2 < Mbc < 5.3", 1,True, path)

#toolsTrackKaon = ['InvMass','^K+:loose']
#toolsTrackKaon += ['Kinematics','^K+:pid']
#toolsTrackPi = ['InvMass','^pi-:all']
toolsK_S0 = ['InvMass','^K_S0:all']

toolsPiLoose = ['InvMass','^pi0:loose']
#toolsTrackPi += ['Kinematics','^pi-:all']
toolsKStar0_kpiminus = ['InvMass','^K*0:kpiminus']
toolsKStar0_kpiminus += ['MCTruth','^K*0 -> K+ pi-']

toolsKStar0_kpi0 = ['InvMass','^K*0:kpi0']
toolsKStarPlus_kpi0 = ['InvMass','^K*+:kpi0']
toolsKStarPlus_kpiplus = ['InvMass','^K*+:kpiplus']

toolsTrackE = ['InvMass','^e+:loose']

toolsB0 = ['DeltaEMbc','^B0:kee']
toolsB0 += ['InvMass','^B0:kee']

ntupleFile('recoB_test.root')

ntupleTree('B0','B0:kee',toolsB0)
#ntupleTree('Kaons','K+:loose',toolsTrackKaon)
#ntupleTree('Pi','pi-:all',toolsTrackPi)
ntupleTree('KStar0_KPlus_PiMinus','K*0:kpiminus',toolsKStar0_kpiminus)
ntupleTree('KStar0_K_S0_Pi0','K*0:kpi0',toolsKStar0_kpi0)
ntupleTree('KStarPlus_KPlus_Pi0','K*+:kpi0',toolsKStarPlus_kpi0)
ntupleTree('KStarPlus_K_S0_PiPlus','K*+:kpiplus',toolsKStarPlus_kpiplus)

ntupleTree('K_S0','K_S0:all',toolsK_S0)
ntupleTree('Pi0','pi0:loose',toolsPiLoose)
#ntupleTree('E', 'e+:loose', toolsTrackE)

process(analysis_main)
print(statistics)