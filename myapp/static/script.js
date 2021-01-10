var copyicon = document.querySelector('img');
var password = document.getElementById('pass').innerText;

copyicon.onclick = function(){
    password.select();
    document.execCommand('copy');
}

