import pygame 


pygame.init()


# oyun ekranı oluşturma 

en = 1000
boy =700

ekran = pygame.display.set_mode((en,boy))
pygame.display.set_caption('Ana Menü')


# oyun variableleri

game_paused = False
menu_state ="main"

# font tanımlaam 

font = pygame.font.SysFont("arialblack", 40)


# yazı rengi tanımlama 

TEXT_COL = (255,255,255)   #BEYAZ RENK 

# butonların resimlerinin yüklenmesi 

resume_img = pygame.image.load("bosbuton.png").convert_alpha()
options_img = pygame.image.load("button_options.png").convert_alpha()
quit_img = pygame.image.load("bosbuton.png").convert_alpha()
video_img = pygame.image.load('button_video.png').convert_alpha()
audio_img = pygame.image.load('button_audio.png').convert_alpha()
keys_img = pygame.image.load('button_keys.png').convert_alpha()
back_img = pygame.image.load('button_back.png').convert_alpha()

main_font = pygame.font.SysFont("arialblack", 40)


class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		ekran.blit(self.image, self.rect)
		ekran.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Butona Basıldı!")
	
	def kapanma(self, position):
		if position[0] in range(self.rect.left ,self.rect.right) and position[1]in range (self.rect.top,self.rect.bottom):
			run == False



	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")

button_surface = pygame.image.load("button_quit.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))





play_button = Button(resume_img, 500, 400, "BAŞLAT")
options_button = Button(options_img, 200, 300, "Button")
quit_button = Button(quit_img, 500, 500, "ÇIKIŞ")
video_button =Button(video_img, 400, 300, "Button")
audio_button =Button(audio_img, 500, 300, "Button")
keys_button =Button(keys_img, 600, 300, "Button")
back_button =Button(back_img, 700, 300, "Button")


# akran rengi 

renk = 52, 78, 91


run = True
while run:
	for event in pygame.event.get():
		if event.type  == pygame.QUIT:
			run = False


		if event.type == pygame.MOUSEBUTTONDOWN:
			play_button.checkForInput(pygame.mouse.get_pos())
			quit_button.kapanma(pygame.mouse.get_pos())

	ekran.fill(renk)

	play_button.update()
	play_button.changeColor(pygame.mouse.get_pos())

	quit_button.update()
	quit_button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()


