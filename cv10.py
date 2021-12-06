#Instalována knihovna pyproj pro práci se souřadnicovými systémy

from pyproj import Transformer

wgs2jtsk = Transformer.from_crs(4326, 5514, always_xy = True)
jtsk2wgs = Transformer.from_csr(5514,4326, always_xy = True)

out = wgs2jtsk.transform(14, 50) #always xy je true
print(out)
