# a '-' before a shell command causes make to ignore its exit code (errors)

install:
	python setup.py install

uninstall:
	yes | pip uninstall language_models

clean:
	find . -name '*.pyc' -delete
	rm -rf build dist language_models.egg-info __pycache__

reinstall: clean uninstall install

lint:
	flake8 src

