$(document).ready(function() {
  //hide options
  $(".location_options").hide();
  $(".category_options").hide();

  //toggle categories
  $(".categories").click(function() {
    $(".category_options").slideToggle("slow", "swing");
    $(".location_options").slideUp();
  });

  //toggle locations
  $(".location").click(function() {
    $(".location_options").slideToggle("slow", "swing");
    $(".category_options").slideUp();
  });

  //toggle search page
  $("#bottom-widget").click(function() {
    $("#search-panel").fadeIn("slow", "swing");
  });
  $(".close-search").click(function() {
    $(".search-page").fadeOut("slow", "swing");
  });

  $("#dash").click(function() {
    $("#dashboard").fadeIn("slow", "swing");
  });
  $(".close-search").click(function() {
    $("#dashboard").fadeOut("slow", "swing");
  });
});
