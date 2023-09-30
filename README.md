# NBA Player Movements

This is a script for visualization of NBA games using raw logs from the NBA SportVU dataset, which contains player and ball movement throughout NBA games. By running only a single command from the command line, you are able to view the entirety of players positioning throughout any NBA SportVU json file.

Whether you admire both the Spurs' and Warriors' ball movement, Erik Spoelstra's playbook, or just miss KD and Russ in OKC, you'll find this entertaining.

As each game progresses, you can track the movement of each player currently on the court, with the names of all players printed on the screen. You can also see the location of the ball and both the game and shot clocks. This low-CPU visualization helps everyone simply study ball and player movements, and where your favorite team's potential weaknesses lie.

## Examples

![Spurs](https://github.com/linouk23/NBA-Player-Movements/blob/master/examples/spurs.gif)
![Warriors](https://github.com/linouk23/NBA-Player-Movements/blob/master/examples/warriors.gif)
![Celtics](https://github.com/linouk23/NBA-Player-Movements/blob/master/examples/celtics.gif)
![Durant](https://github.com/linouk23/NBA-Player-Movements/blob/master/examples/durant.gif)

## Usage

1. Clone this repo using the following link:

  ```bash
  $ git clone https://github.com/linouk23/NBA-Player-Movements
  ```

2. Choose any NBA game from ```data/2016.NBA.Raw.SportVU.Game.Logs``` directory. Note: At the moment, only games from 2016 are included, but more seasons can be added as needed. (If any contributors would be willing to add games from 2017-present, it would be greatly appreciated.)

3. The program takes two parameters:
   required arguments:
    --path PATH
   a path any json file leading to a SportVU file. You can find examples in the "data/2016.NBA.Raw.SportVU.Game.Logs" directory, or you import them yourself. 
   ex.
   ```bash
   --path=Celtics@Lakers.json
   ```
   optional arguments:
    --event EVENT
   This flag allows you to choose which play to start on. This allows you to skip to different portions of the game, or allows you to see a genius inbounds play drawn up by Steve Kerr. For example, if you wanted to skip to the 10th play of the game, you would enter 9, as in the following example:
    ```bash
    $ python3 main.py --path=Celtics@Lakers.json --event=9
    ```
    -h, --help
   This flag prints information displays a general help menu of how to operate the program, and is also where you go to exit the program (although you can use Ctrl+C to terminate the program as well).

## Contributions
This project has not been updated recently, and as software has changed regarding more advanced ways to track player movement and more advanced techniques have been created, additional contributions are highly encouraged. If anyone interested in AI visualizations would be interested in adding more advanced graphics, that would be greatly appreciated as well.
