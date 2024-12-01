# Py4wrds (Python 4 Water Resources Data Science)

Aakash, Andrew, Rich 

Credits and Acknowledgements - Parts of these materials were sourced from:
* Stanford's "Software Development for Scientists and Engineers": https://github.com/CME211
* NASA Goddard's "Python Bootcamp": https://github.com/kialio/gsfcpyboot/tree/master


# Development

Environment setup

```bash
git clone git@github.com:py4wrds/py4wrds.git
cd py4wrds
conda create -f environment.yaml
conda activate py4wrds
```

Build site locally

```bash
jupyter-book build .
```


Adding new dependencies.

```bash
# Add the new package to environment.yaml. Prefer adding to the conda section so conda can resolve
# all those dependencies together. Fallback to the pip section if the package isn't supported in 
# conda-forge.
conda env update --file environment.yml --prune
```


I like this setup for auto-building the book whenever the file I'm working on has changed:

```bash
pip install watchdog
pip install https://github.com/joh/when-changed/archive/master.zip
when-changed -1 -s ./0-pre-course-setup.ipynb jupyter-book build .
```