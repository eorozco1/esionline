
$(document).on('ready', Iniciar);
function Iniciar()
{
	$varBoton = $('#btnMostrar');


	$varBoton.on('click',Presionar);
	alert ("Este es un mensaje de prueba");
	console.log ('sdfsdf');
}

function Presionar ()
{
	alert("Dato");
}