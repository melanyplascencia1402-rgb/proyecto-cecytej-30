from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colegio de Estudios Científicos y Tecnológicos del Estado de Jalisco</title>
    <link rel="icon" href="https://th.bing.com/th/id/OIP.ALVuYoNiMXR_6LqKFiImAQHaHa?w=163&h=180&c=7&r=0&o=7&pid=1.7&rm=3">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, sans-serif;
        }

        :root {
            --color-primario:      #006341;
            --color-secundario:    #7A1F3D;
            --color-dorado:        #C9A227;
            --color-dorado-claro:  #E8C96A;
            --color-fondo-1:       #EAF5EE;
            --color-fondo-2:       #FDF8E7;
            --color-fondo-3:       #F5E6EB;
            --color-texto:         #2E3A2F;
            --color-texto-suave:   #5A6A5C;
            --color-tarjeta:       #FFFFFF;
            --color-tarjeta-info:  #F4F9F1;
            --color-borde-acento:  #C9A227;
        }

        body {
            background: linear-gradient(135deg, var(--color-fondo-1) 0%, var(--color-fondo-2) 50%, var(--color-fondo-3) 100%);
            min-height: 100vh;
            color: var(--color-texto);
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        header.portada {
            text-align: center;
            padding: 50px 20px;
            background: rgba(255, 255, 255, 0.85);
            border-radius: 25px;
            margin-bottom: 40px;
            box-shadow: 0 8px 24px rgba(0, 99, 65, 0.25);
            border: 3px solid var(--color-dorado);
            position: relative;
            overflow: hidden;
        }

        header.portada::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 8px;
            background: linear-gradient(90deg, var(--color-primario), var(--color-dorado), var(--color-secundario), var(--color-dorado), var(--color-primario));
        }

        .portada-logos {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 30px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .portada-logos img {
            height: 90px;
            width: auto;
            object-fit: contain;
        }
        .logo-cecytej { max-height: 100px; }
        .emblema-30   { max-height: 110px; }

        header.portada h1 {
            color: var(--color-primario);
            font-size: 2.4em;
            margin-bottom: 10px;
        }

        header.portada .bienvenida {
            font-size: 1.15em;
            color: var(--color-texto-suave);
            max-width: 800px;
            margin: 0 auto 15px;
            line-height: 1.6;
        }

        header.portada p {
            font-size: 1.05em;
            color: var(--color-texto-suave);
            margin-bottom: 25px;
        }

        .foto-plantel {
            width: 100%;
            max-width: 750px;
            border-radius: 18px;
            border: 4px solid var(--color-dorado);
            box-shadow: 0 8px 25px rgba(0, 99, 65, 0.25);
            margin: 0 auto 25px;
            display: block;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .card {
            background: var(--color-tarjeta);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 6px 20px rgba(0, 99, 65, 0.25);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
        }

        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 30px rgba(0, 99, 65, 0.4);
        }

        .card-img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            background: var(--color-fondo-1);
        }

        .card-body {
            padding: 22px;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }

        .card-body h3 {
            color: var(--color-primario);
            margin-bottom: 12px;
            font-size: 1.4em;
        }

        .card-body p {
            color: var(--color-texto-suave);
            line-height: 1.6;
            margin-bottom: 18px;
            flex-grow: 1;
        }

        .info-section {
            background: rgba(255, 255, 255, 0.85);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 6px 20px rgba(0, 99, 65, 0.2);
            border: 2px solid var(--color-dorado);
        }

        .info-section h2 {
            color: var(--color-primario);
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
            background: var(--color-tarjeta-info);
            padding: 20px;
            border-radius: 15px;
            border-left: 5px solid var(--color-borde-acento);
        }

        .info-item strong {
            color: var(--color-primario);
            display: block;
            margin-bottom: 6px;
            font-size: 1.1em;
        }

        .btn {
            display: inline-block;
            padding: 12px 26px;
            background: linear-gradient(135deg, var(--color-primario), var(--color-secundario));
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-weight: 600;
            transition: all 0.3s ease;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 99, 65, 0.35);
            border: none;
            cursor: pointer;
            font-size: 1em;
        }

        .btn:hover {
            background: linear-gradient(135deg, var(--color-secundario), var(--color-primario));
            transform: scale(1.05);
            box-shadow: 0 6px 18px rgba(122, 31, 61, 0.5);
        }

        .btn-blanco {
            background: rgba(255, 255, 255, 0.9);
            color: var(--color-primario);
        }

        .btn-blanco:hover {
            background: #FFFFFF;
            color: var(--color-secundario);
        }

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
            box-shadow: 0 15px 40px rgba(0, 99, 65, 0.35);
            background-size: cover;
            background-position: center;
            isolation: isolate;
            padding: 40px 20px;
        }

        .slide::before {
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(
                135deg,
                rgba(0, 99, 65, 0.75),
                rgba(122, 31, 61, 0.55),
                rgba(201, 162, 39, 0.70)
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
            background: rgba(46, 58, 47, 0.35);
            padding: 22px 26px;
            border-radius: 18px;
            backdrop-filter: blur(4px);
        }

        .curiosidad {
            display: inline-block;
            background: rgba(255, 255, 255, 0.9);
            color: var(--color-primario);
            padding: 14px 22px;
            border-radius: 15px;
            font-size: 1em;
            margin-bottom: 35px;
            max-width: 700px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2);
        }

        .curiosidad strong {
            color: var(--color-dorado);
        }

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

        .nav-slide {
            position: fixed;
            bottom: 25px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 12px;
            background: rgba(255, 255, 255, 0.9);
            padding: 10px 15px;
            border-radius: 50px;
            box-shadow: 0 8px 25px rgba(0, 99, 65, 0.35);
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
            background: var(--color-dorado-claro);
            transition: all 0.3s;
        }

        .punto.activo {
            background: var(--color-dorado);
            transform: scale(1.3);
        }

        footer {
            text-align: center;
            padding: 30px;
            margin-top: 40px;
            color: var(--color-texto-suave);
            font-size: 0.95em;
        }

        /* ===== SECCIONES ESPECIALES ===== */
        .seccion-especial {
            max-width: 1100px;
            margin: 0 auto;
            padding: 20px 0 100px;
        }

        .especial-titulo {
            text-align: center;
            color: var(--color-primario);
            font-size: 2.6em;
            margin-bottom: 10px;
        }

        .especial-subtitulo {
            text-align: center;
            color: var(--color-texto-suave);
            font-size: 1.15em;
            margin-bottom: 45px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            line-height: 1.6;
        }

        .especial-bloque {
            background: rgba(255, 255, 255, 0.85);
            border-radius: 20px;
            padding: 35px 30px;
            margin-bottom: 35px;
            box-shadow: 0 6px 20px rgba(0, 99, 65, 0.2);
            border: 2px solid var(--color-dorado);
        }

        .especial-bloque h2 {
            color: var(--color-primario);
            font-size: 1.8em;
            margin-bottom: 8px;
            text-align: center;
        }

        .especial-bloque .bloque-desc {
            text-align: center;
            color: var(--color-texto-suave);
            margin-bottom: 30px;
            font-size: 1.05em;
            line-height: 1.6;
        }

        /* Línea del tiempo */
        .timeline {
            position: relative;
            padding: 20px 0;
        }

        .timeline::before {
            content: "";
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 4px;
            background: linear-gradient(180deg, var(--color-primario), var(--color-dorado), var(--color-secundario));
            transform: translateX(-50%);
            border-radius: 2px;
        }

        .timeline-item {
            position: relative;
            width: 50%;
            padding: 20px 40px;
            box-sizing: border-box;
        }

        .timeline-item:nth-child(odd) {
            left: 0;
            text-align: right;
        }

        .timeline-item:nth-child(even) {
            left: 50%;
            text-align: left;
        }

        .timeline-item::after {
            content: "";
            position: absolute;
            top: 30px;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: var(--color-dorado);
            border: 4px solid var(--color-primario);
            box-shadow: 0 0 0 4px rgba(201, 162, 39, 0.25);
            z-index: 2;
        }

        .timeline-item:nth-child(odd)::after {
            right: -10px;
        }

        .timeline-item:nth-child(even)::after {
            left: -10px;
        }

        .timeline-card {
            background: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 99, 65, 0.15);
            border-left: 4px solid var(--color-dorado);
            display: inline-block;
            max-width: 100%;
            text-align: left;
        }

        .timeline-item:nth-child(odd) .timeline-card {
            border-left: none;
            border-right: 4px solid var(--color-dorado);
        }

        .timeline-fecha {
            display: inline-block;
            background: linear-gradient(135deg, var(--color-primario), var(--color-secundario));
            color: white;
            padding: 5px 16px;
            border-radius: 50px;
            font-weight: 700;
            font-size: 0.95em;
            margin-bottom: 12px;
        }

        .timeline-card img {
            width: 100%;
            height: 160px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 12px;
        }

        .timeline-card h3 {
            color: var(--color-primario);
            font-size: 1.2em;
            margin-bottom: 8px;
        }

        .timeline-card p {
            color: var(--color-texto-suave);
            font-size: 0.95em;
            line-height: 1.6;
        }

        /* Antes / Ahora */
        .antes-ahora {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 10px;
        }

        .antes-ahora > div {
            text-align: center;
        }

        .antes-ahora img {
            width: 100%;
            height: 220px;
            object-fit: cover;
            border-radius: 15px;
            border: 3px solid var(--color-dorado);
        }

        .antes-ahora .etiqueta {
            display: inline-block;
            margin-top: 10px;
            padding: 6px 18px;
            border-radius: 50px;
            font-weight: 700;
            font-size: 0.95em;
        }

        .etiqueta-antes {
            background: var(--color-secundario);
            color: white;
        }

        .etiqueta-ahora {
            background: var(--color-primario);
            color: white;
        }

        /* Listas (mejoras, recuerdos, eventos) */
        .grid-listas {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 18px;
        }

        .item-lista {
            background: var(--color-tarjeta-info);
            padding: 18px;
            border-radius: 12px;
            border-left: 4px solid var(--color-dorado);
            color: var(--color-texto);
            line-height: 1.5;
        }

        .item-lista strong {
            display: block;
            color: var(--color-primario);
            margin-bottom: 5px;
            font-size: 1.1em;
        }

        /* Datos de crecimiento */
        .cifras {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 20px;
            text-align: center;
            margin-top: 15px;
        }

        .cifra {
            background: white;
            padding: 25px 15px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 99, 65, 0.15);
            border-bottom: 5px solid var(--color-dorado);
        }

        .cifra .numero {
            font-size: 2.6em;
            font-weight: 800;
            color: var(--color-primario);
            display: block;
            line-height: 1;
            margin-bottom: 8px;
        }

        .cifra .etiqueta-cifra {
            color: var(--color-texto-suave);
            font-size: 0.95em;
        }

        /* Testimonios */
        .grid-testimonios {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 22px;
        }

        .testimonio {
            background: white;
            border-radius: 18px;
            padding: 25px 20px;
            text-align: center;
            box-shadow: 0 6px 20px rgba(0, 99, 65, 0.18);
            border-top: 5px solid var(--color-dorado);
            transition: transform 0.3s ease;
        }

        .testimonio:hover {
            transform: translateY(-6px);
        }

        .testimonio .nombre {
            color: var(--color-primario);
            font-size: 1.15em;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .testimonio .generacion {
            color: var(--color-secundario);
            font-size: 0.9em;
            font-weight: 600;
            margin-bottom: 15px;
        }

        .testimonio .frase {
            color: var(--color-texto-suave);
            font-style: italic;
            line-height: 1.6;
            font-size: 0.98em;
            position: relative;
            padding: 0 5px;
        }

        .testimonio .frase::before {
            content: "\\201C";
            font-size: 2.5em;
            color: var(--color-dorado);
            position: absolute;
            top: -15px;
            left: -5px;
            line-height: 1;
        }

        .testimonio-tipo {
            display: inline-block;
            background: var(--color-fondo-1);
            color: var(--color-primario);
            font-size: 0.75em;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 50px;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* Formación integral */
        .formacion-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 20px;
        }

        .formacion-item {
            background: white;
            padding: 25px 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 99, 65, 0.15);
            border-bottom: 4px solid var(--color-dorado);
        }

        .formacion-item .icono {
            font-size: 2.5em;
            display: block;
            margin-bottom: 12px;
        }

        .formacion-item h3 {
            color: var(--color-primario);
            margin-bottom: 10px;
            font-size: 1.15em;
        }

        .formacion-item p {
            color: var(--color-texto-suave);
            font-size: 0.95em;
            line-height: 1.6;
        }

        @media (max-width: 768px) {
            .timeline::before { left: 20px; }
            .timeline-item,
            .timeline-item:nth-child(odd),
            .timeline-item:nth-child(even) {
                width: 100%;
                left: 0;
                text-align: left;
                padding: 15px 15px 15px 50px;
            }
            .timeline-item::after,
            .timeline-item:nth-child(odd)::after,
            .timeline-item:nth-child(even)::after {
                left: 10px;
                right: auto;
            }
            .timeline-item:nth-child(odd) .timeline-card {
                border-right: none;
                border-left: 4px solid var(--color-dorado);
            }
            .antes-ahora { grid-template-columns: 1fr; }
            .especial-titulo { font-size: 2em; }
        }

        @media (max-width: 600px) {
            .slide-contenido h1 { font-size: 2em; }
            .slide-contenido .descripcion { font-size: 1em; padding: 18px; }
            .nav-slide { gap: 6px; padding: 8px 10px; }
            .nav-slide .btn { padding: 8px 14px; font-size: 0.85em; }
            .slide-video { max-height: 300px; }
            .portada-logos img { height: 65px; }
        }
    </style>
