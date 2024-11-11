# Python for Water Resources Data Science

Home page.

## Intro

Welcome

## Modules

```{tableofcontents}
```



## Learning objectives

- Master common commands, data types, and data dictionaries.
- Establish best coding practices for managing data and scripts. 
- Master "if/else" statements "for" and "while" loops, and other conditional statements. 
- Write clear functions and documentation to keep code clean and organized. 
- Modularize and disseminate clean codes to facilitate integration and re use with other projects. 
- Analyze model error metrics against observed data. 
- Understand and exploit object-oriented programming. 
- Work with key packages including pandas, numpy, matplotlib, jupyter, etc. 
- Set up and navigate Python integrated development environments such as Jupyter Notebook/Lab, Spyder, Visual Studio Code, Sublime Text, etc 
- Create, run, and disseminate virtual conda environments. 
- Use packages like Numpy, matplotlib, hydrostats, and Pulp for linear programming and matrix multiplication, specifically to optimize water allocations using DWRAT. 
- Develop plots and clear visualizations. 
- Use Jupyter Notebooks or other markdown tools to seamlessly embed Python code with documentation and publish it. 
- Use Git and GitHub for backing up code and collaboration with colleagues


## Dev status

| Module                  | Who | Status        |
| ----------------------- | --- | ------------- |
| 0. Pre-course           | AN  | Not started   |
| 1. Getting started      | AA  | Started   |
| 2. Python I             | AA  | Not started   |
| 3. Python II            | AN  | Not started   |
| 4. DS modules           | AA  | Not started   |
| 5. Geo python           | AN  | Not started   |
| 6. Water DS             | AA  | Not started   |
| 7. Interactive viz      | AN  | Not started   |
| 8. Git                  | AN  | Not started   |
| `intro.md`              | AN  | Not started   |



## Dev setup

Environment setup

```bash
git clone git@github.com:py4wrds/py4wrds.git
cd py4wrds
conda create -n py4wrds python=3.12
conda activate py4wrds
pip install -r requirements.txt
```

Build site locally

```bash
jupyter-book build .
```

