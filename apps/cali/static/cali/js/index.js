$(document).ready(function () {

    /* Navigation scroll */
    $(function () {
        $('a[href*=#]:not([href=#])').click(function () {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        });
    });

    // $('#onclick_menu').click(function (e) {
    //     $.ajax({
    //         type: "GET",
    //         url: "121.0.0.1:8000/menu",
    //     });
    //     return false;
    // });

    // Active link switching//
    // $(window).scroll(function() {
    //     var scrollbarLocation = $(this).scrollTop();

    //     scrollLink.each(function() {
    //         var sectionOffset = $(this.hash).offset().top

    //         if(sectionOffset <= scrollbarLocation) {
    //             $(this).parent().addClass('active');
    //             $(this).parent().siblings().removeClass('active');
    //         }
    //     })
    // });

    $(".close_menu").click(function () {
        $(".sidebar_menu").addClass("hide_menu");
        $(".toggle_menu").addClass("opacity_one");
        $(".title").addClass("opacity_one");
    });

    $(".toggle_menu").click(function () {
        $(".sidebar_menu").removeClass("hide_menu");
        $(".toggle_menu").removeClass("opacity_one");
        $(".title").removeClass("opacity_one")
    });
});