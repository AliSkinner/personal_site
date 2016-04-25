$(document).ready(function(){
  console.log('common.js')

  $('#fork').tooltip()

  $(window).on('resize',function(){
     var winWidth =  $(window).width();
     if(winWidth < 768 ){
        console.log('Window Width: '+ winWidth + 'class used: col-xs');
     }else if( winWidth <= 991){
        console.log('Window Width: '+ winWidth + 'class used: col-sm');
     }else if( winWidth <= 1199){
        console.log('Window Width: '+ winWidth + 'class used: col-md');
     }else{
        console.log('Window Width: '+ winWidth + 'class used: col-lg');
     }
  });
})
