document.getElementById('clear-btn').addEventListener('click', function() {
    var form = document.forms['form1'];
    form.reset();
    for (var i = 0; i < form.elements.length; i++) {
      if (form.elements[i].type === 'text' || form.elements[i].type === 'select-one') {
        form.elements[i].value = '';
      }
    }
});
