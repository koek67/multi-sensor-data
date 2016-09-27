.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3 notebook

#################################################################################
# GLOBALS                                                                       #
#################################################################################

BUCKET = [OPTIONAL] your-bucket-for-syncing-data (do not include 's3://')

#################################################################################
# COMMANDS                                                                      #
#################################################################################

requirements:
	pip install -q -r requirements.txt

data: requirements
	python src/data/make_dataset.py

clean:
	find . -name "*.pyc" -exec rm {} \;

lint:
	flake8 --exclude=lib/,bin/,docs/conf.py .

sync_data_to_s3:
	aws s3 sync data/ s3://$(BUCKET)/data/

sync_data_from_s3:
	aws s3 sync s3://$(BUCKET)/data/ data/

tunnel:
    ssh -N -f -L localhost:8888:localhost:8889 kkrishnan8@socvulcan.cc.gatech.edu

notebook:
    cd notebooks/ && jupyter notebook --no-browser --port=8889

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################
