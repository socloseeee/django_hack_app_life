.PHONY: install
install:
	python3 -m venv venv;\
	source venv/bin/activate;\
	sudo apt install python3-pip;\
	pip install -r requirements.txt;\
	python3 manage.py runserver;\
	echo "Все работает, даун."

.DEFAULT_GOAL := install
