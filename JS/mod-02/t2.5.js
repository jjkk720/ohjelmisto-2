'use strict';



const numerot= []



let numero = parseInt(prompt('anna numero'))
numerot.push(numero)




while(numero!== 0){
  numero = parseInt(prompt('anna numero'))
  for (let i=0; i < numerot.length ; i++) {
    if (numerot[i]===numero){
      numero=0
    }
}numerot.push(numero)


}
numerot.pop()
console.log('olet jo syöttänyt tämän numeron, toiminnot lopetetaan')
console.log(numerot)








//[1,2,3]

//nollan syöttö sulkee ohjelman