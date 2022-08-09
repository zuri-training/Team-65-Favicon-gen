let browse = document.getElementById("browse");
let generate = document.getElementById("generate");

let input = document.createElement('input');
input.type = 'file';

browse.addEventListener("click", () => {
    input.click();
});

input.addEventListener("change", () => {
    console.log(input.files)
    
});


let drop_zone = document.getElementById("drop_zone");

drop_zone.addEventListener("drop", (ev) => {
    ev.preventDefault();

    if(ev.dataTransfer.items) {
        for(let i = 0; i < ev.dataTransfer.items.length; i++) {
            if (ev.dataTransfer.items[i].kind === 'file') {
                const file = ev.dataTransfer.items[i].getAsFile();
                console.log(`… file[${i}].name = ${file.name}`);
            }
        }
    } else {
        for(let i = 0; i < ev.dataTransfer.files.length; i++) {
            console.log(`… file[${i}].name = ${ev.dataTransfer.files[i].name}`);
        }
    }

    
    drop_zone.style.backgroundColor = "#ffffff";


});


drop_zone.addEventListener("dragover", (ev) => {
    ev.preventDefault();

    drop_zone.style.backgroundColor = "#e1e1e1";

});


drop_zone.addEventListener("dragleave", (ev) => {
    ev.preventDefault();

    drop_zone.style.backgroundColor = "#ffffff";

});



let form = document.createElement("form");


// submit form
generate.addEventListener("click", (ev) => {
    form.submit();

});