# Superbowl Football Squares
Football Squares is a betting game for 
[American Football](https://en.wikipedia.org/wiki/American_football).
Other sports probably do similar types of betting, but I discovered
this through watching football. The concept of the game is simple,
make an grid of possible scores and have people purchase each
"spot" for a fixed price. There are _many_ variation to how
a person can win, all of them simplifying to the game score 
needs to match one of your purchased grid spots.


# Analysis
The analysis done in `summarize.py`, looks at one of the more
common versions of the game. There are 5 times when a square
could win:
  1. End of 1st Quarter
  1. End of 2nd Quarter
  1. End of 3rd Quarter
  1. End of 4th Quarter
  1. End of the Game

Typically, there are only 4 winners with the last winning
"double", if there are not overtime periods played.

Grid squares are _distinct_ from one another (2,5) is not the
same as (5,2). Each slot is associated with a given team.

Now we get to the results of the analysis. Looking through
the box scores of all 58 superbowls we get these results for
occurances of each value.

| Last Digit (AFC) | Occurances |
|:----------------:|:----------:|
|0                 | 64         |
|7                 | 42         |
|3                 | 34         |
|4                 | 31         |
|6                 | 19         |
|1                 | 14         |
|8                 | 9          |
|9                 | 9          |
|2                 | 7          |
|5                 | 3          |

| Last Digit (NFC) | Occurances |
|:----------------:|:----------:|
|0                 | 61         |
|7                 | 41         |
|3                 | 40         |
|4                 | 18         |
|1                 | 16         |
|6                 | 16         |
|9                 | 14         |
|8                 | 11         |
|5                 | 8          |
|2                 | 7          |

