## Question 2

The file `script_csv.py` contain the main script of the question. Satisfying all requirements.

### If you had to generate a large number of rows (millions or more), is there anything you would do differently to handle this? 

As implemented in the script, I write the data to the CSV file in chunks: Instead of writing all the data to the file at once, I chose to write it in smaller chunks. This way, if there's an error or the program is interrupted, you can continue where you left off instead of having to start over.

### If this script had to run in a production environment, what tests would you include to ensure it's running correctly? Add the tests.

I created unit tests for the `generate_data()` function. You can view in `tests.py`. We could implement other types of tests too, such as integration tests to test if the data is being writed correctly in the csv file. 

Other type of tests that would be good is performance tests, to test if the script can handle large amounts of data.

### If you were having this code reviewed, what else would you do with your code to ensure the code is clean and well-formatted?

Here are few things I would do

- Add comments: I would add comments throughout the code to explain what the different sections of the code are doing, and to clarify any complex or non-obvious logic.

- Use consistent naming conventions: I would make sure that all variable and function names are clear and descriptive and follow a consistent naming convention.

- Check for edge cases: I would make sure that the code is able to handle any edge cases or unexpected input.

- Handle errors: I would add error handling to the script to ensure that it can gracefully handle any errors that may occur.

- Follow best practices: I would make sure that the code follows best practices such as using functions to break up code, using appropriate data types and structures, and avoiding unnecessary global variables. Probably, I would also use type hints to make the script type safe.





