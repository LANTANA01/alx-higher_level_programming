//adds a <li> element to a list on mouse.click event

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
