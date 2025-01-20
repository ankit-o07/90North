

const menuToggle = document.querySelector('.menu-toggle'); 

menuToggle.addEventListener('click', (e) => {
    const menu = document.querySelector(".left")
    menu.style.width = "250px"
});

const closebtn = document.querySelector(".closebtn");

closebtn.addEventListener('click',(e)=>{
    const menu = document.querySelector(".left")
    menu.style.width = "0"
})

// JavaScript function to adjust the page scaling
function adjustPageSize() {
    const superElement = document.querySelector('.super');

    if (window.innerWidth >= 992 && window.innerWidth <= 1600) {
        superElement.style.transform = 'scale(0.9)';
        superElement.style.transformOrigin = 'top center';
    } else if (window.innerWidth >= 700 && window.innerWidth < 767) {
        superElement.style.transform = 'scale(0.8)';
        superElement.style.transformOrigin = 'top center';
    } else if (window.innerWidth >= 600 && window.innerWidth < 700) {
        superElement.style.transform = 'scale(0.75)';
        superElement.style.transformOrigin = 'top center';
    } else if (window.innerWidth <= 600) {
        superElement.style.transform = 'scale(0.5)';
        superElement.style.transformOrigin = 'top center';
    } else {
        // Reset scaling for larger screens
        superElement.style.transform = 'scale(1)';
        superElement.style.transformOrigin = 'top center';
    }
}

// Add event listeners to handle window resizing
window.addEventListener('resize', adjustPageSize);
window.addEventListener('DOMContentLoaded', adjustPageSize);
