// let post = document.get('post');
// let p = document.createElement("p");
// post.append(p);

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
        var len = data.length
        for (let i = 0; i < len; i++) {
            let li = document.createElement("li");
            var a = document.createElement("button");
            let ne = data[i];
            a.getAttribute('class');
            at = document.createAttribute("class");
            id = document.createAttribute("id");
            at.value = "category" + (i+1);
            id.value = i+1;
            a.setAttributeNode(id);
            a.setAttributeNode(at);
            a.append(ne.category);
            li.append(a);
            bar.appendChild(li)}
            for (let y = 0; y < (len+1); y++) {
                var a = document.getElementsByClassName("category"+(y))[0]
                console.log(a)
                document.getElementsByClassName("category"+ (y))[0].addEventListener('click', function() {
                    post = document.getElementById("post").innerHTML = "";
                    let r = document.getElementsByClassName("category"+ y)[0].getAttribute('id')
                    console.log(r)
                    filter(r)})
        }
    
        return console.log(200)
})
// let bar = document.getElementById("bar");
// document.getElementsByClassName("category0")[0].addEventListener('click', function() {
//     post = document.getElementById("post").innerHTML = "";
//     let r = document.getElementsByClassName("category0")[0].getAttribute('id')
//     console.log(r)
//     filter(r)})
let filter = function(r){
    if (r == 0){fetch('http://127.0.0.1:8000/home/', {
        method: 'GET',
        headers: {
        "Content-Type": "application/json",
            accept: 'index.html',
        },})
        .then(res => res.json())
        .then(function(data) {
        for (let i = 0; i < data.length; i++) {
            let ne = data[i];
            post = document.getElementById("post");
            let p = document.createElement("p");
            let img = document.createElement("img");
            let h1 = document.createElement("h1");
            console.log(content)
            console.log(post)
            content.append(post);
            console.log(p)
            console.log(img)
            console.log(h1)
            src = document.createAttribute("src");
            src.value = ne.img;
            img.setAttributeNode(src);
            console.log(ne.img)
            p.append(h1)
            p.append(img)
            p.append(ne.description);
            h1.append(ne.name);
            img.append(ne.img);
            console.log(post)
            post.append(p)}
            return console.log(200)}
            )}
    else
    {fetch('http://127.0.0.1:8000/home/', {
        method: 'GET',
        headers: {
        "Content-Type": "application/json",
            accept: 'index.html',
        },})
        .then(res => res.json())
        .then(function(data) {
        for (let i = 0; i < data.length; i++) {
            let ne = data[i];
            if (r == ne.category_id){
                post = document.getElementById("post");
                let p = document.createElement("p");
                let img = document.createElement("img");
                let h1 = document.createElement("h1");
                let ne = data[i];
                console.log(content)
                console.log(post)
                content.append(post);
                console.log(p)
                console.log(img)
                console.log(h1)
                src = document.createAttribute("src");
                src.value = ne.img;
                img.setAttributeNode(src);
                console.log(ne.img)
                p.append(h1)
                p.append(img)
                p.append(ne.description);
                h1.append(ne.name);
                img.append(ne.img);
                console.log(post)
                post.append(p)}}
            return console.log(200)}
            )
    }
}




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

col = document.querySelectorAll('button')
console.log(col)