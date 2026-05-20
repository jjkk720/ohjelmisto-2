'use strict';

const targetElem = document.querySelector('#target')

//dem-tekniikka: teen li-elementtejä, jotka tulevat
//html-sivulla olevant ul-elementin sisään(JS-koodissa targetElem)

const firstLiElem = document.createElement('li');
//lisään luodulle li-elementille sen sisällön
firstLiElem.innerHTML = 'First item';

targetElem.appendChild(firstLiElem);

const secondLiElem = dodument.createElement('li');
secondLiElem.innerHTML = 'Second item';


targetElem.appendChild(firstLiElem);
targetElem.appendChild(secondLiElem);