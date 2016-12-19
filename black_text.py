from PIL import Image

# Separate RGB arrays
im = Image.open("sobel.jpg")
R, G, B = im.convert('RGB').split()
r = R.load()
g = G.load()
b = B.load()
w, h = im.size

# Convert non-black pixels to white
for i in range(w):
    for j in range(h):
        if(((r[i, j] >= 30 and r[i, j] <= 50])  or (g[i, j] >= 30  and g[i, j] <= 50]) or (b[i, j] >= 40  and b[i, j] <= 50]))):
            r[i, j] = 255 # Just change R channel

# Merge just the R channel as all channels
im = Image.merge('RGB', (R, R, R))
im.save("black.jpg")


