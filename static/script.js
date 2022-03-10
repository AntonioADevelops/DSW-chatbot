$(document).ready(function(){
    $("#send").on("click", function(){
        $("#hiddenfield").val($("#messages").text());
        alert($("#hiddenfield").val());
        $("form#formID").submit();
    });
});