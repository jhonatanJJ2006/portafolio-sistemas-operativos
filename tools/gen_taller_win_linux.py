# Genera taller-windows-linux.html: infografias de la evolucion de Windows y Linux.
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / "una-pagina.html").read_text(encoding="utf-8")
style = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
extra = """
  .os-head { position:absolute; left:100px; width:1166px; height:64px; background:#12234b; border:2px solid #22427f; border-left:10px solid #f5b82e; border-radius:14px; padding:14px 24px; font-family:'Montserrat',Arial,sans-serif; font-size:26px; font-weight:800; color:#fff; }
  .os-head span { color:#6fb7ff; font-size:16px; font-weight:700; letter-spacing:2px; margin-left:14px; }
  .card { position:absolute; width:568px; height:118px; background:#12234b; border:2px solid #22427f; border-top:5px solid #f5b82e; border-radius:14px; }
  .card .yr { position:absolute; left:16px; top:18px; width:84px; height:76px; border-radius:12px; background:#f5b82e; color:#0b1630; font-family:'Montserrat',Arial,sans-serif; font-weight:800; font-size:24px; text-align:center; padding-top:22px; }
  .card h3 { text-align:left; position:absolute; left:118px; top:14px; font-size:21px; line-height:26px; color:#fff; white-space:nowrap; }
  .card p { text-align:left; position:absolute; left:118px; top:44px; width:432px; font-size:15px; line-height:21px; color:#e3ecff; }
  .card.now { border-top-color:#6fb7ff; background:#10224a; }
  .card.now .yr { background:#6fb7ff; }
  .sources { position:absolute; left:100px; width:1166px; text-align:center; font-size:14px; line-height:22px; color:#9cc9ff; }
"""
WIN = [
 ("1985","Windows 1.0","Entorno gráfico de 16 bits que se ejecutaba sobre MS-DOS (1981). Ventanas en mosaico y uso del ratón."),
 ("1987","Windows 2.0","Ventanas superpuestas y atajos de teclado; primeras versiones de Word y Excel para Windows."),
 ("1990","Windows 3.0 / 3.1","Administrador de programas, mejor manejo de memoria y fuentes TrueType (3.1, 1992). Gran éxito comercial."),
 ("1993","Windows NT 3.1","Nuevo núcleo de 32 bits, sistema de archivos NTFS y seguridad multiusuario; base de las versiones actuales."),
 ("1995","Windows 95","Menú Inicio, barra de tareas, Plug and Play y nombres de archivo largos."),
 ("1998","Windows 98","Soporte USB, Internet Explorer integrado y sistema de archivos FAT32."),
 ("2000","Windows 2000 y ME","2000: núcleo NT para empresas con Active Directory. ME: última versión basada en MS-DOS."),
 ("2001","Windows XP","Une la línea doméstica con el núcleo NT. Interfaz Luna; muy popular por más de una década."),
 ("2007","Windows Vista","Interfaz Aero, Control de cuentas de usuario (UAC) y mayor seguridad, pero altos requisitos."),
 ("2009","Windows 7","Barra de tareas renovada, mejor rendimiento que Vista y soporte táctil básico."),
 ("2012","Windows 8 / 8.1","Pantalla de Inicio con mosaicos para tabletas y la Tienda Windows. 8.1 (2013) recupera el botón Inicio."),
 ("2015","Windows 10","Vuelve el menú Inicio, navegador Edge, asistente Cortana y actualizaciones continuas como servicio."),
 ("2021","Windows 11","Diseño centrado, requisito de TPM 2.0 y Arranque seguro, widgets y diseños de ventanas (Snap)."),
 ("2026","Windows 11, versión 26H2","Versión actual (29 sep 2026), «Windows 11 2026 Update»: llega como paquete de habilitación sobre 24H2 y 25H2."),
]
LIN = [
 ("1969","UNIX","Creado en Bell Labs por Ken Thompson y Dennis Ritchie; reescrito en C en 1973. Inspira a Linux."),
 ("1983","Proyecto GNU","Richard Stallman anuncia GNU para crear un sistema tipo UNIX libre; en 1989 nace la licencia GPL."),
 ("1991","Linux 0.01","Linus Torvalds, estudiante en Helsinki, publica su núcleo para PC con procesador Intel 386."),
 ("1993","Primeras distribuciones","Slackware y Debian unen el núcleo Linux con las herramientas GNU en un sistema listo para instalar."),
 ("1994","Linux 1.0","Primera versión estable del núcleo, con soporte de red. Ese año nace Red Hat Linux."),
 ("1996","Linux 2.0","Soporte para varios procesadores (SMP). En 2003 la serie 2.6 mejora el rendimiento en servidores."),
 ("2004","Ubuntu","Distribución basada en Debian pensada para escritorio; acerca Linux a usuarios comunes."),
 ("2008","Android","Google lanza Android, basado en el núcleo Linux; lleva Linux a miles de millones de teléfonos."),
 ("2011","Linux 3.0","Cambio de numeración por los 20 años de Linux; mejoras en sistemas de archivos como Btrfs."),
 ("2015","Linux 4.0","Parcheo del núcleo en vivo (livepatch) para aplicar arreglos sin reiniciar."),
 ("2019","Linux 5.0","Mayor soporte de hardware nuevo; en 5.1 llega io_uring para entrada y salida asíncrona."),
 ("2022","Linux 6.0","En 6.1 se integra el lenguaje Rust como segundo lenguaje para escribir el núcleo."),
 ("2026","Linux 7.0","Publicado en abril de 2026; continúa la serie con nuevas mejoras de hardware y seguridad."),
 ("2026","Linux 7.2 (actual)","Versión estable más reciente: 7.2.9 (3 oct 2026). Distros clave hoy: Ubuntu, Debian, Fedora, Arch."),
]
out=[]; a=out.append
a('<div class="circle-deco" style="left:1060px; top:24px; width:380px; height:380px;"></div>')
a('<div class="sec-kicker" style="top:70px;">Infografía · Taller · Evolución de los SO</div>')
a('<h2 class="sec-title" style="top:102px;">Taller: Evolución de <b>Windows y Linux</b></h2>')
a('<div class="accent-bar" style="left:100px; top:172px;"></div>')
a('<div class="sec-lead" style="top:196px;">Dos sistemas operativos con historias distintas: Windows, el sistema comercial de Microsoft, y Linux, el núcleo libre creado por una comunidad. Así evolucionaron desde sus primeras versiones hasta hoy.</div>')
y=300
def block(title, sub, items, y):
    a(f'<div class="os-head" style="top:{y}px;">{title}<span>{sub}</span></div>')
    y+=90
    for i,(yr,n,d) in enumerate(items):
        left=100 if i%2==0 else 698
        top=y+(i//2)*136
        cls="card now" if i==len(items)-1 else "card"
        a(f'<div class="{cls}" style="left:{left}px; top:{top}px;"><div class="yr">{yr}</div><h3>{n}</h3><p>{d}</p></div>')
    return y+((len(items)+1)//2)*136
y=block("Evolución de Windows","MICROSOFT · 1985 – 2026",WIN,y)
y+=40; a(f'<div class="divider" style="top:{y}px;"></div>'); y+=50
y=block("Evolución de Linux","UNIX · GNU · LINUX · 1969 – 2026",LIN,y)
y+=30
a(f'<div class="sources" style="top:{y}px;">Fuentes: Microsoft Learn, «Windows 11 release information» (2026); Windows Experience Blog (29/09/2026); kernel.org (10/2026);<br>Torvalds, L. (1991), anuncio en comp.os.minix; gnu.org, «Anuncio inicial» (1983); Tanenbaum, A. S. y Bos, H. (2015). <i>Modern Operating Systems</i>. Pearson.</div>')
f=y+46+40
a(f'<div class="footer" style="top:{f}px;">')
a('  <div class="footer-main">Elaborado por <b>Jhonatan Jara</b> · Computación · UTPL · 2026</div>')
a('  <div class="footer-sub">Taller de la Evolución de los Sistemas Operativos · Windows y Linux</div>')
a('</div>')
H=f+140
head=src.split("<style>")[0].replace("Funciones de los componentes de un Sistema Operativo · Jhonatan Jara","Evolución de Windows y Linux · Jhonatan Jara")
section=f'<section class="page" style="height:{H}px;" data-document-role="page" data-label="Evolución de Windows y Linux">\n  '+"\n  ".join(out)+'\n</section>'
(ROOT/"taller-windows-linux.html").write_text(f"{head}<style>{style}{extra}</style>\n</head>\n<body>\n\n{section}\n\n</body>\n</html>\n",encoding="utf-8")
print("H",H)
