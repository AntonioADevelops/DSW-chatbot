$(document).ready(function(){
    $("#response").onsubmit(function(){
        $(".data").load("/update");
    });
});