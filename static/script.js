function validateText() {

    const textArea = document.querySelector("#text")
    const subBtn = document.querySelector("#sub-btn")

    if (textArea.length == 0) {
        subBtn.classList.add("disabled")
    } else {
        subBtn.classList.remove("disabled")
    }
}

validateText()