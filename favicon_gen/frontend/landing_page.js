let browse = document.getElementById("index_browse");
let generate = document.getElementById("index_generate");

let input = document.createElement('input');
input.type = 'file';
input.name = 'uploaded_image';

browse.addEventListener("click", () => {
    input.click();
});


let drop_zone = document.getElementById("index_drop_zone");

drop_zone.addEventListener("drop", (ev) => {
    ev.preventDefault();

    input = document.createElement('input');
    input.type = 'file';
    input.name = 'uploaded_image';

    input.files = ev.dataTransfer.files;
    
    drop_zone.style.backgroundColor = "#ffffff";

});


drop_zone.addEventListener("dragover", (ev) => {
    ev.preventDefault();

    drop_zone.style.backgroundColor = "#d1d1d1";

});


drop_zone.addEventListener("dragleave", (ev) => {
    ev.preventDefault();

    drop_zone.style.backgroundColor = "#ffffff";

});


// submit form
let form = document.createElement("form");

form.method = 'POST';
form.action = '';
form.enctype = "multipart/form-data";

form.append(input);


generate.addEventListener("click", (ev) => {
    form.submit();

});


// cards
