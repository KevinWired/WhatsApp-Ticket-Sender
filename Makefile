PROGRAM = e-ticket.py

run:
	python3 $(PROGRAM)

# make clean : Limpia archivos generados.
clean:
	rm -f *.pyc __pycache__/* && rm -f *.txt

# make rmtxt : Elimina los archivos txt generados.
rmtxt:
	rm -f *.txt

.DEFAULT_GOAL := run

