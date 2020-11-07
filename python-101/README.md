# Programming 101 with Python

Self-learning roadmap and materials for programming beginners to pick up fundamental concepts of programming through Python practices.

Join our learning community over at [CodeMap Facebook Group](https://www.facebook.com/groups/codemap)!

**Notes**: Most of the materials deal with fundamentals which are universal across programming languages and we try to keep our content that way. However at times, we will need to learn about and use features that are specific to the medium-for-learning language Python. These language specifics points will be marked with ![#ff0000](https://placehold.it/15/FF0000)

## Pre-requisite

- Python 3 installed in learner's machine. Follow instructions from [here](https://www.python.org/downloads/)

## Theme Problem

For this module, we will implement a game where:

- The computer will generate a random number between 1 and 10
- User has to guess it in 5 attempts
- Based on the user's guess, the computer will give various hints if the number is high or low
- When the user's guess matches the number, the computer will print the answer along with the number of attempts

```bash
guess: 2
Your guess is too low
guess: 4
Your guess is too low
guess: 6
You guess the number in 3 tries
```

## Breaking down the problem

The most important step in programming or solving problems in general is breaking it down into smaller, solvable chunks.
Please take your time to think about what are the steps for the implementations of the game.
Please:

- be as specific as possible at every step (at least more specific than the outline from the previous section. i.e. instead of "Based on the user's guess, the computer will give various hints if the number is high or low", we would go for "if the guess is lower than the result, print ..., if the guess is higher than the result, print ...)
- draw a block diagram of the steps to help yourself visualise the implementation

After you are done with your brainstorming, the sample answer can be found [here](./static/diagram.png)

## Implementation and learning materials

In this section, we will try to solve each of the outlined step and pick up knowledge about Python as we solve them

### I. Generation of random number

#### 1. Literals

- [Definition of literals](https://medium.com/@ngubanethabo.ambrose/what-is-a-literal-in-computer-programming-560eace90b5b)
- ![#ff0000](https://placehold.it/15/FF0000) [Python numeric types](https://www.programiz.com/python-programming/numbers)
- ![#ff0000](https://placehold.it/15/FF0000) [Python string type](https://www.programiz.com/python-programming/string)

#### 2. Variables

- [Definition of variables](https://www.tutorialspoint.com/computer_programming/computer_programming_variables.htm)
- ![#ff0000](https://placehold.it/15/FF0000) [Python reserved words](https://www.programiz.com/python-programming/keywords-identifier)
- ![#ff0000](https://placehold.it/15/FF0000) [Python variable naming convention](https://thehelloworldprogram.com/python/python-variable-assignment-statements-rules-conventions-naming/)
- ![#ff0000](https://placehold.it/15/FF0000) [Quiz on Python variables](https://realpython.com/quizzes/python-variables)

#### 3. Expressions and Statements

- [Definition](https://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html)
- ![#ff0000](https://placehold.it/15/FF0000) [Python quizz](https://realpython.com/quizzes/python-operators-expressions/)

#### 4. Functions

- [Definition and importance](https://www.cs.utah.edu/~germain/PPS/Topics/functions.html)
- ![#ff0000](https://placehold.it/15/FF0000) [Python def keyword](https://www.w3schools.com/python/ref_keyword_def.asp)
- Built-in function: A function that is built into an application (in this case python) and can be accessed by users. [Python built-in functions](https://www.w3schools.com/python/python_ref_functions.asp)
- [Return statement](https://stackoverflow.com/a/6182197/6137550)
- [Void function](https://www.cs.fsu.edu/~cop3014p/lectures/ch7/index.html)
- [Arguments and Parameters](https://www.cs.auckland.ac.nz/references/unix/digital/AQTLTBTE/DOCU_056.HTM)
- ![#ff0000](https://placehold.it/15/FF0000) [Python function quizz](https://pynative.com/python-functions-quiz/)
- ![#ff0000](https://placehold.it/15/FF0000) [Python function exercises](https://www.w3resource.com/python-exercises/python-functions-exercises.php)

#### ![#ff0000](https://placehold.it/15/FF0000) 5. Python built-in `print` function

- [Manual](https://www.w3schools.com/python/ref_func_print.asp)
- [Python `printf` function](https://www.python-course.eu/python3_formatted_output.php)
- Exercise:
  - Try to print out number from 1 to 5 on the same line
  - Try to print out a number injected inside a string with `printf`

#### ![#ff0000](https://placehold.it/15/FF0000) 6. Python built-in random.randint function

- [Manual](https://docs.python.org/3/library/random.html#random.randint)
- Exercise: Print out a randomly generated integer within range 1 to 10

#### 7. Solving the first step of theme problem

- Acceptance Criteria:
  - A random integer is generated
  - The generated random integer is assigned to a variable

### II. Get user input

#### 1. Types

- [Primitive & built-in data type definition](https://en.wikibooks.org/wiki/Introduction_to_Programming_Languages/Primitive_Types)
- ![#ff0000](https://placehold.it/15/FF0000) [Python primitive data types](https://realpython.com/python-data-types/)
- ![#ff0000](https://placehold.it/15/FF0000) [Python `type()` built-in function](https://www.geeksforgeeks.org/python-type-function/)
- [Type casting](https://www.programiz.com/python-programming/type-conversion-and-casting)
- ![#ff0000](https://placehold.it/15/FF0000) [Python integer division](https://riptutorial.com/python/example/2797/integer-division)
- ![#ff0000](https://placehold.it/15/FF0000) [Python integer division exercise](https://www.hackerrank.com/challenges/python-division/problem)
- Exercise: Try converting these strings into int: `"1"`, `"1.5"`, `"wadafack"` and print them out. Seeing an error? The next section will address this

#### 2. Error handling

- [Exception handling in Python](https://www.programiz.com/python-programming/exception-handling)
- Exercise: Rewrite the code from the last exercise in Types to handle errors and print out the original string

#### ![#ff0000](https://placehold.it/15/FF0000) 3. Python built-in `input()` function

- [Manual](https://www.w3schools.com/python/ref_func_input.asp)
- This function returns a string and the input is detected upon encoutering a newline character
- Exercise: try running `type()` on result from `input()`

#### 4. Solving the second step of theme problem

- Acceptance Criteria:
  - User input can be accepted
  - Errornuous inputs should be handled and followed by a new attempt to ask for user input
  - Input should be casted into an integer and printed out

### III. Check if user's guess is correct and player still has retry attempts

#### 1. Conditionals:

- [Boolean data type](https://en.wikipedia.org/wiki/Boolean_data_type)
- [Comparision operators](https://data-flair.training/blogs/python-comparison-operators/)
- [Python operator quizz](https://quizizz.com/admin/quiz/5d2bc01e504efd001b4bf1b2/python-operators)

#### 2. Iterations/Loops and Iterables

- [Loop with Python](https://openbookproject.net/thinkcs/python/english3e/iteration.html)
- Exercise:

  - Use a for loop to find whether a number is in an array. Say given `[1, 5, 6, 8, 9]`, check if `5` is in the array
  - Sum all odd numbers in an array

- [Iterables](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html)
- ![#ff0000](https://placehold.it/15/FF0000) [Python list type](https://www.w3schools.com/python/python_lists.asp)
- ![#ff0000](https://placehold.it/15/FF0000) [len() built-in function](https://www.w3schools.com/python/ref_func_len.asp)
- [Iterable slicing](https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/)
- Map, reduce, filter: these built in functions are available in Python and a lot of other languages. A relatively advanced concept under the functional programming umbrella but it’s good to learn for beginners to deal with iterable data more effectively: https://www.learnpython.org/en/Map,_Filter,_Reduce
- Exercise: Map an array of strings to their integer values then filtered for odd number then reduce to the sum. You can start by writing without `map`, `reduce`, `filter` first

#### 3. Strings

- ![#ff0000](https://placehold.it/15/FF0000) [Python strings](https://www.w3schools.com/python/python_strings.asp)
- ![#ff0000](https://placehold.it/15/FF0000) [`strip()` built-in function](https://www.w3schools.com/python/ref_string_strip.asp)
- ![#ff0000](https://placehold.it/15/FF0000) [`split()` built-in function](https://www.w3schools.com/python/ref_string_split.asp)
- ![#ff0000](https://placehold.it/15/FF0000) [`lower()` built-in function](https://www.w3schools.com/python/ref_string_lower.asp)
- ![#ff0000](https://placehold.it/15/FF0000) [`upper()` built-in function](https://www.w3schools.com/python/ref_string_upper.asp)
- [Python string excercises](https://www.w3resource.com/python-exercises/string/)

#### 4. Solving the next step of the theme problem

- You should be able to implement this step without string comparisons or any string or iterable built-in functions
- An additional requirement to the theme problem to implement this step differently: To accept all guesses at once from the start in the format of a comma-separated string, then check result without using for loop

### IV. Upgraded theme problem

#### 1. The program should have an automatic guessing mechanism to solve itself

- "Get user input" step will be replaced with a guessing logic step that guesses a random number at the start then based on the feeedback (low/high messages) it will make subsequent guesses within ght low/high range
- We will be using randint and string comparision for this.

#### 2. Non-fixed feedback messages with work `low` and `high` in the message accordingly

- We need something to store the list of possible messages for low, high guesses feedbacks. 2 list variables with one for low and one for high feedbacks would suffice but we want a more elegant solution. An option to consider is a dictionary

```python
{
    'low': ['your guess was too low', 'this is too low a guess'],
    'high': ['your guess was too high', 'this is so damn high a guess']
}
```

- Hashmap (Or what we call dictionary in Python)
  - Definition: key-value collection
    - List is a stack of plats
    - Dictionary is a bag of unordered, labelled stuffs
    - [Read more](https://www.w3schools.com/python/python_dictionaries.asp)
    - Exercise: Given a list of names, count the occurrences of each name in the list. Your solution should use dictionary
    - [Iterating through a dictionary in Python](https://realpython.com/iterate-through-dictionary-python/)
- Implementing non-fixed feedback messages:
  - We should be able to implement a less predictable feedback message system with dictionary and `randint()` and `len()`
  - Oh no, the auto-guesser from the previous step breaks now as the feedback messages are not fixed strings anymore, how to solve it? We can use the logical `in` operator to check if the message is in such list but in a more realistic scenario when we don't control the info but it's rather given to us by another system => We need a better solution

#### 3. Use regular expressions to deal with less predictable strings

- [Regex in Python](https://www.programiz.com/python-programming/regex)
- [Regex usecases](https://softwareengineering.stackexchange.com/questions/402197/what-is-the-best-use-case-of-a-regular-expression-triplebyte-question)
- Dealing with the various feedback messages:
  - creating regex to check whether feedback string contains "high" or "low" and continue making guess accordingly
  - the auto-guesser should be back to working normally

### V. The best strategy

This theme problem is actually a game of binary guessing where we know if we need to go down "high" or "low" path.

The optimal guessing strategy is to always guess the median of whatever that're left.
With this optiomal strategy give us a guarantee to get the result after at most ![log 2 of n](<https://latex.codecogs.com/gif.latex?log_2(n)>) guesses where n is the number of items in the starting list.  
![log 2 of n](<https://latex.codecogs.com/gif.latex?log_2(n)>) is also the "big O notation" which indicates performance of a function in our code - a more advanced concept that we will cover in Programming 102 module.

The official name of this solution is binary search.
You can read up more about it [here](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
