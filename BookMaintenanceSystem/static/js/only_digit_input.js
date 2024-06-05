var $priceInput = $('#price');

$priceInput.on('keypress', function(event) {
  
  var keyCode = event.which || event.keyCode;

  // 允許數字鍵（0-9）和 backspace(8)
  if ((keyCode < 48 || keyCode > 57) && keyCode !== 46 && keyCode !== 8) {
    event.preventDefault();
  }
});