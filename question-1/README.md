# Question 1

In this script, I am retrieving a list of vehicles from  (https://swapi.dev/api/vehicles/) and extracting the manufacturers of each vehicle. The goal is to return a list of the top 5 unique manufacturers that appeared first in the raw JSON response.

## Why I used OrderedDict? 

By using an OrderedDict object to store the manufacturers, the script is able to preserve the order of the manufacturers as they appear in the JSON. Also, orderedDict is like a set + list structure so is optimal for this problem.

## How to run?

`python3 script.py`



