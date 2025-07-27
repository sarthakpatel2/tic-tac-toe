const board = document.querySelector(".board");
const cells = document.querySelectorAll(".cell");
const message = document.getElementById("message");
const resetBtn = document.getElementById("resetBtn");

let currentPlayer = "X";
let boardState = ["", "", "", "", "", "", "", "", ""];
let gameActive = true;

// Winning combinations
const winPatterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], 
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]
];

// Handling cell clicks
cells.forEach((cell, index) => {
    cell.addEventListener("click", () => {
        if (boardState[index] === "" && gameActive) {
            boardState[index] = currentPlayer;
            cell.textContent = currentPlayer;
            checkWinner();
            currentPlayer = currentPlayer === "X" ? "O" : "X";
            message.textContent = `Player ${currentPlayer}'s Turn`;
        }
    });
});

// Check for a winner or draw
function checkWinner() {
    for (let pattern of winPatterns) {
        const [a, b, c] = pattern;
        if (boardState[a] && boardState[a] === boardState[b] && boardState[a] === boardState[c]) {
            message.textContent = `Player ${boardState[a]} Wins!`;
            gameActive = false;
            return;
        }
    }
    if (!boardState.includes("")) {
        message.textContent = "It's a Draw!";
        gameActive = false;
    }
}

// Reset game
resetBtn.addEventListener("click", () => {
    boardState = ["", "", "", "", "", "", "", "", ""];
    cells.forEach(cell => cell.textContent = "");
    currentPlayer = "X";
    gameActive = true;
    message.textContent = `Player ${currentPlayer}'s Turn`;
});
