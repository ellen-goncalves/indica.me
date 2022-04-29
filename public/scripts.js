function onOff(){
    document
        .querySelector("#modal")
            .classList
            .toggle("hide")
    document
        .querySelector("body")
        .classList
        .toggle("hideScroll")
    document
        .querySelector("#modal")
        .classList
        .toggle("addScroll")

}

function checkFields(event) {

    const valuesToCheck = [
        "title",
        "category",
        "image",
        "description",
        "url",
    ]

    const isEmpty = valuesToCheck.find(function(value){
        const checkifIsString = typeof event.target[value].value === "string"
        const checkIfIsEmpty = !event.target[value].value.trim()
        if(checkifIsString && checkIfIsEmpty){
            return true
        }
    })

    if(isEmpty) {
        event.preventDefault()
        alert("Por favor, preencha todos os campos")
    }
    /* for (let value of valuesToCheck) {
        console.log(event.target[value].value)
    } */
}

/* document
    .querySelector("button.fat")
    .addEventListener("click",function(){
        document
                window.scrollTo({
                top:0,
                behavior: 'smooth'
            })
            
    }) */
