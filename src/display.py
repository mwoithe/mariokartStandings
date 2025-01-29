

# global settings
class Display:

    __settings = {
        "num_teams": 4,
        "num_players" : 12
    }

    @classmethod
    def set_num_teams(cls, num):
        cls.__settings["num_teams"] = num
        cls.update_style()
        
    @classmethod
    def set_num_players(cls, num):
        cls.__settings["num_players"] = num
        cls.update_style()

    @classmethod
    def update_style(cls):
        # calculations
        player_row_height = round(100/(cls.__settings["num_players"]+1), 2) -0.7
         # the percentage of the screen taken by the num_players + header bars, minus a bit to account for margins (so we don't have to scroll)
        player_row_text = 0.6*player_row_height
        player_row_pad_y = 0.2*player_row_height

        team_row_height = round(100/(cls.__settings["num_teams"]+1), 2) -1
        team_row_text = 0.34*team_row_height
        team_row_pad_y = 0.33*team_row_height

        team_row = """.team-row {
    display: flex;
    flex-wrap: wrap;
    margin: 0.5vh 1vw;
    border-radius: 1vw;
    justify-content: center;
    text-align: center;
    vertical-align: middle;
    line-height: 1;
    height: """ + str(team_row_height) + """vh;
    font-size: """ + str(team_row_text) + """vh;
    padding: """ + str(team_row_pad_y) + """vh;\n}\n\n"""

        # player_height = f"""height: {round(90/(cls.__settings["num_players"]), 2)}vh;\n"""

        player_row = """.player-row {
    display: flex;
    flex-wrap: wrap;
    margin: 0.5vh 1vw;
    border-radius: 1vw;
    justify-content: center;
    text-align: center;
    vertical-align: middle;
    line-height: 1;
    height: """ + str(player_row_height) + """vh;
    font-size: """ + str(player_row_text) + """vh;
    padding: """ + str(player_row_pad_y) + """vh;\n}\n\n"""

        # print(team_row)

        file = open("mariokartStandings/data/standings/display.css", "w")
        file.write(team_row)
        file.write(player_row)
        file.close()

Display.update_style()