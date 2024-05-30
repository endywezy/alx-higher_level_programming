$(document).ready(function() {
  function fetchHello() {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    }).fail(function() {
      $('#hello').text('Error fetching the translation.');
    });
  }

  $('#btn_translate').click(fetchHello);

  $('#language_code').keypress(function(event) {
    if (event.which === 13) {
      fetchHello();
    }
  });
});
