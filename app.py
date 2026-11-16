from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cecyte jalisco</title>
    <link rel="icon" href="data:"> 
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #FFE5F1 0%, #FFF0F6 50%, #FFD9E8 100%);
            min-height: 100vh;
            color: #5A3A4A;
            padding: 20px;
        }

        /* ===================== PORTADA ===================== */
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        header.portada {
            text-align: center;
            padding: 50px 20px;
            background: rgba(255, 255, 255, 0.75);
            border-radius: 25px;
            margin-bottom: 40px;
            box-shadow: 0 8px 24px rgba(255, 143, 177, 0.25);
        }

        header.portada h1 {
            color: #D65A8C;
            font-size: 2.8em;
            margin-bottom: 10px;
        }

        header.portada p {
            font-size: 1.2em;
            color: #9A6A80;
            margin-bottom: 25px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .card {
            background: #FFFFFF;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 6px 20px rgba(255, 143, 177, 0.25);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
        }

        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 30px rgba(255, 143, 177, 0.4);
        }

        .card-img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            background: #FFE5F1;
        }

        .card-body {
            padding: 22px;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }

        .card-body h3 {
            color: #D65A8C;
            margin-bottom: 12px;
            font-size: 1.4em;
        }

        .card-body p {
            color: #7A5A6A;
            line-height: 1.6;
            margin-bottom: 18px;
            flex-grow: 1;
        }

        .info-section {
            background: rgba(255, 255, 255, 0.8);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 6px 20px rgba(255, 143, 177, 0.2);
        }

        .info-section h2 {
            color: #D65A8C;
            text-align: center;
            margin-bottom: 25px;
            font-size: 2em;
        }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .info-item {
            background: #FFF0F6;
            padding: 20px;
            border-radius: 15px;
            border-left: 5px solid #FF9EC4;
        }

        .info-item strong {
            color: #D65A8C;
            display: block;
            margin-bottom: 6px;
            font-size: 1.1em;
        }

        /* ===================== BOTONES ===================== */
        .btn {
            display: inline-block;
            padding: 12px 26px;
            background: linear-gradient(135deg, #FF9EC4, #FF7BA9);
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-weight: 600;
            transition: all 0.3s ease;
            text-align: center;
            box-shadow: 0 4px 12px rgba(255, 123, 169, 0.35);
            border: none;
            cursor: pointer;
            font-size: 1em;
        }

        .btn:hover {
            background: linear-gradient(135deg, #FF7BA9, #FF5C91);
            transform: scale(1.05);
            box-shadow: 0 6px 18px rgba(255, 92, 145, 0.5);
        }

        .btn-blanco {
            background: rgba(255, 255, 255, 0.9);
            color: #D65A8C;
        }

        .btn-blanco:hover {
            background: #FFFFFF;
            color: #FF5C91;
        }

        /* ===================== DIAPOSITIVA (SLIDE) ===================== */
        .slide {
            position: relative;
            width: 100%;
            min-height: 88vh;
            border-radius: 30px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            box-shadow: 0 15px 40px rgba(214, 90, 140, 0.35);
            background-size: cover;
            background-position: center;
            isolation: isolate;
            padding: 40px 20px;
        }

        /* Capa oscura semitransparente para que el texto se lea */
        .slide::before {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(
                135deg,
                rgba(214, 90, 140, 0.75),
                rgba(255, 123, 169, 0.55),
                rgba(90, 58, 74, 0.70)
            );
            z-index: -1;
        }

        .slide-contenido {
            max-width: 950px;
            padding: 50px 30px;
            animation: aparecer 0.8s ease;
            width: 100%;
        }

        @keyframes aparecer {
            from { opacity: 0; transform: translateY(25px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        .slide-numero {
            display: inline-block;
            background: rgba(255, 255, 255, 0.25);
            padding: 6px 18px;
            border-radius: 50px;
            font-size: 0.95em;
            letter-spacing: 1px;
            margin-bottom: 20px;
            backdrop-filter: blur(6px);
        }

        .slide-contenido h1 {
            font-size: 3em;
            margin-bottom: 20px;
            text-shadow: 0 4px 15px rgba(0, 0, 0, 0.35);
            line-height: 1.15;
        }

        .slide-contenido .descripcion {
            font-size: 1.15em;
            line-height: 1.8;
            margin-bottom: 25px;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
            background: rgba(90, 58, 74, 0.35);
            padding: 22px 26px;
            border-radius: 18px;
            backdrop-filter: blur(4px);
        }

        .curiosidad {
            display: inline-block;
            background: rgba(255, 255, 255, 0.9);
            color: #D65A8C;
            padding: 14px 22px;
            border-radius: 15px;
            font-size: 1em;
            margin-bottom: 35px;
            max-width: 700px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2);
        }

        .curiosidad strong {
            color: #FF5C91;
        }

        /* ===================== VIDEO LOCAL EN SLIDE ===================== */
        .slide-video {
            width: 100%;
            max-width: 900px;
            height: auto;
            max-height: 520px;
            border: 5px solid rgba(255, 255, 255, 0.7);
            border-radius: 22px;
            margin: 0 auto 30px;
            display: block;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
            background: #000;
        }

        /* Barra de navegación fija abajo */
        .nav-slide {
            position: fixed;
            bottom: 25px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 12px;
            background: rgba(255, 255, 255, 0.85);
            padding: 10px 15px;
            border-radius: 50px;
            box-shadow: 0 8px 25px rgba(214, 90, 140, 0.35);
            backdrop-filter: blur(8px);
            z-index: 100;
        }

        .nav-slide .btn {
            padding: 10px 20px;
            font-size: 0.95em;
        }

        .puntos {
            display: flex;
            gap: 6px;
            align-items: center;
            padding: 0 8px;
        }

        .punto {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #FFC7DD;
            transition: all 0.3s;
        }

        .punto.activo {
            background: #FF5C91;
            transform: scale(1.3);
        }

        footer {
            text-align: center;
            padding: 30px;
            margin-top: 40px;
            color: #9A6A80;
            font-size: 0.95em;
        }

        @media (max-width: 600px) {
            .slide-contenido h1 { font-size: 2em; }
            .slide-contenido .descripcion { font-size: 1em; padding: 18px; }
            .nav-slide { gap: 6px; padding: 8px 10px; }
            .nav-slide .btn { padding: 8px 14px; font-size: 0.85em; }
            .slide-video { max-height: 300px; }
        }
    </style>
</head>
<body>

{% if seccion %}
   
    <div class="slide" style="background-image: url('{{ seccion.img }}');">
        <div class="slide-contenido">
            <span class="slide-numero">
                Diapositiva {{ indice + 1 }} de {{ total }}
            </span>
            <h1>{{ seccion.titulo }}</h1>

            {% if seccion.video %}
            <video class="slide-video" controls preload="metadata">
                <source src="{{ seccion.video }}" type="video/mp4">
                Tu navegador no soporta el video.
            </video>
            {% endif %}

            <p class="descripcion">{{ seccion.descripcion_larga }}</p>
            <div class="curiosidad">
                 <strong>Dato curioso:</strong> {{ seccion.curiosidad }}
            </div>
        </div>
    </div>

   
    <nav class="nav-slide">
        {% if anterior %}
            <a href="/seccion/{{ anterior }}" class="btn">← Anterior</a>
        {% endif %}

        <div class="puntos">
            {% for s in secciones %}
                <span class="punto {% if loop.index0 == indice %}activo{% endif %}"></span>
            {% endfor %}
        </div>

        {% if siguiente %}
            <a href="/seccion/{{ siguiente }}" class="btn">Siguiente →</a>
        {% endif %}

        <a href="/" class="btn btn-blanco">Inicio</a>
    </nav>

{% else %}
   
    <div class="container">
        <header class="portada">
            <h1>CECYTEJ 08 Ixtlahuacan del Rio Jalisco.</h1>
            <p>Colegio de Estudios Cientificos y Tecnologicos del Estado de Jalisco.</p>
            <a href="/seccion/{{ secciones[0].id }}" class="btn">
                Ver informacion.
            </a>
        </header>

        <div class="cards">
            {% for s in secciones %}
            <div class="card">
                <img src="{{ s.img }}" alt="{{ s.titulo }}" class="card-img">
                <div class="card-body">
                    <h3>{{ s.titulo }}</h3>
                    <p>{{ s.descripcion_corta }}</p>
                    <a href="/seccion/{{ s.id }}" class="btn">Ver diapositiva →</a>
                </div>
            </div>
            {% endfor %}
        </div>

        <div class="info-section">
            <h2>📋 Información General</h2>
            <div class="info-grid">
                <div class="info-item">
                    <strong>📍 Dirección</strong>
                    Calle Herrera y Cairo, 45260 Ixtlahuacan del Río, Jalisco
                </div>
                <div class="info-item">
                    <strong>📞 Teléfono</strong>
                    373 734 5002
                </div>

                <div class="info-item">
                    <strong>🕐 Horario</strong>
                    Lunes a Viernes, 6:30a.m - 9:30p.m
                </div>
                <div class="info-item">
                    <strong>🎓 Carreras</strong>
                    Programacion y Electromecanica.
                </div>
                <div class="info-item">
                    <strong>👩‍🎓 Alumnos</strong>
                    Más de 300 estudiantes
                </div>
            </div>
        </div>

        <footer>
            © 2026 Colegio de Estudios Cientificos y Tecnologicos del Estado de Jalisco. 
        </footer>
    </div>
{% endif %}

</body>
</html>
"""


SECCIONES = [
    {
        "id": "historia",
        "titulo": "Nuestra Historia",
        "descripcion_corta": "Hace 30 años que CECYTEJ forma mentes, inspira sueños y construye futuros.",
        "descripcion_larga": "El Plantel 08 Ixtlahuacán del Río forma parte del Colegio de Estudios Científicos y Tecnológicos del Estado de Jalisco (CECyTEJ), institución creada en 1996 para ofrecer educación media superior tecnológica a los jóvenes del estado. A lo largo de los años, el CECyTEJ ha crecido hasta contar con 31 planteles en distintas regiones de Jalisco, entre ellos el Plantel 08, que se ha distinguido por su compromiso con la formación académica, científica y tecnológica de los estudiantes de Ixtlahuacán del Río y comunidades cercanas. Gracias a su labor educativa, ha contribuido al desarrollo de numerosas generaciones, brindándoles las herramientas necesarias para continuar sus estudios superiores e incorporarse al ámbito laboral. Mostrando el cambio en los logos, planteles y los millones de estudiantes que se han graduado de CECYTEJ.",
        "curiosidad": "CECYTEJ #08 ixtlahuacan del Rio Jalisco fue inagurado en el año 2000.",
        "img": "https://cdn.phototourl.com/member/2026-11-13-1b810c92-2973-4fa0-b23e-b804939faaad.jpg"
    },
    {
        "id": "instalaciones",
        "titulo": "Instalaciones",
        "descripcion_corta": "Laboratorios, biblioteca, canchas deportivas, aulas, gimnasio y talleres.",
        "descripcion_larga": "Nuestras instalacionesios han cambiado con el tiempo, incrementado el area psicopedagogicas, dos domos, areas verdes, mas aulas y laboratorios equipados y la expansion de la escuela junto con el material y maquinas con las que cuenta el area de electromecanica.",
        "curiosidad": "Las mayoria de arboles en el plantel fueron plantados hace años por estudiantes de la epoca.",
        "img": "https://cdn.phototourl.com/member/2026-11-13-a5a45b7a-3c06-4b31-9dfe-cea31ece873c.jpg"
    },
    {
        "id": "Carreras.",
        "titulo": "Programacion",
        "descripcion_corta": "Carreras tecnicas.",
        "descripcion_larga": "En el Plantel 08 de Ixtlahuacán del Río, la formación tecnológica ha evolucionado para adaptarse a las necesidades actuales. En sus inicios, la carrera se enfocaba en Soporte Técnico, donde los estudiantes aprendían mantenimiento y reparación de equipos de cómputo. Posteriormente evolucionó a Informática, incorporando el uso de software, redes y sistemas computacionales. Con el avance de la tecnología, la especialidad dio paso a Programación, una carrera centrada en el diseño y desarrollo de aplicaciones, páginas web, bases de datos y soluciones digitales. Hoy en día, la programación es una de las áreas más importantes y demandadas, ya que permite a los estudiantes desarrollar habilidades para crear tecnología e innovar en distintos ámbitos profesionales.",
        "curiosidad": "Muchas personas creen que la Inteligencia Artificial reemplazará a los programadores, la realidad es que la IA también necesita programadores para ser creada, entrenada y mejorada.",
        "img": "https://cdn.phototourl.com/member/2026-11-13-3c3fe275-825c-4b29-9ff4-3e238b0c0c13.jpg"
    },
    {
        "id": "Carreras",
        "titulo": "Electromecanica.",
        "descripcion_corta": "Carreras tecnicas.",
        "descripcion_larga": "La electromecánica es una carrera enfocada en el funcionamiento, instalación, mantenimiento y reparación de máquinas y sistemas que combinan componentes mecánicos, eléctricos y electrónicos. Los estudiantes aprenden a trabajar con motores, circuitos eléctricos, equipos industriales, sistemas automatizados y herramientas de control, conocimientos que se utilizan en fábricas, talleres, procesos de producción y tecnología industrial..",
        "curiosidad": "Muchas de las máquinas que se utilizan para fabricar autos, alimentos, ropa o dispositivos electrónicos son operadas y mantenidas por técnicos e ingenieros electromecánicos.",
        "img": "https://cdn.phototourl.com/member/2026-11-13-ca3133ce-65bd-4f41-826c-8f92f1a7f070.jpg"
    },
    {
        "id": "Eventos",
        "titulo": "Eventos escolares.",
        "descripcion_corta": "Una escuela donde cada evento se vive con la participación de todos.",
        "descripcion_larga": "El plantel promueve la participación integral de sus estudiantes mediante eventos deportivos como torneos de fútbol y voleibol y ferias académicas, además de concursos de conocimientos en distintas áreas. Asimismo, fomenta las tradiciones y valores culturales a través de actividades conmemorativas como el Día de Muertos, las celebraciones patrias y los desfiles cívicos, fortaleciendo la convivencia, el trabajo en equipo y el sentido de pertenencia a la comunidad escolar.",
        "curiosidad": "La escuela cuenta con una gran coleccion de trofeos de los eventos participados.",
        "img": "https://cdn.phototourl.com/member/2026-11-13-479971ce-af78-42af-8372-9eda9776c424.jpg"
    },
    {
        "id": "contacto",
        "titulo": "Contacto e Informacion",
        "descripcion_corta": "Informacion general de la escuela.",
        "descripcion_larga": "Ubicacion: Herrera y Cairo No. 120, Col. La Garita / La Escondida, Ixtlahuacán del Río, Jalisco, C.P. 45260."
        "CCT:14ETC0008B."
        "Telefono: 373 734 5002",
        
        "Dato": "Puedes solicitar tres tipos de becas diferentes..",
        "img": "data:image/webp;base64,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"
    },
    # 🎬 NUEVA SECCIÓN CON VIDEO LOCAL aki si use chatgepete
    {
        "id": "video",
        "titulo": "Entrevista",
        "descripcion_corta": "Entrevista a los egresados del CECyTEJ.",
        "descripcion_larga": "En este video se mostraran las respuestas de las entrevistas a los agresados del cecytej y se conoceran sus opiniones respecto su experiencia en la escuela.",
        "curiosidad": "La entrevista fue para personas reales, pero por motivos de privacidad y distancia, tuvieron que ser escritas.",
        "img": "https://cdn.phototourl.com/member/2026-11-16-c6489ee3-c0e3-49d1-bf32-4600cbd842f0.jpg",
        "video": "/static/1112(2).mp4"
    }
]


@app.route("/")
def inicio():
    return render_template_string(HTML, secciones=SECCIONES, seccion=None)


@app.route("/seccion/<identificador>")
def detalle(identificador):
    # Buscar índice de la sección actual
    indice = next((i for i, s in enumerate(SECCIONES) if s["id"] == identificador), None)
    if indice is None:
        return "<h1>Sección no encontrada</h1><a href='/'>Volver</a>", 404

    seccion = SECCIONES[indice]
    anterior = SECCIONES[indice - 1]["id"] if indice > 0 else None
    siguiente = SECCIONES[indice + 1]["id"] if indice < len(SECCIONES) - 1 else None

    return render_template_string(
        HTML,
        secciones=SECCIONES,
        seccion=seccion,
        indice=indice,
        total=len(SECCIONES),
        anterior=anterior,
        siguiente=siguiente
    )


if __name__ == "__main__":
    print(" http://127.0.0.1:5000 ")
    app.run(debug=True)