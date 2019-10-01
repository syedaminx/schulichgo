$(document).ready(function() {

  // star ratings
  $('.rating').rating({
    initialRating: 0,
    maxRating: 5
  });

  $('.rating').rating('disable')

  // syllabus upload modal
  $('#upload-syllabus').click(function() {
    $('#upload-modal').modal('show');

    var url = $('#syllabus-form-ajax').attr('url')
    var method = $('#syllabus-form-ajax').attr('method')

    function upload(event) {
      event.preventDefault();
      var data = new FormData($('#syllabus-form-ajax').get(0));

      $.ajax({
        url: url,
        type: method,
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function(data) {
          location.reload();
          alert('success');
        }
      });
      return false
    }

    $(function() {
      $('#syllabus-submit-ajax').click(upload);
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
