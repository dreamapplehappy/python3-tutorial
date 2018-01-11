from io import BytesIO

bio = BytesIO()

with open('./js.png', 'rb') as f:
    bio.write(f.read())

print(bio.getvalue())


with open('./js-test.png', 'wb') as f:
    f.write(bio.getvalue())