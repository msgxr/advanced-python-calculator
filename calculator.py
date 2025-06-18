import math
import statistics
import sys
from typing import Union, List

class AdvancedCalculator:
    """
    Gelişmiş Hesap Makinesi Sınıfı
    
    Özellikler:
    - Temel matematiksel işlemler (+, -, *, /, **)
    - Trigonometrik fonksiyonlar
    - Logaritmik fonksiyonlar  
    - İstatistiksel hesaplamalar
    - Sayı sistemi dönüşümleri
    - Geçmiş kayıtları
    """
    
    def __init__(self):
        self.history = []
        self.memory = 0
        
    def add_to_history(self, operation: str, result: Union[int, float]):
        """İşlem geçmişine ekle"""
        self.history.append(f"{operation} = {result}")
        
    def show_history(self):
        """Geçmişi göster"""
        if not self.history:
            print("Henüz işlem yapılmamış.")
            return
        
        print("\n=== İŞLEM GEÇMİŞİ ===")
        for i, operation in enumerate(self.history[-10:], 1):  # Son 10 işlem
            print(f"{i}. {operation}")
        print("=" * 25)
    
    def clear_history(self):
        """Geçmişi temizle"""
        self.history.clear()
        print("Geçmiş temizlendi.")
    
    # Temel Matematik İşlemleri
    def add(self, a: float, b: float) -> float:
        """Toplama"""
        result = a + b
        self.add_to_history(f"{a} + {b}", result)
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Çıkarma"""
        result = a - b
        self.add_to_history(f"{a} - {b}", result)
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Çarpma"""
        result = a * b
        self.add_to_history(f"{a} × {b}", result)
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Bölme"""
        if b == 0:
            raise ValueError("Sıfıra bölme hatası!")
        result = a / b
        self.add_to_history(f"{a} ÷ {b}", result)
        return result
    
    def power(self, a: float, b: float) -> float:
        """Üs alma"""
        result = a ** b
        self.add_to_history(f"{a}^{b}", result)
        return result
    
    def sqrt(self, a: float) -> float:
        """Karekök"""
        if a < 0:
            raise ValueError("Negatif sayının karekökü alınamaz!")
        result = math.sqrt(a)
        self.add_to_history(f"√{a}", result)
        return result
    
    def factorial(self, n: int) -> int:
        """Faktöriyel"""
        if n < 0:
            raise ValueError("Negatif sayının faktöriyeli hesaplanamaz!")
        result = math.factorial(n)
        self.add_to_history(f"{n}!", result)
        return result
    
    # Trigonometrik Fonksiyonlar
    def sin(self, angle: float, degree: bool = True) -> float:
        """Sinüs"""
        if degree:
            angle = math.radians(angle)
        result = math.sin(angle)
        unit = "°" if degree else "rad"
        self.add_to_history(f"sin({angle if not degree else math.degrees(angle)}{unit})", result)
        return result
    
    def cos(self, angle: float, degree: bool = True) -> float:
        """Kosinüs"""
        if degree:
            angle = math.radians(angle)
        result = math.cos(angle)
        unit = "°" if degree else "rad"
        self.add_to_history(f"cos({angle if not degree else math.degrees(angle)}{unit})", result)
        return result
    
    def tan(self, angle: float, degree: bool = True) -> float:
        """Tanjant"""
        if degree:
            angle = math.radians(angle)
        result = math.tan(angle)
        unit = "°" if degree else "rad"
        self.add_to_history(f"tan({angle if not degree else math.degrees(angle)}{unit})", result)
        return result
    
    # Logaritmik Fonksiyonlar
    def log(self, a: float, base: float = math.e) -> float:
        """Logaritma"""
        if a <= 0:
            raise ValueError("Logaritma için pozitif sayı gerekli!")
        result = math.log(a, base)
        base_str = "e" if base == math.e else str(base)
        self.add_to_history(f"log_{base_str}({a})", result)
        return result
    
    def log10(self, a: float) -> float:
        """10 tabanında logaritma"""
        if a <= 0:
            raise ValueError("Logaritma için pozitif sayı gerekli!")
        result = math.log10(a)
        self.add_to_history(f"log₁₀({a})", result)
        return result
    
    # İstatistiksel Fonksiyonlar
    def mean(self, numbers: List[float]) -> float:
        """Ortalama"""
        if not numbers:
            raise ValueError("Liste boş olamaz!")
        result = statistics.mean(numbers)
        self.add_to_history(f"ortalama({numbers})", result)
        return result
    
    def median(self, numbers: List[float]) -> float:
        """Medyan"""
        if not numbers:
            raise ValueError("Liste boş olamaz!")
        result = statistics.median(numbers)
        self.add_to_history(f"medyan({numbers})", result)
        return result
    
    def mode(self, numbers: List[float]) -> float:
        """Mod"""
        if not numbers:
            raise ValueError("Liste boş olamaz!")
        result = statistics.mode(numbers)
        self.add_to_history(f"mod({numbers})", result)
        return result
    
    def standard_deviation(self, numbers: List[float]) -> float:
        """Standart sapma"""
        if len(numbers) < 2:
            raise ValueError("En az 2 sayı gerekli!")
        result = statistics.stdev(numbers)
        self.add_to_history(f"std_dev({numbers})", result)
        return result
    
    # Sayı Sistemi Dönüşümleri
    def decimal_to_binary(self, n: int) -> str:
        """Ondalık sayıyı ikili sisteme çevir"""
        result = bin(n)[2:]  # '0b' prefix'ini kaldır
        self.add_to_history(f"{n} (ondalık) → ikili", result)
        return result
    
    def decimal_to_hex(self, n: int) -> str:
        """Ondalık sayıyı onaltılı sisteme çevir"""
        result = hex(n)[2:].upper()  # '0x' prefix'ini kaldır ve büyük harf yap
        self.add_to_history(f"{n} (ondalık) → onaltılı", result)
        return result
    
    def binary_to_decimal(self, binary_str: str) -> int:
        """İkili sistemi ondalık sayıya çevir"""
        result = int(binary_str, 2)
        self.add_to_history(f"{binary_str} (ikili) → ondalık", result)
        return result
    
    def hex_to_decimal(self, hex_str: str) -> int:
        """Onaltılı sistemi ondalık sayıya çevir"""
        result = int(hex_str, 16)
        self.add_to_history(f"{hex_str} (onaltılı) → ondalık", result)
        return result
    
    # Hafıza İşlemleri
    def memory_store(self, value: float):
        """Hafızaya kaydet"""
        self.memory = value
        print(f"Hafızaya kaydedildi: {value}")
    
    def memory_recall(self) -> float:
        """Hafızadan çağır"""
        print(f"Hafızadan çağrıldı: {self.memory}")
        return self.memory
    
    def memory_clear(self):
        """Hafızayı temizle"""
        self.memory = 0
        print("Hafıza temizlendi.")
    
    def memory_add(self, value: float):
        """Hafızaya ekle"""
        self.memory += value
        print(f"Hafızaya eklendi. Yeni değer: {self.memory}")
    
    def memory_subtract(self, value: float):
        """Hafızadan çıkar"""
        self.memory -= value
        print(f"Hafızadan çıkarıldı. Yeni değer: {self.memory}")


def get_number_input(prompt: str) -> float:
    """Kullanıcıdan sayı al"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")


