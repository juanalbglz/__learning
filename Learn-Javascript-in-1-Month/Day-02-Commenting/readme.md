# Commenting

Even in recipes, sometimes we need to include things that aren't actions—like notes or other comments necessary to follow the instructions.
In JavaScript, comments can be written in two ways:

1. By adding double slashes (//) before the line you want to comment.
2. By enclosing multiple lines of text between /_ and _/.

These comments are ignored by the compiler when the code is executed.

```javascript
//Try hitting run. See what happens.
//console.log("Hello")
```

The code above will not output anything. As you can see, both lines are commented out, so the interpreter ignores them.

Comments can be useful for identifying and fixing bugs. In the following example, we can comment out the line causing the error to prevent the program from crashing:

```javascript
console.log("Hello Angela");
console.log("Goodbye Angela');
```

After running the script, the interpreter throws the following error:
/script.js: Unterminated string constant. (2:12)

To avoid this error and allow the program to run, we can comment out the problematic line:

```javascript
console.log("Hello Angela");
// console.log("Goodbye Angela');
```

## In-line comments
As we saw earlier, text following double slashes (//) will not be interpreted by the compiler.

```javascript
// This is a program that prints "Hello" and "World".
console.log("Hello"); // The semicolon at the end is optional
console.log("World"); // Text inside quotes is treated as a string
console.log(World);   // This line will cause an error: 'World' is not defined
```

## Multi-line comments
If we need to comment multiple lines, we can use /* at the beginning of the comment block and */ at the end. This works as if we had added double slashes (//) to each individual line.

[Day 02 exercise 01](Day-02-exercise-01.js)

[Day 02 exercise 02](Day-02-exercise-02.js)