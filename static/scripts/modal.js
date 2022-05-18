const open = document.querySelector(".open-popup");
const close = document.querySelector(".close-popup");
const modal = document.querySelector('.modal');

open.addEventListener('click', () => {
    modal.classList.add('show');
});

close.addEventListener('click', () => {
    modal.classList.remove('show')
});