const toggle = document.querySelector(".toggle")
const links = document.querySelector(".links") //se crea constante links y se pude que tenga dentro los elementos de la clase links

//al presionar sobre icono-menu se ejecute un evento
toggle.addEventListener("click", () => {
    toggle.classList.toggle("rotate") //se crea la clase .rotate  dentro de la case toggle y se alterna
    links.classList.toggle("active")
})