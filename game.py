import tkinter as tk;
class TicTacToe:
  def __init__(self, master):
      
      self.master = master
      self.master.title("Tic Tac Toe")

      
      self.current_player = "X"

      
      self.board = [
          ["", "", ""],
          ["", "", ""],
          ["", "", ""]
      ]

      
      self.buttons = []
      for row in range(3):
          button_row = []
          for col in range(3):

              button = tk.Button(
                  self.master,
                  text="",
                  font=("Helvetica", 30),
                  width=3,
                  height=1,
                  command=lambda row=row, col=col: self.handle_click(row, col)
              )
             
              button.grid(row=row, column=col, sticky="nsew")
              button_row.append(button)
          self.buttons.append(button_row)

  def handle_click(self, row, col):
      
      if self.board[row][col] == "":
          
          self.board[row][col] = self.current_player
          self.buttons[row][col].config(text=self.current_player)
         
          if self.check_win() or self.check_tie():
             
              self.game_over()
          else:
             
              self.switch_player()

  def switch_player(self):
      
      if self.current_player == "X":
          self.current_player = "O"
      else:
          self.current_player = "X"

  def check_win(self):
      
      for i in range(3):
          if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
              return True
      
          if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
              return True
    
      if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
          return True
      
      if self.board[2][0] == self.board[1][1] == self.board[0][2] != "":
          return True
      
      return False

  def check_tie(self):
      
      for i in range(3):
          for j in range(3):
              if self.board[i][j] == "":
                  return False
      
      return True
  def reset_board(self):
        self.board[['', '', ''], ['', '', ''], ['', '', '']]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
  def game_over(self):
      
      for row in self.buttons:
          for button in row:
              button.config(state="disabled")
              if self.check_win():
                  winner = self.current_player
                  message = f"Player {winner} wins!"
              else:
                  message = "It's a tie!"
      
      msg_label = tk.Label(self.master, text=message, font=("Helvetica", 20))
      msg_label.grid(row=3, column=0, columnspan=3)
  
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()