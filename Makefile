.PHONY: test

test:
	@python -m unittest discover -s src/ -p "_test_*.py"
