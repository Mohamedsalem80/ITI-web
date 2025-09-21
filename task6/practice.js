// Check
let number = 13;

if (number % 2 === 0) {
    console.log(number + " is Even");
} else {
    console.log(number + " is Odd");
}

// Print
let num2 = 5;

for (let i = 1; i <= 10; i++) {
    console.log(num2 + " x " + i + " = " + (num2 * i));
}

// Store
let names = ["Alice", "Bob", "Charlie", "David", "Eva"];

for (let name of names) {
    console.log("Hello, " + name + "!");
}
