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
    teamName = input("\n<INPUT REQUEST> Which teams colour would you like to change?\n+ ")
    if teamName not in team.Team.teamList:
        print(f"<WARNING> `{teamName}` is not a registered team.")
        return
    
    colour = input(f"\n<INPUT REQUEST> What should {teamName}'s new colour be?\n+ ")
    team.Team(teamName, colour=colour.lower())

### button press handlers
form_list = [1,5,10,20]
def refreshDisplay():
    try:
        print("<INFO> Refreshing display...")
        start = time.time()
        stand = Standings()
        try:
            for num in form_list:
                stand.displayTeamStandings(num)
                stand.displayIndStandings(num)
        except e.NoDataError as fail:
            print(fail.message)

        # I want the last one called to be overall so the player summaries show that
        stand.displayTeamStandings()
        stand.displayIndStandings()
        end = time.time()
        showTime(end-start)
    except e.DataError as failure:
        showErrorMessage(failure.message)


def teamAddPlayer():
    playername = input(f"\n<INPUT REQUEST> Which player are you adding to a team?\n+ ")

    if playername not in player.Player.playerList:
        print(f"<WARNING> `{playername}` is not a registered player.")
        return

    teamName = input(f"\n<INPUT REQUEST> Which team should {playername} be in?\n+ ")
    if teamName not in team.Team.teamList:
        print(f"<WARNING> `{teamName}` is not a registered team.")
        return
    
    team.Team.getTeamByName(teamName).addPlayer(playername)

def getPlayer():
    playername = input(f"\n<INPUT REQUEST> Which player do you want?\n+ ")
    
    print(f"<INFO> {player.Player.getPlayerByName(playername)}")

def changePlayerAlias():
    playername = input(f"\n<INPUT REQUEST> Which player's name do you want to change?\n+ ")
    person = player.Player.getPlayerByName(playername)
    if person is None:
        print(f"<WARNING> `{playername}` is not a registered player")
        return

    newname = input(f"\n<INPUT REQUEST> What would you like to change `{playername}`'s name to? \n+ ")

    person.changeName(newname)




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

btn_getPlayer = tk.Button(
    master=otherFrame,
    text="Get player",
    width=25,
    height=5,
    bg="#70fa8c",
    command=getPlayer
)
lButtonList.append(btn_getPlayer)

btn_changeName = tk.Button(
    master=otherFrame,
    text="Change player name",
    width=25,
    height=5,
    bg="#70fa8c",
    command=changePlayerAlias
)
lButtonList.append(btn_changeName)

buttons = [pButtonList, tButtonList, lButtonList]



    


# playerFrame.pack()
# teamFrame.pack(side="left")
# otherFrame.pack(side="left")
packButtons()
window.mainloop()