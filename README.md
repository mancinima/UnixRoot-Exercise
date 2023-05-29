# MyFirstRepository

This repository will contain some example scripts and code.

This is the Unix&Root Excercise repository Here's the aim of such exercise: Create a git repository containing the following things:

- a bash script that takes the path of a folder as a command line argument, checks if the folder exists, and if it does it runs on all the files in the folder and prints the message "the file XXX is an image" if the file ends with ".png" or ".jpg"
- a python script that takes via command line input at execution the name of a csv file structred like this example, it reads that file, sorts the entries by birthdate and prints them out. The script should correctly treat any possible mistake in the input file, and it should also have an option to print the entries in opposite order.
- a pyroot scripts that reads the "mc_410000.ttbar_lep.exactly2lep.filtered.root" file we used above, applies a selection requiring at least one jet in the event with pT>50000 MeV and requires that the leading lepton (i.e. the one with the higest pt) passes TightID requirements (i.e. its variable lep_isTightID is 1). Produce a plot of the leading lepton pt, one of the leading jet pt, and use a 2D plot to study if these two variables are correlated. Write in output a tree containing just the leading lepton pt and type, and the jet pt and trueflavor for all the jets in the event. Also, the script must calculate efficiencies vs pt for the isTightID requirement, separetely for electrons and muons.
- a second pyroot script that reads that output and produce 1D histograms to superimpose, in order to compare the leeading lepton pt for electron and muons, and one to compare the pt distribution for b-jets (the ones with trueflav==5) vs non-b-jets (all the others).
