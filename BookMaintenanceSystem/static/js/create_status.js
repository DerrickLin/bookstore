var codeBorrowed = 'B';
var codeAvailable = 'Y';
var codeUnavailable = 'N';
$(document).ready(function() {
    // 选择借阅人时自动选择对应的借阅状态为"已借出"
    $('#borrower').change(function() {
        
        console.log(codeBorrowed);
        var borrowerId = $(this).val();
        var statusSelect = $('#status');
        
        // 重置借阅状态选项
        statusSelect.val('');
        
        if (borrowerId) {
            // 选中"已借出"的选项
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