//get data
//json from https://github.com/dwyl/english-words/
let fiveLetter = [];
let sevenLetter = [];
let nineLetter = [];
fetch('words_dictionary.json')
    .then(
        function(response) {
            if (response.status !== 200) {
                console.log('There was an issue');
                return;
            }

            response.json().then(function(data) {
                let objectKeys = Object.keys(data);
                for (let i=0; i<objectKeys.length; i++){
                    if (objectKeys[i].length==5){
                        fiveLetter.push(objectKeys[i]);
                    }
                    else if (objectKeys[i].length==7){
                        sevenLetter.push(objectKeys[i]);
                    }
                    else if (objectKeys[i].length==9){
                        nineLetter.push(objectKeys[i]);
                    }
                }
            });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error');
    });
// let fiveLetter = [
//     "hares",
//     "bears"
// ];
//
// let sevenLetter = [
//     "brioche",
//     "crashed"
// ];
//
// let nineLetter = [
//     "abilities",
//     "recognize"
// ];

var word = null;
var wrongGuess = 0;
var letterCheckArray = [];
var checkedLetters = [];

function startGame (difficulty) {
    document.getElementById("message").innerText = "";
    //choose the array to select from based on difficulty
    let arrayToChooseFrom;
    if (difficulty==0){
        arrayToChooseFrom=fiveLetter;
    }
    else if (difficulty==1){
        arrayToChooseFrom=sevenLetter;
    }
    else if (difficulty==2){
        arrayToChooseFrom=nineLetter;
    }
    //select a word
    word = arrayToChooseFrom[Math.floor(Math.random() * arrayToChooseFrom.length)];
    //reset checkedLetters and wrongGuess
    checkedLetters = [];
    wrongGuess = 0;
    //set letterCheckArray to an array length = word length filled with false, except spaces are true
    letterCheckArray = [];
    for (let i=0; i<word.length; i++){
        letterCheckArray.push(false);
    }
    //hide difficulty selection elements
    document.getElementById("selection").style.display="none";
    //show game elements
    document.getElementById("game").style.display="block";
    //update display
    displayWord();
}

function guess (letter) {
    document.getElementById(userInput.value="")
    if (word == null || letterCheckArray.length < 1 || letter == "") {
        return;
    }
    //validate single letter check
    if (letter.length > 1) {
        document.getElementById("message").innerText = "Only one letter at a time";
        return;
    }
    //don't guess the same letter again
    if (checkedLetters.includes(letter)) {
        document.getElementById("message").innerText = "You already guessed " + letter;
        return;
    }
    //if the string doesn't include the letter, increment wrongGuess. If it does,
    //find the index of each instance of the letter in word, then set letterCheckArray to true at that index
    if (word.includes(letter)){
        for (let i=0; i<word.length; i++){
            if (letter==word[i]){
                letterCheckArray[i]=true;
            }
        }
    }
    else{
        document.getElementById("message").innerText = "The word does not include the letter " + letter;
        wrongGuess=wrongGuess+1;
    }
    //add letter to checkedLetters
    checkedLetters.push(letter);
    //check the game status
    checkGameStatus();
    //lastly, update the display
    displayWord();
}

function checkGameStatus() {
    //if wrongGuess is 6 or higher, put "You lose" in gameResultText, display the selection div, hide the game div, and return
    if (wrongGuess>=6){
        document.getElementById("gameResultText").innerText = "Game Over";
        document.getElementById("game").style.display="none";
        document.getElementById("selection").style.display="block";
        return;
    }
    //check whether every index of letterCheckArray is true
    //if a single one is false, set indexCheck to false and break the loop
    let indexCheck = true;
    for (let i=0; i<letterCheckArray.length; i++){
        if (letterCheckArray[i]==false){
            indexCheck=false;
            break;
        }
    }
    //if every index of letterCheckArray is true, put "You win" in gameResultText, display the selection div, hide the game div, and return
    if (indexCheck==true){
        document.getElementById("gameResultText").innerText = "You Win";
        document.getElementById("game").style.display="none";
        document.getElementById("selection").style.display="block";
        return;
    }
}

function displayWord () {
    document.getElementById("checkedLetter").innerText = checkedLetters;
    if (word == null || letterCheckArray.length < 1) {
        return;
    }
    //set src of the hangmanImage to the image matching the number of mistakes
    document.getElementById("hangmanImage").src = "img/" + wrongGuess.toString() + ".png";
    //display "_ " for each unguessed letter, "{letter} " for each correctly guessed letter
    //also add newline character \n if it's a space, in order to separate the words
    let stringToDisplay = "";
    //add a loop here
    for (let i=0; i<letterCheckArray.length; i++){
        if (letterCheckArray[i]==true){
            stringToDisplay+=word[i]+ " ";
        }
        else{
            stringToDisplay+="_ ";
        }
    }

    document.getElementById("wordDisplay").innerText = stringToDisplay;
}

function backButton () {
    document.getElementById("game").style.display="none";
    document.getElementById("selection").style.display="block";
}