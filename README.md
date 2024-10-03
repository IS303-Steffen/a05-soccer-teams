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
        `Enter the name of the away team for game 1: `
- After entering in the away team name, randomly generate scores between 0 and 5 
(inclusive) for the home team and the away team.
    - Look up the `random` library in python if you don't know how to do this.
    - As a rule, you cannot have tie scores. In the case that there is a tie between the home and the away teams, keep generating new scores for the home and away teams until there isn’t a tie. 
- Keep track of the number of wins / losses of your home team however you want. (If the home team score is higher than the away team, that is a win, if it is lower, then that is a loss). You just need to be able to calculate
- You also need to keep track of the names of teams that your team won against and lost against in a dictionary. You dictionary will have two keys: `"Won Against"` and `"Lost Against"`. Both keys will have lists for the values.
    - If the home team won, store the name of the away team in the list associated with the `"Won Against"` key.
    - If the home team lost, store the name of the away team in the list associated with the `"Lost Against"` key.
    - The exact way you code this is up to you, but the automated tests will be specifically looking for a dictionary with 2 keys called `"Won Against"` and `"Lost Against"` with lists as their values, so you must store them this way to get credit.
- Print out the name of the home team’s name and their score, as well as the away team’s name and their score like this:
    - `<home team name>'s score: <home team score> - <away team name>'s score: <away team score>`
    - For example, if your home team is BYU and the away team is UVU, it might look like this:
    - `BYU's score: 4 - UVU's score: 2`
- Do this however many times the user inputted for the number of games the home team would play in the season. (E.g. if they inputted 3 for the number of games, go through the above logic 3 times).

### After playing all the games
- Print out: `Teams won against:` 
    - Then print out the name of each team your home team won against. You can put a tab before each name to make it look nicer if you'd like:
        - 
        ```
        Teams won against:
            UVU
            U of U
        ```
- Print out: `Teams lost against:` 
    - Then print out the name of each team your home team won against. You can put a tab before each name to make it look nicer if you'd like:
        - 
        ```
        Teams lost against:
            Utah State
        ```
- Print out `Final season record` followed by your home team name and their record, which is the number of wins, with a dash, then the number of losses. Like this: 
    - `Final season record: <number of wins> - <number of losses>`
- After all of this, print out a final message based on the record of the home team. 
    - If they won at least 75% of their games, print out:
        `Qualified for the NCAA Soccer Tournament` 
- If the team won at least 50% but less than 75% then print out “You had a 
good season”. 
    - Otherwise print out “Your team needs to practice!”.

## Running the automated tests
Feel free to run the included automated tests to see what score you'll get:
1. Go to the Testing Tab
2. Click "Configure Python Tests"
3. Choose "Pytest" (NOT "UNITTEST")
    - If you accidentally choose "UNITTEST", you can reselect by going to View > Command Palette and then typing "Python: Configure Tests" and pressing enter on your keyboard
4. Choose "tests"
5. Click the play button near the top of the Testing tab, or press the little arrows next to the assignment name until you can see individual tests to run.

If a test doesn't pass, scroll up in the "Test Results" window in the Terminal area until you see the "IS 303 STUDENTS: READ THE EERROR MESSAGESS IN RED BELOW" message. Read the error messages to see why a test did not pass.


## Example Output
Below is an example of
- entering in 2 friends
- checking the hobby of one of the friends
- checking the hobby of a friend that doesn't exist
- trying to enter in a friend that was already added
- entering invalid input
- quitting

