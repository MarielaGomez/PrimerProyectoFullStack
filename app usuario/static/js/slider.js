
var slider = $('#slider'); //guardar slidern en una variable
//almacenar botones en variables
var siguiente = $('#btn-next');
var anterior = $('#btn-prev');

//mover ultima imagen al primer lugar
$('#slider .slider__section:last').insertBefore('#slider .slider__section:first'); //.insertBefore inserte antes
//mostrar la primera imagen con un margen de -100%
slider.css('margin-left', '-'+100+'%');

function moverD() {
	slider.animate({
		marginLeft:'-'+200+'%'
	} ,700, function(){
		$('#slider .slider__section:first').insertAfter('#slider .slider__section:last');
		slider.css('margin-left', '-'+100+'%'); //para ver la primera imagen debe estar en -100%
	});
}

//crear funciones para el cambio de imagen 
function moverI() {
	slider.animate({ //para que se anime
		marginLeft:0
	} ,700, function(){ //700 es el tiempo de animación
		$('#slider .slider__section:last').insertBefore('#slider .slider__section:first');
		slider.css('margin-left', '-'+100+'%');
	});
}

function autoplay() {
	interval = setInterval(function(){
		moverD();
	}, 5000); //tiempo movimiento autoplay
}
//al hacer click, ejecuta funsion "moverD"
siguiente.on('click',function() {
	moverD();
	clearInterval(interval);
	autoplay();
});

anterior.on('click',function() {
	moverI();
	clearInterval(interval);
	autoplay();
});

//movimiento automatico
autoplay();