# Arithmetic Operators

| Operator | Description         | Example          | Result      |
| -------- | ------------------- | ---------------- | ----------- |
| `+`      | Addition            | `5 + 3`          | `8`         |
| `-`      | Subtraction         | `10 - 7`         | `3`         |
| `*`      | Multiplication      | `4 * 6`          | `24`        |
| `/`      | Division            | `20 / 5`         | `4`         |
| `%`      | Modulus (Remainder) | `10 % 3`         | `1`         |
| `**`     | Exponentiation      | `2 ** 3`         | `8`         |
| `++`     | Increment           | `let a = 1; a++` | `2` (after) |
| `--`     | Decrement           | `let b = 2; b--` | `1` (after) |


Examples:
```javascript
console.log(5 + 3);     // 8
console.log(10 - 7);    // 3
console.log(4 * 6);     // 24
console.log(20 / 5);    // 4
console.log(10 % 3);    // 1
console.log(2 ** 3);    // 8

let a = 1;
a++;
console.log(a);         // 2

let b = 2;
b--;
console.log(b);         // 1
```

[Day 04 Exercise 01 - Basic Arithmetic Operators](Day-04-exercise-01.js)


### Operator Precedence
- `()` **P**arentheses.
- `**` **E**xponentiation.
- `*`, `/`, `%` **M**ultiplication, **D**ivision and **M**odulus.
- `+` and `-` **A**dittion and **S**ubstraction.

This precedence will always be evaluated from left to right.

[Day 04 Exercise 02 - Operator Precedence](Day-04-exercise-02.js)

```javascript
console.log(2 + 3 * 4);    // 14
console.log((2 + 3) * 4);  // 20
console.log(2 ** 3 ** 2);  // 512
```

### Unary Operators

Unary operators work on one operand:

```javascript
let a = 5; 
console.log(++a);  // 6 (increments then returns)
console.log(a--);  // 6 (returns then decrements)
console.log(a);    // 5`
```

### Shorthand Assignment Operators

They combine arithmetic with assignment:

| Operator | Meaning             | Example  | Equivalent to |
| -------- | ------------------- | -------- | ------------- |
| `+=`     | Add and assign      | `x += 3` | `x = x + 3`   |
| `-=`     | Subtract and assign | `x -= 2` | `x = x - 2`   |
| `*=`     | Multiply and assign | `x *= 4` | `x = x * 4`   |
| `/=`     | Divide and assign   | `x /= 5` | `x = x / 5`   |
| `%=`     | Modulus and assign  | `x %= 3` | `x = x % 3`   |

```javascript
let x = 10;
x += 5;   // x = 15
x *= 2;   // x = 30
console.log(x);  // 30
```

# Prefix vs Postfix Increment/Decrement

- **Prefix (`++a` or `--a`)**: increments/decrements the variable **before** returning its value.
- **Postfix (`a++` or `a--`)**: returns the variable’s current value **then** increments/decrements it.

```javascript
let a = 5;
console.log(++a);  // 6  (increments first, then prints)
console.log(a++);  // 6  (prints first, then increments)
console.log(a);    // 7
```

# NaN and Infinity

- **NaN**: stands for _Not a Number_. It appears when an operation that expects a number fails.

```javascript
console.log("hello" / 2);   // NaN
console.log(typeof NaN);    // "number"
```


- **Infinity**: represents a value larger than any finite number, often from division by zero or overflow.

```javascript
console.log(1 / 0);          // Infinity
console.log(-1 / 0);         // -Infinity
console.log(typeof Infinity); // "number"
```

## Body Mass Index (BMI)

The correct BMI formula is:
$$
\text{BMI} = \frac{\text{peso (kg)}}{(\text{altura (m)})^2}
$$
In JavaScript, you can write it as:

```javascript
let weight = 70;      // in kilograms 
let height = 1.75;    // in meters  
let bmi = weight / (height ** 2); 
console.log(bmi);`
```


So you divide the weight by the square of the height (`height ** 2`), **not height to the power of height**.

## Body Fat Percentage (BFP)

$$
\text{BFP}_{men} = 0.32810 \times \text{weight (kg)} + 0.33929 \times \text{waist (cm)} - 29.5336
$$

$$
\text{BFP}_{women} = 0.29569 \times \text{weight (kg)} + 0.41813 \times \text{waist (cm)} - 43.2933
$$
This formula estimates body fat percentage using the waist circumference in centimeters.