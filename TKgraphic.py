try:
    import pygame
except:
    import pip
    pip.main[('install','pygame')]
import random
pygame.init()
pygame.font.init()
pygame.display.init()

__versione__ = '1.5.0'

display = 0

class Display:
    def __init__(self,base=800,altezza=600,schermo_intero=False,nome_schermo='untitle'):
        self.b = base
        self.h = altezza
        self.b_s,self.h_s = base,altezza
        self.schermo = schermo_intero
        self.nome = nome_schermo

    def draw(self):
        global display
        if self.schermo == True:
            self.display = pygame.display.set_mode((self.b,self.h),pygame.FULLSCREEN)
        else:
            self.display = pygame.display.set_mode((self.b,self.h))
            
        display = self.display
        pygame.display.set_caption(self.nome)
        return self.display

    def fill(self,color=(255,255,255)):
        self.display.fill(color)

    def update(self,cosa):
        pygame.display.update(cosa)

    def flip(self):
        pygame.display.flip()

    def close(self):
        pygame.quit()

    def icon(self,image):
        pygame.display.set_icon(image)

    def blit(self,image,x,y):
        display.blit(image,(x,y))

class Cerchio:
    def __init__(self,x,y,r,spessore=1,colore=(0,0,0)):
        self.x = x
        self.y = y
        self.r = r
        self.spessore = spessore
        self.colore = colore

class Minimenù:
    def __init__(self,xbt=0,ybt=0,bbt=0,hbt=0,numero_bt=0,colore=(200,200,200),nomi=[],funzioni=[]):
        self.xbt = xbt
        self.ybt = ybt
        self.numero_bt = numero_bt
        self.color = colore
        self.nomi = nomi
        self.funzioni = funzioni
        self.bbt = bbt
        self.hbt = hbt
        self.button = {}
    
    def draw(self):
        for i in range(numero_bt):
            self.button[i+1] = Button(self.xbt,self.ybt,self.bbt,self.hbt,self.color,self.funzioni[i])
            messageToScreen(self.xbt+round(self.xbt*5/100),nomi[i]).draw()

    def ColPoint(self,x,y,key):
        for i in range(numero_bt):
            a = self.button[i+1]
            a.ColPoint(x,y,keys)


class ButtonRandom:
    def __init__(self,x,y,b,h,color,max_click=1,min_num=1,max_num=100000000):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.min_num = min_num
        self.max_num = max_num
        self.max_click = max_click
        self.button = pygame.Rect(x,y,b,h)
        self.coord = [x,y,b,h]
        self.red = color[0] 
        self.green = color[1] 
        self.blue = color[2]
        self.red_ = self.red
        self.green_ = self.green
        self.blue_ = self.blue
        self.click = 0
        self.locket = False
        self.clocket = False # clicato
        
    def draw(self):
        self.color = (self.red_,self.green_,self.blue_)
        pygame.draw.rect(display,self.color,self.coord)

    def ColPoint(self,x,y,keys,keys_=(1,0,0),movimento=False):
        qwerty = 0
        if self.locket == False:
            if (self.button).collidepoint(x,y):
                if self.red_-50 >= 0:
                    self.red_ = self.red-50
                if self.green_-50 >= 0:    
                    self.green_ = self.green-50
                if self.blue_-50 >= 0:    
                    self.blue_ = self.blue-50
                if keys == keys_ and self.click < self.max_click and self.funzione != None:
                    self.click += 1
                    if self.red_-75 >= 0:
                        self.red_ = self.red-75
                    if self.green_-75 >= 0:    
                        self.green_ = self.green-75
                    if self.blue_-75>= 0:    
                        self.blue_ = self.blue-75
                    if movimento == True:
                        self.y -= 5
                        
                    return random.randint(self.min_num,self.max_num)
                    self.clocket = True
                
                elif keys == keys_ and self.click < self.max_click and self.funzione == None:
                    self.click += 1
                    if self.red_-75 >= 0:
                        self.red_ = self.red-75
                    if self.green_-75 >= 0:    
                        self.green_ = self.green-75
                    if self.blue_-75>= 0:    
                        self.blue_ = self.blue-75
                    if movimento == True:
                        self.y -= 5
                    self.clocket = True
                else:
                    self.clocket = False

            else:
                self.red_ = self.red
                self.green_ = self.green
                self.blue_ = self.blue
                self.click = 0
                if movimento == True and qwerty == 0:
                    qwerty += 1
                    self.y += 5

        self.color = (self.red_,self.green_,self.blue_)

    def Click(self):
        return random.randint(self.min_num,self.max_num)

    def Locket(self,attive=True):
        self.locket = attive

    def Return(self):
        return self.clocket

    def UPDATE(self,color):
        self.red = color[0] 
        self.green = color[1] 
        self.blue = color[2]

         
