# Genera evolucion.html (solo la nueva seccion) y una-pagina-con-evolucion.html (vista previa completa).
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://jhonatanjj2006.github.io/portafolio-sistemas-operativos/icons/"
local = "--local" in sys.argv
ICON = "icons/" if local else BASE

src = (ROOT / "una-pagina.html").read_text(encoding="utf-8")
style = re.search(r"<style>(.*?)</style>", src, re.S).group(1)

extra = """
  /* Linea de tiempo: evolucion de los SO */
  .tl-line { position: absolute; left: 98px; width: 4px; background: #1e3a72; border-radius: 2px; }
  .tl-node { position: absolute; left: 72px; width: 56px; height: 56px; border-radius: 50%; background: #f5b82e; border: 4px solid #0b1630; text-align: center; padding-top: 9px; font-family: 'Montserrat', Arial, sans-serif; font-weight: 800; font-size: 24px; color: #0b1630; }
  .gen { position: absolute; left: 160px; width: 1146px; height: 232px; background: #12234b; border: 2px solid #22427f; border-top: 6px solid #f5b82e; border-radius: 16px; }
  .gen .icon { position: absolute; left: 24px; top: 22px; width: 58px; height: 58px; }
  .gen .years { position: absolute; left: 98px; top: 20px; font-size: 15px; font-weight: 700; color: #6fb7ff; letter-spacing: 2px; text-transform: uppercase; white-space: nowrap; }
  .gen h3 { position: absolute; left: 98px; top: 44px; font-size: 24px; line-height: 30px; color: #ffffff; white-space: nowrap; }
  .gen .list { position: absolute; left: 24px; top: 100px; width: 600px; }
  .gen .li { display: flex; align-items: flex-start; margin-bottom: 8px; }
  .gen .dot { flex: 0 0 9px; width: 9px; height: 9px; margin-top: 7px; margin-right: 11px; border-radius: 50%; background: #f5b82e; }
  .gen .lt { flex: 1; font-size: 16px; line-height: 23px; color: #e3ecff; }
  .ex { position: absolute; left: 660px; top: 22px; width: 460px; height: 182px; background: #10224a; border: 2px solid #2b6cd4; border-radius: 14px; padding: 16px 20px; }
  .ex h4 { font-family: 'Montserrat', Arial, sans-serif; font-size: 16px; font-weight: 700; color: #f5b82e; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; }
  .ex p { font-size: 16px; line-height: 25px; color: #e3ecff; }
  .ex p b { color: #ffffff; }
  .hito { position: absolute; width: 133px; height: 112px; background: #10224a; border: 2px solid #2b6cd4; border-radius: 14px; padding: 14px 12px; text-align: center; }
  .hito h3 { font-size: 24px; color: #f5b82e; margin-bottom: 4px; }
  .hito .n { font-family: 'Montserrat', Arial, sans-serif; font-weight: 700; font-size: 15px; color: #ffffff; margin-bottom: 2px; white-space: nowrap; }
  .hito p { font-size: 13px; line-height: 17px; color: #cfe3ff; }
  .sources { position: absolute; left: 100px; width: 1166px; text-align: center; font-size: 15px; line-height: 23px; color: #9cc9ff; }
"""

def li(t):
    return f'<div class="li"><div class="dot"></div><div class="lt">{t}</div></div>'

