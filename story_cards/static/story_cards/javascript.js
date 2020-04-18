function translate_word() {
    let address = '/story_cards/translate/?word=';
    let word = $("#id_source_word").val();
    address = address.concat(word);
    $.ajax({
        type: 'GET',
        url: address,
        success: function (data) {
            let target_word = $("#id_target_word");
            target_word.html(data);
        },
        error: function (data) {
            alert('Something went wrong');
        }
    });
}

document.addEventListener("DOMContentLoaded", function () {
    let source_input = $("#id_source_word");
    source_input.click(translate_word);
});