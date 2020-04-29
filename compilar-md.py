import fitz
pdffile = "livro.pdf"
doc = fitz.open(pdffile)
md = open('README.md','w',encoding='utf-8')
md.write("""[![Download](https://github-basic-badges.herokuapp.com/downloads/papborges/MATEMATICA_C/livro.pdf.svg)](https://github.com/papborges/MATEMATICA_C/raw/master/livro.pdf)
# Livro matemática C
""")
i=1
while True :
    try :
        page = doc.loadPage(i-1) #number of page
        pix = page.getPixmap()
        output = f"paginas_png/pagina{i}.png"
        md.write(f"[![Página {i}]({output})](https://github.com/papborges/MATEMATICA_C/raw/master/livro.pdf)\n---\n")
        pix.writePNG(output)
    except :
        break
    i+=1
md.close()