GENS = [
    ("1", "valvula", "Primera generación · 1945 – 1955", "Tubos de vacío y tableros",
     ["Computadoras enormes construidas con miles de tubos de vacío.",
      "Se programaban en lenguaje máquina, conectando cables en tableros.",
      "No había sistema operativo: cada programador operaba la máquina a mano."],
     "<b>ENIAC</b> (1945) y <b>UNIVAC I</b> (1951). Desde inicios de los años 50 los programas se cargaban con <b>tarjetas perforadas</b>."),
    ("2", "transistor", "Segunda generación · 1955 – 1965", "Transistores y procesamiento por lotes",
     ["Los transistores hacen las computadoras más confiables (mainframes).",
      "Los trabajos se agrupan en lotes en cinta magnética y se ejecutan uno tras otro.",
      "Aparece el monitor residente, el primer sistema operativo."],
     "<b>GM-NAA I/O</b> (1956, IBM 704), considerado el primer SO. <b>FMS</b> (Fortran Monitor System) e <b>IBSYS</b> en la IBM 7094."),
    ("3", "circuito", "Tercera generación · 1965 – 1980", "Circuitos integrados y multiprogramación",
     ["Multiprogramación: varios trabajos en memoria para no dejar la CPU ociosa.",
      "Spooling y tiempo compartido: muchos usuarios conectados por terminales.",
      "Nace UNIX (1969), reescrito en lenguaje C en 1973."],
     "<b>OS/360</b> de IBM (1966), <b>CTSS</b> del MIT (1961), <b>MULTICS</b> (1965) y <b>UNIX</b> de Bell Labs (1969)."),
    ("4", "pc", "Cuarta generación · 1980 – hoy", "Computadoras personales",
     ["Los microprocesadores llevan la computadora a hogares y oficinas.",
      "Las interfaces gráficas (GUI), con ventanas y ratón, reemplazan a los comandos.",
      "Surgen los SO de red, los distribuidos y el software libre."],
     "<b>CP/M</b> (1974), <b>MS-DOS</b> (1981), sistema del <b>Macintosh</b> con GUI (1984, hoy macOS), <b>Windows</b> (1985) y <b>Linux</b> (1991)."),
    ("5", "movil", "Quinta generación · 1990 – hoy", "Dispositivos móviles, nube e IoT",
     ["SO para teléfonos y tabletas: pantalla táctil, batería y sensores como el GPS.",
      "Virtualización y nube: varios SO funcionan sobre un mismo servidor.",
      "SO embebidos para el Internet de las cosas (IoT)."],
     "<b>Palm OS</b> (1996), <b>Symbian</b> (1998), <b>iPhone OS</b> (2007, hoy iOS) y <b>Android</b> (2008). Nube: Amazon EC2 (2006)."),
]

HITOS = [
    ("1956", "GM-NAA I/O", "Primer SO por lotes"),
    ("1969", "UNIX", "Bell Labs"),
    ("1981", "MS-DOS", "IBM PC"),
    ("1984", "Macintosh", "GUI con ratón"),
    ("1985", "Windows 1.0", "Microsoft"),
    ("1991", "Linux", "Linus Torvalds"),
    ("2007", "iPhone OS", "Hoy iOS"),
    ("2008", "Android", "Google"),
]

out = []
a = out.append
a('<div class="circle-deco" style="left:1060px; top:24px; width:380px; height:380px;"></div>')
a('<div class="sec-kicker" style="top:70px;">Infografía · Taller 1.4 · Punto 1</div>')
a('<h2 class="sec-title" style="top:102px;">Evolución de los <b>sistemas operativos</b></h2>')
a('<div class="accent-bar" style="left:100px; top:172px;"></div>')
a('<div class="sec-lead" style="top:196px;">Los sistemas operativos evolucionaron junto con el hardware: pasaron de no existir a administrar desde computadoras de tubos de vacío hasta teléfonos inteligentes y servidores en la nube.</div>')

TOP0, STEP = 290, 258
last = TOP0 + STEP * (len(GENS) - 1)
a(f'<div class="tl-line" style="top:{TOP0 + 40}px; height:{last - TOP0}px;"></div>')
for i, (n, icon, years, title, bullets, ex) in enumerate(GENS):
    t = TOP0 + STEP * i
    a(f'<div class="tl-node" style="top:{t + 12}px;">{n}</div>')
    a(f'<div class="gen" style="top:{t}px;">')
    a(f'  <img class="icon" src="{ICON}{icon}.png" alt="">')
    a(f'  <div class="years">{years}</div>')
    a(f'  <h3>{title}</h3>')
    a('  <div class="list">' + "".join(li(b) for b in bullets) + '</div>')
    a(f'  <div class="ex"><h4>Ejemplos</h4><p>{ex}</p></div>')
    a('</div>')

