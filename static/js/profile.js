const months = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}
const faviconContainer = document.querySelectorAll('.user_favicon');
const editButton = document.querySelector('.edit_profile');
const editContainer = document.querySelector('.edit_user_profile');
const topSection = document.querySelector('.user_section_top');
const middleSection = document.querySelector('.user_section_middle');
const bottomSection = document.querySelector('.user_section_bottom');
const editDisplay = document.querySelector('.edit_profile_display');

faviconContainer.forEach(favicon => {
    // TOGGLE OPTIONS FUNCTIONALITY
    const optionToggle = favicon.querySelector('.user_options');
    const options = favicon.querySelector('.user_option_list');
    optionToggle.addEventListener('click', () => {
        options.classList.toggle('open_options');
    });
    // COPY HTML TO CLIPBOARD FUNCTIONALITY
    const copyButton = favicon.querySelector('.user_btn');
    copyButton.addEventListener('click', () => {
        const text = `
            <link rel="apple-touch-icon" sizes="180x180" href="/favicon180x180.png">
            <link rel="icon" sizes="32x32" href="/favicon32x32.png" >
            <link rel="icon" sizes="16x16" href="/favicon16x16.png">
            <link rel="manifest" href="/site.webmanifest">`;
        navigator.clipboard.writeText(text);
    });
    // CREATION DATE FUNCTIONALITY
    const creationDate = favicon.querySelector('.favicon_date');
    const currentYear = new Date().getFullYear();
    const currentMonth = new Date().getMonth();
    const currentDay = new Date().getDate();
    let previousDate = creationDate.dataset.date;
    previousDate = previousDate.split(' ');
    const previousYear = previousDate[2];
    const previousMonth = months[previousDate[0].slice(0, -1)];
    const previousDay = eval(previousDate[1].slice(0, -1));
    if (currentYear - previousYear >= 1) {
        creationDate.innerText = `Created ${currentYear - previousYear} ${(currentYear - previousYear > 1) ? 'years' : 'year'} ago`;
    } else if (currentMonth - previousMonth >= 1) {
        creationDate.innerText = `Created ${currentMonth - previousMonth} ${(currentMonth - previousMonth > 1) ? 'months' : 'month'} ago`;
    } else if (currentDay - previousDay >= 1) {
        creationDate.innerText = `Created ${currentDay - previousDay} ${(currentDay - previousDay > 1) ? 'days' : 'day'} ago`;
    } else {
        creationDate.innerText = `Created today`;
    }
});

// EDIT PROFILE FUNCTIONALITY
// EDIT TOGGLE FUNCTIONALITY
editButton.addEventListener('click', () => {
    topSection.classList.add('isEditting');
    editDisplay.classList.add('showEditDisplay');
    middleSection.style.display = 'none';
    bottomSection.style.display = 'none';
    editContainer.style.display = 'none';
});

// EDIT IMAGE PREVIEW FUNCTIONALITY
const editImage = document.querySelector('.user_img img');
const watchImage = document.querySelector('#new_image');
watchImage.addEventListener('change', () => {
    const file = new_image.files[0];
    previewFile(file);
})
function previewFile(file) {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = function (e) {
        editImage.src = reader.result;
    }
}