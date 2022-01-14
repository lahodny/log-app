$(document).ready(function(){
  $(".filter").click(function(){
      $(".workout").css("display", "block");
      if ($(this).hasClass("active")) {
          $(this).removeClass("active");
      }
      else{
          $(this).addClass("active");
          $(".workout").not(".workout." + this.id).css("display", "none");
      }
  });
});


