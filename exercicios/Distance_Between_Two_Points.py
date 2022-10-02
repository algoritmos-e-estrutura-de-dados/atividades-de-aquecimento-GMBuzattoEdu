import math
linha = (map(float,input().split(" ")))
x1,y1 = linha
linha2 = (map(float,input().split(" ")))
x2,y2 = linha2
resultado = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print("%0.4f"%resultado)