// printing something
console.log("JS starting!");

// variable declare
var x = 100;
var y = 200;

// console.log(x);
// console.log(y);

//typeof checking
console.log(typeof 100);
console.log(typeof "100");
console.log(typeof true);

// parseFloat, parseInt
console.log(parseFloat("100"));
console.log(parseInt(100.99));

//if,else if, else condition

var x = 100;
if (x > 100) {
    console.log("x is greater than 100");
} else if (x < 100) {
    console.log("x is less than 100");
} else {
    console.log("x is equal to 100");
}

//object declare
var person = {
    name: "John",
    age: 30,
    city: "New York"
};
console.log(person);
console.log(person.name);
console.log(Object.keys(person));
console.log(Object.values(person));
console.log(Object.entries(person));

//array declare
var arr = [100, 200, 300];
console.log(arr);
console.log(arr[0]);

//array methods - push, pop, unshift, shift, concat, reverse, join, slice, indexof, includes
var arr = [100, 200, 300];
arr.pop();
console.log(arr);
arr.push(300);
arr.push(400);
arr.push(500);
console.log(arr);
arr.shift(100);
console.log(arr);
arr.unshift(100);
console.log(arr);
console.log(arr.concat([600,700]));
console.log(arr.slice(0, 3));
console.log(arr.indexOf(100));
console.log(arr.includes(800));

//loop
for (var i = 0; i < 10; i++) {
    console.log(i);
}

// loop in a string array 
var arr = ["a", "b", "c"];
for (var i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

//function for sum 
function sum(a, b) {
    return a + b;
}
result=sum(100, 200);
console.log(result);

//function with default parameter

function sum(a, b = 100) {
    return a + b;
}
result=sum(100);
console.log(result);