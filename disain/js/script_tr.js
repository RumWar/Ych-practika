// let post = document.get('post');
// let p = document.createElement("p");
// post.append(p);
fetch('http://127.0.0.1:8000/home/', {
    method: 'GET',
    headers: {
    "Content-Type": "application/json",
        accept: 'index.html',
    },})
    .then(res => res.json())
    .then(function(data) {
    for (let i = 0; i < data.length; i++) {
    let p = document.createElement("p");
    let ne = data[i];
    console.log(post)
    p.append(ne.name);
    post.append(p)}
    post = document.getElementById("post");
        return console.log(200)
})
bar = document.getElementById("bar")
console.log(bar);
fetch('http://127.0.0.1:8000/category/', {
    method: 'GET',
    headers: {
    "Content-Type": "application/json",
        accept: 'index.html',
    },})
    .then(res => res.json())
    .then(function(data) {
        let bar = document.getElementById("bar");
        console.log(bar);
        for (let i = 0; i < data.length; i++) {
            let li = document.createElement("li");
            let a = document.createElement("a");
            a.href="";
            let ne = data[i];
            console.log(bar)
            a.append(ne.category);
            li.append(a);
            bar.appendChild(li)}
    
        return console.log(200)
})