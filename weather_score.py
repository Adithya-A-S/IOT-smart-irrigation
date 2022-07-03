from weather import weather_data
#import random
def ws():
  list = weather_data()
  temp = list[0]
  humi = list[1]
  cloud = list[2]
  #n = random.randint(15,25)

  def clouds(cloud):
    l1 = ['clear sky','few clouds']
    l2 = ['scattered clouds','broken clouds']
    l3 = ['mist','snow','haze']
    l4 = ['shower rain','rain']
    l5 = ['thunderstorm']
    if cloud in l1:
      cs = 50
    elif cloud in l2:
      cs = 40
    elif cloud in l3:
      cs = 30
    elif cloud in l4:
      cs = 20
    elif cloud in l5:
      cs = 10
    else:
      cs = 0
    return cs

  def temperature(temp):
    if temp<5:ts = 10
    elif temp>5  and temp<=10:ts = 20
    elif temp>10 and temp<=15:ts = 30
    elif temp>15 and temp<=20:ts = 40
    elif temp>20 and temp<=25:ts = 50
    elif temp>25 and temp<=30:ts = 60
    elif temp>30 and temp<=35:ts = 70
    elif temp>35 and temp<=40:ts = 80
    elif temp>40 and temp<=45:ts = 90
    else: ts = 100
    ts = ts/4
    return ts

  def humidity(humi):
    if humi<10: hs = 100
    elif humi>10 and humi<=20: hs = 90
    elif humi>20 and humi<=30: hs = 80
    elif humi>30 and humi<=40: hs = 70
    elif humi>40 and humi<=50: hs = 60
    elif humi>50 and humi<=60: hs = 50
    elif humi>60 and humi<=70: hs = 40
    elif humi>70 and humi<=80: hs = 30
    elif humi>80 and humi<=90: hs = 20
    else: hs = 10
    hs /= 4
    return hs
  ws = clouds(cloud)+temperature(temp)+humidity(humi)
  return round(ws/5)
                 

