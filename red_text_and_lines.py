from PIL import Image

# Separate RGB arrays
im = Image.open("test.jpg")
R, G, B = im.convert('RGB').split()
r = R.load()
g = G.load()
b = B.load()
w, h = im.size

# Convert non-red pixels to white
for i in range(w):
    for j in range(h):
        if(r[i, j] <= 200 or g[i, j] >= 150 or b[i, j] >= 50):
            r[i, j] = 255 # Just change R channel
	    g[i, j] = 255
            b[i, j] = 255

# Merge just the R channel as all channels
im = Image.merge('RGB', (R, G, B))
im.show()
im.save("red_and_wh.jpg")
