$(document).ready(function () {


    $("#p1").text("Merhaba");


    $("p").hover(function () {
        $(this).addClass("highlight");
    }, function () {
        $(this).removeClass("highlight");
    });


});