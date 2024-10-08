# BTO (British Trust for Ornithology) Data Wrangler

## Overview
This is a toy project that takes publicly available data from the BTO to use for exercises in data loading, processing, 
and visualisation.

The source data 

## Getting Started

### Pre-requisites

* Python 3.12
* MySQL
* Download the source data from https://www.bto.org/sites/default/files/atlas_open_data_files.zip and unzip the file
These instructions are for MacOS. The project hasn't been tested on Windows or other OS but should work with some adjustment 
to the scripts.

### Setting up
#### Create the bto_data database
Run the scripts into your MySQL environment. The user will need the ability to create schemas and tables
* `>mysql -u <your_user> -p < ./db/create-tables.sql`

#### Python environment
* `git clone https://github.com/datasoc-ltd/bto-data`
* `cd bto-data`
* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`

### Running the data load
Export the database details to your environment. this shows the database running locally
* `EXPORT DB_HOST=localhost`
* `EXPORT DB_USER=<your_user>`
* `EXPORT DB_PASS=<your_pass>`
Then from the root directory of the project:
* `>python ./load/loader.py`
This will load the species (465 rows) and distributions (1,410,938 rows)
