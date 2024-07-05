import tkinter as tk
from standings import Standings
from race import Race
import exceptions as e

def showErrorMessage(message):
    def command():
        warning.pack_forget()
        for btn in buttonList:
            btn.pack()
    
    for btn in buttonList:
            btn.pack_forget()

    warning = tk.Button(
        text=message,
        width=50,
        height=10,
        bg="red",
        command=command
    )

    warning.pack()

### button press handlers
def overallPlayer():
    try:
        stand = Standings()
        stand.displayIndStandings()
    except e.DataError as failure:
        showErrorMessage(failure.message)


def overallTeam():
    try:
        stand = Standings()
        stand.displayTeamStandings()
    except e.DataError as failure:
        showErrorMessage(failure.message)

def form5Player():
    try:
        stand = Standings()
        stand.displayIndStandings(5)
    except e.DataError as failure:
        showErrorMessage(failure.message)

def form5Team():
    try:
        stand = Standings()
        stand.displayTeamStandings(5)
    except e.DataError as failure:
        showErrorMessage(failure.message)

# def checkData():
#     r = Race()
#     r.checkData()

def logData():
    try:
        Race()
    except e.DataError as failure:
        showErrorMessage(failure.message)
    # r.readData()

####


window = tk.Tk()
greeting = tk.Label(text="Good ebening")
greeting.pack()


btn_op = tk.Button(
    text="Overall Player Standings",
    width=25,
    height=5,
    bg="grey",
    command=overallPlayer
)

btn_ot = tk.Button(
    text="Overall Team Standings",
    width=25,
    height=5,
    bg="grey",
    command=overallTeam
)

btn_fp = tk.Button(
    text="Last 5 Player Standings",
    width=25,
    height=5,
    bg="grey",
    command=form5Player
)

btn_ft = tk.Button(
    text="Last 5 Team Standings",
    width=25,
    height=5,
    bg="grey",
    command=form5Team
)

btn_ld = tk.Button(
    text="Log race data",
    width=25,
    height=5,
    bg="yellow",
    command=logData
)

buttonList = [btn_op, btn_ot, btn_fp, btn_ft, btn_ld]
for btn in buttonList:
    btn.pack()

window.mainloop()