const formFieldsEl = document.getElementsByClassName('form-control');
const usernameInputEl = formFieldsEl[0];
const usernameMsgEl = formFieldsEl[1];
const saveScoreBtn = document.getElementsByClassName('btn btn-primary col-10 mt-2')[0];
const finalScoreEl = document.getElementById('final-score-text');
const categoryEl = document.getElementById('category-result-text');

finalScoreEl.innerText = localStorage.getItem('finalScore');
categoryEl.innerText = localStorage.getItem('category');

saveScoreBtn.classList.add('disabled');

usernameInputEl.addEventListener('keyup', () => {
    usernameInputEl.value ? saveScoreBtn.classList.remove('disabled') : saveScoreBtn.classList.add('disabled');
});

saveScoreBtn.addEventListener('click', onSaveScore);

/* var UserHighscoreModel = Backbone.Model.extend({
    url: '/api/highscores',
    defaults: {
        id: '',
        user_id: '',
        score: '',
        message: '',
        date_of_score: '',
    }
}); */

var onSaveScore = function() {
    let scoreData = {
        score: localStorage.getItem('finalScore'),
        category: localStorage.getItem('category'),
        message: usernameMsgEl.value,
        username: usernameInputEl.value,
        date_of_score: '2021-07-20 19:55:00'
    };

    $.ajax({
        type: "POST",
        url: "/save-score",
        data: JSON.stringify(scoreData),
        contentType: "application/json",
        dataType: 'json' 
      });
};