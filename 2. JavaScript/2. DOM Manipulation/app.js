console.log("hello world!");
var h1 = document.getElementsByTagName("h1");
console.log(h1[0].innerText);

var title = document.getElementById("dom");
title.style.color = "red";
title.textContent = "Center";
console.log(title);
title.style.removeProperty("color");

var child = document.getElementsByClassName("child");
console.log(child[0]);

var img = document.getElementById("pic");
img.setAttribute("src","/1. HTML-CSS-Bootstrap/2. CSS/image/image.jpg");
img.style.width = "500px";
img.classList.add("image-class");
console.log(img);

var text = document.getElementById("text");
console.log(text.innerText);

var parent = document.getElementById("parent").innerHTML;
console.log(parent);

var test = document.getElementsByClassName("test");
console.log(test[0].childNodes[1].parentNode.parentNode.parentNode.childNodes[5]);

function createElmnt(text){
    var p = document.createElement("p");
    p.innerText = text;
    test[0].appendChild(p)
}

document.getElementById("sbtn").addEventListener("click",function(e){
    var input = document.getElementById("number").value;
    createElmnt(input);
});