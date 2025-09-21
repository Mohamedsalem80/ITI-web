let num1 = prompt("Enter the first number:");
let num2 = prompt("Enter the second number:");

num1 = parseFloat(num1);
num2 = parseFloat(num2);

if (!isNaN(num1) && !isNaN(num2)) {
    let sum = num1 + num2;
    let difference = num1 - num2;
    let product = num1 * num2;
    let quotient = num2 !== 0 ? (num1 / num2) : "undefined (division by zero)";

    alert(
    "Results:\n" +
    "Sum = " + sum + "\n" +
    "Subtraction = " + difference + "\n" +
    "Multiplication = " + product + "\n" +
    "Division = " + quotient
    );

    console.log("Sum:", sum);
    console.log("Subtraction:", difference);
    console.log("Multiplication:", product);
    console.log("Division:", quotient);

} else {
    alert("Please enter valid numbers!");
    console.log("Invalid input detected.");
}