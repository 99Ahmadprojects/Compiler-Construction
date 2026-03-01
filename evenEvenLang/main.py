import tkinter as tk
from tkinter import messagebox
import math

States = ['q0','q1','q2','q3']
START = "q0"
finalStates = {"q0"}

delta = {

    ("q0","a"):"q1",
    ("q0","b"):"q2",

    ("q1","a"):"q0",
    ("q1","b"):"q3",

    ("q2","a"):"q3",
    ("q2","b"):"q0",

    ("q3","a"):"q2",
    ("q3","b"):"q1"
}

root = tk.Tk()
root.title("EVEN-EVEN DFA Simulator")
root.geometry("850x850")
root.configure(bg="#eaf4ff")

title = tk.Label(

    root,
    text="DFA Simulator: EVEN EVEN Language",
    font=("Segoe UI",18,"bold"),
    bg="#eaf4ff"
)

title.pack(pady=10)
cv = tk.Canvas(

    root,
    width=780,
    height=550,
    bg="white",
    highlightthickness=2,
    highlightbackground="#4a90e2"

)

cv.pack(pady=10)



coords={

    "q0":(390,70),
    "q1":(170,210),
    "q2":(610,210),
    "q3":(390,350)

}


R=38
circles={}



def drawState(name,x,y):

    c = cv.create_oval(

        x-R,y-R,
        x+R,y+R,
        width=2,
        outline="#2c3e50"

    )

    cv.create_text(

        x,y,
        text=name,
        font=("Segoe UI",13,"bold")

    )


    if name in finalStates:

        cv.create_oval(

            x-R+6,y-R+6,
            x+R-6,y+R-6,
            width=2

        )

    circles[name]=c
def arrow(x1,y1,x2,y2,label):

    ang = math.atan2(y2-y1,x2-x1)

    sx=x1+R*math.cos(ang)
    sy=y1+R*math.sin(ang)

    ex=x2-R*math.cos(ang)
    ey=y2-R*math.sin(ang)

    cv.create_line(

        sx,sy,ex,ey,
        arrow=tk.LAST,
        width=2,
        fill="#34495e"

    )

    cv.create_text(

        (sx+ex)/2,
        (sy+ey)/2-12,
        text=label,
        font=("Segoe UI",11,"bold"),
        fill="#1f618d"

    )

def mark(state):

    for s in circles:

        cv.itemconfig(

            circles[s],
            outline="#2c3e50",
            width=2

        )

    cv.itemconfig(

        circles[state],
        outline="red",
        width=5

    )

for st,(x,y) in coords.items():

    drawState(st,x,y)

arrow(*coords["q0"],*coords["q1"],"a")
arrow(*coords["q0"],*coords["q2"],"b")

arrow(*coords["q1"],*coords["q0"],"a")
arrow(*coords["q1"],*coords["q3"],"b")

arrow(*coords["q2"],*coords["q3"],"a")
arrow(*coords["q2"],*coords["q0"],"b")

arrow(*coords["q3"],*coords["q2"],"a")
arrow(*coords["q3"],*coords["q1"],"b")

controlFrame = tk.Frame(root,bg="#eaf4ff")

controlFrame.pack(pady=8)

tk.Label(

    controlFrame,
    text="Input String (a,b only):",
    font=("Segoe UI",12,"bold"),
    bg="#eaf4ff"

).grid(row=0,column=0,padx=6)

entry = tk.Entry(

    controlFrame,
    font=("Segoe UI",14),
    width=22,
    justify="center"

)

entry.grid(row=0,column=1,padx=6)

status = tk.Label(

    root,
    text="",
    font=("Segoe UI",12),
    bg="#eaf4ff"

)

status.pack()


result = tk.Label(

    root,
    text="",
    font=("Segoe UI",15,"bold"),
    bg="#eaf4ff"

)

result.pack(pady=5)
inp=""
idx=0
current=START
def start():

    global inp,idx,current

    inp = entry.get().strip()

    if inp == "":

        messagebox.showwarning(

            "Input Required",
            "Please enter a string"
        )

        return
    for ch in inp:

        if ch not in ("a","b"):

            messagebox.showerror(

                "Invalid Input",
                "Alphabet must be {a , b}"

            )
            return

    idx=0
    current=START
    mark(current)
    status.config(

        text="Simulation Started at q0"
    )
    result.config(text="")
def step():

    global idx,current
    if inp == "":

        return
    if idx >= len(inp):

        if current in finalStates:

            result.config(

                text=" ACCEPTED (Even a , Even b)",
                fg="green"
            )

        else:

            result.config(

                text=" REJECTED",
                fg="red"
            )

        status.config(

            text="Input Finished"
        )
        return
    sym = inp[idx]

    current = delta[(current,sym)]

    idx += 1
    mark(current)

    status.config(

        text=f"Read '{sym}' → Current State : {current}"

    )
def reset():

    entry.delete(0,tk.END)

    status.config(text="")

    result.config(text="")

    mark("q0")

btnFrame = tk.Frame(root,bg="#eaf4ff")

btnFrame.pack(pady=10)
tk.Button(

    btnFrame,
    text="Start Simulation",
    width=18,
    font=("Segoe UI",11,"bold"),
    bg="#4CAF50",
    fg="white",
    command=start

).grid(row=0,column=0,padx=8)
tk.Button(

    btnFrame,
    text="Next Step",
    width=18,
    font=("Segoe UI",11,"bold"),
    bg="#2196F3",
    fg="white",
    command=step

).grid(row=0,column=1,padx=8)
tk.Button(

    btnFrame,
    text="Reset",
    width=18,
    font=("Segoe UI",11,"bold"),
    bg="#e74c3c",
    fg="white",
    command=reset

).grid(row=0,column=2,padx=8)
mark("q0")
root.mainloop()