```
Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 1
Enter friend's name: Jimmer
Enter Jimmer's hobby: Basketball

Jimmer added to your dictionary!

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 1
Enter friend's name: Reena
Enter Reena's hobby: Listening to Sonic Youth

Reena added to your dictionary!

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 2
Enter a friend's name to find their hobby: Reena

Reena's hobby is Listening to Sonic Youth.

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 2
Enter a friend's name to find their hobby: Tim

Tim is not in the dictionary.

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 1
Enter friend's name: Jimmer

Jimmer is already in your dictionary.

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): asdf

Invalid choice. Please choose a valid option.

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 3

Exiting the program. Goodbye!
```
asdf

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
        <td>1-6</td>
        <td>All the these tests are expecting 4 <code>input()</code> prompts to be present in your code. You must use <code>input()</code> to ask the user the following prompts, depending on the input the user provides:
        <ul>
          <li><code>Enter an option (1, 2, or 3):  </code></li>
        </ul>
        <ul>
          <li><code>Enter friend's name:  </code></li>
        </ul>
        <ul>
          <li><code>Enter &lt;Friend's name&gt;'s hobby: : </code></li>
        </ul>
        <ul>
          <li><code>Enter a friend's name to find their hobby: </code></li>
        </ul> 
        </td>
        <td>25</td>
    </tr>
    <tr>
        <td>2. Printed Messages</td>
        <td>1-6</td>
        <td>Your printed output must contain these phrases, though only some should print out depending on what the user inputs:
          <ul>
            <li><code>Menu:</code></li>
            <li><code>1. Add a Friend</code></li>
            <li><code>2. Find a Friend's Hobby</code></li>
            <li><code>3. Quit</code></li>
            <li><code>&lt;Friend's name&gt; is already in your dictionary.</code></li>
            <li><code>&lt;Friend's name&gt; added to your dictionary!</code></li>
            <li><code>&lt;Friend's name&gt;'s hobby is &lt;Friend's hobby&gt;.</code></li>
            <li><code>&lt;Friend's name&gt; is not in the dictionary.</code></li>
            <li><code>Exiting the program. Goodbye!</code></li>
            <li><code>Invalid choice. Please choose a valid option.</code></li>
          </ul>        
        </td>
        <td>25</td>
    </tr>
    <tr>
        <td>3. Creation of Dictionary</td>
        <td>1-2, 4, 6</td>
        <td>Your code must store friends' names and hobbies in a dictionary data type. See the test cases section for examples.
        </td>
        <td>45</td>
    </tr>
    <tr>
        <td>4. Sufficient Comments </td>
        <td>None</td>
        <td>Your code must include at least <code>5</code> comments. You can use any form of commenting:
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
    <td><a href="#testcase1">1: Single name/hobby, no lookup</a></td>
    <td><ul>
  <li><code>1</code></li>
  <li><code>Jimmer</code></li>
  <li><code>Basketball</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td><a href="#testcase2">2: Single name/hobby with lookup</a></td>
    <td><ul>
  <li><code>1</code></li>
  <li><code>Jimmer</code></li>
  <li><code>Basketball</code></li>
  <li><code>2</code></li>
  <li><code>Jimmer</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td><a href="#testcase3">3: Invalid input</a></td>
    <td><ul>
  <li><code>INVALID INPUT!</code></li>
  <li><code>4</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td><a href="#testcase4">4: Single name/hobby, repeat name</a></td>
    <td><ul>
  <li><code>1</code></li>
  <li><code>Jimmer</code></li>
  <li><code>Basketball</code></li>
  <li><code>1</code></li>
  <li><code>Jimmer</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td><a href="#testcase5">5: Lookup before entering name/hobby</a></td>
    <td><ul>
  <li><code>2</code></li>
  <li><code>Jimmer</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td><a href="#testcase6">6: Multiple friends/hobbies</a></td>
    <td><ul>
  <li><code>1</code></li>
  <li><code>Jimmer</code></li>
  <li><code>Basketball</code></li>
  <li><code>1</code></li>
  <li><code>Reena</code></li>
  <li><code>Listening to Sonic Youth</code></li>
  <li><code>1</code></li>
  <li><code>Link</code></li>
  <li><code>Breaking pots</code></li>
  <li><code>2</code></li>
  <li><code>Reena</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
</table>

<h3 id="testcase1">Test Case 1 Details - Single name/hobby, no lookup</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>1</code></li>
  <li><code>Jimmer</code></li>
  <li><code>Basketball</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter an option (1, 2, or 3):</code></li>
  <li><code>Enter friend's name:</code></li>
  <li><code>Enter Jimmer's hobby:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td><ul>
  <li><code>Enter a friend's name to find their hobby:</code></li>
  <li><code>Enter Reena's hobby:</code></li>
  <li><code>Enter Link's hobby:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Menu:</code></li>
  <li><code>1. Add a Friend</code></li>
  <li><code>2. Find a Friend's Hobby</code></li>
  <li><code>3. Quit</code></li>
  <li><code>Jimmer added to your dictionary!</code></li>
  <li><code>Exiting the program. Goodbye!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>Jimmer's hobby is Basketball.</code></li>
  <li><code>Jimmer is not in the dictionary.</code></li>
  <li><code>Reena added to your dictionary!</code></li>
  <li><code>Jimmer is already in your dictionary.</code></li>
  <li><code>Reena's hobby is Listening to Sonic Youth.</code></li>
  <li><code>Invalid choice. Please choose a valid option.</code></li>
  <li><code>Link added to your dictionary!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Dicts</td>
    <td><ul>
  <li><code>{"Jimmer": "Basketball"}</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 1
Enter friend's name: Jimmer
Enter Jimmer's hobby: Basketball

Jimmer added to your dictionary!

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 3

