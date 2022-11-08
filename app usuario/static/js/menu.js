// .active se busca que a  <ul class="links"> se le agregue active, ej: <ul class="links active">
//para lograr que aparezca el menu desplegable


 //se crea constante links y se pude que tenga dentro los elementos de la clase links
const pago = document.getElementById("pago");
const pagoTarjeta = document.querySelectorAll(".pago-tarjeta")
const pagoD = document.getElementById("pago-d");
const pagoDebito = document.querySelectorAll(".pago-debito")

//const pagoTarjeta = document.querySelector(".pago-tarjeta")



pago.addEventListener("click", () => {
  
    for (var i = 0; i < pagoTarjeta.length; i++) {
        pagoTarjeta[i].classList.toggle("mostrar");
      }
      for (var i = 0; i < pagoDebito.length; i++) {
        pagoDebito[i].classList.remove("mostrar");
      }

})

pagoD.addEventListener("click", () => {
    
     for (var i = 0; i < pagoDebito.length; i++) {
         pagoDebito[i].classList.toggle("mostrar");
       }
       for (var i = 0; i < pagoTarjeta.length; i++) {
        pagoTarjeta[i].classList.remove("mostrar");
      }
 
 })
 function myFunction() {
  alert("Dinero  ingresado");
}


