
venv:
	@python3 -m venv venv
	@./venv/bin/pip3 install -r requirements.txt

sensor: venv
	@./venv/bin/python3 app/sensor.py

edge:
	@./venv/bin/python3 app/edge.py

.PHONY: sensor edge