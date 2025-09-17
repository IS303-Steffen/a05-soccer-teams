
# Rubric
Your grade is based on whether you pass the automated tests, listed below.

The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.

<table border="1" style="width: 100%; text-align: center;">
<thead>
    <tr>
        <th style="text-align: center;">Test</th>
        <th style="text-align: center;">Description</th>
        <th style="text-align: center;">Points</th>
    </tr>
</thead>
<tbody>
    <tr style="text-align: left">
        <td>1. Input Prompts</td>
        <td>
        <b>Input test cases used:</b> 1<br><br>
        Your input prompts must be the same as the expected input prompts of each input test case. 
        <br>
        <br>
        See the <code>descriptions_of_test_cases</code> folder for expected input prompts for each input test case.
        </td>  
        </td>
        <td>10</td>
    </tr>
    <tr style="text-align: left">
        <td>2. Printed Messages</td>
        <td>
        <b>Input test cases used:</b> 1<br><br>
        Your printed output must be the same as the expected output of each input test case. This includes the correct BMI calculations and BMI categories.
        <br>
        <br>
        See the <code>descriptions_of_test_cases</code> folder for expected printed messages for each input test case.       
        </td>
        <td>10</td>
    </tr>
    <tr style="text-align: left">
        <td>3. No Tie Scores</td>
        <td>
        <b>Input test cases used:</b> 1 (repeated multiple times)<br><br>
        Your code must not allow tie scores. This test will run the test case 50 times and check for any ties occuring in any of the games.  
        </td>
        <td>25</td>
    </tr>
    <tr style="text-align: left">
        <td>4. Correct Range of Random Scores</td>
        <td>
        <b>Input test cases used:</b> 1 (repeated multiple times)<br><br>
        Your code must allow scores from 0-3 (inclusive) be generated, no more and no less. 
        </td>
        <td>15</td>
    </tr>
    <tr style="text-align: left">
        <td>5. Storing Teams Won and Lost Against</td>
        <td>
        <b>Input test cases used:</b> 1<br><br>
        You need to create a dictionary with the keys "Won Against" and "Lost Against" and store the teams won and lost against in lists associated with each key. <br><br>One possible example is:
        <ul>
          <li><code>{"Won Against": ["UVU", "Utah State", "UNLV", "TCU"], "Lost Against": ["University of Utah"]}</code>
          </li>
        </ul>
        </td>
        <td>25</td>
    </tr>
    <tr style="text-align: left">
        <td>6. Final Performance Messages</td>
        <td>
        <b>Input test cases used:</b> 1(repeated multiple times)<br><br>
        Your printed output must accurately calculate the win/loss ratio and always print out one of 3 messages based on the logic given in the instructions section above:
          <ul>
            <li><code>Qualified for the NCAA Soccer Tournament!</code></li>
            <li><code>You had a good season.</code></li>
            <li><code>Your team needs to practice!</code></li>
          </ul>        
        </td>
        </td>
        <td>10</td>
    </tr>
    <tr style="text-align: left">
        <td>7. Sufficient Comments </td>
        <td>
        <b>Input test cases used:</b> None<br><br>
        Your code must include at least <code>7</code> comments. You can use any form of commenting:
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


## Test Cases
If you fail a test during a specific test case, see the `descriptions_of_test_cases` folder for the following:
<table border="1" style="width: 100%; text-align: left;">
  <tr>
    <th>Test Case</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Input Test Case 01</td>
    <td>5 Game Season</td>
  </tr>
</table>