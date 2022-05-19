var modals = document.getElementsByClassName("modal");
var btns = document.getElementsByClassName("open-popup");
var closes = document.getElementsByClassName("close-popup");
var funcs = [];

function Modal(num) {
    return function () {
        btns[num].onclick = function () {
            modals[num].style.display = "block";
            console.log(num);
        };

        closes[num].onclick = function () {
            modals[num].style.display = "none";
        };
    };
}

for (var i = 0; i < btns.length; i++) {
    funcs[i] = Modal(i);
}

for (var j = 0; j < btns.length; j++) {
    funcs[j]();
}

function comment_get() {
    $('#comment-box').empty()
    $.ajax({
        type: 'GET',
        url: '/modal/comment',
        data: {},
        success: function (response) {
            let comments = response['comments']
            for (let i = 0; i < comments.length; i++) {
                let comment = comments[i]['comment']

                let temp_html = `<p>${comment}</p>`
                $('#comment-box').append(temp_html)
            }

        }
    })
}

function comment_save() {
    let comment = $('#comment-detail').val()

    $.ajax({
        type: 'POST',
        url: '/modal/comment',
        data: {
            comment_give: comment
        },
        success: function (response) {
            console.log(response['msg'])
        }
    })
    comment_get()
}


