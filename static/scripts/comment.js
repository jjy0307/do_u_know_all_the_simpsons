$(document).ready(function () {
    show_comment();
});

function show_comment() {
    $('#comment-box').empty()
    $.ajax({
        type: 'GET',
        url: '/comments',
        data: {},
        success: function (response) {
            let rows = response['comments']
            for (let i = 0; i < rows.length; i++) {
                let comment = rows[i]['comment']
                let num = rows[i]['num']

                let temp_html = `
                                    <div>
                                        <p>${comment}<button class="delete-btn" onclick="delete_comment(${num})">삭제</button></p>
                                    </div>
                                  `
                $('#comment-box').append(temp_html)
            }
        }
    });
}

function save_comment() {

    let comment = $('#comments').val()

    $.ajax({
        type: 'POST',
        url: '/comments',
        data: {comment_give: comment},
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    });
}

function delete_comment(num) {
    $.ajax({
        type: 'POST',
        url: '/delete',
        data: {count: num},
        success: function (response) {
            alert(response['msg']);
            window.location.reload()
        }
    });
}