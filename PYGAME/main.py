from turtle import width
import pygame

#initial config
pygame.init()

BG_COLOR = (227, 220, 218)

#create a player screen
WIDHT = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("My game")

#main loop
status = True 
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            status = False 


    screen.fill(BG_COLOR)
    pygame.display.flip()

pygame.quit            




################


import turtle
import time
import random 

posponer = 0.1

#marcador
score = 0
high_score = 0

#Configuracion de la ventana 
wn = turtle.Screen()
wn.title("Juego Snake")
wn.bgcolor("gray")
wn.setup(width=700, height=700)
wn.tracer(0)

#Cabeza de serpiente 
cabeza = turtle.Turtle() 
cabeza.speed(1)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle() 
comida.speed(1)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)


#texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,290)
texto.write("Score : 0      High Score : 0", align= "center", font=("Courier", 24, "normal"))

#cuerpo serpiente
segmentos = []




#funciones
def  arriba():
     cabeza.direction = "up"
     
def abajo():
    cabeza.direction = "down"
    
def izquierda():
    cabeza.direction = "left"
    
def derecha():
    cabeza.direction = "right"  
    
     

def mov():
    if cabeza.direction == "up":
       y = cabeza.ycor()
       cabeza.sety(y + 20)
       
    if cabeza.direction == "down":
       y = cabeza.ycor()
       cabeza.sety(y - 20) 
       
    if cabeza.direction == "left":
       x = cabeza.xcor()
       cabeza.setx(x - 20)
       
    if cabeza.direction == "right":
       x = cabeza.xcor()
       cabeza.setx(x + 20)
       
 
#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


while True:
   wn.update()
   
   
   #colisiones bordes
   if cabeza.xcor() > 300 or cabeza.xcor() < -300 or cabeza.ycor() > 300 or cabeza.ycor() < -300:
       time.sleep(1)
       cabeza.goto(0,0)
       cabeza.direction = "stop"
       for segmento in segmentos:
            segmento.hideturtle()
       segmentos.clear()
       
       #resetear marcador
       score = 0  
       texto.clear()   
       texto.write("Score : {}      High Score : {}".format(score, high_score),
            align= "center", font=("Courier", 24, "normal"))
   
   #colisiones con la comdia 
   if cabeza.distance(comida) < 20:
       #mover la comida a posicion random 
       x = random.randint(-280,280)
       y = random.randint(-280,280)
       comida.goto(x,y)
       
       nuevo_segmento = turtle.Turtle() 
       nuevo_segmento.speed(1)
       nuevo_segmento.shape("square")
       nuevo_segmento.color("white")
       nuevo_segmento.penup()
       segmentos.append(nuevo_segmento)
       
       
       #Aumentar marcador 
       score += 10
       
       if score > high_score:
           high_score = score 
       texto.clear()   
       texto.write("Score : {}      High Score : {}".format(score, high_score),
            align= "center", font=("Courier", 24, "normal"))
    #mover el cuerpo de la serpiente
    
   totalSeg = len(segmentos)
   for index in range(totalSeg -1, 0, -1):
       x = segmentos[index - 1].xcor()
       y = segmentos[index - 1].ycor()
       segmentos[index].goto(x,y)
       
   if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
        
   mov()
   time.sleep(posponer)
   
    #Colisiones con el cuerpo 
   for segmento in segmentos: 
     if segmento.distance(cabeza) < 10:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            for segmento in segmentos: 
              segmento.hideturtle()
            segmentos.clear()
            
            
         #resetear marcador
            score = 0  
            texto.clear()   
            texto.write("Score : {}      High Score : {}".format(score, high_score),
                 align= "center", font=("Courier", 24, "normal"))
