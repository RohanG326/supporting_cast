//get data

let fiveLetter = [
    "hares",
    "bears"
];

let sevenLetter = [
    "brioche",
    "crashed"
];

let nineLetter = [
    "abilities",
    "recognize"
];

var word = null;
var wrongGuess = 0;
var letterCheckArray = [];
var checkedLetters = [];

function startGame (difficulty) {
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
    document.getElementById("selction").style.display="none";
    //show game elements
    document.getElementById("game").style.display="block";
    //update display
    displayWord();
}

function guess (letter) {
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
        for (let i=0; i<word.length: i++){
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

    //check the game status

    //lastly, update the display

}

function checkGameStatus() {
    //if wrongGuess is 6 or higher, put "You lose" in gameResultText, display the selection div, hide the game div, and return

    //check whether every index of letterCheckArray is true
    //if a single one is false, set indexCheck to false and break the loop
    let indexCheck = true;

    //if every index of letterCheckArray is true, put "You win" in gameResultText, display the selection div, hide the game div, and return

}

function displayWord () {
    if (word == null || letterCheckArray.length < 1) {
        return;
    }
    //set src of the hangmanImage to the image matching the number of mistakes
    document.getElementById("hangmanImage").src = "img/" + wrongGuess.toString() + ".png";
    //display "_ " for each unguessed letter, "{letter} " for each correctly guessed letter
    //also add newline character \n if it's a space, in order to separate the words
    let stringToDisplay = "";
    //add a loop here

    document.getElementById("wordDisplay").innerText = stringToDisplay;
}
