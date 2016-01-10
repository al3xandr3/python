
import sys; import os; sys.path.append(os.path.expanduser('~/DropBox/my/projects/python/'))
import glob
import os
import shutil

read_files = glob.glob(os.path.expanduser("~/DropBox/my/projects/_autom/ipynb/") + "*.ipynb")

for f in read_files:
	print f
	run = "ipython nbconvert --to=html --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=360 {0} --stdout | python {1}ipynb_clean_html_output.py > {0}.html".format(f, os.path.expanduser('~/DropBox/my/projects/python/'))
	os.system(run)
	shutil.copy(f+'.html', os.path.expanduser("~/DropBox/Public/ipynb/"))

