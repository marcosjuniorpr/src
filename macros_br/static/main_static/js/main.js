$(document).ready(function(){

   //mobile menu toggle button
    $("#mobile-menu-button").click(function(){
     
       $("#mobile-menu-list").fadeToggle( "slow", "linear" );

    });

   //////////////////////any where click menu hide
    var $menu = $('#mobile-menu-list');
    var $mainButton = $("i.fa.fa-bars.side-menu-bar");

    $(document).mouseup(function (e) {
       if (!$menu.is(e.target) // if the target of the click isn't the container...
       && !$mainButton.is(e.target)) // ... nor a descendant of the container
       {
         $menu.fadeOut(600);
      }
     }); 


   
   ///////////////////////current date
   var date = new Date();
   var strDate = date.getFullYear() + "/" + (date.getMonth()+1) + "/" + date.getDate();
   var time = date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
   $("#print-current-date").html(strDate);
   $("#print-current-time").html(time);
   $("#print-current-date1").html(strDate);
   $("#print-current-time1").html(time);
   console.log(strDate)

    
   $("#top-textbox-button").click(function(){
        $("#contact-from-box ").show( "slow" );
   }); 

   //////////////////////////hide contact from
   $("i.fas.fa-times").click(function(){
      $("#contact-from-box").hide( "slow" );
   })



})


$(document).scroll(function() {
	//Main Menu
           if($(window).scrollTop() > 50){

            $("#main-menu").css("background","#19202ee0");
 
           }else if($(window).scrollTop() < 50){

            $("#main-menu").css("background","");
  
           }

    //Mobile menu
           if($(window).scrollTop() > 50){

            $("#mobile-menu").css("background","#19202ee0");
 
           }else if($(window).scrollTop() < 50){

            $("#mobile-menu").css("background","");
  
           }
       
    });