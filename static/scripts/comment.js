// $(document).ready(function () {
//     show_comment();
// });

// function show_comment() {
//     $('#comment-box').empty()
//     $.ajax({
//         type: 'GET',
//         url: '/comments',
//         data: {},
//         success: function (response) {
//             let rows = response['comments']
//             for (let i = 0; i < rows.length; i++) {
//                 let comment = rows[i]['comment']
//                 let num = rows[i]['num']
//
//                 let temp_html = `
//                                     <div>
//                                         <p>${comment}<button class="delete-btn" onclick="delete_comment(${num})">삭제</button></p>
//                                     </div>
//                                   `
//                 $('#comment-box').append(temp_html)
//             }
//         }
//     });
// }

function save_comment(id) {

    let comment = $('#comments').val()
    let comment_id = document.getElementById(id).id
    let character_name = comment_id.split("-")[0]
    $.ajax({
        type: 'POST',
        url: '/comments',
        data: {
            comment_give: comment,
            character: character_name
        },
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    });
}

function delete_comment(id) {
    let button_id = document.getElementById(id).id;
    let character = button_id.split("+")[0];
    let content = button_id.split("+")[1];
    $.ajax({
        type: 'POST',
        url: '/delete',
        data: {
            character_name: character,
            comment: content
        },
        success: function (response) {
            alert(response['msg']);
            window.location.reload()
        }
    });
}