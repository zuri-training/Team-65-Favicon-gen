const openSidebar = document.querySelector('.header_hamburger');
const closeSidebar = document.querySelector('.close_sidebar');
const sidebar = document.querySelector('.header_sidebar');
const footerYear = document.querySelector('.footer_year');
const faviconDrop = document.getElementById('favicon');
const faviconDropBox = document.querySelector('.header_dropdown_box[data-drop="favicon"]');
const helpDrop = document.getElementById('help&support');
const helpDropBox = document.querySelector('.header_dropdown_box[data-drop="help&support"]');

openSidebar.addEventListener('click', () => {
    sidebar.classList.add('open_sidebar');
    setTimeout(() => document.body.classList.add('body_modal'), 500);
});
closeSidebar.addEventListener('click', () => {
    sidebar.classList.remove('open_sidebar')
    setTimeout(() => document.body.classList.remove('body_modal'), 500);
});
footerYear.innerText = new Date().getFullYear();
// DROP DOWN MENU FOR FAVICON AND HELP & SUPPORT
faviconDrop.addEventListener('click', () => {
    const nav_bottom = faviconDrop.getBoundingClientRect().bottom;
    const nav_left = faviconDrop.getBoundingClientRect().left;
    faviconDrop.classList.toggle('active');
    const icon = faviconDrop.querySelector('i');
    icon.classList.toggle('fa-sort-up');
    faviconDropBox.style.top = `${nav_bottom + 16}px`;
    faviconDropBox.style.left = `${nav_left - 16}px`;
    faviconDropBox.classList.toggle('open_dropdown');
});
helpDrop.addEventListener('click', () => {
    const nav_bottom = helpDrop.getBoundingClientRect().bottom;
    const nav_left = helpDrop.getBoundingClientRect().left;
    helpDrop.classList.toggle('active');
    const icon = helpDrop.querySelector('i');
    icon.classList.toggle('fa-sort-up')
    helpDropBox.style.top = `${nav_bottom + 16}px`;
    helpDropBox.style.left = `${nav_left + 16}px`;
    helpDropBox.classList.toggle('open_dropdown');
});