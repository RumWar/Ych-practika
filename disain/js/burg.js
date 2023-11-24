col = document.querySelectorAll('p')
console.log(col)
document.querySelector('button').addEventListener('click', function() {
    document.getElementById('one').classList.toggle("hidden");
    document.getElementById('two').classList.toggle("hidden");
  })
