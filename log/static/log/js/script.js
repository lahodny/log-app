$(document).ready(function(){
  $(".filter").click(function(){
    //$(".workout").not(".workout." + this.id).css("display", "none");
      $(".workout").not(".workout." + this.id).toggle();

      if ($(".filter").hasClass("active")) {
          $(".filter").removeClass("active");
      }
      /*else if ($(this).hasClass("active");) {
        $(this).removeClass("active");
      }*/

      $(this).addClass("active");
  });
});