Exiting the program. Goodbye!
```

<h3 id="testcase2">Test Case 2 Details - Single name/hobby with lookup</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>1</code></li>
  <li><code>Jimmer</code></li>
  <li><code>Basketball</code></li>
  <li><code>2</code></li>
  <li><code>Jimmer</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter an option (1, 2, or 3):</code></li>
  <li><code>Enter friend's name:</code></li>
  <li><code>Enter Jimmer's hobby:</code></li>
  <li><code>Enter a friend's name to find their hobby:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td><ul>
  <li><code>Enter Reena's hobby:</code></li>
  <li><code>Enter Link's hobby:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Menu:</code></li>
  <li><code>1. Add a Friend</code></li>
  <li><code>2. Find a Friend's Hobby</code></li>
  <li><code>3. Quit</code></li>
  <li><code>Jimmer added to your dictionary!</code></li>
  <li><code>Jimmer's hobby is Basketball.</code></li>
  <li><code>Exiting the program. Goodbye!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>Jimmer is already in your dictionary.</code></li>
  <li><code>Jimmer is not in the dictionary.</code></li>
  <li><code>Reena added to your dictionary!</code></li>
  <li><code>Reena's hobby is Listening to Sonic Youth.</code></li>
  <li><code>Invalid choice. Please choose a valid option.</code></li>
  <li><code>Link added to your dictionary!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Dicts</td>
    <td><ul>
  <li><code>{"Jimmer": "Basketball"}</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 1
Enter friend's name: Jimmer
Enter Jimmer's hobby: Basketball

Jimmer added to your dictionary!

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 2
Enter a friend's name to find their hobby: Jimmer

Jimmer's hobby is Basketball.

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 3

Exiting the program. Goodbye!
```

<h3 id="testcase3">Test Case 3 Details - Invalid input</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>INVALID INPUT!</code></li>
  <li><code>4</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter an option (1, 2, or 3):</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td><ul>
  <li><code>Enter a friend's name to find their hobby:</code></li>
  <li><code>Enter Jimmer's hobby:</code></li>
  <li><code>Enter friend's name:</code></li>
  <li><code>Enter Reena's hobby:</code></li>
  <li><code>Enter Link's hobby:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Menu:</code></li>
  <li><code>1. Add a Friend</code></li>
  <li><code>2. Find a Friend's Hobby</code></li>
  <li><code>3. Quit</code></li>
  <li><code>Invalid choice. Please choose a valid option.</code></li>
  <li><code>Exiting the program. Goodbye!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>Jimmer's hobby is Basketball.</code></li>
  <li><code>Jimmer is not in the dictionary.</code></li>
  <li><code>Reena added to your dictionary!</code></li>
  <li><code>Jimmer is already in your dictionary.</code></li>
  <li><code>Reena's hobby is Listening to Sonic Youth.</code></li>
  <li><code>Jimmer added to your dictionary!</code></li>
  <li><code>Link added to your dictionary!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Dicts</td>
    <td><ul>
  <li><code>{}</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): INVALID INPUT!

Invalid choice. Please choose a valid option.

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 4

Invalid choice. Please choose a valid option.

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 3

Exiting the program. Goodbye!
```

<h3 id="testcase4">Test Case 4 Details - Single name/hobby, repeat name</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>1</code></li>
  <li><code>Jimmer</code></li>
  <li><code>Basketball</code></li>
  <li><code>1</code></li>
  <li><code>Jimmer</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter an option (1, 2, or 3):</code></li>
  <li><code>Enter friend's name:</code></li>
  <li><code>Enter Jimmer's hobby:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td><ul>
  <li><code>Enter a friend's name to find their hobby:</code></li>
  <li><code>Enter Reena's hobby:</code></li>
  <li><code>Enter Link's hobby:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Menu:</code></li>
  <li><code>1. Add a Friend</code></li>
  <li><code>2. Find a Friend's Hobby</code></li>
  <li><code>3. Quit</code></li>
  <li><code>Jimmer added to your dictionary!</code></li>
  <li><code>Jimmer is already in your dictionary.</code></li>
  <li><code>Exiting the program. Goodbye!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>Jimmer's hobby is Basketball.</code></li>
  <li><code>Jimmer is not in the dictionary.</code></li>
  <li><code>Reena added to your dictionary!</code></li>
  <li><code>Reena's hobby is Listening to Sonic Youth.</code></li>
  <li><code>Invalid choice. Please choose a valid option.</code></li>
  <li><code>Link added to your dictionary!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Dicts</td>
    <td><ul>
  <li><code>{"Jimmer": "Basketball"}</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 1
Enter friend's name: Jimmer
Enter Jimmer's hobby: Basketball

Jimmer added to your dictionary!

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 1
Enter friend's name: Jimmer

Jimmer is already in your dictionary.

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 3

Exiting the program. Goodbye!
```

