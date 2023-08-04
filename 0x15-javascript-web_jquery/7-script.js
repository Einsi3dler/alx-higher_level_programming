$(function (){
    var $character = $('#character');
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        success: function(character)
        {$character.text(character.name)}
    });
});

//$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data, textStatus, jqXHR) {
//    $("#character").text(data.name)
//});
// Alternative solution using $.get() instead of $.ajax()