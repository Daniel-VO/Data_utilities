import glob
import os
import ray

files=glob.glob('*.pdf')

ray.init()
funcs=[]

@ray.remote
def pdfcrop(i):
	return os.system('pdfcrop --hires '+i+' '+i)
	
for i in files:
	funcs.append(pdfcrop.remote(i))
	
ray.get(funcs)
