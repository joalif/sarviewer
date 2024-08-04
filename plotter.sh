#!/bin/bash
#
# Script        :plotter.sh
# Author        :Julio Sanz
# Website       :www.elarraydejota.com
# Email         :juliojosesb@gmail.com
# Description   :Script to generate graphs in the folder graphs/ of this repository
# Dependencies  :sar,gnuplot
# Usage         :1)Give executable permissions to script -> chmod +x plotter.sh
#                2)Execute script -> ./plotter.sh
# License       :GPLv3
#

# Read sarviewer.properties file
. sarviewer.properties

if [ $# -ne 0 ];then
	echo "This script doesn't accept parameters"
elif [ "$graph_generator" == "gnuplot" ];then
	cd plotters/gnuplot
	gnuplot loadaverage.gplot
	gnuplot tasks.gplot
	gnuplot cpu.gplot
	gnuplot ram.gplot
	gnuplot swap.gplot
	gnuplot iotransfer.gplot
	gnuplot proc.gplot
	gnuplot contextsw.gplot
	#gnuplot netinterface.gplot
	gnuplot sockets.gplot
elif [ "$graph_generator" == "matplotlib" ];then
	cd plotters/matplotlib
	python3 loadaverage.py
	python3 tasks.py
	python3 dm0-await.py
	python3 dm1-await.py
	python3 dm2-await.py
	python3 cpu.py
	# python3 ram.py
	# python3 swap.py
	python3 iotransfer.py
	# python3 proc.py
	python3 contextsw.py
#	python3 netinterface.py
	python3 sockets.py
	python3 iowait.py
else
	echo "Variable graph_generator must be \"gnuplot\" or \"matplotlib\", please check sarviewer.properties"
fi
