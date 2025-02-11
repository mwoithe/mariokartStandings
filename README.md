# Mariokart standings

## Intro
Hi, welcome to my app. It is very epic.




## How to use
To start a new tournament, delete all files from the `/players/`, `/races/` and `/teams/` folders within the `/data/` folder.
1. Open the `init` folder. In there there should be two files
    - If there are three files, delete the `init` file. (This is an empty file used only by the program to determine whether initialisation has been done.)
    - In `players.txt`, list the names of all players, with each player name on a separate line. (NOTE: names cannot have `,` characters, and there shouldn't be a trailing newline)
    - In `teams.txt`, list the names of all teams, in the same way as the players. Save and close both files.

2. Run `main.py`. All data storage and display files will be created programatically, and the gui will open.
    - Files in the `/init/` must not be changed after `main.py` has been run. If a mistake has been made, reset and start again.
    - Open as many of the display files in `data/standings/` as desired in a web browser. 

3. Open the `/data/resultInput.txt` file in a text editor, and input race results as they happen. Once finished each one, hit the "Log race data" button, and the result will be written. Bob may well be your uncle.

All other actions are completed using the buttons in the gui.

### Log race data
Checks and logs the input data in the `resultInput.txt`. If there are errors present, both the gui and terminal will display the reason, and the write will not procede. If all checks pass, the terminal will prompt for confirmation. Type 'yes' in the terminal to confirm, and the write will take place. Any other input will cancel the write. Writing does not update displays.

### Change team colour
Terminal will prompt for the name of a team who's colour should be changed (case sensitive). If the team name provided is valid, the terminal will prompt for a colour (not case sensitive). If a valid colour is provided, the team's colour will be changed. The displays are not updated by this command.

### Refresh display
Updates all displays (players, teams, overall and form). All scores, team colours and team allocations are updated in the display files.

### Add player to team
Prompts for a player name. If a player is found with the name (or alias), then the terminal will ask for a team to add the player to. If the teamname provided is valid and the player is not already in a team, the player will be added to the team. If the player is already in a team, the terminal will ask for confirmation that the player is to be removed from their current team, and added to the new team. Input 'yes' to procede, all other input will cancel.

### Get player
Prompts for a player name. If a player is found with the given name (or alias), a summary of the player will be shown, including name, current alias and overall statistics.

### Change player name
Prompts for a player name. If a player is found with the given name (or alias), the terminal will prompt for a new name to give the player. If the name doesn't already belong to another player, the given player's alias will be changed.


## Features

### Names
All players have a `name` attribute. In the code, the name has two parts: `name` and `current`. The `name` is the name in the `/init/players.txt` file, and is used as the name of the player's data file. The `name` cannot be changed. However, the player can also be referred to using it's `current` alias. The alias can be changed during program use to suit whatever need may arise. The alias the player is under is logged for each race in the player data file. What this means in practice is if you want a player to have it's `name` as the person's name, but you want to be able to refer to them by their in-game name, then you change their alias to their in-game name. 

Currently, the name displayed is the `name`. However, this is rather straight forward to change if desired. In `player.py` line 181 (in function `getPlayerBar()`), change `{self.name.get_name()}` to `{self.name.get_current()} `, and you're cooking.


### Colours
Each team has a colour that will be used in the displays. The players in a team take the colour of their team. A team's colour can be changed by either changing the `colour=<colour>` line of the team data file, or using the "Change team colour" button (recommended). Currently, there is no designed way to have the players in the player standings use different colours to their respective teams, unless teams are not being used, in which case just create a separate team for each player and allocate colours that way.

The colours currently available are:

- blue
- green
- grey
- lime
- orange
- pink
- purple
- red
- sky
- yellow


### Closing/reopening
While writing absolutely everything to files may seem excessive, it means that if execution of the program stops (error (although there shouldn't be too many of those left), taking a break, unexpected restart, etc.) it can be restarted by running `main.py` again, and the program will reload data into memory and you can resume use as if nothing happened. [Theoretically, it also means that if the data, init and src folders are copied onto another computer (with python installed), the change of machine will not affect the use of the program. But don't quote me on that, it hasn't been tested.]

## Tips
- Open the display files in a web browser or other program that periodically refreshes automatically. Saves the user a bit of time.

- If the gui is closed during operation, run `main.py` again to reload the data into memory and reopen the gui. As long as the files in the `/init/` folder haven't been changed (i.e. `init.txt` exists, and the names in `teams.txt` and `players.txt` remain the same), no files/data will be changed or removed by the program.

- I did this on windows. If your on a mac, and s*** hits the fan, I'm sorry, I can't help you.




