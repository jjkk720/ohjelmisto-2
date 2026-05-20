'use strict';

//etsitään haluttu elementit html-sivulta
//etsitään kuva, id="target"
const targetElem = document.querySelector('#target');
//etsitään tapahtuman laukaiseva teksit
const triggerElem=document.querySelector('#trigger');
//määrittelen funktion, joka vaihtaa kuvan sisällön
//kun hiiri tulee triggerin päälle
function mousePaalle(){
    targetElem.src = "img/picA.jpg"
                 }
function mouseUP(){}
//asetetaan elementille tapahtumankuuntelija
triggerElem.addEventListener('mouseenter', mousePaalle);