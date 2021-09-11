if(localStorage.getItem('cart')==null){
    localStorage.setItem('cart','{}')
}
else{
    var cart=JSON.parse(localStorage.getItem('cart'));
    var l=Object.keys(cart).length;
    function showcart(cart){
        var cartRowContents ="";
        var cartItems = document.getElementsByClassName('cart-items')[0];
        for (const key in cart) {
            var prodid=key.slice(2,)
            cartRowContents+=`
            <div class='cart-row'>
            <div class="cart-item cart-column">
                <img class="cart-item-image" src="`+ cart[key][1] +`" width="100" height="100">
                <span class="cart-item-title">` + cart[key][2] + `</span>
            </div>
            <span class="cart-price cart-column">₹` + cart[key][3] + `</span>
            <div class="cart-quantity cart-column">
            <span class="cart-quantity-input">` + cart[key][0] + `</span>
            </div>
            </div>`;
            cartItems.innerHTML = cartRowContents;
        }
    }

    function updateCartTotal(cart) {
        var cartItemContainer = document.getElementsByClassName('cart-items')[0]
        var cartRows = cartItemContainer.getElementsByClassName('cart-row')
        var total = 0
        for (var i = 0; i < cartRows.length; i++) {
            var cartRow = cartRows[i]
            var priceElement = cartRow.getElementsByClassName('cart-price')[0]
            var quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
            var price = parseFloat(priceElement.innerText.replace('₹', ''))
            console.log();
            var quantity = quantityElement.innerText;
            quantity=parseInt(quantity)
            total = total + (price * quantity);
        }
        total = Math.round(total * 100) / 100
        document.getElementsByClassName('cart-total-price')[0].innerText = '₹' + total
    }


    function quantityChanged(event) {
        var cart=JSON.parse(localStorage.getItem('cart'))
        var input = event.target
        if (isNaN(input.value) || input.value <= 0) {
            input.value = 1
        }
        updateCartTotal(cart)
    }
    
    function addtoview(){
        var cart=localStorage.getItem('cart')
        document.getElementById('cartjson').value=cart
        document.getElementById('total').value=(document.getElementsByClassName('cart-total-price')[0].innerText).slice(1,)
    }


    showcart(cart);
    updateCartTotal(cart);
    addtoview();
}