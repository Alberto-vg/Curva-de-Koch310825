#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 23:12:45 2025

@author: albertovargas
"""

import turtle


turtle.setup(800, 600)
turtle.hideturtle()      # Ocultar la tortuga
turtle.penup()

# Posicionar para mejor visualización
turtle.goto(-200, 0)
turtle.pendown()

# Sistema L para la Curva de Koch con ángulos rectos
axioma = "F"
regla = "F+F-F-F+F"
angulo = 90  # Ángulos rectos
iteraciones = 4


cadena = axioma
for _ in range(iteraciones):
    nueva_cadena = ""
    for caracter in cadena:
        if caracter == "F":
            nueva_cadena += regla
        else:
            nueva_cadena += caracter
    cadena = nueva_cadena


longitud = 5  # Longitud del segmento (ajustada para varias iteraciones)

for caracter in cadena:
    if caracter == "F":
        turtle.forward(longitud)
    elif caracter == "+":
        turtle.left(angulo)
    elif caracter == "-":
        turtle.right(angulo)


turtle.mainloop()