       		$(document).ready( //siempre. para seleccionar objetos $... siempre estas dos primeras lineas para empezar
                function(){     //estas dos lineas
                      $("#idaClick").click(
                      		function(){
    							$("#ida").fadeTo(1000, 0.4);
    							alert('Ha seleccionado billete de ida');
    						}	

                    );//click1

                      $("#ivClick").click(
                      		function(){
    							$("#iv").fadeTo(1000, 0.4);
    							alert('Ha seleccionado billete de ida y vuelta');
    						}	

                    );//click2

                      $("#menClick").click(
                      		function(){
    							$("#men").fadeTo(1000, 0.4);
    							alert('Ha seleccionado el billete mensual');
    						}	

                    );//click3

                  }//primera funcion despues de ready
                );//ready
	