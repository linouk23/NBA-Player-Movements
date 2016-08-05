from Constant import Constant
from Moment import Moment
from Team import Team
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle, Rectangle, Arc


class Event:
    """A class for handling and showing events"""

    def __init__(self, event):
        moments = event['moments']
        self.moments = [Moment(moment) for moment in moments]
        home_players = event['home']['players']
        guest_players = event['visitor']['players']
        players = home_players + guest_players
        player_ids = [player['playerid'] for player in players]
        player_names = [" ".join([player['firstname'],
                        player['lastname']]) for player in players]
        player_jerseys = [player['jersey'] for player in players]
        values = list(zip(player_names, player_jerseys))
        # Example: 101108: ['Chris Paul', '3']
        self.player_ids_dict = dict(zip(player_ids, values))

    def update_radius(self, i, player_circles, ball_circle, annotations, clock_info):
        moment = self.moments[i]
        for j, circle in enumerate(player_circles):
            circle.center = moment.players[j].x, moment.players[j].y
            annotations[j].set_position(circle.center)
            clock_test = 'Quarter {:d}\n {:02d}:{:02d}\n {:03.1f}'.format(
                         moment.quarter,
                         int(moment.game_clock) % 3600 // 60,
                         int(moment.game_clock) % 60,
                         moment.shot_clock)
            clock_info.set_text(clock_test)
        ball_circle.center = moment.ball.x, moment.ball.y
        ball_circle.radius = moment.ball.radius / Constant.NORMALIZATION_COEF
        return player_circles, ball_circle

    def show(self):
        # Leave some space for inbound passes
        ax = plt.axes(xlim=(Constant.X_MIN,
                            Constant.X_MAX),
                      ylim=(Constant.Y_MIN,
                            Constant.Y_MAX))
        ax.axis('off')
        fig = plt.gcf()
        ax.grid(False)  # Remove grid
        start_moment = self.moments[0]
        player_dict = self.player_ids_dict

        clock_info = ax.annotate('', xy=[Constant.X_CENTER, Constant.Y_CENTER],
                                 color='black', horizontalalignment='center',
                                   verticalalignment='center')

        annotations = [ax.annotate(self.player_ids_dict[player.id][1], xy=[0, 0], color='w',
                                   horizontalalignment='center',
                                   verticalalignment='center', fontweight='bold')
                       for player in start_moment.players]

        # Prepare table
        sorted_players = sorted(start_moment.players, key=lambda player: player.team.id)
        
        home_player = sorted_players[0]
        guest_player = sorted_players[5]
        column_labels = tuple([home_player.team.name, guest_player.team.name])
        column_colours = tuple([home_player.team.color, guest_player.team.color])
        cell_colours = [column_colours for _ in range(5)]
        
        home_players = [' #'.join([player_dict[player.id][0], player_dict[player.id][1]]) for player in sorted_players[:5]]
        guest_players = [' #'.join([player_dict[player.id][0], player_dict[player.id][1]]) for player in sorted_players[5:]]
        players_data = list(zip(home_players, guest_players))

        table = plt.table(cellText=players_data,
                              colLabels=column_labels,
                              colColours=column_colours,
                              colWidths=[Constant.COL_WIDTH, Constant.COL_WIDTH],
                              loc='bottom',
                              cellColours=cell_colours,
                              fontsize=Constant.FONTSIZE,
                              cellLoc='center')
        table.scale(1, Constant.SCALE)
        table_cells = table.properties()['child_artists']
        for cell in table_cells:
            cell._text.set_color('white')

        player_circles = [plt.Circle((0, 0), Constant.PLAYER_CIRCLE_SIZE, color=player.color)
                          for player in start_moment.players]
        ball_circle = plt.Circle((0, 0), Constant.PLAYER_CIRCLE_SIZE,
                                 color=start_moment.ball.color)
        for circle in player_circles:
            ax.add_patch(circle)
        ax.add_patch(ball_circle)

        anim = animation.FuncAnimation(
                         fig, self.update_radius,
                         fargs=(player_circles, ball_circle, annotations, clock_info),
                         frames=len(self.moments), interval=Constant.INTERVAL)
        court = plt.imread("court.png")
        plt.imshow(court, zorder=0, extent=[Constant.X_MIN, Constant.X_MAX - Constant.DIFF,
                                            Constant.Y_MAX, Constant.Y_MIN])
        plt.show()
