import tkinter as tk
from standings import Standings
from race import Race

### button press handlers

def overallPlayer():
    stand = Standings()
    stand.displayIndStandings()

def overallTeam():
    stand = Standings()
    stand.displayTeamStandings()

def form5Player():
    stand = Standings()
    stand.displayIndStandings(5)

def form5Team():
    stand = Standings()
    stand.displayTeamStandings(5)

def checkData():
    r = Race()
    r.checkData()

def logData():
    r = Race()
    r.readData()

####


window = tk.Tk()
greeting = tk.Label(text="Good ebening")
greeting.pack()


btn_op = tk.Button(
    text="Overall Player Standings",
    width=25,
    height=5,
    bg="blue",
    command=overallPlayer
)

btn_ot = tk.Button(
    text="Overall Team Standings",
    width=25,
    height=5,
    bg="red",
    command=overallTeam
)

btn_fp = tk.Button(
    text="Last 5 Player Standings",
    width=25,
    height=5,
    bg="yellow",
    command=form5Player
)

btn_ft = tk.Button(
    text="Last 5 Team Standings",
    width=25,
    height=5,
    bg="green",
    command=form5Team
)

btn_cd = tk.Button(
    text="Check race input data",
    width=25,
    height=5,
    bg="purple",
    command=checkData
)

btn_ld = tk.Button(
    text="Log race data",
    width=25,
    height=5,
    bg="pink",
    command=logData
)

btn_op.pack()
btn_ot.pack()
btn_fp.pack()
btn_ft.pack()
btn_cd.pack()
btn_ld.pack()

window.mainloop()