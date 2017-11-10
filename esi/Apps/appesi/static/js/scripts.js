$(document).on('ready',iniciar);

function iniciar()
{
	$varProveedor=$('#vproveedor');
	$varClasificacion=$('#vclasificacion');
	$varDonacion=$('#vdonacion');
	$varBienes=$('#vbien');
	$varTarjeta=$('#vtarjeta');
	
 

	$varProveedor.hide();
	$varClasificacion.hide();
	$varDonacion.hide();
	$varBienes.hide();
	$varTarjeta.hide();
	


	$('#bproveedor').on('click',proveedor1);
	$('#bclasifiacion').on('click',clasificacion1);
	$('#bdonacion').on('click',donacion1);
	$('#bbien').on('click',bienes1);
	$('#btarjeta').on('click',tarjeta1);

	
}





function proveedor1()
{
  $varProveedor.show();
  $varClasificacion.hide();
  $varDonacion.hide();
  $varBienes.hide();
  $varTarjeta.hide();

}

function clasificacion1()
{
	$varProveedor.hide();
	$varClasificacion.show();
	$varDonacion.hide();
	$varBienes.hide();
	$varTarjeta.hide();

}

function donacion1()
{
    $varProveedor.hide();
	$varClasificacion.hide();
	$varDonacion.show();
	$varBienes.hide();
	$varTarjeta.hide();

}

function bienes1()
{
	$varProveedor.hide();
	$varClasificacion.hide();
	$varDonacion.hide();
	$varBienes.show();
	$varTarjeta.hide();

}

function tarjeta1()
{
	$varProveedor.hide();
	$varClasificacion.hide();
	$varDonacion.hide();
	$varBienes.hide();
	$varTarjeta.show();
	

}