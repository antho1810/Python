from turtle import *
import colorsys

speed(-1)
bgcolor("black")
h = 0

for i in range(36):  # Aumentamos el número de iteraciones para cerrar la flor
    for j in range(10):  # Ajustamos el número de círculos internos
        c = colorsys.hsv_to_rgb(h, 0.9, 1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 10, 90)  # Ajustamos el radio para que los círculos sean más proporcionales
        lt(90)
        circle(150 - j * 10, 90)  # Usamos el mismo radio en ambas direcciones
        rt(180)
    rt(10)  # Ajustamos el ángulo de rotación para un patrón más completo

done()
