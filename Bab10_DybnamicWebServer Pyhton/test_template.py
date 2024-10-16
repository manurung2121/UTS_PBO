# Definisikan data
nama = "Gandi Rahmad"
buah = ["Apel", "Pisang", "Nanas"]

# Buat HTML
html_output = f"""
<html>
<body>
    <h1>Halo, {nama}!</h1>
    <ul>
        {"".join(f"<li>{b}</li>" for b in buah)}
    </ul>
</body>
</html>
"""

# Tampilkan output HTML
print(html_output)
