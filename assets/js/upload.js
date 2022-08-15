const uploadForm = document.querySelector('.upload_label');
const uploadInput = document.querySelector('#imageForm');
const previewBox = document.querySelector('.preview_img');
const copyText = document.querySelector('#copy_text');
const copyBtn = document.querySelector('#copy_btn');
const isUploadingShow = document.querySelector('.isUploading');

// DRAG AND DROP FUNCTIONALITY
function isUploading() {
    isUploadingShow.style.display = 'block';
}
function previewFile(file) {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = function (e) {
        const img = document.createElement('img');
        img.src = reader.result;
        img.alt = file.name;
        previewBox.appendChild(img);
    }
}
function uploadFile(file) {
    const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const formData = new FormData();
    formData.append('image', file);
    const xhr = new XMLHttpRequest();
    xhr.onload = function () {
        if (xhr.status === 200) {
            window.location.href = '/';
            window.location.reload();
        }
    }
    xhr.open('POST', '/my-favicons/');
    xhr.setRequestHeader('X-CSRFToken', token);
    xhr.send(formData);
    isUploading();
}
function highlightZone(e) {
    e.preventDefault();
    e.stopPropagation();
    uploadForm.classList.add('over');
}
function unhighlightZone(e) {
    e.preventDefault();
    e.stopPropagation();
    uploadForm.classList.remove('over');
}
['dragenter', 'dragover'].forEach(eventName => { uploadForm.addEventListener(eventName, highlightZone) });
['dragleave', 'drop'].forEach(eventName => { uploadForm.addEventListener(eventName, unhighlightZone) });
uploadForm.addEventListener('drop', handleDrop);
function handleDrop(e) {
    const files = e.dataTransfer.files;
    const file = files[0];
    previewFile(file);
    uploadFile(file);
}
uploadInput.addEventListener('change', () => {
    const file = imageForm.files[0];
    previewFile(file);
})

// COPY TEXT FUNCTIONALITY
text = copyText.innerText;
copyBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(text);
});