</head>
<body>

{% if seccion and seccion.tipo == "especial" %}
    <div class="seccion-especial">
        <h1 class="especial-titulo">{{ seccion.titulo }}</h1>
        <p class="especial-subtitulo">{{ seccion.descripcion_larga }}</p>

        {% if seccion.linea_tiempo %}
        <div class="especial-bloque">
            <h2>Línea del Tiempo</h2>
            <p class="bloque-desc">Etapas clave en la historia del Plantel 08 y del CECyTEJ.</p>
            <div class="timeline">
                {% for etapa in seccion.linea_tiempo %}
                <div class="timeline-item">
                    <div class="timeline-card">
                        <span class="timeline-fecha">{{ etapa.fecha }}</span>
                        {% if etapa.img %}<img src="{{ etapa.img }}" alt="{{ etapa.titulo }}">{% endif %}
                        <h3>{{ etapa.titulo }}</h3>
                        <p>{{ etapa.descripcion }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if seccion.antes_ahora %}
        <div class="especial-bloque">
            <h2>Antes y Ahora</h2>
            <p class="bloque-desc">{{ seccion.antes_ahora.texto }}</p>
            <div class="antes-ahora">
                <div>
                    {% if seccion.antes_ahora.antes_img %}
                    <img src="{{ seccion.antes_ahora.antes_img }}" alt="Antes">
                    {% endif %}
                    <span class="etiqueta etiqueta-antes">ANTES</span>
                </div>
                <div>
                    {% if seccion.antes_ahora.ahora_img %}
                    <img src="{{ seccion.antes_ahora.ahora_img }}" alt="Ahora">
                    {% endif %}
                    <span class="etiqueta etiqueta-ahora">AHORA</span>
                </div>
            </div>
        </div>
        {% endif %}

        {% if seccion.mejoras %}
        <div class="especial-bloque">
            <h2>Mejoras</h2>
            <p class="bloque-desc">Cambios y mejoras que ha tenido el plantel a lo largo del tiempo.</p>
            <div class="grid-listas">
                {% for m in seccion.mejoras %}
                <div class="item-lista">
                    <strong>{{ m.titulo }}</strong>
                    {{ m.descripcion }}
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if seccion.recuerdos %}
        <div class="especial-bloque">
            <h2>Recuerdos</h2>
            <p class="bloque-desc">Anécdotas y memorias de quienes han formado parte del plantel.</p>
            <div class="grid-listas">
                {% for r in seccion.recuerdos %}
                <div class="item-lista">
                    <strong>{{ r.titulo }}</strong>
                    {{ r.descripcion }}
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if seccion.eventos_clave %}
        <div class="especial-bloque">
            <h2>Eventos Clave</h2>
            <p class="bloque-desc">Momentos históricos que marcaron el rumbo del plantel.</p>
            <div class="grid-listas">
                {% for e in seccion.eventos_clave %}
                <div class="item-lista">
                    <strong>{{ e.fecha }} — {{ e.titulo }}</strong>
                    {{ e.descripcion }}
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if seccion.datos_crecimiento %}
        <div class="especial-bloque">
            <h2>Datos de Crecimiento</h2>
            <p class="bloque-desc">El crecimiento del CECyTEJ en números.</p>
            <div class="cifras">
                {% for d in seccion.datos_crecimiento %}
                <div class="cifra">
                    <span class="numero">{{ d.numero }}</span>
                    <span class="etiqueta-cifra">{{ d.etiqueta }}</span>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if seccion.testimonios %}
        <div class="especial-bloque">
            <h2>Testimonios</h2>
            <p class="bloque-desc">Voces de exalumnos y alumnos.</p>
            <div class="grid-testimonios">
                {% for t in seccion.testimonios %}
                <div class="testimonio">
                    <span class="testimonio-tipo">{{ t.tipo }}</span>
                    <div class="nombre">{{ t.nombre }}</div>
                    {% if t.generacion %}<div class="generacion">{{ t.generacion }}</div>{% endif %}
                    <p class="frase">{{ t.frase }}</p>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if seccion.formacion_integral %}
        <div class="especial-bloque">
            <h2>Formación Integral</h2>
            <p class="bloque-desc">Áreas que complementan la formación académica de nuestros estudiantes.</p>
            <div class="formacion-grid">
                {% for f in seccion.formacion_integral %}
                <div class="formacion-item">
                    <span class="icono">{{ f.icono }}</span>
                    <h3>{{ f.titulo }}</h3>
                    <p>{{ f.descripcion }}</p>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}
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