def get_number_list_input(prompt: str) -> List[float]:
    """Kullanıcıdan sayı listesi al"""
    while True:
        try:
            numbers_str = input(prompt)
            numbers = [float(x.strip()) for x in numbers_str.split(',')]
            return numbers
        except ValueError:
            print("Lütfen virgülle ayrılmış geçerli sayılar girin! (örn: 1,2,3,4)")


def print_menu():
    """Ana menüyü yazdır"""
    print("\n" + "="*50)
    print("           GELİŞMİŞ HESAP MAKİNESİ")
    print("="*50)
    print("TEMEL İŞLEMLER:")
    print("1. Toplama            11. Sinüs")
    print("2. Çıkarma            12. Kosinüs")
    print("3. Çarpma             13. Tanjant")
    print("4. Bölme              14. Logaritma (ln)")
    print("5. Üs alma            15. Logaritma (log10)")
    print("6. Karekök            16. Ortalama")
    print("7. Faktöriyel         17. Medyan")
    print("8. Mod                18. Standart Sapma")
    print("\nSAYI SİSTEMLERİ:")
    print("19. Ondalık → İkili   23. İkili → Ondalık")
    print("20. Ondalık → Onaltılı 24. Onaltılı → Ondalık")
    print("\nHAFIZA İŞLEMLERİ:")
    print("25. Hafızaya Kaydet   28. Hafızaya Ekle")
    print("26. Hafızadan Çağır   29. Hafızadan Çıkar")
    print("27. Hafızayı Temizle")
    print("\nDİĞER:")
    print("30. Geçmişi Göster    32. Çıkış")
    print("31. Geçmişi Temizle")
    print("="*50)


