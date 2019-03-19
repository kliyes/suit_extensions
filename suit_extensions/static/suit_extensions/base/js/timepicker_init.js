$(document).ready(function(){
    $("input[timepicker=1]").each(function(){
        var options = $(this).data("timepicker-options");
        if (options !== ""){
            options = options.replace(/\'/g, '"');
            $(this).timepicker(JSON.parse(options));
        }else{
            $(this).timepicker();
        }
    });
});