class Image:
    def __init__(self,nome,x,y):
        self.x,self.y = x,y
        self.image = pygame.image.load(nome)

    def draw(self):
        display.blit(self.image,(self.x,self.y))

    def Scalare(self,b,h):
        self.image = pygame.transform.scale(self.image,(b,h))

    def ICONE(self):
        return self.image
        
        
class Button:
    def __init__(self,x,y,b,h,color,funzione,max_click=1):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.max_click = max_click
        self.funzione = funzione
        self.button = pygame.Rect(x,y,b,h)
        self.coord = [x,y,b,h]
        self.red = color[0] 
        self.green = color[1] 
        self.blue = color[2]
        self.red_ = self.red
        self.green_ = self.green
        self.blue_ = self.blue
        self.click = 0
        self.locket = False
        self.clocket = False # clicato
        
    def draw(self):
        self.color = (self.red_,self.green_,self.blue_)
        pygame.draw.rect(display,self.color,self.coord)

    def ColPoint(self,x,y,keys,keys_=(1,0,0),movimento=False):
        qwerty = 0
        if self.locket == False:
            if (self.button).collidepoint(x,y):
                if self.red_-50 >= 0:
                    self.red_ = self.red-50
                if self.green_-50 >= 0:    
                    self.green_ = self.green-50
                if self.blue_-50 >= 0:    
                    self.blue_ = self.blue-50
                if keys == keys_ and self.click < self.max_click and self.funzione != None:
                    self.click += 1
                    if self.red_-75 >= 0:
                        self.red_ = self.red-75
                    if self.green_-75 >= 0:    
                        self.green_ = self.green-75
                    if self.blue_-75>= 0:    
                        self.blue_ = self.blue-75
                    if movimento == True:
                        self.y -= 5
                        
                    self.funzione()
                    self.clocket = True
                
                elif keys == keys_ and self.click < self.max_click and self.funzione == None:
                    self.click += 1
                    if self.red_-75 >= 0:
                        self.red_ = self.red-75
                    if self.green_-75 >= 0:    
                        self.green_ = self.green-75
                    if self.blue_-75>= 0:    
                        self.blue_ = self.blue-75
                    if movimento == True:
                        self.y -= 5
                    self.clocket = True
                else:
                    self.clocket = False

            else:
                self.red_ = self.red
                self.green_ = self.green
                self.blue_ = self.blue
                self.click = 0
                if movimento == True and qwerty == 0:
                    qwerty += 1
                    self.y += 5

        self.color = (self.red_,self.green_,self.blue_)

    def Click(self):
        self.funzione()

    def Locket(self,attive=True):
        self.locket = attive

    def Return(self):
        return self.clocket

    def UPDATE(self,color):
        self.red = color[0] 
        self.green = color[1] 
        self.blue = color[2]

        
def reset():
    global display
    display = 0


class Progressivebar:
    def __init__(self,x,y,b,h,capacity=100,colore=(200,200,200)):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.capacity = capacity
        self.colore = colore
        self.color = (0,200,0)
        self.select = False
        self.s = False
        self.progressiv = pygame.Rect(x,y,b,h)

    def draw(self):
        pygame.draw.rect(display,self.colore,(self.x,self.y,self.b+10,self.h))

    def counter(self,numero_tacche):
        if self.select == True:
            pygame.draw.rect(display,self.color,(self.x+5,self.y+self.h/10,(self.b/self.capacity)*numero_tacche,self.h-self.h/5))
        else:
            pass

    def ColPoint(self,x,y,keys):
        if self.progressiv.collidepoint(x,y):
            self.select = True
            self.color = (0,200,0)
        else:
            self.select = False
            self.color = (0,255,0)
            
        if self.progressiv.collidepoint(x,y) and keys == (1,0,0):
            self.s = True
            self.color = (0,200,0)
        else:
            self.s = False
            self.color = (0,255,0)

    def Return(self):
        return self.s,self.select


class messageToScreen:
    def __init__(self,x,y,msg,NumFont=24,color=(0,0,0),font=None):
        self.x = x
        self.y = y
        self.msg = msg
        self.NumFont = NumFont
        self.color = color
        self.font = font
        
    def draw(self):
        font = pygame.font.SysFont(self.font,self.NumFont)
        text = font.render(str(self.msg),True,self.color)
        display.blit(text, (self.x,self.y))       



