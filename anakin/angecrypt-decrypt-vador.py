from Crypto.Cipher import AES

algo = AES.new('Anger = DarkSide', AES.MODE_CBC, '\xae$\x8e\x08\xae\xdc\x8d\x0c\xdeYVM\x07\x11\xa7\xe9')

with open('angecrypt-darthvador.png', "rb") as f:
        d = f.read()

d = algo.decrypt(d)

with open("angedecrypt-" + 'anakin-skywalker.png', "wb") as f:
        f.write(d)
