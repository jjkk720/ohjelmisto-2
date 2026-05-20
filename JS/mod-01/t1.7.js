'use strict';
console.log('moi')
let rolls= 0
let a, b, c ,d, number


let dices= prompt("Number of dices.")
dices = parseInt(dices)
while (rolls<dices){}

function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}

const tja= getRandomArbitrary(1,5)
console.log(tja)


 a= Math.random();
if (a<0.5){
     b = Math.random()
  if (b<0.5){ number=1}
  else{number=2}}
else if(a>0.5){
  c=Math.random()
  if (c<0.5){
    number=3}
  else{number=4}
}
console.log(number)




//kesken