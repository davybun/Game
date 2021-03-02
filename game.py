# import
import tkinter as tk

# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# main
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")
root.title('Game')

# Add images
Robot= tk.PhotoImage(file='image\\robot.png')
Coin= tk.PhotoImage(file='image\\coin.png')
Home= tk.PhotoImage(file='image\\home.png')
wall= tk.PhotoImage(file='image\\wall.png')

# VARIABLES
grid = [ [2,0,0,0,0,0,0,0,0,0,3,1],
         [1,1,1,1,1,0,1,0,3,1,1,1],
         [0,0,1,0,0,0,1,0,1,0,0,0],
         [0,0,1,0,3,1,1,0,0,0,0,3],
         [1,1,1,0,3,1,1,1,1,1,0,1],
         [0,0,1,0,0,0,0,0,3,1,0,0],
         [1,1,0,1,1,1,0,1,3,1,0,3],
         [3,3,0,0,0,0,0,1,3,0,3,1],
         [0,1,1,1,1,1,0,0,0,0,1,0],
         [0,0,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,3,3,1,0,1,1,1,1],
         [4,1,1,1,1,1,0,0,0,0,3,3]
         
]

# FUNCTIONS
def drawwall():
    global Robot,Coin,Home,wall
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            X=row*50
            Y=col*50
            if grid[col][row]==1:
                
                canvas.create_image(X+25,Y+27, image=wall)
            elif grid[col][row]==2:
                
                canvas.create_image(X+20,Y+25, image=Robot)
            elif grid[col][row]==3:
                
                canvas.create_image(X+25,Y+27, image=Coin)
            elif grid[col][row]==4:
                
                canvas.create_image(X+25,Y+27, image=Home)
              
            else:
                canvas.create_rectangle(row*50,(col*50),50+(row*50),50+(col*50),outline="white",fill="white")


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

    

# Press Key
root.bind("<Left>", MoveLeft)
root.bind("<Right>", MoveRight)  
root.bind("<Up>", MoveUp) 
root.bind("<Down>", MoveDown) 

drawwall()
# display
root.mainloop()