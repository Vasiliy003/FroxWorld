let cartList = document.querySelector(".cart-list");
let donateBtn = document.querySelector(".donate-cart");

function donateMenu(event){
    cartList.classList.toggle("cart-list-show")
}

donateBtn.addEventListener("click", donateMenu)