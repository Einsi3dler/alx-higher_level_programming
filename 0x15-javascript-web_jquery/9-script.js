$(function() {

    var $hello = $('#hello');

    function handleResponse(data)
    {
        $('$hello').text(data.hello);
    }
    $.ajax({
        type: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        dataType: 'jsonp',
        jsonpCallback: 'handleResponse'
    })
})