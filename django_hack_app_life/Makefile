.PHONY: install
install:
	python3 -m venv venv;\
	source venv/bin/activate;\
	pip install -r requirements.txt;\
	python manage.py runserver;\
	echo "Все работает, даун."

.DEFAULT_GOAL := install
