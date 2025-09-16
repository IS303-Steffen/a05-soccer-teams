#### Assignment 5
# Soccer Teams
You’ll be writing a python program that asks the user to enter a home soccer team and the number of games they’ll play in a season. It will then ask about the teams they play against and randomly generate scores for games they play. It will then display information about the home team’s wins, losses, and overall performance

Put your code in the `a05_soccer_teams.py` file. Do not edit or delete any other files.

## Libraries Required
- `import random`

## Logical Flow
- Prompt the user:
    - `Enter the name of your home team: `
- Then, prompt the user:
    - `Enter the number of games that <home team name>  will play: `
    - You can assume the user will enter a valid integer, you don't need enter checks for invalid input.
    - Tip: When first testing your code, keep the number of games low (like 2) so it is quicker to run through.

### For each game you home team will play:
- Ask the name of the away team (e.g. “Utah State”) and include which number 
game this will be for.
  - `Enter the name of the away team for game <game number>: `
  - e.g. for the first game your team plays it should say:
    - `Enter the name of the away team for game 1: `
- After entering in the away team name, randomly generate scores between 0 and 3 (inclusive) for the home team and the away team.
    - Look up the `random` library in python if you don't know how to do this.
    - However, you CANNOT have tie scores.
      - You must either keep generating new scores until there isn't a tie, or figure out a way to never generate the same score for both teams in the first place. 
- Keep track of the number of wins / losses of your home team however you want.
  - If the home team score is higher than the away team, that is a win. If it is lower, that is a loss.
  - You just need to be able to print the total wins and losses in the end of your code, as well as use that information to display a specific message.
- You also need to keep track of the names of teams that your team won against and lost against in a dictionary. You dictionary will have two keys: `"Won Against"` and `"Lost Against"`. Both keys will have lists as their values.
    - If the home team won, store the name of the away team in the list associated with the `"Won Against"` key.
    - If the home team lost, store the name of the away team in the list associated with the `"Lost Against"` key.
    - The exact way you code this is up to you, but the automated tests will be specifically looking for a dictionary with 2 keys called `"Won Against"` and `"Lost Against"` with lists as their values, so you must store them this way to get credit. The keys must be spelled correctly and capitalized for the test to find them.
- Print out the name of the home team’s name and their score, as well as the away team’s name and their score like this:
    - `<home team name>'s score: <home team score> - <away team name>'s score: <away team score>`
    - For example, if your home team is BYU and the away team is UVU, it might look like this:
    - `BYU's score: 3 - UVU's score: 2`
- Do this however many times the user inputted for the number of games the home team would play in the season. (E.g. if they inputted 3 for the number of games, go through the above logic 3 times).

### After playing all the games
- Print out: `Teams won against:` 
    - Then print out the name of each team your home team won against. You can put a tab before each name to make it look nicer if you'd like:
      - ```
        Teams won against:
          UVU
          U of U
        ```
- Print out: `Teams lost against:` 
  - Then print out the name of each team your home team won against. You can put a tab before each name to make it look nicer if you'd like:
    - ```
      Teams lost against:
        Utah State
      ```
- Print out `Final season record` followed by their record, which is the number of wins, with a dash, then the number of losses. Like this: 
  - `Final season record: <number of wins> - <number of losses>`
- After all of this, print out a final message based on the record of the home team. 
    - If they won at least 75% of their games, print out:
      - `Qualified for the NCAA Soccer Tournament!` 
    - If the team won at least 50% but less than 75% then print out:
      - `You had a good season.` 
    - Otherwise print out:
      - `Your team needs to practice!`

Push your code up to your GitHub repository to receive credit. 

## Rubric
Note that because this assignment depends on random number generation, some of the tests take a few seconds longer to run because they are running many times to test out many different number generation possibilities.

- See `RUBRIC.md` for details on each of the tests you're scored on.
- To see what score you'll receive, run the tests using the testing tab (it looks like a beaker).
    - In the testing tab, press `Configure Python Tests`, then choose `pytest`, then `tests`, and then press the `Run Tests` button.
        - If you accidentally choose the wrong options for `Configure Python Tests`, to choose again, go to `View` > `Command Palette` and then type `Python: Configure Tests` and hit enter. Then choose the options above again.
- To see your results and any error messages, right click the `TEST_RESULTS_SUMMARY.md` file and choose `Open Preview`.


## Example Output
Note that because scores are randomly chosen, your output will vary, even with identical inputs.

```Enter the name of your home team: BYU
Enter the number of games that BYU will play: 5

Enter the name of the away team for game 1: University of Utah
BYU's score: 1 - University of Utah's score: 2

Enter the name of the away team for game 2: UVU
BYU's score: 3 - UVU's score: 1

Enter the name of the away team for game 3: Utah State
BYU's score: 3 - Utah State's score: 1

Enter the name of the away team for game 4: UNLV
BYU's score: 2 - UNLV's score: 1

Enter the name of the away team for game 5: TCU
BYU's score: 2 - TCU's score: 0

Teams won against:
  UVU
  Utah State
  UNLV
  TCU

Teams lost against:
  University of Utah

Final season record: 4 - 1
Qualified for the NCAA Soccer Tournament!
```
