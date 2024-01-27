var timerInterval;

function startTimer() {
  var start = new Date();
  var end = new Date(start.getTime() + 60 * 1000); // Конечное время: 1 минута от начала

  // Обновляем таймер каждую секунду
  timerInterval = setInterval(function() {
    var current = new Date();

    // Вычисляем оставшееся время
    var remainingTime = end - current;
    var minutes = Math.floor(remainingTime / 60000);
    var seconds = Math.floor((remainingTime % 60000) / 1000);

    var timerDisplay = document.getElementById("timer");
    timerDisplay.textContent = "До конца теста осталось " + formatTime(minutes) + ":" + formatTime(seconds);
    timerDisplay.style.color = "red";
    timerDisplay.style.fontWeight = "bold";
    // Таймер истек
    if (remainingTime < 0) {
      clearInterval(timerInterval);
      timerDisplay.textContent = "Время вышло";
      submitAnswers(); // Автоматически отправляем ответы при истечении времени
    }
  }, 1000);
}
// форматирует время (минуты и секунды), добавляя ведущий ноль, если значение меньше 10.
function formatTime(time) {
  return time < 10 ? "0" + time : time;
}
// Останавливает таймер, вычисляет и отображает набранные баллы, отключает кнопку отправки ответов и вызывает функцию showNotification().
function submitAnswers() {
  clearInterval(timerInterval); // Остановка таймера
  var score = calculateScore();
var scoreDisplay = document.getElementById("score");
scoreDisplay.textContent = "Вы набрали " + score + " баллов";
scoreDisplay.style.color = "red";
scoreDisplay.style.fontWeight = "bold";
  document.getElementById("submit").disabled = true;

  showNotification(score);
}
// вычисляет и возвращает общее количество набранных баллов на основе выбранных ответов на вопросы
function calculateScore() {
  var score = 0;

  var question1 = document.querySelector('input[name="question1"]:checked');
  var question2 = document.querySelector('input[name="question2"]:checked');
  var question3 = document.querySelector('input[name="question3"]:checked');

  if (question1 && question1.value === "2") {
    score += 1;
  }
  if (question2 && question2.value === "1") {
    score += 1;
  }
  if (question3 && question3.value === "1") {
    score += 1;
  }

  return score;
}
// выводит всплывающее окно с сообщением о количестве набранных баллов
function showNotification(score) {
  alert("Вы набрали " + score + " баллов");
}

startTimer();