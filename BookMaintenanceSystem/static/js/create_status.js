var codeBorrowed = 'B';
var codeAvailable = 'Y';
var codeUnavailable = 'N';
$(document).ready(function() {

    $('#borrower').change(function() {
        
        console.log(codeBorrowed);
        var borrowerId = $(this).val();
        var statusSelect = $('#status');
        
        // 清空狀態選單
        statusSelect.val('');
        
        if (borrowerId) {
            // 借閱人選擇了借閱人，則狀態選單設置為已借出
            statusSelect.val(codeBorrowed);
        }
    });

    $('#status').change(function() {
        var statusValue = $(this).val();
        var borrowerSelect = $('#borrower');

        if (statusValue === codeAvailable || statusValue === codeUnavailable) {
            // 禁用並清空借閱人選單
            borrowerSelect.val('').prop('disabled', true);
        } else {
            // 啟用借閱人選單
            borrowerSelect.prop('disabled', false);
        }
    });
});




