import math
import turtle

# Ekranı ayarla
window = turtle.Screen()
window.bgcolor("black")  # Arka plan rengini siyah yap

# Kaplumbağayı (turtle) ayarla
pen = turtle.Turtle()
pen.speed(0)  # En hızlı çizim hızı
pen.color("red")  # Kaplumbağa çizim rengini kırmızı yap

# Kalp şeklinin matematiksel fonksiyonu
def heart(t):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, y  # Hesaplanan x ve y koordinatlarını döndür

# Kalp desenini çiz
pen.penup()  # Çizim yapmayı geçici olarak durdur
for i in range(10):  # kaç adet kalp çizileceğini belirle
    pen.goto(0, 0)  # Başlangıç konumuna dön
    pen.pendown()  # Çizimi başlat
    for t in range(0, 100, 2):  # Adım boyutunu artırarak nokta sayısını azalt
        x, y = heart(t / 5)  # Kalp fonksiyonunun karmaşıklığını belirt ne kadar yüksek sayı olursa kalp o kadar net olur
        pen.goto(x * i, y * i)  # Koordinatlara git
    pen.penup()  # Çizimi geçici olarak durdur

# Kaplumbağayı gizle ve pencereyi açık bırak
pen.hideturtle()
turtle.done()