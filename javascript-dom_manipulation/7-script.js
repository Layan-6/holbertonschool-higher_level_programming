fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const ul = document.querySelector('#list_movies');
    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      ul.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });
