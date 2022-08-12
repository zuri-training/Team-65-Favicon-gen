const openSidebar = document.querySelector('.header_hamburger');
const closeSidebar = document.querySelector('.close_sidebar');
const sidebar = document.querySelector('.header_sidebar');

openSidebar.addEventListener('click', () => {
    sidebar.classList.add('open_sidebar');
    setTimeout(() => document.body.classList.add('body_modal'), 500);
});
closeSidebar.addEventListener('click', () => {
    sidebar.classList.remove('open_sidebar')
    setTimeout(() => document.body.classList.remove('body_modal'), 500);
});