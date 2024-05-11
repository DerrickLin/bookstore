document.addEventListener('DOMContentLoaded', function() {
    // 獲取表單元素
    var form = document.forms['form1'];

    // 監聽表單的 submit 事件
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // 阻止表單提交
        saveFormValuesToLocalStorage(form); // 將表單值保存到本地存儲中
        form.submit(); // 提交表單
    });

    // 恢復表單值
    restoreFormValuesFromLocalStorage(form);
});

// 將表單值保存到本地
function saveFormValuesToLocalStorage(form) {
    var formData = {};
    // 遍歷表單中的所有元素，將元素的 name 和 value 屬性保存到 formData 對象中
    for (var i = 0; i < form.elements.length; i++) {
        var element = form.elements[i];
        if (element.name && (element.type !== 'submit' && element.type !== 'reset')) {
            formData[element.name] = element.value;
        }
    }
    // 將 formData 對象轉換為 JSON 字符串，並保存到本地存儲中
    localStorage.setItem('formData', JSON.stringify(formData));
}

// 從本地存儲中恢復表單值
function restoreFormValuesFromLocalStorage(form) {
    var formData = JSON.parse(localStorage.getItem('formData'));
    if (formData) {
        // 將 formData 對象中的值填充回表單中的相應輸入字段中
        for (var i = 0; i < form.elements.length; i++) {
            var element = form.elements[i];
            if (element.name && formData[element.name]) {
                element.value = formData[element.name];
            }
        }
    }
}
