'use strict';
const a =(Math.random())
const name =prompt('Nimesi');
console.log(a)
let b ='';

if (a > 0.75) {
  b = 'Rohkelikko';
  console.log('Rohkelikko');
}

if (a > 0.50 && a<=0.75) {
  b = 'Korpinkynsi';
  console.log('Korpinkynsi')
}

if (a > 0.25 && a<=0.5) {
  b = 'Puuskupuh';
  console.log('Puuskupuh')
}

if (a <= 0.25) {
  b = 'Luihuinen';
  console.log('Luihuinen')
}

document.querySelector('#target').innerHTML= name + ', olet ' + b + '.'

//en saanut rajoitettua numeroihin 1,2,3,4