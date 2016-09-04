def CreatePPM(filename, size, lst):
    imgx, imgy = size
    rgbPixels = [bytes(p) for p in lst]
    f = open(filename, "wb")
    f.write(b"P6\n")
    f.write(b"# PyPy \n")  # comment
    f.write(b"%d %d\n" % (imgx, imgy))
    f.write(b"%d\n" % (255,))  # max color value
    f.write(b"".join(rgbPixels))
    f.close()