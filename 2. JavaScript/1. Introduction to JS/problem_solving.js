// even or odd 
var num = 77;

if (num%2 == 0) {
    console.log(num + " is a even number");
}
else{
    console.log(num + " is a odd number");
}

// sort numbers
var numbers = [1, 3, 7, 4, 2, 6, 11, 8, 9, 10, 5];

numbers.sort(function(a, b){
    return a - b;
});
console.log(numbers);

// find the big name
var friends = ["rhaim", "karim", "ferdous"];

var biggest = friends[0];

for (var i = 0; i < friends.length; i++) {
    if (friends[i].length > biggest.length) {
        biggest = friends[i];
    }
}
console.log(biggest);

//remove duplicates
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 2]

var uniqueNumbers = [];

for (var i = 0; i < numbers.length; i++) {
    if (uniqueNumbers.indexOf(numbers[i]) === -1) {
        uniqueNumbers.push(numbers[i]);
    }
}
console.log(uniqueNumbers);

//Filter Even numbers 
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 2]

var evenNumbers = [];
for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 == 0) {
        evenNumbers.push(numbers[i]);
    }
}
console.log(evenNumbers);

//Reverse String
var str = "Hello World";

var reverseStr = str.split("").reverse().join("");
console.log(reverseStr);

//Check Prime Numbers
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 2]
var primeNumbers = [];
for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] > 1) {
        for (var j = 2; j < numbers[i]; j++) {
            if (numbers[i] % j == 0) {
                break;
            }
            else if (j == numbers[i] - 1) {
                primeNumbers.push(numbers[i]);
                break;
            }
        }
    }
}
console.log(primeNumbers);

//Check Palindrome
var str = "pop";

var reverseStr = str.split("").reverse().join("");

if (str == reverseStr) {
    console.log(str + " is a palindrome");
}
else{
    console.log(str + " is not a palindrome");
}

//Find Common Elements
var arr1 = [1, 2, 3, 5, 6,  8, 10];
var arr2 = [1, 3, 4, 5, 6, 7, 9];

var commonArray = [];

for (var i = 0; i < arr1.length; i++) {
    for (var j = 0; j < arr2.length; j++) {
        if (arr1[i] == arr2[j]) {
            commonArray.push(arr1[i]);
        }
    }
}
console.log(commonArray);
