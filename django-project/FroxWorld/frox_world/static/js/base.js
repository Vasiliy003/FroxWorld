let profileMenu = document.querySelector(".profile-menu");
let burgerBtn = document.querySelector("#profile-btn");

function burgerMenu(event){
    profileMenu.classList.toggle("profile-menu-show")
}

burgerBtn.addEventListener("click", burgerMenu)

console.log(profileMenu)
console.log(burgerBtn)