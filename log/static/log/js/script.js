$(document).ready(function(){
  $(".filter").click(function(){
    $(".workout").not(".workout." + this.id).css("display", "none");
  });
});

