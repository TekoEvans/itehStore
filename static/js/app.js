function loadImagePicker(id) {
    document.getElementById(id + "Upload").onchange = function (event) {
        document.getElementById(id + "Img").src = URL.createObjectURL(event.target.files[0]);
    };
}

function load(id, event) {
    document.getElementById(id + "Img").src = URL.createObjectURL(event.target.files[0]);
}

function loadAdd(id, event) {
    id = id + "AddForm"
    document.getElementById(id + "Img").src = URL.createObjectURL(event.target.files[0]);
}

const imagePickersId = [
    'logo',
    'header',
    'about',
    'contact',
    'main',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six'
]

imagePickersId.forEach(id => {
    loadImagePicker(id)
});



