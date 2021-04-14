"""
Created 14. April 2020 by Daniel Van Opdenbosch, Technical University of Munich

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. It is distributed without any warranty or implied warranty of merchantability or fitness for a particular purpose. See the GNU general public license for more details: <http://www.gnu.org/licenses/>
"""

import glob, os, ray

files=glob.glob('*.pdf')

ray.init()

@ray.remote
def func(i):
	os.system('pdfcrop --hires '+i+' '+i)

ray.get([func.remote(i) for i in files])
