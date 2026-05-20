'use strict';

const osallistujat= []





let määrä =prompt('Montako osallistujaa?')
 määrä = parseInt(määrä);



for (let i=1; i <= määrä ; i++) {
    osallistujat[i]=prompt('Osallistujan nimi')
}


osallistujat.sort()
console.log(osallistujat)

//listan printtaus kesken