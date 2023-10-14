let basket = []

function addToBasket(event){
    console.log("Добавленно!")
}

let Privileges = document.querySelectorAll(".add-basket-btn")

for(let i = 0; i < Privileges.length; i++){
    Privileges[i].addEventListener("click", addToBasket)
}

function addToBasket(event){
    let name = event.currentTarget.parentNode.querySelector(".donate-name").innerHTML
    let price = event.currentTarget.parentNode.querySelector(".donate-price").innerHTML
    let id = event.currentTarget.parentNode.parentNode.getAttribute("privilegeId")
    let img = event.currentTarget.parentNode.parentNode.querySelector(".img-content").getAttribute("src")
    
    let basketObj = {
        name: name,
        price: price,
        id: id,
        img: img
    }
    basket.push(basketObj)
    console.log(basket)

    let number = document.querySelector(".shopping-count")
    number.innerHTML = basket.length
}

let basketBackground = document.querySelector(".basket-background");
let basketOpenBtn = document.querySelector(".donate-cart");
let basketExitBtn = document.querySelector(".basket-exit-btn");
let body = document.querySelector("#body")

function openCloseBasket(event){
    basketBackground.classList.toggle("basket-show")
    body.classList.toggle("disable-overlow")
}

basketOpenBtn.addEventListener("click", openCloseBasket)
basketExitBtn.addEventListener("click", openCloseBasket)