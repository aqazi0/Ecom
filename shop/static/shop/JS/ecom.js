if(localStorage.getItem('cart')=='null')
{
    var len=0;
}
else{
    var cart=JSON.parse(localStorage.getItem('cart'));
    var len=Object.keys(cart).length;
}
document.getElementById('lencart').innerText=len;