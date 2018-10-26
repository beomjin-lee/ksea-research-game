from random import randrange as rand
import pygame
import sys

######################
# FRONT END SETTINGS #
######################
cell_size = 18
maxfps = 30

colors = [
(0,   0,   0),
(220, 0,   20),
(60,  165, 50),
(100, 100, 255),
(255, 90,  0),
(255, 200, 40),
(160, 50,  210),
(70,  230, 210),
(35,  35,  35)
]

#########
# BOARD #
#########


class Board:
	def __init__(self, x_size=10, y_size=20):
		self.x_size = x_size
		self.y_size = y_size
		self.is_piece_set = False  # piece moving
		self.board = self.new_board()

	def new_board(self):
		"""
		Creates new board - dictionary with arrays
		"""
		return []
		# TODO: Complete function

	def remove_row(self, board, row):
		"""
		Removes row from board
		"""
		# TODO: Complete function
		return []

	def join_board(self, mat1, mat2, mat2_off):
		"""
		Join two board together
		"""
		off_x, off_y = mat2_off
		for cy, row in enumerate(mat2):
			for cx, val in enumerate(row):
				mat1[cy + off_y - 1][cx + off_x] += val
		return mat1

#########
# PIECE #
#########


class Piece:
	def __init__(self):
		self.tetris_shapes = {
		1: 	[[1, 1, 1],
			 [0, 1, 0]],

		2:	[[0, 2, 2],
			 [2, 2, 0]],

		3:	[[3, 3, 0],
			 [0, 3, 3]],

		4:	[[4, 0, 0],
			 [4, 4, 4]],

		5:	[[0, 0, 5],
			 [5, 5, 5]],

		6:	[[6, 6, 6, 6]],

		7:	[[7, 7],
			 [7, 7]]
		}

		self.curr_piece = self.tetris_shapes[1]

		self.next_piece = self.tetris_shapes[1]

	def rotate_right(shape):
		"""
		Rotate clockwise / right
		"""
		# TODO: Complete the function