{% elif seccion %}
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
            <div class="portada-logos">
                <img src="https://th.bing.com/th/id/OIP.ALVuYoNiMXR_6LqKFiImAQHaHa?w=163&h=180&c=7&r=0&o=7&pid=1.7&rm=3"
                     alt="Logo CECyTEJ" class="logo-cecytej">
                <img src="https://tse3.mm.bing.net/th/id/OIP.dM7RWnT0ewqYID_Q3GZKTgHaHK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
                     alt="Emblema 30 años CECyTEJ" class="emblema-30">
            </div>

            <h1>Colegio de Estudios Científicos y Tecnológicos del Estado de Jalisco</h1>

            <p class="bienvenida">
                ¡Bienvenidos al Plantel 08 Ixtlahuacán del Río! Un espacio donde la ciencia,
                la tecnología y los valores forman a las nuevas generaciones de Jalisco.
            </p>

            <p>Plantel 08 · Ixtlahuacán del Río, Jalisco</p>

            <img src="https://cdn.phototourl.com/member/2026-11-13-1b810c92-2973-4fa0-b23e-b804939faaad.jpg"
                 alt="Fotografía del Plantel 08 Ixtlahuacán del Río"
                 class="foto-plantel">

            <a href="/seccion/{{ secciones[0].id }}" class="btn">
                Ver información
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
            <h2>Información General</h2>
            <div class="info-grid">
                <div class="info-item">
                    <strong>Dirección</strong>
                    Calle Herrera y Cairo, 45260 Ixtlahuacán del Río, Jalisco
                </div>
                <div class="info-item">
                    <strong>Teléfono</strong>
                    373 734 5002
                </div>
                <div class="info-item">
                    <strong>Horario</strong>
                    Lunes a Viernes, 6:30 a.m. - 9:30 p.m.
                </div>
                <div class="info-item">
                    <strong>Carreras</strong>
                    Programación y Electromecánica
                </div>
                <div class="info-item">
                    <strong>Alumnos</strong>
                    Más de 300 estudiantes
                </div>
            </div>
        </div>

        <footer>
            © 2026 Colegio de Estudios Científicos y Tecnológicos del Estado de Jalisco.
        </footer>
    </div>
{% endif %}

