
fetch('http://127.0.0.1:8000/home/',{
            mode: 'no-cors',
            method: "get",
            headers: {
                 "Content-Type": "application/json"
            },
 })
        .then(res => res.json())
        .then(data => {console.log(data)})
//post = getElementsByClassName("post")
//p = createElement("p")

//document.body.insertBefore(newDiv, currentDiv)
function fetch(data):
console.log(data)