let profileMenu = document.querySelector(".profile-menu");
let burgerBtn = document.querySelector("#profile-btn");

function burgerMenu(event){
    profileMenu.classList.toggle("profile-menu-show")
}

if (burgerBtn) {
    burgerBtn.addEventListener("click", burgerMenu)
}