</body>
</html>
"""


SECCIONES = [
    {
        "id": "Historia",
        "titulo": "Nuestra Historia",
        "descripcion_corta": "Hace 30 años que CECyTEJ forma mentes, inspira sueños y construye futuros.",
        "descripcion_larga": "El Plantel 08 Ixtlahuacán del Río forma parte del Colegio de Estudios Científicos y Tecnológicos del Estado de Jalisco (CECyTEJ), institución creada en 1996 para ofrecer educación media superior tecnológica a los jóvenes del estado. A lo largo de los años, el CECyTEJ ha crecido hasta contar con 31 planteles en distintas regiones de Jalisco, entre ellos el Plantel 08, que se ha distinguido por su compromiso con la formación académica, científica y tecnológica de los estudiantes de Ixtlahuacán del Río y comunidades cercanas. Gracias a su labor educativa, ha contribuido al desarrollo de numerosas generaciones, brindándoles las herramientas necesarias para continuar sus estudios superiores e incorporarse al ámbito laboral, mostrando el cambio en los logos, planteles y los millones de estudiantes que se han graduado de CECyTEJ.",
        "curiosidad": "CECyTEJ #08 Ixtlahuacán del Río, Jalisco fue inaugurado en el año 2000.",
        "img": "https://cdn.phototourl.com/member/2026-11-13-1b810c92-2973-4fa0-b23e-b804939faaad.jpg"
    },
    {
        "id": "Instalaciones",
        "titulo": "Instalaciones",
        "descripcion_corta": "Laboratorios, biblioteca, canchas deportivas, aulas, gimnasio y talleres.",
        "descripcion_larga": "Nuestras instalaciones han cambiado con el tiempo: se incrementó el área psicopedagógica, dos domos, áreas verdes, más aulas y laboratorios equipados, y la expansión de la escuela junto con el material y las máquinas con las que cuenta el área de electromecánica.",
        "curiosidad": "La mayoría de los árboles del plantel fueron plantados hace años por estudiantes de la época.",
        "img": "https://cdn.phototourl.com/member/2026-11-13-a5a45b7a-3c06-4b31-9dfe-cea31ece873c.jpg"
    },
    {
        "id": "Programacion",
        "titulo": "Programación",
        "descripcion_corta": "Carreras técnicas.",
        "descripcion_larga": "En el Plantel 08 de Ixtlahuacán del Río, la formación tecnológica ha evolucionado para adaptarse a las necesidades actuales. En sus inicios, la carrera se enfocaba en Soporte Técnico, donde los estudiantes aprendían mantenimiento y reparación de equipos de cómputo. Posteriormente evolucionó a Informática, incorporando el uso de software, redes y sistemas computacionales. Con el avance de la tecnología, la especialidad dio paso a Programación, una carrera centrada en el diseño y desarrollo de aplicaciones, páginas web, bases de datos y soluciones digitales. Hoy en día, la programación es una de las áreas más importantes y demandadas, ya que permite a los estudiantes desarrollar habilidades para crear tecnología e innovar en distintos ámbitos profesionales.",
        "curiosidad": "Muchas personas creen que la Inteligencia Artificial reemplazará a los programadores; la realidad es que la IA también necesita programadores para ser creada, entrenada y mejorada.",
        "img": "https://cdn.phototourl.com/member/2026-11-13-3c3fe275-825c-4b29-9ff4-3e238b0c0c13.jpg"
    },
    {
        "id": "Electromecanica",
        "titulo": "Electromecánica",
        "descripcion_corta": "Carreras técnicas.",
        "descripcion_larga": "La electromecánica es una carrera enfocada en el funcionamiento, instalación, mantenimiento y reparación de máquinas y sistemas que combinan componentes mecánicos, eléctricos y electrónicos. Los estudiantes aprenden a trabajar con motores, circuitos eléctricos, equipos industriales, sistemas automatizados y herramientas de control, conocimientos que se utilizan en fábricas, talleres, procesos de producción y tecnología industrial.",
        "curiosidad": "Muchas de las máquinas que se utilizan para fabricar autos, alimentos, ropa o dispositivos electrónicos son operadas y mantenidas por técnicos e ingenieros electromecánicos.",
        "img": "https://cdn.phototourl.com/member/2026-11-13-ca3133ce-65bd-4f41-826c-8f92f1a7f070.jpg"
    },
    {
        "id": "Eventos",
        "titulo": "Eventos escolares",
        "descripcion_corta": "Una escuela donde cada evento se vive con la participación de todos.",
        "descripcion_larga": "El plantel promueve la participación integral de sus estudiantes mediante eventos deportivos como torneos de fútbol y voleibol y ferias académicas, además de concursos de conocimientos en distintas áreas. Asimismo, fomenta las tradiciones y valores culturales a través de actividades conmemorativas como el Día de Muertos, las celebraciones patrias y los desfiles cívicos, fortaleciendo la convivencia, el trabajo en equipo y el sentido de pertenencia a la comunidad escolar.",
        "curiosidad": "La escuela cuenta con una gran colección de trofeos de los eventos en los que ha participado.",
        "img": "https://cdn.phototourl.com/member/2026-11-13-479971ce-af78-42af-8372-9eda9776c424.jpg"
    },
    {
        "id": "Contacto",
        "titulo": "Contacto e Información",
        "descripcion_corta": "Información general de la escuela.",
        "descripcion_larga": "Ubicación: Herrera y Cairo No. 120, Col. La Garita / La Escondida, Ixtlahuacán del Río, Jalisco, C.P. 45260. CCT: 14ETC0008B. Teléfono: 373 734 5002.",
        "curiosidad": "Puedes solicitar tres tipos de becas diferentes.",
        "img": "https://th.bing.com/th/id/OIP.rJwMMnO10X6RKbY6gfHXJQHaC6?w=312&h=138&c=7&r=0&o=7&pid=1.7&rm=3"
    },
    {
        "id": "Video",
        "titulo": "Entrevista",
        "descripcion_corta": "Entrevista a los egresados del CECyTEJ.",
        "descripcion_larga": "En este video se mostrarán las respuestas de las entrevistas a los egresados del CECyTEJ y se conocerán sus opiniones respecto a su experiencia en la escuela.",
        "curiosidad": "La entrevista fue a personas reales, pero por motivos de privacidad y distancia, tuvieron que ser escritas.",
        "img": "https://cdn.phototourl.com/member/2026-11-16-c6489ee3-c0e3-49d1-bf32-4600cbd842f0.jpg",
        "video": "/static/1112(2).mp4"
    },
    {
        "id": "LineaTiempo",
        "tipo": "especial",
        "titulo": "Línea del Tiempo",
        "descripcion_corta": "Etapas, mejoras, recuerdos y eventos.",
        "descripcion_larga": "Recorrido visual por la historia del Plantel 08 y del CECyTEJ: sus etapas, transformaciones y momentos clave.",
        "img": "https://cdn.imagetourls.com/uploads/tyImg/sIiBLhPV.jpg",
        
        # --- AQUÍ ESTÁ TU LISTA CORREGIDA ---
        "linea_tiempo": [
            {"fecha": "2000", "titulo": "Inauguración del Plantel 08", "descripcion": "Abre sus puertas en Ixtlahuacán del Río y comienza a formar a las primeras generaciones.", "img": "https://www.geocities.ws/cecytej08ixtlahuacan/IMG_0017.JPG"},
            {"fecha": "2005", "titulo": "Logo del Plantel", "descripcion": "Logo del Plantel.", "img": "data:image/webp;base64,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"},
            {"fecha": "2019", "titulo": "Cambio de logo y color", "descripcion": "El plantel adopta el logo y los colores institucionales actuales.", "img": "https://tse1.mm.bing.net/th/id/OIP.gtGHr1XdSWXQyOuZJZScyQHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"},
            {"fecha": "2024", "titulo": "Torneo", "descripcion": "Los estudiantes del CECyTEJ organizan un torneo de voleibol en acción por la diabetes.", "img": "https://cdn.phototourl.com/member/2026-11-22-067aa110-e462-48f6-a799-3f6c948b6296.jpg"},
            {"fecha": "2024", "titulo": "Programación como carrera", "descripcion": "Se incorpora la carrera de Programación al plantel.", "img": "https://www.geocities.ws/cecytej08ixtlahuacan/DSC06101.JPG"},
            {"fecha": "2024", "titulo": "25 años", "descripcion": "25 años de historia del CECyTEJ.", "img": "https://scontent-qro1-2.xx.fbcdn.net/v/t39.30808-6/492230248_1259108679550023_2689160221924469700_n.jpg?stp=dst-jpg_tt6&cstp=mx1280x720&ctp=s1280x720&_nc_cat=106&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFfqhtvhb21_Rn6ZSzkZT_6v1EzwuhWTay_UTPC6FZNrGO64O6sinrA8AgJ_pnr5yFVT1zapl8RZ6JhwAsLITSv&_nc_ohc=2vJOIyxs4b0Q7kNvwEmcznE&_nc_oc=AdomDIyxzV9kUolN7YrTznWBK1OJVImSTVRt8Sk33kQ34kGo-MfjgSWaso7lgkdrP24&_nc_pt=1&_nc_zt=23&_nc_ht=scontent-qro1-2.xx&_nc_gid=dP6xOIaNa7XX9EpDr24KXQ&_nc_ss=7b2a8&oh=00_AQRgBhUVTsHF860nfc4f5zmHMV6QqYFsVfKIoDDkLmP_xA&oe=6B0935D0"},
            {"fecha": "2026", "titulo": "30 años de historia", "descripcion": "El CECyTEJ celebra tres décadas formando mentes, inspirando sueños y construyendo futuros.", "img": "https://cdn.imagetourls.com/uploads/tyImg/sIiBLhPV.jpg"},
            {"fecha": "2026", "titulo": "Familia CECyTEJ", "descripcion": "Docentes y todo el personal del CECyTEJ Ixtlahuacán del Río.", "img": "https://scontent-qro1-1.xx.fbcdn.net/v/t51.82787-15/612994072_18441428350103797_1329935273663950464_n.webp?stp=dst-jpg_tt6&cstp=mx1440x1440&ctp=s1440x1440&_nc_cat=102&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeEEDhb6BKFfOAcLDS3jHgqtiSmm-H4jMkuJKab4fiMyS5iVsRjm0c-Tv7lvWCE0utNKBhS19syyXQ7TREfEaU_9&_nc_ohc=ppfkbaVid-EQ7kNvwHBlEIv&_nc_oc=AdpUvCkmaPhi60xUneZXQm9Db7kaTb9U0KAEdlzPHzDgSIvc1b-mbvGPP3WlECd_32Q&_nc_pt=1&_nc_zt=23&_nc_ht=scontent-qro1-1.xx&_nc_gid=MXLFb6_bdx1QvO0UdhNQoA&_nc_ss=7b2a8&oh=00_AQSWaxgKn4Fwb7IDogC69V4PUtaHnLWi7oBV_9rO1-mz0A&oe=6B0916E4"},
            {"fecha": "2026", "titulo": "Mejoras al plantel", "descripcion": "La inauguración de una nueva escalera en el plantel.", "img": "https://scontent-qro3-1.xx.fbcdn.net/v/t51.82787-15/792252907_18487418884103797_1016789262045885399_n.webp?stp=dst-jpg_tt6&cstp=mx1440x1440&ctp=s1440x1440&_nc_cat=102&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeG3_GQotHJ_-R8D7bxUiuGoZNdQsYzBfT1k11CxjMF9PewkqajnGAIJA0EJvq6TWMmJq4Tencs-aqryi4A08-Bk&_nc_ohc=-yYy7YSa3UYQ7kNvwHm_dal&_nc_oc=AdpjaBp6fy34IL4YQLH_fXEA3HBDFFc3y3czz0DXqqyAbp3FSpvMw73FwR3jLBzjHgY&_nc_pt=1&_nc_zt=23&_nc_ht=scontent-qro3-1.xx&_nc_gid=CgZNNrRbwb_xpBCEH3kYMw&_nc_ss=7b2a8&oh=00_AQSXxtdR7_UCLJFTqT9SqDxp3f_3z8IsnL1ffhGVxsxvhQ&oe=6B093BA9"}
        ],

        "antes_ahora": {
            "texto": "Así lucía el plantel en sus inicios y así luce hoy.",
            "antes_img": "https://tse1.mm.bing.net/th/id/OIP.gtGHr1XdSWXQyOuZJZScyQHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
            "ahora_img": "https://cdn.imagetourls.com/uploads/tyImg/sIiBLhPV.jpg"
        },
        "mejoras": [
            {"titulo": "Área psicopedagógica", "descripcion": "Espacio de atención para los estudiantes."},
            {"titulo": "Dos domos", "descripcion": "Para actividades deportivas y cívicas."},
            {"titulo": "Áreas verdes", "descripcion": "Ampliación de las áreas verdes del plantel."},
            {"titulo": "Aulas y laboratorios", "descripcion": "Más aulas y laboratorios equipados."},
            {"titulo": "Expansión", "descripcion": "Crecimiento junto con material y máquinas de electromecánica."}
        ],
        "recuerdos": [
            {"titulo": "Los árboles del plantel", "descripcion": "Plantados hace años por estudiantes de la época."},
            {"titulo": "Eventos cívicos", "descripcion": "Desfiles y celebraciones patrias de siempre."}
        ],
        "eventos_clave": [
            {"fecha": "1996", "titulo": "Fundación del CECyTEJ", "descripcion": "Creación de la institución a nivel estatal."},
            {"fecha": "2000", "titulo": "Inauguración del Plantel 08", "descripcion": "Apertura oficial en Ixtlahuacán del Río."},
            {"fecha": "2026", "titulo": "30 Aniversario", "descripcion": "Tres décadas de historia y formación."}
        ],
        "datos_crecimiento": [
            {"numero": "31", "etiqueta": "Planteles en Jalisco"},
            {"numero": "30", "etiqueta": "Años de historia"},
            {"numero": "+300", "etiqueta": "Alumnos actuales"},
            {"numero": "2", "etiqueta": "Carreras técnicas"}
        ]
    },
    {
        "id": "Testimonios",
        "tipo": "especial",
        "titulo": "Testimonios",
        "descripcion_corta": "Exalumnos y alumnos.",
        "descripcion_larga": "Voces de quienes han formado parte del CECyTEJ Plantel 08: exalumnos y alumnos comparten su experiencia.",
        "img": "https://tse1.mm.bing.net/th/id/OIP.PsJRDP5auWe9qYhFWzLGkgHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
        "testimonios": [
            {"tipo": "Exalumno", "nombre": "Fernando", "generacion": "Generación 2022-2025", "frase": "La escuela es bien bonita, convives y haces amigos, lo que importa es sentirse bien."},
            {"tipo": "Alumno", "nombre": "Valeria", "generacion": "2023-2026", "frase": "Me gusta la experiencia, aunque sea de último año agradezco todo lo que pasé aquí."},
            {"tipo": "Exalumno", "nombre": "Cristopher", "frase": "Sean autodidactas."}
        ],
        "formacion_integral": [
            {"icono": "📚", "titulo": "Académica", "descripcion": "Formación técnica de calidad."},
            {"icono": "⚽", "titulo": "Deportiva", "descripcion": "Torneos y trabajo en equipo."},
            {"icono": "🎭", "titulo": "Cultural", "descripcion": "Tradiciones y celebraciones."},
            {"icono": "🤝", "titulo": "Valores", "descripcion": "Convivencia y pertenencia."}
        ]
    }
]


@app.route("/")
def inicio():
    return render_template_string(HTML, secciones=SECCIONES, seccion=None)


@app.route("/seccion/<identificador>")
def detalle(identificador):
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
