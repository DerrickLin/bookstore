$(document).ready(function() {
    $(document).on('click', '#delete-book', function() {
        var bookId = $(this).data('book-id');
        var bookName = $(this).data('book-name');
  
        if (confirm('確定要刪除書籍 : [' + bookName + '] 嗎?')) {
            deleteBook(bookId);
        }

        function deleteBook(bookId) {
            $.ajax({
                url: '/book_delete/' + bookId,
                type: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                success: function(response) {
                    //alert(response.message);
                    if (response.message === 'unable') {
                        alert("此書外借中，無法刪除");
                    } else if (response.message === 'success'){
                        alert("刪除成功");
                        // 重新導向至書籍查詢頁面
                        window.location.href = '/book/';
                    }
                },
        
            });
        }
    });
});
