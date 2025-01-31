# Test Case 1

## Description
5 Game Season

## Inputs
```
1: "BYU"
2: "5"
3: "University of Utah"
4: "UVU"
5: "Utah State"
6: "UNLV"
7: "TCU"
```

## Expected Input Prompts
```
1: "Enter the name of your home team: "
2: "Enter the number of games that BYU will play: "
3: "Enter the name of the away team for game 1: "
4: "Enter the name of the away team for game 2: "
5: "Enter the name of the away team for game 3: "
6: "Enter the name of the away team for game 4: "
7: "Enter the name of the away team for game 5: "
```

## Expected Printed Messages (the exact scores will differ)
```
1: "BYU's score: 1 - University of Utah's score: 2"
2: "BYU's score: 3 - UVU's score: 1"
3: "BYU's score: 3 - Utah State's score: 1"
4: "BYU's score: 2 - UNLV's score: 1"
5: "BYU's score: 2 - TCU's score: 0"
6: "Teams won against:"
7: "UVU"
8: "Utah State"
9: "UNLV"
10: "TCU"
11: "Teams lost against:"
12: "University of Utah"
13: "Final season record: 4 - 1"
14: "Qualified for the NCAA Soccer Tournament!"
```

## Example Output **(combined Inputs, Input Prompts, and Printed Messages)**
### (The exact scores will differ)
```
Enter the name of your home team: BYU
Enter the number of games that BYU will play: 5

Enter the name of the away team for game 1: University of Utah
BYU's score: 1 - University of Utah's score: 2

Enter the name of the away team for game 2: UVU
BYU's score: 3 - UVU's score: 1

Enter the name of the away team for game 3: Utah State
A tie score! Generating scores again.
BYU's score: 3 - Utah State's score: 1

Enter the name of the away team for game 4: UNLV
BYU's score: 2 - UNLV's score: 1

Enter the name of the away team for game 5: TCU
A tie score! Generating scores again.
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
