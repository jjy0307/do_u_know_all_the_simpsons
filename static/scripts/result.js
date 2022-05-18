new Chart(document.getElementById("bar-chart"), {
    type: 'bar',
    data: {
        labels: ["심슨1", "심슨2", "심슨3", "심슨4", "심슨5"],
        datasets: [
            {
                label: "Population (millions)",
                backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
                data: [10,
                       8,
                       6,
                       4,
                       2]
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