$(".B1").on('click',function(){
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

$(".FormB").on("click",function(){
    if($(".Inform").val().length<10)
         $(".error").html("Error");
    else
        $(".error").html("");

})

window.onload= function (){
    $(".FormB").click();
}

$("h2").on('click',function (){
    var newobj =$(this).clone();

    $(".simpleText").replaceWith(newobj);
})