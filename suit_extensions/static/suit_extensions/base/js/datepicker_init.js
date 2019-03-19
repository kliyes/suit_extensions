$(document).ready(function(){
    $("input[datepicker=1]").each(function(){
        var options = $(this).data("datepicker-options");
        if (options !== ""){
            options = options.replace(/\'/g, '"');
            $(this).datepicker(JSON.parse(options));
        }else{
            $(this).datepicker();
        }
    });
});