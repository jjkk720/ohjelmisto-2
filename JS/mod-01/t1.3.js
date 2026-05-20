'use strict';



var num1= prompt('Number1?');
  var num2= prompt('Number2?');
  var num3= prompt('Number3?');
  var num1 = parseInt(num1);
  var num2 = parseInt(num2);
  var num3 = parseInt(num3);


  const sum= num1+num2+num3;
  const product =num1*num2*num3;
  const average= sum/3
  console.log(sum)
  console.log(product)
  console.log(average)

  document.querySelector('#target').innerHTML = `Sum is  ${sum}. 
  Product is  ${product}.
  Average is ${average}.`;