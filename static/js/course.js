$(document).ready(function() {

  // syllabus modal
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
});
