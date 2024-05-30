// Fetches and replaces the name of the API data then replaces the name
// and update it on the page

let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (data, stat) {
  $('div#character').text(data.name);
});
