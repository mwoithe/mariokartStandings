import tkinter as tk
import time
import team
import player
from standings import Standings
from race import Race
import exceptions as e

def packButtons():
    for i in [0,1,2]:
        for btn in buttons[i]:
            btn.pack()
        frames[i].pack(side="left")

def unpackButtons():
    for i in [0,1,2]:
        for btn in buttons[i]:
            btn.pack_forget()
        frames[i].pack_forget()


def showErrorMessage(message):
    def command():
        warning.pack_forget()
        packButtons()
    
    unpackButtons()

    warning = tk.Button(
        text=message,
        width=50,
        height=10,
        bg="red",
        command=command
    )
    print(message)

    warning.pack()

def showTime(exTime):
    v.set(f"Execution took {exTime*1000} ms")


# Players 
# def overallPlayer():
#     try:
#         start = time.time()
#         stand = Standings()
#         stand.displayIndStandings()
#         end = time.time()
#         showTime(end-start)
#     except e.DataError as failure:
#         showErrorMessage(failure.message)

# def lastPlayer():
#     try:
#         start = time.time()
#         stand = Standings()
#         stand.displayIndStandings(1)
#         end = time.time()
#         showTime(end-start)
#     except e.DataError as failure:
#         showErrorMessage(failure.message)

# def form5Player():
#     try:
#         start = time.time()
#         stand = Standings()
#         stand.displayIndStandings(5)
#         end = time.time()
#         showTime(end-start)
#     except e.DataError as failure:
#         showErrorMessage(failure.message)

# def form10Player():
#     try:
#         start = time.time()
#         stand = Standings()
#         stand.displayIndStandings(10)
#         end = time.time()
#         showTime(end-start)
#     except e.DataError as failure:
#         showErrorMessage(failure.message)

# def form20Player():
#     try:
#         start = time.time()
#         stand = Standings()
#         stand.displayIndStandings(20)
#         end = time.time()
#         showTime(end-start)
#     except e.DataError as failure:
#         showErrorMessage(failure.message)

# # Team buttons
# def overallTeam():
#     try:
#         start = time.time()
#         stand = Standings()
#         stand.displayTeamStandings()
#         end = time.time()
#         showTime(end-start)
#     except e.DataError as failure:
#         showErrorMessage(failure.message)

# def lastTeam():
#     try:
#         start = time.time()
#         stand = Standings()
#         stand.displayTeamStandings(1)
#         end = time.time()
#         showTime(end-start)
#     except e.DataError as failure:
#         showErrorMessage(failure.message)

# def form5Team():
#     try:
#         start = time.time()
#         stand = Standings()
#         stand.displayTeamStandings(5)
#         end = time.time()
#         showTime(end-start)
#     except e.DataError as failure:
#         showErrorMessage(failure.message)

# def form10Team():
#     try:
#         start = time.time()
#         stand = Standings()
#         stand.displayTeamStandings(10)
#         end = time.time()
#         showTime(end-start)
#     except e.DataError as failure:
#         showErrorMessage(failure.message)

# def form20Team():
#     try:
#         start = time.time()
#         stand = Standings()
#         stand.displayTeamStandings(20)
#         end = time.time()
#         showTime(end-start)
#     except e.DataError as failure:
#         showErrorMessage(failure.message)

# Log
def logData():
    try:
        start = time.time()
        Race()
        end = time.time()
        showTime(end-start)
    except e.DataError as failure:
        showErrorMessage(failure.message)
    # r.readData()

def changeTeamColour():
    teamName = input("Which teams colour would you like to change? ")
    if teamName not in team.Team.teamList:
        print(f"WARNING: `{teamName}` is not a registered team.")
        return
    
    colour = input(f"What should {teamName}'s new colour be? ")
    team.Team(teamName, colour=colour.lower())

### button press handlers
form_list = [-1,1,5,10,20]
def refreshDisplay():
    try:
        start = time.time()
        stand = Standings()
        for num in form_list:
            stand.displayTeamStandings(num)
            stand.displayIndStandings(num)
        end = time.time()
        showTime(end-start)
    except e.DataError as failure:
        showErrorMessage(failure.message)


