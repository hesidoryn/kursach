from PIL import Image

# Separate RGB arrays
im = Image.open("test.jpg")
R, G, B = im.convert('RGB').split()
r = R.load()
g = G.load()
b = B.load()
w, h = im.size

# Convert non-black pixels to white
for i in range(w):
    for j in range(h):
        if(r[i, j] >= 100 or g[i, j] >= 100 or b[i, j] >= 100):
            r[i, j] = 255 # Just change R channel

# Merge just the R channel as all channels
im = Image.merge('RGB', (R, R, R))
im.show()
im.save("black_text.jpg")
