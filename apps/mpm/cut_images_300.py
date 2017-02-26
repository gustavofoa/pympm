from PIL import Image, ImageOps, ImageDraw
import glob, os, math

width = 300

for infile in glob.glob("static/images/diasLiturgicos/*.*"):
    name = os.path.basename(infile)
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)

    height = math.floor(im.size[1] * width / im.size[0])

    output = ImageOps.fit(im, (width, height), centering=(0.5, 0.5))
        
    output.save("static/images/diasLiturgicos/300/" + name)
