//otetaan käyttöön ns. tiukka moodi
'use strict';

//etsitään web-sivulta html-elementti, jonka id="target"

const= targetElem  document.querySelector('#target');

//lisään target elementille luokkamäärityksen
targetElem.classList.add('my-list');

//lisätään löydetylle html-elemtille sisältö inner Html-avulla
targetElem.innerHTML=
    <li>First item</li>
<li>Second item</li>
<li>Third item</li>
