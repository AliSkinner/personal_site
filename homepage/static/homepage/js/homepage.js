$(document).ready(function(){

<<<<<<< HEAD
  // $('#email-me-form').submit(function(e){
  //   e.preventDefault()
  //
  //   $.post('/email_me/', $(this).serialize(), function(response){
  //     if (response == 'success' ){
  //       $('[name="email-me-message"]').val('')
  //       $('button').after('<h4 class="message-success">Message Sent. Thanks!</h4>')
  //     } else {
  //       console.log(response)
  //     }
  //   })
  //   return false
  // })

  $('.project-tile').on('click', function(){
    var project = $(this)
      , name = project.data('name')
      , shortDescription = project.data('short-description')
      , longDescription = project.data('long-description')
      , projectUrl = project.data('project-url')
      , githubUrl = project.data('github-url')
      , image = project.find('img').attr('src')

    $('.modal-title').text(name)
    $('.project-image').attr('src', image)
    $('.project-short-description').text(shortDescription)
    $('.project-text').text(longDescription)
    $('.github-link').attr('href', githubUrl)
    $('.project-link').attr('href',projectUrl)

    $('.modal').modal('show')
  })

})