<h3 id="testcase5">Test Case 5 Details - Lookup before entering name/hobby</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>2</code></li>
  <li><code>Jimmer</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter an option (1, 2, or 3):</code></li>
  <li><code>Enter a friend's name to find their hobby:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td><ul>
  <li><code>Enter Jimmer's hobby:</code></li>
  <li><code>Enter friend's name:</code></li>
  <li><code>Enter Reena's hobby:</code></li>
  <li><code>Enter Link's hobby:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Menu:</code></li>
  <li><code>1. Add a Friend</code></li>
  <li><code>2. Find a Friend's Hobby</code></li>
  <li><code>3. Quit</code></li>
  <li><code>Jimmer is not in the dictionary.</code></li>
  <li><code>Exiting the program. Goodbye!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>Jimmer's hobby is Basketball.</code></li>
  <li><code>Jimmer is already in your dictionary.</code></li>
  <li><code>Reena added to your dictionary!</code></li>
  <li><code>Reena's hobby is Listening to Sonic Youth.</code></li>
  <li><code>Jimmer added to your dictionary!</code></li>
  <li><code>Invalid choice. Please choose a valid option.</code></li>
  <li><code>Link added to your dictionary!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Dicts</td>
    <td><ul>
  <li><code>{}</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 2
Enter a friend's name to find their hobby: Jimmer

Jimmer is not in the dictionary.

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 3

Exiting the program. Goodbye!
```

<h3 id="testcase6">Test Case 6 Details - Multiple friends/hobbies</h3>

<table>
  <tr>
    <th>Requirement</th>
    <th>Components</th>
  </tr>
  <tr>
    <td>Inputs</td>
    <td><ul>
  <li><code>1</code></li>
  <li><code>Jimmer</code></li>
  <li><code>Basketball</code></li>
  <li><code>1</code></li>
  <li><code>Reena</code></li>
  <li><code>Listening to Sonic Youth</code></li>
  <li><code>1</code></li>
  <li><code>Link</code></li>
  <li><code>Breaking pots</code></li>
  <li><code>2</code></li>
  <li><code>Reena</code></li>
  <li><code>3</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Input Prompts</td>
    <td><ul>
  <li><code>Enter an option (1, 2, or 3):</code></li>
  <li><code>Enter friend's name:</code></li>
  <li><code>Enter Jimmer's hobby:</code></li>
  <li><code>Enter Reena's hobby:</code></li>
  <li><code>Enter Link's hobby:</code></li>
  <li><code>Enter a friend's name to find their hobby:</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Input Prompts</td>
    <td></td>
  </tr>
  <tr>
    <td>Printed Messages</td>
    <td><ul>
  <li><code>Menu:</code></li>
  <li><code>1. Add a Friend</code></li>
  <li><code>2. Find a Friend's Hobby</code></li>
  <li><code>3. Quit</code></li>
  <li><code>Jimmer added to your dictionary!</code></li>
  <li><code>Reena added to your dictionary!</code></li>
  <li><code>Link added to your dictionary!</code></li>
  <li><code>Reena's hobby is Listening to Sonic Youth.</code></li>
  <li><code>Exiting the program. Goodbye!</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Invalid Printed Messages</td>
    <td><ul>
  <li><code>Jimmer's hobby is Basketball.</code></li>
  <li><code>Jimmer is not in the dictionary.</code></li>
  <li><code>Invalid choice. Please choose a valid option.</code></li>
  <li><code>Jimmer is already in your dictionary.</code></li>
</ul></td>
  </tr>
  <tr>
    <td>Dicts</td>
    <td><ul>
  <li><code>{"Jimmer": "Basketball", "Reena": "Listening to Sonic Youth", "Link": "Breaking pots"}</code></li>
</ul></td>
  </tr>
</table>

<h4>Example Ouput:</h4>

```
Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 1
Enter friend's name: Jimmer
Enter Jimmer's hobby: Basketball

Jimmer added to your dictionary!

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 1
Enter friend's name: Reena
Enter Reena's hobby: Listening to Sonic Youth

Reena added to your dictionary!

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 1
Enter friend's name: Link
Enter Link's hobby: Breaking pots

Link added to your dictionary!

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 2
Enter a friend's name to find their hobby: Reena

Reena's hobby is Listening to Sonic Youth.

Menu:
1. Add a Friend
2. Find a Friend's Hobby
3. Quit
Enter an option (1, 2, or 3): 3

Exiting the program. Goodbye!
```
