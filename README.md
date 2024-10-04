#### Assignment 5
# Soccer Teams
You’ll be writing a python program that asks the user to enter a home soccer team and the number of games they’ll play in a season. It will then ask about the teams they play against and randomly generate scores for games they play. It will then display information about the home team’s wins, losses, and overall performance

Put your code in the `a5_soccer_teams.py` file. Do not edit or delete any other files.

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
  - If the home team score is higher than the away team, that is a win, if it is lower, then that is a loss.
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
- Print out `Final season record` followed by your home team name and their record, which is the number of wins, with a dash, then the number of losses. Like this: 
  - `Final season record: <number of wins> - <number of losses>`
- After all of this, print out a final message based on the record of the home team. 
    - If they won at least 75% of their games, print out:
      - `Qualified for the NCAA Soccer Tournament` 
    - If the team won at least 50% but less than 75% then print out:
      - `You had a good season.` 
    - Otherwise print out:
      - `Your team needs to practice!`

Push your code up to your GitHub repository to receive credit. If you pass all the automated tests you will receive full credit.

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

## Rubric
This assignment contains the automated tests listed below. The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.

After this table, see the Test Cases table below to see what inputs will be run for each of the tests below. To receive points for a test, the test must pass each of the individual test cases.

<table>
<thead>
    <tr>
        <th>Test</th>
        <th>Test Cases Used </th>
        <th>Description</th>
        <th>Points</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>1. Input Prompts</td>
        <td>1</td>
        <td>All the these tests are expecting 3 <code>input()</code> prompts to be present in your code. You must use <code>input()</code> to ask the user the following prompts, depending on the input the user provides:
        <ul>
          <li><code>Enter the name of your home team: </code></li>
        </ul>
        <ul>
          <li><code>Enter the number of games that &lt;home team name&gt; will play:  </code></li>
        </ul>
        <ul>
          <li><code>Enter the name of the away team for game &lt;game number&gt;:  </code></li>
        </ul>
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td>2. Printed Messages</td>
        <td>1</td>
        <td>Your printed output must contain these phrases. You will not be docked if you print out any extra statements not included here:
          <ul>
            <li><code>Teams won against:</code></li>
            <li><code>Teams lost against:</code></li>
            <li><code>Final season record: &lt;# won&gt; - &lt;# lost&gt;</code></li>
          </ul>        
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td>3. No tie scores</td>
        <td>1 (repeated 50 times)</td>
        <td>Your code must not allow tie scores. This test will run the test case 50 times and check for any ties occuring in any of the games.
        </td>
        <td>25</td>
    </tr>
        <tr>
        <td>4. Correct Range of Random Scores</td>
        <td>1 (repeated 50 times)</td>
        <td>Your code must allow scores from 0-3 (inclusive) be generated
        </td>
        <td>15</td>
    </tr>
    <tr>
        <td>5. Storing Teams Won and Lost Against</td>
        <td>1</td>
        <td>You need to create a dictionary with the keys "Won Against" and "Lost Against" and store the teams won and lost against in lists associated with eacy key. <br><br>One possible example is:
        <ul>
          <li><code>{"Won Against": ["UVU", "Utah State", "UNLV", "TCU"], "Lost Against": ["University of Utah"]}</code>
          </li>
        </ul>
        </td>
        <td>25</td>
    </tr>
    <tr>
        <td>6. Final Performance Messages</td>
        <td>1 (repeated 50 times)</td>
        <td>Your printed output must accurately calculate the win/loss ratio and always print out one of 3 messages based on the logic given in the instructions section above:
          <ul>
            <li><code>Qualified for the NCAA Soccer Tournament!</code></li>
            <li><code>You had a good season.</code></li>
            <li><code>Your team needs to practice!</code></li>
          </ul>        
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td>7. Sufficient Comments </td>
        <td>None</td>
        <td>Your code must include at least <code>10</code> comments. You can use any form of commenting:
        <ul>
          <li><code>#</code></li> 
          <li><code>''' '''</code></li>
          <li><code>""" """</code></li>
        </ul>
        </td>
        <td>5</td>
    </tr>
    <tr>
        <td colspan="2">Total Points</td>
        <td>100</td>
  </tr>
</tbody>
</table>

<br><br>


## Test Cases Summary
<table>
  <tr>
    <th>Test Case Description</th>
    <th>Inputs</th>
  </tr>
  <tr>
    <td><a href="#testcase1">1: 5 Game Season</a></td>
    <td><ul>
  <li><code>BYU</code></li>
  <li><code>5</code></li>
  <li><code>University of Utah</code></li>
  <li><code>UVU</code></li>
  <li><code>Utah State</code></li>
  <li><code>UNLV</code></li>
  <li><code>TCU</code></li>
</ul></td>
  </tr>
</table>

<h3 id="testcase1">Test Case 1 Details - 5 Game Season</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>BYU</code></li>
  <li><code>5</code></li>
  <li><code>University of Utah</code></li>
  <li><code>UVU</code></li>
  <li><code>Utah State</code></li>
  <li><code>UNLV</code></li>
  <li><code>TCU</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter the name of your home team:</code></li>
  <li><code>Enter the number of games that BYU will play:</code></li>
  <li><code>Enter the name of the away team for game 1:</code></li>
  <li><code>Enter the name of the away team for game 2:</code></li>
  <li><code>Enter the name of the away team for game 3:</code></li>
  <li><code>Enter the name of the away team for game 4:</code></li>
  <li><code>Enter the name of the away team for game 5:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>BYU's score: &lt;score&gt; - University of Utah's score: &lt;score&gt;</code></li>
  <li><code>BYU's score: &lt;score&gt; - UVU's score: &lt;score&gt;</code></li>
  <li><code>BYU's score: &lt;score&gt; - Utah State's score: &lt;score&gt;</code></li>
  <li><code>BYU's score: &lt;score&gt; - UNLV's score: &lt;score&gt;</code></li>
  <li><code>BYU's score: &lt;score&gt; - TCU's score: &lt;score&gt;</code></li>
  <li><code>Teams won against:</code></li>
  <li><code>UVU</code></li>
  <li><code>Utah State</code></li>
  <li><code>UNLV</code></li>
  <li><code>TCU</code></li>
  <li><code>Teams lost against:</code></li>
  <li><code>University of Utah</code></li>
  <li><code>Final season record: &lt;wins&gt; - &lt;losses&gt;</code></li>
  <li><code>Qualified for the NCAA Soccer Tournament!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Dicts</td>
    <td><ul>
  <li><code>{"Won Against": ["UVU", "Utah State", "UNLV", "TCU"], "Lost Against": ["University of Utah"]}</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

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

