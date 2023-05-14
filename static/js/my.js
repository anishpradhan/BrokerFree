$(document).ready(function () {
    $(".location-ul li").click(function () {
        $("#location-id").val($(this).attr('data-value'));
        $('#location-id').attr("name", "location");
     
    });
    
    $(".district-ul li").click(function () {
        $("#district-id").val($(this).attr('data-value'));
        $('#district-id').attr("name", "district");
     
    });
    $(".type-ul li").click(function () {
        $("#type-id").val($(this).attr('data-value'));
        $('#type-id').attr("name", "type");
     
    });
  
});