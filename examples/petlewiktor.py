zwierzenta_miesozerne = ['lew', 'krokodyl', 'sep', 'waz', 'wilk' ]
zwierzentaaa_roslinozerne = ['krowa', 'krolik', 'zebra', 'zyrafa', 'papuga']
print zwierzenta_miesozerne
print zwierzentaaa_roslinozerne
zwierzenta = zwierzenta_miesozerne + zwierzentaaa_roslinozerne
print zwierzenta

for zwierze in zwierzenta:
    if zwierze in zwierzentaaa_roslinozerne:
        okrzyk = "zjedza_mnie"
    elif zwierze in zwierzenta_miesozerne:
        okrzyk = 'zjem ich'
    print zwierze + " " + okrzyk

