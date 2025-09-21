let myName = "Mohamed";
console.log("Hello " + myName);

function addNumbers(a, b) {
  console.log("Sum is:", a + b);
}
addNumbers(5, 7);

function checkResult(studentName, grade) {
  if (grade >= 50) {
    console.log(studentName + " passed with grade " + grade);
  } else {
    console.log(studentName + " failed with grade " + grade);
  }
}
checkResult("Ali", 70);
checkResult("Sara", 45);

const square = (num) => num * num;
console.log("Square of 6 is:", square(6));

function testScope() {
  let localLet = "I am let inside function";
  const localConst = "I am const inside function";
  console.log("Local Let: " + localLet);
  console.log("Local Const: " + localConst);
}
testScope();

console.log("Global Let: " + localLet);
console.log("Global Const: " + localConst);
