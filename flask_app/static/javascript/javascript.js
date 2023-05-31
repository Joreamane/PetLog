function invalidLogin() {
    if ("{{ get_flashed_messages(category_filter = ['login']) == True }}") {
        var element = document.getElementById("email")
        element.classList.add("is-invalid")
    }
}
