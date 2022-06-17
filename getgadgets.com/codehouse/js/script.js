// not ready function


function notReady() {
    alert("This page is currently offline, please try again later, thank you!!!");
}

//password visibility

function showPassword() {
    var x = document.getElementById("password");
    var y = document.getElementById("eyeControl");
    if (x.type === "password") {
        x.type = "text";
        y.className = "fa fa-eye-slash";
    } else {
        x.type = "password";
        y.className = "fa fa-eye"
    }


}