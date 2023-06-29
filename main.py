from tkinter import *

root = Tk()

root.geometry("500x600")
root.title("Paint")

color = "yellow"
strokeType = StringVar()
strokeType.set("Oval")
stroke = IntVar()
stroke.set(5)

previous_x = 0
previous_y = 0
painting = False

def paint(event):
    global previous_x,previous_y
    global painting

    if(painting==False):
        previous_x=event.x
        previous_y=event.y
    
    
    if(strokeType.get()=="Oval"):
        canvas.create_oval(event.x, event.y, event.x+stroke.get(), event.y+stroke.get(), fill = color, outline = color)
    elif(strokeType.get()=="Outlined"):
        canvas.create_oval(event.x, event.y, event.x+stroke.get(), event.y+stroke.get(), fill = color, outline = "black")   
    elif(strokeType.get()=="Polygon"):
        canvas.create_polygon(previous_x, previous_y, event.x, event.y, fill=color,outline=color, width=stroke.get())
    elif(strokeType.get()=="Line"):
        canvas.create_line(previous_x, previous_y, previous_x+10, previous_y+10, fill=color, width=stroke.get())
    else:
         canvas.create_line(previous_x, previous_y, previous_x+10, previous_y+10, fill=color, width=stroke.get()+20)

    previous_x = event.x
    previous_y = event.y

    painting = True
    if(event.type=="5"):
        painting=False

def changeColor (event):
    global color
    color = event.widget.cget("bg")

def changeStrokeType (event):
    global strokeType
    strokeType.set(event.widget.cget("text"))

def clearAll():
    global canvas
    canvas.delete("all")

canvas = Canvas(width = 400, height = 400, bg = "white", border = 2)
canvas.grid(row= 0, column = 0, columnspan = 8)
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)

strokeScale = Scale(root, from_=5, to=50, variable=stroke, length = 300)
strokeScale.grid(row=0, column=9)

colorLabel = Label(text = "Colors - ", font = ("Arial",12))
colorLabel.grid(row=1, column =0)

redButton = Button(text="Red", bg = "red", height = 2, width = 2)
redButton.grid(row = 1, column = 1)
redButton.bind("<Button-1>", changeColor)

orangeButton = Button(text="Orange", bg = "orange", height = 2, width = 2)
orangeButton.grid(row = 1, column = 2)
orangeButton.bind("<Button-1>", changeColor)

yellowButton = Button(text="Yellow", bg = "yellow", height = 2, width = 2)
yellowButton.grid(row = 1, column = 3)
yellowButton.bind("<Button-1>", changeColor)

greenButton = Button(text="Green", bg = "green", height = 2, width = 2)
greenButton.grid(row = 1, column = 4)
greenButton.bind("<Button-1>", changeColor)

blueButton = Button(text="Blue", bg = "blue", height = 2, width = 2)
blueButton.grid(row = 1, column = 5)
blueButton.bind("<Button-1>", changeColor)

purpleButton = Button(text="Purple", bg = "purple", height = 2, width = 2)
purpleButton.grid(row = 1, column = 6)
purpleButton.bind("<Button-1>", changeColor)

eraserButton = Button(text="Eraser", bg = "white", height = 2, width = 2)
eraserButton.grid(row = 2, column = 1)
eraserButton.bind("<Button-1>", changeColor)

clearButton = Button(text = "Clear", bg="white",height = 2, width = 2, command = clearAll)
clearButton.grid(row=2,column=2)

strokeLabel = Label(text = "Strokes - ", font = ("Arial",12))
strokeLabel.grid(row=3, column =0)

ovalStroke = Button(text = "Oval", bg = "white", height = 2, width = 2)
ovalStroke.grid(row = 3, column = 1)
ovalStroke.bind("<Button-1>", changeStrokeType)

ovalOutlinedStroke = Button(text = "Outlined", bg = "white", height = 2, width = 2)
ovalOutlinedStroke.grid(row = 3, column = 2)
ovalOutlinedStroke.bind("<Button-1>", changeStrokeType)

polygonStroke = Button(text = "Polygon", bg = "white", height = 2, width = 2)
polygonStroke.grid(row = 3, column = 3)
polygonStroke.bind("<Button-1>", changeStrokeType)

lineStroke = Button(text = "Line", bg = "white", height = 2, width = 2)
lineStroke.grid(row = 3, column = 4)
lineStroke.bind("<Button-1>", changeStrokeType)

blockStroke = Button(text = "Block", bg = "white", height = 2, width = 2)
blockStroke.grid(row = 3, column = 5)
blockStroke.bind("<Button-1>", changeStrokeType)


root.mainloop()