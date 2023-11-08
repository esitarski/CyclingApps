import os
import glob
import base64

for fname in glob.glob('*.png'):
	with open(fname, 'rb') as f:
		base_name, extension = os.path.splitext( fname )
		with open(base_name + '.base64', 'w') as f_out:
			f_out.write( '<img src="data:image/{};base64,{}" />'.format(extension[1:], base64.standard_b64encode(f.read()).decode()) )