def teamAddPlayer():
    playername = input(f"Which player are you adding to a team? ")

    if playername not in player.Player.playerList:
        print(f"WARNING: `{playername}` is not a registered player.")
        return

    teamName = input(f"Which team should {playername} be in? ")
    if teamName not in team.Team.teamList:
        print(f"WARNING: `{teamName}` is not a registered team.")
        return
    
    team.Team.getTeamByName(teamName).addPlayer(playername)

####


window = tk.Tk()
v = tk.StringVar()
timeMessage = tk.Label(textvariable=v)
timeMessage.pack()

playerFrame = tk.Frame(padx=5, pady=5)
teamFrame = tk.Frame(padx=5, pady=5)
otherFrame = tk.Frame(padx=5, pady=5)

frames = [playerFrame, teamFrame, otherFrame]


pButtonList = []
tButtonList = []
lButtonList = []


# btn_lp = tk.Button(
#     master=playerFrame,
#     text="Last race Player",
#     width=25,
#     height=5,
#     bg="#d7aafa",
#     command=lastPlayer
# )
# pButtonList.append(btn_lp)


# btn_5p = tk.Button(
#     master=playerFrame,
#     text="Last 5 Player Standings",
#     width=25,
#     height=5,
#     bg="#c27cf7",
#     command=form5Player
# )
# pButtonList.append(btn_5p)

# btn_10p = tk.Button(
#     master=playerFrame,
#     text="Last 10 Player Standings",
#     width=25,
#     height=5,
#     bg="#a943f7",
#     command=form10Player
# )
# pButtonList.append(btn_10p)

# btn_20p = tk.Button(
#     master=playerFrame,
#     text="Last 20 Player Standings",
#     width=25,
#     height=5,
#     bg="#8f02fa",
#     command=form20Player
# )
# pButtonList.append(btn_20p)

# btn_op = tk.Button(
#     master=playerFrame,
#     text="Overall Player Standings",
#     width=25,
#     height=5,
#     bg="#6902b8",
#     command=overallPlayer
# )
# pButtonList.append(btn_op)


# btn_lt = tk.Button(
#     master=teamFrame,
#     text="Last race Team",
#     width=25,
#     height=5,
#     bg="#c8fbfb",
#     command=lastTeam
# )
# tButtonList.append(btn_lt)

# btn_5t = tk.Button(
#     master=teamFrame,
#     text="Last 5 Team Standings",
#     width=25,
#     height=5,
#     bg="#96fbfb",
#     command=form5Team
# )
# tButtonList.append(btn_5t)

# btn_10t = tk.Button(
#     master=teamFrame,
#     text="Last 10 Team Standings",
#     width=25,
#     height=5,
#     bg="#48fbfb",
#     command=form10Team
# )
# tButtonList.append(btn_10t)

# btn_20t = tk.Button(
#     master=teamFrame,
#     text="Last 20 Team Standings",
#     width=25,
#     height=5,
#     bg="#00fbfb",
#     command=form20Team
# )
# tButtonList.append(btn_20t)

# btn_ot = tk.Button(
#     master=teamFrame,
#     text="Overall Team Standings",
#     width=25,
#     height=5,
#     bg="#00c8c8",
#     command=overallTeam
# )
# tButtonList.append(btn_ot)

btn_log = tk.Button(
    master=otherFrame,
    text="Log race data",
    width=25,
    height=5,
    bg="#70fa8c",
    command=logData
)
lButtonList.append(btn_log)

btn_ctc = tk.Button(
    master=otherFrame,
    text="Change team colour",
    width=25,
    height=5,
    bg="#70fa8c",
    command=changeTeamColour
)
lButtonList.append(btn_ctc)

btn_refresh = tk.Button(
    master=otherFrame,
    text="Refresh display",
    width=25,
    height=5,
    bg="#70fa8c",
    command=refreshDisplay
)
lButtonList.append(btn_refresh)

btn_addPlayer = tk.Button(
    master=otherFrame,
    text="Add player to team",
    width=25,
    height=5,
    bg="#70fa8c",
    command=teamAddPlayer
)
lButtonList.append(btn_addPlayer)

buttons = [pButtonList, tButtonList, lButtonList]



    


# playerFrame.pack()
# teamFrame.pack(side="left")
# otherFrame.pack(side="left")
packButtons()
window.mainloop()