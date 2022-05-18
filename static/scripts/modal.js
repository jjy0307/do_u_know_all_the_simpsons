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

