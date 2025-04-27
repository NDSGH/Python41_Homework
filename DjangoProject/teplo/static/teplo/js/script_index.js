// Time to start heating period (october)
let restOfDays;
let restOfHours;
let restOfMinutes;
let restOfSeconds;

function toNewYearTimer() {
    let dateNow = Date.now();  // object of current date
    let actYear = new Date().getFullYear();  // object of current year
    let actMonth = new Date().getMonth();  // object of current month
    let newYear = actMonth >= 9 ? actYear + 1 : actYear;  // year of next october

    let dateNew = new Date(newYear, 9, 1);  // date of a new heating period
    let restOfTime = dateNew - dateNow;  // rest of time to october (milliseconds)
    
    let days = Math.floor(restOfTime / 1000 / 60 / 60 / 24);
    let hours = Math.floor(restOfTime / 1000 / 60 / 60 % 24);
    let minutes = Math.floor(restOfTime / 1000 / 60 % 60);
    let seconds = Math.floor(restOfTime / 1000 % 60);
    
    let unitDay, unitHour, unitMin, unitSec;

    if (days == 11 || days == 12 || days == 13 || days == 14) {
        unitDay = ' дней';
    } else if (String(days)[String(days).length - 1] == 1) {
        unitDay = ' день';
    } else if (String(days)[String(days).length - 1] == 2 || String(days)[String(days).length - 1] == 3  || String(days)[String(days).length - 1] == 4) {
        unitDay = ' дня';
    } else {
        unitDay = ' дней';
    }
    
    if (hours == 11 || hours == 12 || hours == 13 || hours == 14) {
        unitHour = ' часов';
    } else if (String(hours)[String(hours).length - 1] == 1) {
        unitHour = ' час';
    } else if (String(hours)[String(hours).length - 1] == 2 || String(hours)[String(hours).length - 1] == 3  || String(hours)[String(hours).length - 1] == 4) {
        unitHour = ' часа';
    } else {
        unitHour = ' часов';
    }

    if (minutes == 11 || minutes == 12 || minutes == 13 || minutes == 14) {
        unitMin = ' минут';
    } else if (String(minutes)[String(minutes).length - 1] == 1) {
        unitMin = ' минута';
    } else if (String(minutes)[String(minutes).length - 1] == 2 || String(minutes)[String(minutes).length - 1] == 3  || String(minutes)[String(minutes).length - 1] == 4) {
        unitMin = ' минуты';
    } else {
        unitMin = ' минут';
    }

    if (seconds == 11 || seconds == 12 || seconds == 13 || seconds == 14) {
        unitSec = ' секунд';
    } else if (String(seconds)[String(seconds).length - 1] == 1) {
        unitSec = ' секунда';
    } else if (String(seconds)[String(seconds).length - 1] == 2 || String(seconds)[String(seconds).length - 1] == 3  || String(seconds)[String(seconds).length - 1] == 4) {
        unitSec = ' секунды';
    } else {
        unitSec = ' секунд';
    }

    restOfDays = days < 10 ? '0' + days + unitDay : days + unitDay;  // rest of days
    restOfHours = hours < 10 ? '0' + hours + unitHour : hours + unitHour;  // rest of hours
    restOfMinutes = minutes < 10 ? '0' + minutes + unitMin : minutes + unitMin;  // rest of minutes
    restOfSeconds = seconds < 10 ? '0' + seconds + unitSec : seconds + unitSec;  // rest of seconds

    d.textContent = restOfDays;
    h.textContent = restOfHours;
    m.textContent = restOfMinutes;
    s.textContent = restOfSeconds;
}

setInterval(toNewYearTimer, 1000);

document.writeln()
