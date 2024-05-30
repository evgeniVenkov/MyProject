     var bool = 0;

    var count = 1;
$("button, input").css({"margin":"5px",
    "border-radius":"5px",
    "padding":"7px"
});

$("button").css({"color":"#FF5533",
"font-weight":"bold",});

$(".el").css({
    "border":"1px solid #A9A9A9",
    "width": "190px",
    "background-color":"#CCCCCC",
    "padding": "7px",
    "margin":"5px",
    "border-radius":"5px",
    "font-weight":"bold",
    "color":"#696969",
    "text-align":"center"
});

$(".el").hide();
$(".content").hide();
$(".task").css({"margin":"7px"});


$(".add").on('click',function ()
{
    var text = `<div class = "task"> Задание № ${count} ${$("input").val()} </div>`
    $(".content").append(text)
    count++;
    $(".el").slideDown();
    setTimeout(
  function()
  {
    $(".el").slideUp();
  }, 2000);
});
$(".show").on('click',function (){
    $(".content").toggle();
    if (bool == 0){
        $(".show").html("Cкрыть");
        bool = 1;

    }
    else if (bool == 1){
        $(".show").html("Отобразить");
        bool = 0;
    }
    var mass = getmass();
})


 function getmass(){

    var mass = document.querySelectorAll(".task");
    for(var i = 0; i<mass.length;i++)
    {
        console.log(mass[i]);
    }
    return mass;
 }


 insertAfter
