# import
import tkinter as tk

# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# VARIABLES
grid = [ [2,0,0,0,0,0,3,3,3,0,0,1],
         [1,1,1,1,1,0,1,0,3,1,1,1],
         [0,0,1,0,0,0,1,0,1,0,0,0],
         [0,0,1,0,0,1,1,0,0,0,0,0],
         [1,1,1,0,0,1,1,1,1,1,0,1],
         [0,0,1,0,0,0,0,0,3,1,0,0],
         [1,1,1,1,1,1,0,1,3,1,0,0],
         [3,3,0,0,0,0,0,1,3,0,0,1],
         [0,1,1,1,1,1,0,0,0,0,1,0],
         [0,0,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,3,3,1,0,1,1,1,1],
         [4,1,1,1,1,1,0,0,0,0,0,0]
         
]

# FUNCTIONS
def drawwall():
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            if grid[col][row]==1:
                canvas.create_rectangle(row*50,(col*50),50+(row*50),50+(col*50),fill="black")
            elif grid[col][row]==2:
                canvas.create_oval(row*50,(col*50),50+(row*50),50+(col*50),fill="pink")
            elif grid[col][row]==3:
                canvas.create_rectangle(row*50,(col*50),50+(row*50),50+(col*50),fill="yellow")
            elif grid[col][row]==4:
                canvas.create_rectangle(row*50,(col*50),50+(row*50),50+(col*50),fill="green")
            else:
                canvas.create_rectangle(row*50,(col*50),50+(row*50),50+(col*50),outline="cyan",fill="cyan")

# position
def PositionOfPlayer(grid) :
    for k in range(len(grid)):
        for j in range(len(grid[k])):
            if grid[k][j]== 2:
                position=[k,j]
    return position

def MoveRight(event):
    global grid
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    if grid[playerrow][playercolumn +1]!=1:
        grid[playerrow][playercolumn ]=0
        grid[playerrow][playercolumn +1]=2
    drawwall()

def MoveLeft(event):
    global grid
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    if grid[playerrow][playercolumn -1]!=1:
        grid[playerrow][playercolumn ]=0
        grid[playerrow][playercolumn -1]=2
    drawwall()

def MoveUp(event):
    global grid
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    if grid[playerrow-1][playercolumn ]!=1:
        grid[playerrow][playercolumn ]=0
        grid[playerrow-1][playercolumn ]=2
    drawwall()

def MoveDown(event):
    global grid
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn  = position[1]
    if grid[playerrow+1][playercolumn ]!=1:
        grid[playerrow][playercolumn ]=0
        grid[playerrow+1][playercolumn ]=2
    drawwall()

    
# main
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))

# Press Key
root.bind("<Left>", MoveLeft)
root.bind("<Right>", MoveRight)  
root.bind("<Up>", MoveUp) 
root.bind("<Down>", MoveDown) 

canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")

drawwall()


root.mainloop()