install-local:
	pip install -r requirements.txt

install-conda:
	conda install --file requirements.txt

update-requirements-local:
	pip freeze > requirements.txt

update-requirements-conda:
	conda list --export > requirements.txt

local-run:
	uvicorn kiwi.webservice.main:app --reload