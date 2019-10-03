$(document).ready(function() {

  $('input:text, .ui.button', '.ui.action.input').on('click', function (e) {
    $('input:file', $(e.target).parents()).click();
});

$('input:file', '.ui.action.input').on('change', function (e) {
    var name = e.target.files[0].name;
    $('input:text', $(e.target).parent()).val(name);
});

  // star ratings
  $('.rating').rating({
    initialRating: 0,
    maxRating: 5
  });

  $('.rating').rating('disable')

  // closing messages
  $('.message .close')
    .on('click', function() {
      $(this)
        .closest('.message')
        .transition('fade')
      ;
    })
  ;

  // syllabus upload modal
  $('#upload-syllabus').click(function() {
    $('#upload-modal').modal('show');

    var url = $('#syllabus-form-ajax').attr('url')
    var method = $('#syllabus-form-ajax').attr('method')

    console.log(url)

    function upload(e) {
      e.preventDefault();
      var file = $('#id_syllabus').prop('files')[0];

      valid_type = false
      valid_size = false

      // checking to see if file was uploaded
      if (file == undefined) {
        $('.ui.container').prepend('<div class="ui negative message"><i class="close icon"></i><div class="header">Please upload a file.</div></div>');
      }

      // checking to see file is a pdf
      if (file.type == "application/pdf") {
        valid_type = true
      } else {
        valid_type = false
        $('.ui.container').prepend('<div class="ui negative message"><i class="close icon"></i><div class="header">Please upload a syllabus in PDF form.</div></div>');
      }

      // checking to see file is <5 mb
      if (file.size <= 5242880) {
        valid_size = true
      } else {
        valid_size = false
        $('.ui.container').prepend('<div class="ui negative message"><i class="close icon"></i><div class="header">Please upload a syllabus in PDF form that is under 5 MB.</div></div>');
      }

      if (valid_type == true && valid_size == true) {
        $('form#syllabus-form').submit();
      }

    }

    $(function() {
      $('#syllabus-submit-button').click(upload);
    });
  });

  // syllabus view modal
  $('#view-syllabus').click(function() {
    $('#view-modal').modal('show');
  });

  // instructor filtering
  var current_instructor = 0;

  $('.instructor-button').click(function() {
    var instructor = this.id;

    // if there is no instructor already selected
    if (current_instructor == 0) {
      current_instructor = instructor

      // hiding all the review divs
      $('.review').fadeOut(500)

      // checking to see if there is a review with the instructor selected
      if ($('.review[data-instructor="' + instructor + '"]').data('instructor') == undefined) {
        // if there isnt, let the user know
        $( '.message-div' ).show(500);
      } else {
        // otherwise, show the reviews that are for this instructor
        $('.review[data-instructor="' + instructor + '"]').fadeIn(500)
        $( '.message-div' ).hide();
      }
    } else {
      // if they click on the currently selected instructor
      if ($('.review[data-instructor="' + instructor + '"]').is(':visible') || ($('.review[data-instructor="' + instructor + '"]').data('instructor') == undefined)) {
        // show all the reviews
        $('.review').show(500)
        $( '.message-div' ).hide();
        current_instructor = 0
      } else {
        // if an instructor is selected and they choose another instructor
        current_instructor = instructor

        // hiding all the review divs
        $('.review').fadeOut(500)

        // checking to see if there is a review with the instructor selected
        if ($('.review[data-instructor="' + instructor + '"]').data('instructor') == undefined) {
          // if there isnt, let the user know
          $( '.message-div' ).show();
        } else {
          // otherwise, show the reviews that are for this instructor
          $('.review[data-instructor="' + instructor + '"]').fadeIn(500)
          $( '.message-div' ).hide();
        }
      }
    }
  });
});
