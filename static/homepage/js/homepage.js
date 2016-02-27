$(document).ready(function(){
  console.log('homepage.js')

  $('#nav-list > ul > li').mouseenter(function(){
    console.log($(this))
  })

  $('#email-me-form').submit(function(e){
    e.preventDefault()

    $.post('/email_me/', $(this).serialize(), function(response){
      if (response == 'success' ){
        $('[name="email-me-message"]').val('')
        $('button').after('<h4 class="message-success">Message Sent. Thanks!</h4>')
      } else {
        console.log(response)
      }
    })
    return false
  })

})
