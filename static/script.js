$(document).ready(function(){
    $("#send").on("click", function(){
        $("#storedData").val($("#messages").html());
        $("form#formID").submit();
    });
});