# A scrapy poc
Python/Scrapy

## Dependencies
- Python 3.5 or above
- Scrapy

If you're using docker:
- docker && docker-compose

## Python Version 3.8

As suggested in the official scrapy docs, it is recommended to use a virtual env, therefore, in order to use the python version requested by the test, a virtual environment will be setup as follows:

``` bash
# Download the desired python version
> wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz

# Extract it somewhere
> tar -xvf Python-3.8.2.tar.xz

# Enter the directory
> cd path/to/pytho3.8

# Install it (altinstall)
> ./configure
> make
> make test
> sudo make altinstall

# Make a directory for your virtual env
> mkdir pvenv

# Create the virtual environment
> python3.8 -m venv /path/to/pvenv

# Activate the use of the venv (in this case, for fish)
> source /path/to/pvenv/bin/activate.fish

# You're goot to go
```

## Running:

This scrapy project takes a list of teams as argument, so run it as follows:
```bash
 > cd inter_spider
 > scrapy crawl -a teams_list=list inter
 # OR, to run using docker
 > sh run.sh
```

## Expected output:

The main output artifact is the file `~/inter_spider/output.csv` containing the game results for the teams listed in the input file `~/inter_spider/list` (already provided in the repository).

The output file format is:
> Team_name_1,Score,Team_name_2,Score

## References:
- https://docs.scrapy.org/en/latest/index.html
- https://docs.python.org/3/tutorial/venv.html#tut-venv
- https://github.com/python/cpython#build-instructions
