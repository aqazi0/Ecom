if(localStorage.getItem('cart')=='null'){
    localStorage.setItem('cart','{}')
}
else{
    var cart=JSON.parse(localStorage.getItem('cart'));
    function showcart(cart){
        var cart1=document.getElementById('cartdata').value
        var l=Object.keys(cart1).length;
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
            <button type='submit' id="sub`+prodid+`" class="btn btn-primary sub" type="button">-</button>&nbsp &nbsp
            <input id="val`+prodid+`" class="cart-quantity-input" type="number" value="`+ cart[key][0] +`">
            <button type='submit' id="add`+prodid+`" class="btn btn-primary add" type="button">+</button>
            &nbsp &nbsp &nbsp &nbsp &nbsp
                <button type='submit' id="del`+prodid+`" class="btn btn-danger" type="button">REMOVE</button>
            </div>
            </div>`;
            cartItems.innerHTML = cartRowContents;
        }
    }


    function updateCartTotal(cart) {
        var cartItemContainer = document.getElementsByClassName('cart-items')[0]
        var cartRows = cartItemContainer.getElementsByClassName('cart-row')
        var total = 0
        for (var i = 0; i < Object.keys(cart).length; i++) {
            var cartRow = cartRows[i]
            var priceElement = cartRow.getElementsByClassName('cart-price')[0]
            var quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
            var price = parseFloat(priceElement.innerText.replace('₹', ''))
            var quantity = quantityElement.value
            cart[Object.keys(cart)[i]][0]=quantity;
            total = total + (price * quantity)
        }
        total = Math.round(total * 100) / 100
        document.getElementsByClassName('cart-total-price')[0].innerText = '₹' + total
        localStorage.setItem('cart',JSON.stringify(cart))
    }


    function quantityChanged(event) {
        var cart=JSON.parse(localStorage.getItem('cart'))
        var input = event.target
        if (isNaN(input.value) || input.value <= 0) {
            input.value = 1
        }
        updateCartTotal(cart)
    }
    
    showcart(cart);
    updateCartTotal(cart);

    $('.cart-quantity-input').change(quantityChanged)
    
    $('.btn-danger').click(function(){
        var k="pr"+this.id.toString().slice(3,);
        delete cart[k];
        localStorage.setItem('cart',JSON.stringify(cart));
        document.getElementById('cartdata').value=JSON.stringify(cart);
    });

    $('.add').click(function(){
        var k="pr"+this.id.toString().slice(3,);
        cart[k][0]=parseInt(cart[k][0])
        cart[k][0]+=1;
        localStorage.setItem('cart',JSON.stringify(cart));
        document.getElementById('cartdata').value=JSON.stringify(cart);
    });

    $('.sub').click(function(){
        var k="pr"+this.id.toString().slice(3,);
        cart[k][0]=parseInt(cart[k][0])
        if(cart[k][0]!=1){
            cart[k][0]-=1;
        }
        localStorage.setItem('cart',JSON.stringify(cart));
        document.getElementById('cartdata').value=JSON.stringify(cart);
    });
}