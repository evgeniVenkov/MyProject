$("button").on('click',function(){
    var p = $("<p> </p>");
    p.text("Neprimetni block");
    p.addClass("block");

    p.insertAfter("button");

})

$("#chek").change(function (){
    $(this).prop("disabled",true);

})

$(window).on('click', function()
{
    $("span").removeClass("heading");
})

$(".newIn").on("mouseover",function (){
    $(this).attr('placeholder','EnterText')
    $(this).removeAttr("value");
    $(this).attr("title","butiful pole")
})