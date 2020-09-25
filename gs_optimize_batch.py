import glob
import os

files=glob.glob('*.pdf')

for i in files:
	filename=os.path.splitext(i)[0]
	os.system('gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile='+filename+'_opt.pdf '+i)
