function review() {
    let evaluation = $('#comment').val()
    let cookies = document.cookie.split(';')
    let result = null
    for (let i=0; i<cookies.length; i++) {
        let cookie = cookies[i].trim()
        if (cookie.startsWith('result=')) {
            result = cookie.split('=')[1]
        }
    }
    // const result = document.cookie.split(';')[1].split('result=')[1]
    $.ajax({
        type: "POST",
        url: "/comment",
        data: {
            'comment': evaluation,
            'result': result
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert('작성 완료!');
            }
        }
    })
}