function calculator(a, b, symbol) {
	if (symbol === '+') {
		return a + b;
	} else if (symbol === '-') {
		return a - b;
	} else if (symbol === '*') {
		return a * b;
	} else if (symbol === '/') {
		if (b === 0) return 'Division by zero';
		return a / b;
	} else if (symbol === '%') {
		return a % b;
	} else {
		return 'Invalid operator';
	}
}


console.log(calculator(10, 5, '+')); // 15
console.log(calculator(10, 5, '-')); // 5
console.log(calculator(10, 5, '*')); // 50
console.log(calculator(10, 5, '/')); // 2
console.log(calculator(10, 0, '/')); // Division by zero
console.log(calculator(10, 5, '%')); // 0
console.log(calculator(10, 5, '^')); // Invalid operator