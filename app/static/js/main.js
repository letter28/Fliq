$(function () {
    let $highscoresList = $('#highscores-list');

    function buildHighscoreMenu(element) {
        let $el;
        
        $el = $('<li class="list-group-item d-flex align-items-start">' +
                    '<div class="ms-2 me-auto">' +
                        '<div class="fw-bold">'+ element.username + '</div>' +
                        element.date_of_score +
                        '<div>'+ element.category + '</div>' +
                    '</div>' +
                    '<span id="score-tag" class="badge bg-primary rounded-pill">' + element.score + '</span>' +
                '</li>');
        
        return $el;
    }
    
    $.get('/api/highscores/5', function (data) {
        if (data) {
            data = data['highscores'];
            data.forEach(element => {
                $highscoresList.append(buildHighscoreMenu(element));
            });
        };
    });
});