class CheckBox:
    def __init__(self,x,y,b,h,funzione_true,funzione_false,color=(200,200,200),max_click=1,colore_attivo=(0,255,0),colore_disattivo=(255,0,0)):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.color_attive = colore_attivo
        self.color_disattive = colore_disattivo
        self.color_mini = colore_disattivo
        self.color = color
        self.coord = [x,y,b,h]
        self.button = pygame.Rect(self.coord)
        self.locket = False
        self.attive = True
        self.funzione_t = funzione_true
        self.funzione_f = funzione_false
        self.click = 0
        self.max_click = max_click

    def ColPoint(self,x,y,keys):
        if self.locket == False:
            if (self.button).collidepoint(x,y):
                if keys == (1,0,0) and self.click < self.max_click:
                    self.click += 1
                    if self.attive == True and self.funzione_t != None:
                        self.attive = False
                        self.funzione_t()
                        self.color_mini = self.color_attive
                    else:
                        if self.funzione_t != None:
                            self.attive = True
                            self.funzione_f()
                            self.color_mini = self.color_disattive
    
            else:
                self.click = 0

    def draw(self):
        pygame.draw.rect(display,self.color,self.coord)
        pygame.draw.rect(display,self.color_mini,(self.x+18,self.y+self.y/2-7,15,15))

    def Locket(self,attive=True):
        self.locket = attive

    def Return(self):
        return self.attive


class NumBox:
    def __init__(self,x,y,b=100,h=25,num_min=0,num_max=10,num_partenza=None,color=(200,200,200),NumFont=24,font=None,color_font=(0,0,0)):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.color = color
        if num_partenza == None:
            self.num = num_min
        else:
            self.num = num_partenza
        self.num_min = num_min
        self.num_max = num_max
        self.NumFont = NumFont
        self.color_font = color_font
        self.font = font

    def draw(self):
        pygame.draw.rect(display,self.color,(self.x,self.y,self.b,self.h))

        pygame.draw.rect(display,(0,255,0),
                        (self.x+self.b-self.b/3,self.y+1,self.b/3,self.h/2))
                
        pygame.draw.rect(display,(255,0,0),
                         (self.x+self.b-self.b/3,self.y+self.h/2,self.b/3,self.h/2))

        messageToScreen(self.x+5,self.y+self.h/4,self.num,self.NumFont,self.color_font,self.font).draw()

    def ColPoint(self,x,y,keys):
        if pygame.Rect(self.x+self.b-self.b/3,self.y+1,self.b/3,self.h/2).collidepoint(x,y):
            if keys == (1,0,0) and not self.num +1 > self.num_max:
                self.num += 1

        if pygame.Rect(self.x+self.b-self.b/3,self.y+self.h/2,self.b/3,self.h/2).collidepoint(x,y):
            if keys == (1,0,0) and not self.num -1 < self.num_min:
                self.num -= 1

    def Return(self):
        return self.num


class Line:
    def __init__(self,xstart,ystart,xarrive,yarrive,color=(0,0,0),spessore=1):
        self.xs = xstart
        self.ys = ystart
        self.xa = xarrive
        self.ya = yarrive
        self.color = color
        self.spess = spessore

    def draw(self):
        pygame.draw.line(display,self.color,(self.xs,self.ys),(self.xa,self.ya),self.spess)


class Mouse:
    def __init__(self):
        pass

    def return_pos(self):
        return pygame.mouse.get_pos()

    def return_press(self):
        return pygame.mouse.get_pressed()

    def ReturnPosKey(self):
        return (pygame.mouse.get_pos(),pygame.mouse.get_pressed())

    def Settare(self,x,y,visibile=True):
        pygame.mouse.set_visible(visibile)
        pygame.mouse.set_pos(x,y)


password = []
account = {}
class Password:
    def __init__(self,password):
        self.password = password

    def controllo(self,PASSWORD):
        if PASSWORD == self.password:
            return True
        elif PASSWORD == '' and self.password != '':
            return None
        else:
            return False

    def aggiungi(self):
        password.append(password)


class Account:
    def __init__(self,nome,cognome,data_nascita,email,età):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.email = email
        self.età = età

    def scheda(self):
        return self.nome,self.cognome,self.data_nascita,self.email,self.età

    def aggiungi(self):
        account[self.email] = [self.email,self.nome,self.cognome,self.data_nascita,self.età]

class Sezione:
    def __inin__(self,x,y,b,h,color):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.color = color

    def draw(self):
        pygame.draw.rect(display,self.color,(self.x,self.y,self.b,self.h))


class Square:
    def __init__(self,x,y,b,h,color=(0,0,0),spess=1):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.color = color
        self.spess = spess

    def draw(self):
        pygame.draw.rect(schermo,self.color,(self.x,self.y,self.b,self.h),self.spess)
        
        
class Poligono:
    def __init__(self,coord,color,spess):
        self.coord = coord
        self.color = color
        self.spess = spess

    def draw(self):
        pygame.draw.polygon(display,self.color,self.coord,self.spess)


