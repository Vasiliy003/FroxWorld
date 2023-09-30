let profileMenu = document.querySelector(".profile-menu");
let burgerBtn = document.querySelector("#profile-btn");
let navigationBtn = document.querySelector("#header-navigation-btn");

function burgerMenu(event){
    profileMenu.classList.toggle("profile-menu-show")
}

function navigationDecorate(event){
    if(event.type==="mouseover")
        event.target.classList.toggle(".navigation-target");
    else if(event.type==="mouseout")
        event.target.classList.toggle(".navigation-target");
}


burgerBtn.addEventListener("click", burgerMenu)

navigationBtn.addEventListener("mouseover", navigationDecorate)
navigationBtn.addEventListener("mouseout", navigationDecorate)