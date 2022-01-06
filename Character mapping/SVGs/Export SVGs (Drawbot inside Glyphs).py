from GlyphsApp import *
f = Glyphs.font
fill(0,0,0,1)

yMin = min([l.bounds[0][1] for l in f.selectedLayers])
yMax = max([l.bounds[0][1]+l.bounds[1][1] for l in f.selectedLayers])
height = yMax-yMin+100

for l in f.selectedLayers:
    g = l.parent
    thePath = l.completeBezierPath
    lb = (l.bounds[0][0],l.bounds[0][1],l.bounds[1][0],l.bounds[1][1])
    newPage(lb[2], height)
    translate(-lb[0], -f.masters[0].descender+100)
    drawPath(thePath)
    saveImage("/Users/toshi/Github repos/Alcarin-Tengwar/Character mapping/SVGs/%s.svg" % g.unicode)