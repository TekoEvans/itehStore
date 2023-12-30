function loadImagePicker(id) {
    document.getElementById(id + "Upload").onchange = function (event) {
        document.getElementById(id + "Img").src = URL.createObjectURL(event.target.files[0]);
        document.getElementById(id + "Label").innerHTML = "Changer l'image"
    };
}

function load(id, event) {
    document.getElementById(id + "Img").src = URL.createObjectURL(event.target.files[0]);
    document.getElementById(id + "Label").innerHTML = "Changer l'image"
}

const imagePickersId = [
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



