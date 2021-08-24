const question = document.getElementById('question');
const choices = Array.from(document.getElementsByClassName('choice-text'));
const currentQuestionEl = document.getElementById('question-number');
const scoreEl = document.getElementById('score-text')
const progressBar = document.getElementById('progress-bar');

let currentQuestion = {};
let acceptingAnswers = false;
let score = 0;
let questionNumber = 1;
let availableQuestions = [];

let questions = [];

// Loading the questions from local json file
getQuestions = async function() {
    const response = await fetch("../static/resources/questions.json");
    return response.json();
};

getQuestions().then(loadedQuestions => {
    questions = loadedQuestions;
    startGame();
});

const CORRECT_BONUS = 10;
const INCORRECT_BONUS = -3;
const MAX_QUESTIONS = 10;

startGame = () => {
    questionNumber = 1;
    score = 0;  
    availableQuestions = [...questions];

    getNextQuestion();
};

getNextQuestion = () => {
    // ako je ponestalo pitanja, preusmjeri na rezultate
    if (questionNumber > MAX_QUESTIONS || availableQuestions.length === 0) {
        localStorage.setItem('finalScore', score.toString());
        return window.location.assign('../quiz-results');
    } else {
        // odabiremo random pitanje
        let randomNumber = Math.floor(Math.random() * availableQuestions.length);
        currentQuestion = availableQuestions[randomNumber];
        question.innerText = unescape(currentQuestion.question);
        choices.forEach(choice => {
            let num = choice.dataset['number'];
            choice.innerText = unescape(currentQuestion['choice' + num]);
            choice.classList.remove('highlight-correct');
        });
    
        availableQuestions.splice(randomNumber, 1);
    
        acceptingAnswers = true;
    
        updateProgress();
        updateScore();
        questionNumber++;
    };
};

updateProgress = () => {
    let progress = questionNumber / MAX_QUESTIONS * 100; 
    progressBar.setAttribute('aria-valuenow', progress.toString());
    progressBar.style.width = progress.toString() + '%';

    currentQuestionEl.innerText = `${questionNumber}/${MAX_QUESTIONS}`;
};

updateScore = () => {
    scoreEl.innerText = score.toString();
};

choices.forEach(choice => {
    choice.addEventListener("click", event => {
        if (!acceptingAnswers) return;

        acceptingAnswers = false;
        const selectedChoice = event.target;
        const selectedAnswer = selectedChoice.dataset['number'];

        const classToApply = selectedAnswer == currentQuestion.answer ? 'correct' : 'incorrect';

        selectedChoice.parentElement.classList.add(classToApply);

        choices.forEach(c => {
            if (currentQuestion.answer == c.dataset['number']) c.classList.add('highlight-correct');
        });

        setTimeout(() => {
            selectedAnswer == currentQuestion.answer ? score += CORRECT_BONUS : score += INCORRECT_BONUS;
            selectedChoice.parentElement.classList.remove(classToApply);
            getNextQuestion();
        }, 1000);
    });
});