def main():
    """Ana program"""
    calc = AdvancedCalculator()
    
    print("Python Gelişmiş Hesap Makinesi'ne Hoş Geldiniz!")
    print("GitHub: https://github.com/yourusername/advanced-calculator")
    
    while True:
        try:
            print_menu()
            choice = input("\nSeçiminizi yapın (1-32): ").strip()
            
            if choice == '32':
                print("Hesap makinesinden çıkılıyor. Güle güle!")
                break
            
            elif choice == '1':  # Toplama
                a = get_number_input("Birinci sayı: ")
                b = get_number_input("İkinci sayı: ")
                result = calc.add(a, b)
                print(f"Sonuç: {result}")
            
            elif choice == '2':  # Çıkarma
                a = get_number_input("Birinci sayı: ")
                b = get_number_input("İkinci sayı: ")
                result = calc.subtract(a, b)
                print(f"Sonuç: {result}")
            
            elif choice == '3':  # Çarpma
                a = get_number_input("Birinci sayı: ")
                b = get_number_input("İkinci sayı: ")
                result = calc.multiply(a, b)
                print(f"Sonuç: {result}")
            
            elif choice == '4':  # Bölme
                a = get_number_input("Bölünen: ")
                b = get_number_input("Bölen: ")
                result = calc.divide(a, b)
                print(f"Sonuç: {result}")
            
            elif choice == '5':  # Üs alma
                a = get_number_input("Taban: ")
                b = get_number_input("Üs: ")
                result = calc.power(a, b)
                print(f"Sonuç: {result}")
            
            elif choice == '6':  # Karekök
                a = get_number_input("Sayı: ")
                result = calc.sqrt(a)
                print(f"Sonuç: {result}")
            
            elif choice == '7':  # Faktöriyel
                n = int(get_number_input("Sayı (tam sayı): "))
                result = calc.factorial(n)
                print(f"Sonuç: {result}")
            
            elif choice == '8':  # Mod
                numbers = get_number_list_input("Sayıları virgülle ayırarak girin: ")
                result = calc.mode(numbers)
                print(f"Sonuç: {result}")
            
            elif choice in ['11', '12', '13']:  # Trigonometrik
                angle = get_number_input("Açı: ")
                unit = input("Derece için 'd', radyan için 'r' girin: ").lower()
                degree = unit == 'd'
                
                if choice == '11':
                    result = calc.sin(angle, degree)
                elif choice == '12':
                    result = calc.cos(angle, degree)
                else:
                    result = calc.tan(angle, degree)
                print(f"Sonuç: {result}")
            
            elif choice == '14':  # Logaritma (ln)
                a = get_number_input("Sayı: ")
                result = calc.log(a)
                print(f"Sonuç: {result}")
            
            elif choice == '15':  # Logaritma (log10)
                a = get_number_input("Sayı: ")
                result = calc.log10(a)
                print(f"Sonuç: {result}")
            
            elif choice == '16':  # Ortalama
                numbers = get_number_list_input("Sayıları virgülle ayırarak girin: ")
                result = calc.mean(numbers)
                print(f"Sonuç: {result}")
            
            elif choice == '17':  # Medyan
                numbers = get_number_list_input("Sayıları virgülle ayırarak girin: ")
                result = calc.median(numbers)
                print(f"Sonuç: {result}")
            
            elif choice == '18':  # Standart sapma
                numbers = get_number_list_input("Sayıları virgülle ayırarak girin: ")
                result = calc.standard_deviation(numbers)
                print(f"Sonuç: {result}")
            
            elif choice == '19':  # Ondalık → İkili
                n = int(get_number_input("Ondalık sayı: "))
                result = calc.decimal_to_binary(n)
                print(f"İkili sistem: {result}")
            
            elif choice == '20':  # Ondalık → Onaltılı
                n = int(get_number_input("Ondalık sayı: "))
                result = calc.decimal_to_hex(n)
                print(f"Onaltılı sistem: {result}")
            
            elif choice == '23':  # İkili → Ondalık
                binary = input("İkili sayı: ")
                result = calc.binary_to_decimal(binary)
                print(f"Ondalık sistem: {result}")
            
            elif choice == '24':  # Onaltılı → Ondalık
                hex_num = input("Onaltılı sayı: ")
                result = calc.hex_to_decimal(hex_num)
                print(f"Ondalık sistem: {result}")
            
            elif choice == '25':  # Hafızaya kaydet
                value = get_number_input("Kaydedilecek değer: ")
                calc.memory_store(value)
            
            elif choice == '26':  # Hafızadan çağır
                calc.memory_recall()
            
            elif choice == '27':  # Hafızayı temizle
                calc.memory_clear()
            
            elif choice == '28':  # Hafızaya ekle
                value = get_number_input("Eklenecek değer: ")
                calc.memory_add(value)
            
            elif choice == '29':  # Hafızadan çıkar
                value = get_number_input("Çıkarılacak değer: ")
                calc.memory_subtract(value)
            
            elif choice == '30':  # Geçmişi göster
                calc.show_history()
            
            elif choice == '31':  # Geçmişi temizle
                calc.clear_history()
            
            else:
                print("Geçersiz seçim! Lütfen 1-32 arası bir sayı girin.")
        
        except ValueError as e:
            print(f"Hata: {e}")
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")
        
        input("\nDevam etmek için Enter'a basın...")


if __name__ == "__main__":
    main()
