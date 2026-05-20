'use strict';

const numerot=[]

let numero;
numero =prompt('anna numero')
numero = parseInt(numero);
if(numero!==0){
  numerot.push(numero)
}

while (numero!==0){
  numerot.push(numero)
  numero =prompt('anna numero')
  numero = parseInt(numero);

}

numerot.sort((a,b)=> b-a)
console.log(numerot)





document.querySelector('#target').innerHTML= 'grethryjtmj'