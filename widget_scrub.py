import nbformat
# Clean Colab widgets to make sure the notebook renders on GitHub

notebook_path = 'chem_5080_Assignment_5.ipynb'
ntbk = nbformat.read(notebook_path, as_version=4)
if 'widgets' in ntbk.metadata:
    del ntbk.metadata['widgets']
    print("Widgets metadata removed.")
else:
    print("No widgets metadata found.")

nbformat.write(ntbk, notebook_path)