// Fetches all movie titles from an API then inserts them
// into the UL#list_movies tag


$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
