# Data Types

[@kommanderkarl](https://youtu.be/UHi-xECyGTU)  

While learning to code, we must understand that not all actions are suitable for all data types. In other words, certain operations depend on the type of data they are used with—just like a toaster wouldn't work with a pizza, it needs bread to function.

```javascript
//Before hitting run, predict the output of the next line of code.
console.log("3" + "2");
```

At first glance, you might expect this code to output 5. However, if we look more carefully, both numbers are inside double quotes. As we learned in [Day 1](../Day-01-Console-Log/readme.md), anything inside double quotes is treated as a string. When we use the + operator between two strings, it's not addition—it’s called concatenation. Therefore, the output will be "32" as a string.

## String datatype

In JavaScript, a string is a sequence of characters enclosed in quotes. You can use single ('), double ("), or backticks (` `) to define a string.

```javascript
"Hello"
'World'
`Hello, World!`
```

Strings can hold letters, numbers, symbols, and even spaces. They're commonly used to display text, combine messages, or store user input.

Example:

```javascript
console.log("My age is " + "25"); // Output: My age is 25
```


# Number datatype

In JavaScript, the number datatype represents both whole numbers (integers) and decimals (floating-point numbers).

```javascript
let age = 30;
let price = 19.99;
```
Numbers can be used in math operations like addition, subtraction, multiplication, and division.


Example:
```javascript
console.log(10 + 5);    // Output: 15
console.log(8 * 2.5);   // Output: 20
```
Unlike strings, numbers are not enclosed in quotes. Using quotes would make them strings instead.
[Number exercise](Day-03-exercise-01.js)


## Boolean datatype

In JavaScript, the Boolean datatype has only two possible values:
true or false.

Booleans are often used to make decisions in programs, especially with conditions and comparisons.

Examples:

```javascript
let isSunny = true;
let isTired = false;

console.log(5 > 3);   // Output: true
console.log(2 === 4); // Output: false
```
They help control the flow of a program, like in if statements.

## Type Check
In JavaScript, the typeof operator is used to check the datatype of a value or variable. It returns a string describing the type.

Examples:
```javascript
console.log(typeof "Hello"); // "string"
console.log(typeof 42);      // "number"
console.log(typeof true);    // "boolean"
```
You can use it to debug or ensure you're working with the correct type of data.

```javascript
let value = "123";
if (typeof value === "string") {
  console.log("This is a string.");
}
```

[typeo exercise](Day-03-exercise-02.js)

## Automatic Type Conversion

JavaScript has a quirk called automatic type conversion, or type coercion. This means it sometimes converts values from one type to another behind the scenes, especially when combining different types.

```javascript
console.log("5" + 1);   // "51" — number 1 becomes a string
console.log("5" - 1);   // 4 — string "5" becomes a number
console.log(true + 1);  // 2 — true becomes 1
```
This behavior can be confusing, so it’s important to always be aware of the types you’re working with.

## Explicit (Manual) Type Conversion
You convert types intentionally using built-in functions:

### To String:
```javascript
String(123)    // "123"
(123).toString() // "123"
```
### To Number:

```javascript
Number("42")   // 42
parseInt("42") // 42
parseFloat("42.5") // 42.5
```
### To Boolean:
```javascript
Boolean(0)      // false
Boolean("hello") // true
```

📝 Be aware:
The functions String(), Number(), and Boolean() used for explicit type conversion in JavaScript all start with a capital letter. This is important, because JavaScript is case-sensitive — writing string(), number(), or boolean() would result in an error or unexpected behavior.

✅ Correct:

```javascript
String(123)
Number("42")
Boolean(0)
```
❌ Incorrect:

```javascript
string(123)   // Error
number("42")  // Error
boolean(0)    // Error
```

[Day 03 Project - Hero Name Generator](Day-03-project-Hero-Name-Generator.html)

