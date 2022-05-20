function ABC() {
    let evaluation = $("#comment").val()
    $.ajax({
        type: "POST",
        url: "/comment",
        data: {
            'comment': evaluation
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert('작성 완료!');
            }
        }
    })
}

new Chart(document.getElementById("bar-chart"), {
    type: 'bar',
    data: {
        labels: ["심슨1", "심슨2", "심슨3", "심슨4", "심슨5"],
        datasets: [
            {
                label: "Population (millions)",
                backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
                data: [1,
                    1,
                    1,
                    1,
                    1]
            }
        ]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: '사진에 나온 심슨들(명)'
        }
    }
});