install-local:
	pip install -r requirements.txt

update-requirements-local:
	pip freeze > requirements.txt

local-run:
	uvicorn app.main:app --reload
