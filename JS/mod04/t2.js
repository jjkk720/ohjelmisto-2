'use strict';
const tvForm = document.querySelector('#tv');

tvForm.addEventListener('submit', async function(evt:))

evt.preventDefault();

const query = document.querySelector('input[name=q]');
const kysely = `https://api.tvmaze.com/search/shows?q=${hakuarvo}`;

try{
  const raakadata = await fetch(kysely);

  const jsonData = await raakadata.json();
  console.log("-Saatu json-data, js-rules")
}catch(error{
  console.log(error.message);
})
})