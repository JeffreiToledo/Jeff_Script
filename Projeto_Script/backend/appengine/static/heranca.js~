function construtorObservador() {

  var lista = [];
  var evento = {contador:0};

  var objeto = {

    contar: function () {
      lista.forEach(function (valor) {
        valor(evento);
        evento.contador ++;
      });
    }
  };

  function adicionarOuvinte(funcao) {
    lista.push(funcao);

  }

  objeto.adicionarOuvinte = adicionarOuvinte;

  return objeto;
}

function observador(evento) {
  console.log('Contando...' + evento.contador);
}



var contadorObservador = construtorObservador();
console.log(contadorObservador);

contadorObservador.adicionarOuvinte(observador);


contadorObservador.contar();
contadorObservador.contar();


