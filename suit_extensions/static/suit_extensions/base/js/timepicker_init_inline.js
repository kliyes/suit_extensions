// execute after page load
// ref: https://css-tricks.com/snippets/jquery/run-javascript-only-after-entire-page-has-loaded/
$(window).bind("load", function() {
    $("div.add-row").click(function(){
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
});