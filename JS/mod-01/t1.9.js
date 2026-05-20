'use strict';
console.log('hello')

let integer = prompt('Give an integer.');
integer = parseInt(integer)

if (integer ===1 ||integer === 2 || integer=== 3 || integer=== 5 || integer=== 7){
  console.log(integer + ' is a prime number.')
  document.querySelector('#target').innerHTML= integer + ' is a prime number.'}
  else if (integer % 2 === 0 || integer % 3 ===0 || integer % 5 === 0 || integer % 7 ===0 ){
    console.log(integer + ' is not a prime number.')
    document.querySelector('#target').innerHTML= integer + ' is not a prime number.'}
  else {console.log(integer + ' is a prime number.')
    document.querySelector('#target').innerHTML= integer + ' is a prime number.'}


  


