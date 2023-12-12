$(document).ready(function(){
    let slide_number = 1;
    function background_changer(some_number){
        $('.category-advertismant-slider').removeClass('f s t');
        switch (some_number){
            case 1:
                $('.category-advertismant-slider').addClass('f');
                break;
            case 2:
                $('.category-advertismant-slider').addClass('s');
                break;
            case 3:
                $('.category-advertismant-slider').addClass('t');
                break;
        };
            
        

    };
    $('.slide_left').click(function(){
        switch (slide_number){
            case 2:
                $('.slider-child-second').removeClass('active');
                $('.slider-child-first').addClass('active');
                slide_number--;
                break;
            case 3:
                $('.slider-child-third').removeClass('active');
                $('.slider-child-second').addClass('active');
                slide_number--;
                break;
            case 1:
                $('.slider-child-first').removeClass('active');
                $('.slider-child-third').addClass('active');
                slide_number = 3;
                break;
        };
        background_changer(slide_number);
    });
    $('.slide_right').click(function(){
        switch (slide_number){
            case 1:
                $('.slider-child-first').removeClass('active');
                $('.slider-child-second').addClass('active');
                slide_number++;
                break;
            case 2:
                $('.slider-child-second').removeClass('active');
                $('.slider-child-third').addClass('active');
                slide_number++;
                break;
            case 3:
                $('.slider-child-third').removeClass('active');
                $('.slider-child-first').addClass('active');
                slide_number = 1;
                break;
        };
        background_changer(slide_number);
    });
});