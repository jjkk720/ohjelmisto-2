'use strict';

const year =prompt('enter year ');
const yearint=parseInt(year);
let a=0

if (yearint % 4 === 0 && yearint % 100 !== 0){
  a=1}
  else if (yearint%4 === 0 && yearint % 100 === 0 && yearint % 400 === 0){
    a=1}
  else if (yearint%4 === 0 && yearint % 100 === 0 && yearint % 400 !== 0){
    a=2}
  else if (yearint%4 === 0 && yearint % 100 !== 0){
    a=1}
  else{
    a=2}



if (a===2){
  console.log('not a leap year');
document.querySelector('#target').innerHTML= 'not a leap year'}
else{
  console.log('leap year');
document.querySelector('#target').innerHTML= 'leap year'}





