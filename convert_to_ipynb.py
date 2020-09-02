import IPython.nbformat.current as nbf
nb = nbf.read(open('Read_API.py', 'r'), 'py')
nbf.write(nb, open('Read_API.ipynb', 'w'), 'ipynb')