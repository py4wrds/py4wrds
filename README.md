# Py4wrds (Python 4 Water Resources Data Science)

This repository builds the jupyter-book website hosted at [py4wrds.com](https://www.py4wrds.com).

Andrew, Aakash, Rich 



## Development

### Environment setup

```bash
git clone git@github.com:py4wrds/py4wrds.git
cd py4wrds
conda env create -f environment.yml
conda activate py4wrds
```

### Build site locally

```bash
jupyter-book build .
```

### Adding new dependencies.

```bash
# Add the new package to environment.yaml. Prefer adding to the conda section so conda can resolve
# all those dependencies together. Fallback to the pip section if the package isn't supported in 
# conda-forge.
conda env update --file environment.yml --prune
```


### Autobuild

I like this setup for auto-building the book whenever the file I'm working on has changed:

```bash
pip install watchdog
pip install https://github.com/joh/when-changed/archive/master.zip
when-changed -1 -s ./0-pre-course-setup.ipynb jupyter-book build .
```

### Assets

Files places in `assets` will be available on the py4wrds domain. So `assets/raster.tif` will be deployed to `https://py4wrds.com/raster.tif`.


### Code formatting

```bash
python -m black --line-length 140 -t py311  ./*.ipynb
```


## Credits and Acknowledgements 

Parts of these materials were sourced from:



* Stanford's "Software Development for Scientists and Engineers": https://github.com/CME211
* NASA Goddard's "Python Bootcamp": https://github.com/kialio/gsfcpyboot/tree/master
* Professor Dr. Qiusheng Wu's Introduction to GIS Programming class: https://geog-312.gishub.org/index.html
