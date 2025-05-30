# Console Log

## What is Code?

Computers are made of wires and transistors. The most basic unit of the computer is a switch that can be turn on and off.

If we had millions of switches we could achive much more.

## How can we use Code to control a computer?

Code is like a Recipe. Imagine a recipe for bread, so can the computer know which switches to turn on and off.

```javascript
console.log("Starting up...");
console.log("I am a computer);
console.log("I can do things if you write the instructions");
console.log("Shutting down...");
```

When code is passed to the computer, a process called **compilation** happens behind the scenes, allowing human readable text to be transformed to machine readable instructions in binary code.

The code is composed by actions ant things. In the case of the recipy the action could be for example "Mix" and the thing "flour and water", while on the computer instructions the action is console.log() and the thing is "Starting up...".

### Exercise 01

#### Instructions

Write a computer program to console log Hello, world! in to the Output area.

**IMPORTANT**: Make sure your output matches the Expected Output exactly, including punctuation.

Expected Output: Hello, world!

[Day 01 exercise 01](Day-01-exercise-01.js)

## Ending a sentence of Code

Each line in Javascript usually performs an action, and usually each line ends in a semicolon, but in modern javascript is optional

### Exercise 02

#### Instructions

Create the following 5 lines of output using console.log() to print the entire recipe into the Output area:

1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes.

[Day 01 exercise 02](Day-01-exercise-02.js)

With strings, we can run into an issue when we use double quotes to define the string and also need double quotes inside the text.

We can solve this issue by using:

- Single quotes at the beginning and end of the string
- **Character escaping**, by adding a backslash before the double quotes: \"

[Day 01 exercise 03](Day-01-exercise-03.js)
