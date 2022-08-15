const review_container = document.querySelector('#index_card_container');
const startSlider = () => {
    // get all three slides active,last next
    const active = document.querySelector('.review_active')
    const last = document.querySelector('.review_last')
    let next = active.nextElementSibling
    if (!next) {
        next = review_container.firstElementChild
    }
    active.classList.remove('review_active')
    last.classList.remove('review_last')
    next.classList.remove('review_next')

    active.classList.add('review_last')
    last.classList.add('review_next')
    next.classList.add('review_active')
}
window.addEventListener('load', () => setInterval(startSlider, 10000))