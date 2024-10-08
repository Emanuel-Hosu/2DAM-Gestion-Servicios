words = ["Emi", "Mundo", "Pera", "Manzana"]
long_words = []

for i in words:
    if len(i) > 4:
        long_words.append(i)
        
print(long_words)