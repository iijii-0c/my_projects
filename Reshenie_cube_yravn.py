import math
print('''Решение кубических уравнений.
Данная программа решает кубические уравнения вида a*x^3+b*x^2+c*x+d=0
Введите коэффициены a,b,c,d или "!" для выхода.''')
j=(-1)**(1/2)
def proverka_koef (koef):
	koef_dop=input(f' Введите коэффициент {koef}=')
	if koef_dop=='!':
		exit()
	else:
		try:
			koef_dop=int(koef_dop)
			return(koef_dop)
		except:
			print('Вы ввели не число! Введите число.')
			return(proverka_koef(koef))
#def vvod(a,b,c,d):
#	a,b,c,d=proverka_koef(a),proverka_koef(b),proverka_koef(c),proverka_koef(d)
	
#	return(a,b,c,d,D,p,q)
def fi(q,D):
	if q==0:
		fi=math.pi/2
	elif q>0:
		fi=math.atan(((-D)**(1/2))/(-q/2))+math.pi
	else:
		fi=math.atan(((-D)**(1/2))/(-q/2))
	return(fi)

def korni(a,b,c,d):
  a,b,c,d=proverka_koef(a),proverka_koef(b),proverka_koef(c),proverka_koef(d)
  print(f'Ищем корни уравнения: {a}*x^3+{b}*x^2+{c}*x+{d}=0')
  print(''' Находим дискриминант "D=(q/2)^2+(p/3)^3",\n а также вспомогательные переменные\n "p=c/a-(b/a)^2/3" и\n "q=d/a+2*(b/a)^3/27-b*c/(3*a^2)" ''')
  p=c/a-((b/a)**2)/3
  q=d/a+2*((b/a)**3)/27-(b*c)/(3*a**2)
  D=((q/2)**2+(p/3)**3)
  print(f''' D={D},\n p={p},\n q={q}''')
  if D<0:
    print('D<0, 3 действительных корня')
    x1=round((-b/(3*a)+2*((-p/3)**(1/2))*math.cos(fi(q,D)/3)),4)
    x2=round((-b/(3*a)+2*((-p/3)**(1/2))*math.cos(fi(q,D)/3+2*(math.pi)/3)),4)
    x3=round((-b/(3*a)+2*((-p/3)**(1/2))*math.cos(fi(q,D)/3+4*(math.pi)/3)),4)
    return(f'x1={x1}, x2={x2}, x3={x3}')
  elif D==0:
    if q==0:
      print('D=0, q=0, 1 действительный корень')
      x1=round((-b/(3*a)),4)
      x2='2-го корня нет'
      x3='3-го корня нет'
      return(f'x1={x1}, {x2}, {x3}')
    else:
      print('D=0, q≠0, 1 или 2 действительных корня')
      x1=round((-b/(3*a)+2*get_cube(-q/2)),4)
      x2=round((-b/(3*a)-get_cube(-q/2)),4)
      x3='3-го корня нет'
      return(f'x1={x1}, x2={x2}, {x3}')
  else:
    print('D>0, 1 действительный и 2 комплексно сопряженных корня')
    x1=round((-b/(3*a))+(get_cube((-q/2)+D**(1/2))+get_cube((-q/2)-D**(1/2))),4)
    x2=round(((-b/(3*a))+(-1/2)*(get_cube((-q/2)+D**(1/2))+get_cube((-q/2)-D**(1/2)))),4)+j*round((3**(1/2)/2)*(get_cube((-q/2)+D**(1/2))-get_cube((-q/2)-D**(1/2))),4)
    x3=round(((-b/(3*a))+(-1/2)*(get_cube((-q/2)+D**(1/2))+get_cube((-q/2)-D**(1/2)))),4)-j*round((3**(1/2)/2)*(get_cube((-q/2)+D**(1/2))-get_cube((-q/2)-D**(1/2))),4)
    return(f'x1={x1}, x2={x2}, x3={x3}')
def get_cube(x):
    #print(x)
    if x < 0:
        x = abs(x)
        cube_root = x**(1/3)*(-1)
    else:
        cube_root = x**(1/3)
    return cube_root
print(korni('a','b','c','d'))
def loop():
  if input('Нажмите "!" для выхода или любую другую клавишу для продолжения')=="!":
    exit()
  else:
    print(korni('a','b','c','d'))
    loop()
loop()