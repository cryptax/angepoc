all: encrypt decrypt

encrypt:
	python angecrypt-encrypt-anakin.py
	@echo "Look at image angecrypt-darthvador.png: should be Darth Vador"

decrypt:
	python angecrypt-decrypt-vador.py
	@echo "View image angedecrypt-anakin-skywalker.png: should be Anakin Skywalker"

clean: 
	rm -f *~
	rm -f darthvador.png angecrypt-darthvador.png angedecrypt-anakin-skywalker.png
