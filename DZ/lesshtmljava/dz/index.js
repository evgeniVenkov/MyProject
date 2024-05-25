choise = 8;


function whil(){
    while (true)
{
    num = prompt("enter Number");
    if (num == choise)
    {
        break;
    }
    console.log("NEVERNO!")

}

}

whil();

let Zagol = document.getElementsByTagName("h1")[0];

function info(){
Zagol.innerText = `height: ${window.innerHeight} widht: ${window.innerWidth}`;
}

info();

var simpletext = document.querySelectorAll(".text b");
let focus = document.querySelector(".text");

function Mdown() {
for( var i = 0; i < simpletext.length;i++)
simpletext[i].style.color = "black";
}

focus.onmouseenter = function()  {
for( var i = 0; i < simpletext.length;i++)
simpletext[i].style.color = "red";
}

window.onresize = function (){
info();
}


function getAttributes(){
let el = document.getElementById("link");
for(var i = 0; i < el.attributes.length;i++)
{
    console.log(`Значение атрибута: ${el.attributes[i].name} = ${el.attributes[i].value}`)
}
}