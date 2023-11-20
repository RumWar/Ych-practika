//let data = fetch('http://127.0.0.1:8000/home/',{
//            mode: 'no-cors',
//            method: "get",
//            headers: {
//                 "Content-Type": "application/json"
//            },
// })
//        .then(res => res.json())
//        .then(data => {alert(data)})
let d = 12
console.log(d);
fetch('http://127.0.0.1:8000/home/', {
//    mode: 'no-cors',
    method: 'GET',
    headers: {
    "Content-Type": "application/json",
        accept: 'index.html',
    },})
    .then(res => res.json())
    .then(function(data) {
   for (let i = 0; i < 9; i++) {
  console.log(data[i]);}
        return console.log(200)
})

var s = [{"Select":"11", "PhotoCount":"12"},{"Select":"21", "PhotoCount":"22"}];