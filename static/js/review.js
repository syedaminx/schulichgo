$(document).ready(function() {

  // star ratings
  $('.rating').rating({
    initialRating: 0,
    maxRating: 5
  });

  // dropdown
  $('.ui.dropdown').dropdown();

  // anonymous toggle
  $('.ui.checkbox').checkbox();

  // form & validation
  $('.ui.form')
    .form({
      on: 'blur',
      fields: {
        taken_season: {
          identifier: 'season-dd',
          rules: [
            {
              type: 'empty',
              prompt: 'Please select a term.'
            }
          ]
        },
        taken_year: {
          identifier: 'year-dd',
          rules: [
            {
              type: 'empty',
              prompt: 'Please select a year.'
            }
          ]
        },
        instructor: {
          identifier: 'instructor-dd',
          rules: [
            {
              type: 'empty',
              prompt: 'Please select a instructor.'
            }
          ]
        },
        id_comment: {
          identifier: 'id_comment',
          rules: [
            {
              type: 'empty',
              prompt: 'Please write a comment about the course.'
            }
          ]
        }
      }
    });

    var rated = true

    function validate_ratings() {
      var usefulness_rating = $('#id_usefulness_rating').rating('get rating')
      var difficulty_rating = $('#id_difficulty_rating').rating('get rating')
      var instructor_rating = $('#id_instructor_rating').rating('get rating')

      if (usefulness_rating == 0) {
        $('ul').append("<li>Rate the usefulness of this course.</li>")
        rated = false
      }
      if (difficulty_rating == 0) {
        $('ul').append("<li>Rate the difficulty of this course.</li>")
        rated = false
      }
      if (instructor_rating == 0) {
        $('ul').append("<li>Rate the instructor for this course.</li>")
        rated = false
      }
      if (usefulness_rating > 0 && difficulty_rating > 0 && instructor_rating > 0) {
        rated = true
      }
    }

  $('#id_instructor').change(function() {
    if ($('#id_instructor').dropdown('get text') == "Other") {
      document.getElementById("other_instructor_div").style.display = "block";
    } else {
      document.getElementById("other_instructor_div").style.display = "none";
    }
  });

  $('#post-form').on('submit', function(event){
    event.preventDefault();
    validate_ratings();
    if( $('.ui.form').form('is valid') && rated == true) {
      submit_review();
    }
  });

  // submit review
  function submit_review() {

    if ($('#id_anonymous').checkbox('is checked') == true) {
      anonymous = true
    } else {
      anonymous = false
    }

    if ($('#id_instructor').dropdown('get text') == "Other") {
      other_instructor = $('#other_instructor_text').val();
    } else {
      other_instructor = ""
    }

    $.ajax({
      url: url_review,
      type: "POST",
      data: {
        taken_season: $('#id_taken_season').dropdown('get text'),
        taken_year: $('#id_taken_year').dropdown('get text'),
        instructor: $('#id_instructor').dropdown('get text'),
        other_instructor: other_instructor,
        usefulness_rating: $('#id_usefulness_rating').rating('get rating'),
        difficulty_rating: $('#id_difficulty_rating').rating('get rating'),
        instructor_rating: $('#id_instructor_rating').rating('get rating'),
        comment: $('#id_comment').val(),
        anonymous: anonymous,
        csrfmiddlewaretoken : csrf_token
      },
      success: function(redirect) {
        window.location.href=url_course
      },
      error: {
        alert: 'There has been an error.'
      }
    });
  };
});
