console.log("internships available");

let nav = document.querySelector(".nav-ul");

let burger = document.querySelector(".burger");
burger.addEventListener("click", () => {
    console.log("thanks for clicking ");
    nav.classList.toggle("nav-display");

})