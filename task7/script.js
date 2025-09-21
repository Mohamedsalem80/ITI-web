function showDanger() {
    const contentDiv = document.querySelector('.content');
    contentDiv.style.backgroundColor = 'red';
}

function clearDanger() {
    const contentDiv = document.querySelector('.content');
    contentDiv.innerText = '';
}