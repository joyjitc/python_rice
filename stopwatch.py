# "Stopwatch: The Game"
import simpleguitk as simplegui

global dsec 
dsec = 0

global status
status = False

global x,y
x=y=0

def format():
    global D
    D = dsec%10
    BC= (dsec//10)%60
    A = (dsec//10)//60 
    if BC<10:
        return str(A)+':'+'0'+str(BC)+'.'+str(D)
    else:
        return str(A)+':'+str(BC)+'.'+str(D)
    
def increment():
    global dsec 
    dsec+=1

def start():
    timer.start()
    global status
    status = True
    
def stop():
    timer.stop()
    global D
    global x,y
    global status
    if status==True:
        y+=1
        if D==0:
            x+=1
        status= False

    

def reset():
    global dsec
    global x,y
    global status
    x=y=0
    status= False
    timer.stop()
    dsec=0
    
    
def draw(canvas):
    canvas.draw_text(format(), [80,120], 60, "Red")
    canvas.draw_text(str(x)+'/'+str(y), [220,50], 40, "Green")

    
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset", reset,100)

frame.set_draw_handler(draw)

timer = simplegui.create_timer(100,increment)

frame.start()

