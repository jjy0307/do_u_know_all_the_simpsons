function review() {
    let evaluation = $('#comment').val()
    const result = document.cookie.split(';')[1].split('result=')[1]
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