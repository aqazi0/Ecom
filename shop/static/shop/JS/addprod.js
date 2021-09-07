if(localStorage.getItem('cart')==null){
    localStorage.setItem('cart','{}')
}
else{
    var cart=JSON.parse(localStorage.getItem('cart'))
}

var atc=document.getElementsByClassName('prod')[0];
if(cart[atc.id]!=undefined)
{
    atc.innerHTML="Go to Cart";
}



$('.prod').click(function(){
    var myid=this.id.toString();
    if(cart[myid]==undefined){
        qty=1;
        var image=document.getElementById('pic').getAttribute('src');
        var name=document.getElementById('name').innerText;
        var price=document.getElementById('rate').innerText.slice(1,);
        cart[myid]=[qty,image,name,price];
        this.innerHTML="Go To Cart";
        this.class="btn btn-primary";
        document.getElementById('cartdata').value=JSON.stringify(cart);
        console.log(document.getElementById('cartdata').value)
        localStorage.setItem('cart',JSON.stringify(cart));
    }
})