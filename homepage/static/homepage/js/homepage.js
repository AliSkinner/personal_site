$(document).ready(function(){

  $('#fork').tooltip()

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
