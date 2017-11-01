#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################
#
#  BelleII tutorial - February 2017
#
#  Steering file for the generation and reconstruction
#  of 100 signal events using EvtGen incl. FullSim,
#  starting from an user-defined decay file
#
#  Syntax:
#  basf2 B2T_generate_Upsilon4S.py decfile_name.dec output_name.root
#
#  Umberto Tamponi - Jan 16th 2017
########################################################

from basf2 import *
from simulation import add_simulation
from reconstruction import add_reconstruction

# Used if you want to generate non-Upsilon(4S) events
# from beamparameters import add_beamparameters


# Suppress messages and warnings during processing:
#set_log_level(LogLevel.ERROR)

# Create the module path
main = create_path()

# event info setter. Sets experiment, run and even numbers
main.add_module("EventInfoSetter", expList=1, runList=1, evtNumList=10)

# To run the framework the used modules need to be registered
evtgen = register_module('EvtGenInput')

# Sets evtgen only in a more verbose mode
evtgen.set_log_level(LogLevel.INFO)
# Gets the user-defined decay file 
evtgen.param('userDECFile', sys.argv[1]) 

# These lines are needed to generate non-Upsilon(4S) events.
# As example we report here the Upsilon(3S) case
#evtgen.param('ParentParticle', 'Upsilon(3S)') 
#beamparameters = add_beamparameters(main, "Y3S")

# run
main.add_module("Progress")
main.add_module("Gearbox")
main.add_module("Geometry")
main.add_module(evtgen)
add_simulation(main)
add_reconstruction(main)

# Shows immediately what is being generated as text output on the terminal
#main.add_module("PrintMCParticles", logLevel=LogLevel.DEBUG, onlyPrimaries=True)
# sets the output name
main.add_module("RootOutput", outputFileName=sys.argv[2]) 

# Process the events
process(main)

# show call statistics
print(statistics)
