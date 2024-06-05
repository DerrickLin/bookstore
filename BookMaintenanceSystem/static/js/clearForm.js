$('#clear-btn').on('click', function() {
  var $form = $('form[name="form1"]');
  $form[0].reset();
  $form.find('input[type="text"], select').val('');
});