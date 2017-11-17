'''
Created on 15 нояб. 2017 г.

Библитека для работы с DDS (Direct Digital Sintese).
Класс DDS даёт генерацию волны с нужнымим параметрами.

@author: jogick
'''

import math

class DDS(object):
	'''
	Генерация волны с параметрами:
		freq - частота в Гц
		level - максимальная амплитуда в % (0...100)
		time - длительность сигнала в мс
		framerate - частота дискретизации в Гц
		phase - начальная фаза сигнала (0...359)
		sampwidth - уровень квантования в байтах (2 = 16 бит)
	'''

	def __init__(self):
		self.__freq = 0
		self.__time = 1
		self.__level = 75
		self.__sampwidth = 2
		self.__framerate = 44100
		self.__phase = 0
		self.Wave = []							# готовая волна
		# приватне переменные
		self.__m_sin = []						# таблица синусоиды    
		self.__len_table = 360					# размер таблицы синуса
		self.__generate_table()
		self.__generate()

	def __generate_table(self):                 # генерация таблицы синусоиды
		i = 0
		self.__m_sin = []
		
		u_max = int((((0xff+1)**self.__sampwidth)-1)/2*float(self.__level)/100)
		offset = (((0xff+1)**self.__sampwidth)-1)/2

		for i in range(0, self.__len_table + 1): # заполнение таблицы синуса
			d = 2*math.pi/360*i/(self.__len_table/360)
			
			s = int((math.sin(d) * u_max) + offset)
			self.__m_sin.append(s)

	def __generate(self):
		n = 0
		self.Wave = []
		
		dsin = float(self.__freq) / self.__framerate * self.__len_table	# вычисление приращения одного шага
		i = self.__phase/360.0 * self.__len_table							# задаём начальный сдвиг фазы
		if i > self.__len_table: i -= self.__len_table

		while (n < int(self.__time * self.__framerate)/1000):				# формирование выходного массива
			d = self.__m_sin[int(i)]
			self.Wave.append(d)
			i += dsin
			if i > self.__len_table:
				i -= self.__len_table
			n += 1
	
	@property
	def freq(self):
		'''
		Возвращает текущую частоту
		'''
		return self.__freq
	@freq.setter
	def freq(self, f):
		'''
		Установить частоту генерируемого сигнала
		'''
		try:
			self.__freq = abs(int(f))
			self.__generate()
		except():
			pass
	
	@property
	def level(self):
		'''
		Возвращает установленный уровень сигнала
		'''
		return self.__level
	@level.setter
	def level(self, lvl):
		'''
		Установить уровень сигнала в %
		'''
		try:
			self.__level = abs(int(lvl))
			self.__generate_table()
			self.__generate()
		except:
			pass
	
	@property
	def time(self):
		'''
		Возвращает текущую длительность сигнала в мс
		'''
		return self.__time
	@time.setter
	def time(self, t):
		'''
		Установить длительность генерируемого сигнала
		'''
		try:
			self.__time = abs(int(t))
			self.__generate()
		except:
			pass
	
	@property
	def framerate(self):
		'''
		Возвращает установленную частоту дискретизации
		'''
		return self.__framerate
	@framerate.setter
	def framerate(self, fr):
		'''
		Установить частоту дискретизации
		'''
		try:
			self.__framerate = abs(int(fr))
			self.__generate()
		except:
			pass
	
	@property
	def phase(self):
		return self.__phase
	@phase.setter
	def phase(self, ph):
		try:
			self.__phase = abs(int(ph))
			self.__generate()
		except:
			pass
	
	@property
	def sampwidth(self):
		return self.__sampwidth
	@sampwidth.setter
	def sampwidth(self, sw):
		try:
			self.__sampwidth = abs(int(sw))
			self.__generate_table()
			self.__generate()
		except:
			pass
	