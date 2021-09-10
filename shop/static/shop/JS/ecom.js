function getcart(flag){
    if(flag=='0'){
        var cart=JSON.parse(document.getElementById('cartdata').value)
        var len=Object.keys(cart).length;
        document.getElementById('lencart').innerText=len;
        localStorage.setItem('cart', JSON.stringify(cart))
    }
    else{
        function cartlen(){
            var cart=JSON.parse(localStorage.getItem('cart'));
            var len=Object.keys(cart).length;
            document.getElementById('lencart').innerText=len;
        }
        if(localStorage.getItem('cart')==null)
            localStorage.setItem('cart','{}');
        cartlen();
    }
}

flag=document.getElementById('cartdata').getAttribute('flag')
console.log(flag)
getcart(flag)