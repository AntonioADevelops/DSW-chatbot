$(document).ready(function(){
    $(function(){
        $("#send").on("click", function () {
            $("#hiddenfield").val($("#dash_new_shout_textarea").text());
            alert($("#hiddenfield").val());   
            $("form#formID").submit();
        });
    });
})