$(function() {
    var $list = $('#list_movies');

    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function(data)
        {
            //$list.append('<li>'+ data.count +'</li>');
           const results = data.results
           $.each(results, function(index, result){
            $list.append('<li>' + result.title + '</li>');
        });
        }
    })

})
