sizeEl =900

def setup():
       size(600,400)
       background(255)
       
def draw():
      global sizeEl
      translate(300,200)
      fill(254,200,sizeEl)
      ellipse(0,0,sizeEl,sizeEl)
      sizeEl=sizeEl-3