########
# GAME #
########
class Game:
	def __init__(self):
		# Initialize classes
		self.board_class = Board()
		self.pieces = Piece()

		# Initialize game variables
		self.score = 0

		# Initialize PyGame
		pygame.init()
		pygame.key.set_repeat(250, 25)

		# Initialize front-end board settings
		self.width = cell_size * (self.board_class.x_size + 6)
		self.height = cell_size * self.board_class.y_size
		self.rlim = cell_size * self.board_class.x_size

		self.bground_grid = [
			[8 if x % 2 == y % 2 else 0 for x in range(self.board_class.x_size)] for y in range(self.board_class.y_size)
			]

		self.default_font = pygame.font.Font(pygame.font.get_default_font(), 12)

		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.event.set_blocked(pygame.MOUSEMOTION)

		try:
			self.pieces.next_piece = self.pieces.tetris_shapes[ rand(len(self.pieces.tetris_shapes.keys()))]
		except KeyError, e:
			self.pieces.next_piece = self.pieces.tetris_shapes[ rand(len(self.pieces.tetris_shapes.keys()))]

		self.new_stone()

	def check_collision(self, board, shape, offset_x, offset_y):
		"""
		Check collisions
		"""
		off_x, off_y = offset_x, offset_y
		for cy, row in enumerate(shape):
			for cx, cell in enumerate(row):
				try:
					if cell and board[cy + off_y][cx + off_x]:
						return True
				except IndexError:
					return True
		return False

	def new_stone(self):
		self.pieces.curr_piece = self.pieces.next_piece[:]
		try:
			self.pieces.next_piece = self.pieces.tetris_shapes[ rand(len(self.pieces.tetris_shapes.keys()))]
		except KeyError, e:
			self.pieces.next_piece = self.pieces.tetris_shapes[ rand(len(self.pieces.tetris_shapes.keys()))]

		self.piece_x = int(self.board_class.x_size / 2 - len(self.pieces.curr_piece) / 2)
		self.piece_y = 0

		if self.check_collision(board=self.board_class.board, shape=self.pieces.curr_piece, offset_x=self.piece_x, offset_y=self.piece_y):
			self.gameover = True

	def disp_msg(self, msg, topleft):
		"""
		Displays message
		"""
		x, y= topleft
		for line in msg.splitlines():
			self.screen.blit(
				self.default_font.render(
					line,
					False,
					(255, 255, 255),
					(0, 0, 0)),
				(x, y))
			y += 14

	def center_msg(self, msg):
		for i, line in enumerate(msg.splitlines()):
			msg_image=self.default_font.render(line, False,
				(255, 255, 255), (0, 0, 0))

			msgim_center_x, msgim_center_y=msg_image.get_size()
			msgim_center_x //= 2
			msgim_center_y //= 2

			self.screen.blit(msg_image, (
			  self.width // 2 - msgim_center_x,
			  self.height // 2 - msgim_center_y + i * 22))

	def concat_dictionary(self, dictionary):
		"""
		Combines the arrays in dictionary for board
		"""
		return_matrix=[]
		for arr in dictionary.values():
			return_matrix.append(arr)

		return return_matrix

	def draw_matrix(self, matrix, offset):
		off_x, off_y=offset
		for y, row in enumerate(matrix):
			for x, val in enumerate(row):
				if val:
					pygame.draw.rect(
						self.screen,
						colors[val],
						pygame.Rect(
							(off_x + x) *
							  cell_size,
							(off_y + y) *
							  cell_size,
							cell_size,
							cell_size), 0)

	def move(self, delta_x):
		if not self.gameover and not self.paused:
			new_x=self.piece_x + delta_x
			if new_x < 0:
				new_x=0
			if new_x > cols - len(self.pieces.curr_piece[0]):
				new_x=cols - len(self.pieces.curr_piece[0])
			if not check_collision(self.board_class.board,
			                       self.pieces.curr_piece,
			                       new_x, self.piece_y):
				self.piece_x = new_x

	def quit(self):
		self.center_msg("Exiting...")
		pygame.display.update()
		sys.exit()

	def drop(self, manual):
		if not self.gameover and not self.paused:
			self.piece_y += 1

			board_arr = concat_dictionary(self.board_class.board)

			if check_collision(self.board_class.board,
			                   self.pieces.curr_piece,
			                   self.piece_x, self.piece_y):
				self.board_class.board = self.board_class.join_board(
				  self.board_class.board,
				  self.pieces.curr_piece,
				  (self.piece_x, self.piece_y))
				self.new_stone()
				cleared_rows = 0
				while True:
					for i, row in enumerate(self.board_class.board[:-1]):
						if 0 not in row:
							self.board_class.board = remove_row(
							  self.board_class.board, i)
							cleared_rows += 1
							break
					else:
						break
				self.add_cl_lines(cleared_rows)
				return True
		return False

	def rotate_piece_with_constraints(self):
		if not self.gameover and not self.paused:
			new_piece = self.pieces.rotate_right(self.pieces.curr_piece)
			if not check_collision(self.board_class.board,
			                       new_stone,
			                       self.piece_x, self.piece_y):
				self.pieces.curr_piece = new_piece

	def toggle_pause(self):
		self.paused = not self.paused

	def start_game(self):
		if self.gameover:
			self.init_game()
			self.gameover = False

	def add_cl_lines(self, n):
		self.score += self.add_score(n)

	def add_score(self, line_number):
		temp_score = (20 * line_number) * (1.2 ** (line_number - 1))
		return int(round(temp_score, -1))

	def run(self):
		key_actions = {
			'ESCAPE':	self.quit,
			'LEFT':		lambda:self.move(-1),
			'RIGHT':	lambda:self.move(1),
			'DOWN':		lambda:self.drop(True),
			'UP':		self.rotate_piece_with_constraints,
			'p':		self.toggle_pause,
			'SPACE':	self.start_game,
		}

		self.gameover = False
		self.paused = False

		clock = pygame.time.Clock()

		while True:
			self.screen.fill((0,0,0))
			if self.gameover:
				self.center_msg("""Game Over!
Press space to continue""")
			else:
				if self.paused:
					self.center_msg("Paused")
				else:
					pygame.draw.line(
						self.screen,
						(255,255,255),
						(self.rlim + 1, 0),
						(self.rlim + 1, self.height - 1)
						)

					self.disp_msg("Next:", (
							self.rlim + cell_size,
							2)
						)

					self.disp_msg(
						str(self.score),
						(self.rlim + cell_size, cell_size * 5)
						)

					self.draw_matrix(self.bground_grid, (0,0))

					self.draw_matrix(self.board_class.board, (0,0))

					self.draw_matrix(
						self.pieces.curr_piece,
						(self.piece_x, self.piece_y)
						)

					self.draw_matrix(self.pieces.next_piece,
						(self.board_class.x_size + 1, 2)
						)

			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
				elif event.type == pygame.KEYDOWN:
					for key in key_actions:
						if event.key == eval("pygame.K_"
						+key):
							key_actions[key]()

			clock.tick(maxfps)

########
# MAIN #
########
if __name__ == '__main__':
	game = Game()
	game.run()
