## In this script, I am retrieving a list of vehicles from  (https://swapi.dev/api/vehicles/) and extracting the manufacturers of each vehicle. The goal is to return a list of the top 5 unique manufacturers that appeared first in the raw JSON response.

### Here's how I attacked the problem and designed the code:

- Imported the requests library to make a GET request to the API endpoint. I then used the get() method to retrieve the JSON data from the API.

- Created an empty OrderedDict object called manufacturers which will later be used to store the unique manufacturers in the order they appear in the JSON.

- Used a for loop to iterate through the results of the JSON data which contains all the vehicles information. For each vehicle, I extracted the manufacturer field, converted it to lowercase using .lower() to eliminate the case sensitivity and added it to the manufacturers ordered dictionary. (I'm supposing that the same name with case differences are the same manufacturer)

- Converted the manufacturers OrderedDict to a list of keys.

- Used another for loop to print the top 5 manufacturers. I used the enumerate method to keep track of the current index and the value(manufacturer) of the iteration, so I can break the loop after the 5th manufacturer.

- Used the break statement to break out of the loop and stop printing after the 5th manufacturer.

### Why I used OrderedDict? 

By using an OrderedDict object to store the manufacturers, the script is able to preserve the order of the manufacturers as they appear in the JSON. Also, orderedDict is like a set + list structure so is optimal for this problem.




