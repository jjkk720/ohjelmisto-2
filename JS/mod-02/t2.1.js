'use strict';

const numbers = []
let tulosta;


numbers[0]= prompt('Number1')
numbers[1]= prompt('Number2')
numbers[2]= prompt('Number3')
numbers[3]= prompt('Number4')
numbers[4]= prompt('Number5')



for (let i = 4; i > -1 ; i--) {
    console.log(numbers[i])
    document.querySelector('#target').innerHTML += `${numbers[i]} `
}                                                     //?


//console.log(numbers[3])