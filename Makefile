VENV_DIR = env

requirements: venv
	if [ -f requirements.txt ]; then pip3 install -r requirements.txt; fi

venv:
ifeq ($(wildcard $(VENV_DIR)/.),)
	python3 -m venv $(VENV_DIR)
endif