# from team import Team
# from player import Player
import team as t
import player as p
# import time

class Standings:
    def __init__(self):
        self.end = """
    </article>
</body>
"""

    def displayTeamStandings(self, form=-1):
        teams = []
        for name in t.Team.teamList:
            teams.append(t.Team(name, form))
        
        teams.sort(reverse=True)
        message = "\tTeam\tPoints\tWins\tPodiums\tSpoons\n"
        html, tail = self.get_html_head("Team", form)

        pos = 1
        for team in teams:
            html += team.getTeamBar(pos)
            message += f"{pos}\t{team.name}\t{team.points}\t{team.wins}\t{team.podiums}\t{team.spoons}\n"
            pos += 1
        
        html += tail

        filename = "mariokartStandings/data/standings/team_"
        if form == -1:
            filename += "overall.html"
        else:
            filename += f"form_{form}.html"

        h = open(filename, "w")
        h.write(html)
        h.close()

        f = open("mariokartStandings/data/standings/standings.txt", "w")
        f.write(message)
        f.close()

    def displayIndStandings(self, form=-1):
        # Yeah, I know this is scuffed but otherwise I can't get the colours
        teams = []
        for name in t.Team.teamList:
            teams.append(t.Team(name, form))


        # Store the player instances, because these can be compared easily 
        players = []
        for name in p.Player.playerList:
            players.append(p.Player(name, form))

        players.sort(reverse=True)
        message = "\tPlayer\tPoints\tWins\tPodiums\tSpoons\n"
        html, tail = self.get_html_head("Player", form)

        pos = 1
        for player in players:
            html += player.getPlayerBar(pos)
            message += f"{pos}\t{player.name}\t{player.points}\t{player.wins}\t{player.podiums}\t{player.spoons}\n"
            pos += 1
        
        html += tail

        filename = "mariokartStandings/data/standings/player_"
        if form == -1:
            filename += "overall.html"
        else:
            filename += f"form_{form}.html"

        h = open(filename, "w")
        h.write(html)
        h.close()

        f = open("mariokartStandings/data/standings.txt", "w")
        f.write(message)
        f.close()



    def get_html_head(self, type, form):
        if form == -1:
            form = "Overall"
        else:
            form = f"Last {form}"


        head = f"""<!doctype html>
<head>
    <title>{type} - {form}</title>

    <meta charset="utf-8">
    <link rel="stylesheet" href="display.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
    <article>
        <div class="{type.lower()}-row {type.lower()}-header">
            <div class="col-1 row-col">
                
            </div>
            <div class="col-3 row-col">
                Player
            </div>
            <div class="col-2 row-col">
                Points
            </div>
            <div class="col-2 row-col">
                Wins
            </div>
            <div class="col-2 row-col">
                Podiums
            </div>
            <div class="col-2 row-col">
                Spoons
            </div>
        </div>
        """

        tail = f"""
    </article>
    <div class="side-bar">{type} - {form}</div>
</body>"""
        return head, tail
    
    # def get_html_tail(self, type, form)




    # def write_html(self, )
        
s=Standings()
s.displayIndStandings()
s.displayTeamStandings()