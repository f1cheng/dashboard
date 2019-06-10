#export PYTHONPATH=$PYTHONPATH:/home/cf/project/dashboard/dashboard/modules/
#echo $PYTHONPATH
pythonPath='/home/cf/project/dashboard/dashboard/modules'
import sys
sys.path.append(pythonPath)
print (sys.path)
