# import
import tkinter as tk
from tkinter import messagebox
import winsound

# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# main
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")
root.title('Labyrinth Game')

# Add images
Robot= tk.PhotoImage(file='image\\robot.png')
Coin= tk.PhotoImage(file='image\\coin.png')
Home= tk.PhotoImage(file='image\\home.png')
wall= tk.PhotoImage(file='image\\wall.png')
monster= tk.PhotoImage(file='image\\monster.png')

        
# VARIABLES
grid = [ [0,0,0,0,0,0,0,0,0,0,0,0],
         [2,0,0,0,1,1,1,1,1,1,1,1],
         [1,1,1,0,0,0,0,0,1,0,0,0],
         [0,5,1,1,0,1,1,0,0,0,3,3],
         [1,1,1,5,0,1,1,1,1,1,0,1],
         [0,0,1,1,0,0,0,0,3,1,0,0],
         [1,1,0,1,1,1,0,1,5,1,0,0],
         [3,3,0,0,0,0,0,1,3,0,0,1],
         [0,1,1,1,1,1,0,1,1,0,1,0],
         [0,0,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,3,3,1,0,1,1,1,1],
         [4,1,1,1,1,1,0,0,0,0,3,3]
    ]
FindContition=0
Score=0
# FUNCTIONS
def drawwall():
    global Robot,Coin,Home,wall,Score
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
            elif grid[col][row]==5:
                canvas.create_image(X+25,Y+27, image=monster)
            else:
                canvas.create_rectangle(row*50,(col*50),50+(row*50),50+(col*50),outline="white",fill="white")
                canvas.create_text(300,20,fill="black",font="Times 16 italic bold",text="Score: "+str(Score))


# position
def PositionOfPlayer(grid) :
        for col in range(len(grid)):
            for row in range(len(grid[col])):
                if grid[col][row]== 2:
                    position=[col,row]
        return position
1   
def MoveRight(event):
        global grid,FindContition,Score
        position = PositionOfPlayer(grid)
        playerrow = position[0]
        playercolumn = position[1]
        if grid[playerrow][playercolumn +1]!=1:
            FindContition=grid[playerrow][playercolumn +1]
            grid[playerrow][playercolumn ]=0
            grid[playerrow][playercolumn +1]=2
        if FindContition==3:
            Score +=5
            winsound.PlaySound("sound\\coin.wav", winsound.SND_LOOP)
        elif FindContition==4:
            messagebox.showinfo("SUCCESS", "You win !")
        elif FindContition==5:
            messagebox.showinfo("LOSS", "you loss !")
        drawwall()

def MoveLeft(event):
        global grid,FindContition,Score
        position = PositionOfPlayer(grid)
        playerrow = position[0]
        playercolumn = position[1]
        if grid[playerrow][playercolumn -1]!=1:
            FindContition=grid[playerrow][playercolumn -1]
            grid[playerrow][playercolumn ]=0
            grid[playerrow][playercolumn -1]=2
        if FindContition==3:
            Score +=5
            winsound.PlaySound("sound\\coin.wav", winsound.SND_LOOP)
        elif FindContition==4:
            messagebox.showinfo("SUCCESS", "You win !")
        elif FindContition==5:
            messagebox.showinfo("LOSS", "you loss !")
        drawwall()

def MoveUp(event):
        global grid,FindContition,Score
        position = PositionOfPlayer(grid)
        playerrow = position[0]
        playercolumn = position[1]
        if grid[playerrow-1][playercolumn ]!=1:
            FindContition=grid[playerrow-1][playercolumn ]
            grid[playerrow][playercolumn ]=0
            grid[playerrow-1][playercolumn ]=2
        if FindContition==3:
            Score +=5
            winsound.PlaySound("sound\\coin.wav", winsound.SND_LOOP)
        elif FindContition==4:
            messagebox.showinfo("SUCCESS", "You win !")
        elif FindContition==5:
            messagebox.showinfo("LOSS", "you loss !")
        drawwall()
def MoveDown(event):
        global grid,FindContition,Score
        position = PositionOfPlayer(grid)
        playerrow = position[0]
        playercolumn  = position[1]
        if grid[playerrow+1][playercolumn ]!=1:
            FindContition=grid[playerrow+1][playercolumn ]
            grid[playerrow][playercolumn ]=0
            grid[playerrow+1][playercolumn ]=2
        if FindContition==3:
            Score +=5
            winsound.PlaySound("sound\\coin.wav", winsound.SND_LOOP)
        elif FindContition==4:
            messagebox.showinfo("SUCCESS", "You win !")
        elif FindContition==5:
            messagebox.showinfo("LOSS", "you loss !")
        drawwall()



# PreesKey
root.bind("<Left>", MoveLeft)
root.bind("<Right>", MoveRight)  
root.bind("<Up>", MoveUp) 
root.bind("<Down>", MoveDown) 
drawwall()

# Display
root.mainloop()