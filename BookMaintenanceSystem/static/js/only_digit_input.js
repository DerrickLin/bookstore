var priceInput = document.getElementById('price');
        
// 監聽鍵盤按下事件
priceInput.addEventListener('keypress', function (event) {
    // 獲取按下的鍵的鍵碼
    var keyCode = event.which || event.keyCode;

    // 允許數字鍵（0-9）、小數點和退格鍵
    if ((keyCode < 48 || keyCode > 57) && keyCode !== 46 && keyCode !== 8) {
        event.preventDefault();
    }
});