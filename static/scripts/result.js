function review() {
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

function chart() {
    // let result_chart = $("#bar-chart").val()
    $.ajax({
        type: "GET",
        url: "/logs",
        data: {},
        success: function (response) {
            if (response['categorized_results'], response['']);
            chart();
        }
    })
}


new Chart(document.getElementById("bar-chart"), {
    type: 'bar',
    data: {
        labels: [['character_name']],
        datasets: [
            {
                label: "Population (millions)",
                backgroundColor: ["#3e95cd"],
                data: ['character_count']
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