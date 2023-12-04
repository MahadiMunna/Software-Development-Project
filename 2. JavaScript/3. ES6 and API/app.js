// let nm = "Munna";
// nm = "Mahadi";
// console.log(nm);

// const nam = "Munna";
// // nam = "Mahadi";//this can't be changed as it is declare with const 
// console.log(nam);

// // template string
// const text = `I love Bangladesh.
//             as I am from Bangladesh. My name is ${nam}`
// console.log(text);

// // split operator 
// const numbers =	[1, 2, 3, 4, 5, 6, 7, 8, 9]
// console.log(...numbers);
// const newArr = ["Apple","Ball",...numbers];
// console.log(newArr);
// console.log(Math.max(...numbers));

// // array destructuring 
// const [first, second, third, fourth] = numbers;
// console.log(first);

// // object destructuring 
// const obj = {
//     name: "Munna",
//     age: 25,
//     city: "Dhaka"
// }
// const {name, age} =obj;

// console.log(name);

// const persons = [
//     {nam: "Munna", friends: [{name:"zahin",age: 25}, {name:"goni", age: 25}],city: "Dhaka"},
//     {nam: "Rakib", friends: [{name:"jami",age: 30}, {name:"sabuj", age: 29}],city: "Dhaka"},
//     {nam: "Monir", friends: [{name:"siam",age: 20}, {name:"alphy", age: 11}],city: "Tangail"}
// ]
// console.log(persons[0].friends[1].name);

// // mapping
// console.log("\n\nmap");
// const sqaure = numbers.map(number=>number*number);
// console.log(sqaure); 

// // filter 
// console.log("\n\nfilter");
// const result = persons.filter((person) => person.city == "Dhaka");
// console.log(result);

// // find 
// console.log("\n\nfind");
// const ans = persons.find((person) => person.city == "Tangail");
// console.log(ans);

// //forEach
// const personContainer = document.getElementById("persons");
// console.log("\n\nFor each");
// const element = persons.forEach((person) => {
//     console.log(person);
//     const  h1 = document.createElement("h1");
//     h1.innerText = person.nam;
//     personContainer.appendChild(h1);
// });
// console.log(ans);

// API 
fetch('https://jsonplaceholder.typicode.com/todos')
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.log(err));

const loadData = async() => {
    try{
        const response = await fetch('https://jsonplaceholder.typicode.com/todos');
        const data = await response.json();
        console.log(data);
    }catch{
        (err) => console.log(err);
    }
}
loadData();

