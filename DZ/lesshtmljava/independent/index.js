console.log(window.innerWidth)
console.log(navigator.platform)

setTimeout(function ()
{
    console.warn("Text")

},5000)

/*
location.href = "https://itproger.com";*/

let Zagol = document.getElementsByTagName("h1")[0];

Zagol.innerHTML = "<p class='conteiner'> Helasdlo!</p> <p id='one'>!</p>"

conteiner = document.querySelectorAll(".conteiner")[0];

one = document.querySelector("#one");

one.innerText = "<h1> innerText! </h1>";

// Для дз
// -----------------------------------------------------------------------
function whil(){
        while (true)
    {
        num = prompt("enter Number");
        if (num == 8)
        {
            break;
        }
        console.log("NEVERNO!")

    }

}

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
        console.log(`Значение атрибута: ${el.attributes[i].name} : ${el.attributes[i].value}`)
    }


}

//--------------------------------------------------------------------
area = document.querySelector("textarea")

area.oninput = function (){
    console.log(area.value)
}
function clic(){
    block.innerText = "old text"
}
block = document.querySelectorAll("div.block")[0];
block.addEventListener("dblclick", clic)