y = TOP0 + STEP * len(GENS) + 20          # 1600
a(f'<div class="divider" style="top:{y}px;"></div>')
a(f'<div class="sec-kicker" style="top:{y + 50}px;">Línea de tiempo</div>')
a(f'<h2 class="sec-title" style="top:{y + 82}px;">Hitos <b>clave</b></h2>')
a(f'<div class="accent-bar" style="left:100px; top:{y + 152}px;"></div>')
hy = y + 186
for i, (yr, name, sub) in enumerate(HITOS):
    left = 100 + i * (133 + 15)
    a(f'<div class="hito" style="left:{left}px; top:{hy}px;"><h3>{yr}</h3><div class="n">{name}</div><p>{sub}</p></div>')

c = hy + 112 + 60                          # conclusion
a(f'<div class="divider" style="top:{c}px;"></div>')
a(f'<div class="circle-deco" style="left:1080px; top:{c + 40}px; width:360px; height:360px;"></div>')
a(f'<div class="sec-kicker" style="top:{c + 70}px;">Cierre</div>')
a(f'<h2 class="sec-title" style="top:{c + 102}px;"><b>Conclusión</b></h2>')
a(f'<div class="accent-bar" style="left:100px; top:{c + 172}px;"></div>')
a(f'<div class="concl-box" style="top:{c + 200}px;"><p>Cada generación trajo un sistema operativo más <b>eficiente</b>, más <b>accesible</b> y más <b>fácil de usar</b>.</p></div>')
bt = c + 435
labels = ["Lotes", "Multitarea", "GUI", "Móvil y nube"]
start = (1366 - (180 * 4 + 30 * 3)) // 2
for i, lab in enumerate(labels):
    a(f'<div class="badge" style="left:{start + i * 210}px; top:{bt}px;">{lab}</div>')
s = bt + 50 + 34
a(f'<div class="sources" style="top:{s}px;">Fuentes: Tanenbaum, A. S. y Bos, H. (2015). <i>Modern Operating Systems</i> (4.ª ed.). Pearson.<br>Videos de la clase: «Evolución de los Sistemas Operativos» y «La evolución de los sistemas operativos» (Vectorialis, YouTube).</div>')
f = s + 46 + 40
a(f'<div class="footer" style="top:{f}px;">')
a('  <div class="footer-main">Elaborado por <b>Jhonatan Jara</b> · Computación · UTPL · 2026</div>')
a('  <div class="footer-sub">Taller 1.4 · La evolución de los Sistemas Operativos</div>')
a('</div>')
H = f + 140

body = "\n  ".join(out)
head = src.split("<style>")[0].replace(
    "Funciones de los componentes de un Sistema Operativo · Jhonatan Jara",
    "Evolución de los Sistemas Operativos · Jhonatan Jara")
section = f'<section class="page" style="height:{H}px;" data-document-role="page" data-label="Evolución de los sistemas operativos">\n  {body}\n</section>'
doc = f"{head}<style>{style}{extra}</style>\n</head>\n<body>\n\n{section}\n\n</body>\n</html>\n"
suffix = "-local" if local else ""
(ROOT / f"evolucion{suffix}.html").write_text(doc, encoding="utf-8")

# Vista previa completa: la pagina actual seguida de la nueva seccion
full_src = src if not local else src.replace(BASE, "icons/")
full = full_src.replace("</style>", extra + "</style>").replace("</body>", section + "\n\n</body>")
full = full.replace('style="height:3506px;" data-document-role="page" data-label="Inicio"', 'style="height:3506px;" data-document-role="page" data-label="Inicio"')
(ROOT / f"una-pagina-con-evolucion{suffix}.html").write_text(full, encoding="utf-8")
print("altura de la seccion:", H)
