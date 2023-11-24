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
    let img = document.createElement("img");
    let h1 = document.createElement("h1");
    let ne = data[i];
    src = document.createAttribute("src");
    src.value = ne.img;
    img.setAttributeNode(src);
    console.log(ne.img)
    p.append(h1)
    p.append(img)
    p.append(ne.description);
    h1.append(ne.name);
    img.append(ne.img);
    post.append(p)
    }
    post = document.getElementById("post");
        return console.log(200)
})
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
            let a = document.createElement("button");
            let ne = data[i];
            a.getAttribute('class', ne.category);
            at = document.createAttribute("class");
            at.value = ne.category;
            a.setAttributeNode(at);
            
            a.append(ne.category);
            li.append(a);
            bar.appendChild(li)}
    
        return console.log(200)
})

col = document.querySelectorAll('button')
console.log(col)