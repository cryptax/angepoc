from Crypto.Cipher import AES

algo = AES.new('Anger = DarkSide', AES.MODE_CBC, '\xae$\x8e\x08\xae\xdc\x8d\x0c\xdeYVM\x07\x11\xa7\xe9')

with open('anakin-skywalker-anged.png', "rb") as f:
        d = f.read()

d = algo.encrypt(d)

with open("angecrypt-" + 'darthvador.png', "wb") as f:
        f.write(d)
