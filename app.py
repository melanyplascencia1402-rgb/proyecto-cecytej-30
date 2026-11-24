from flask import Flask, render_template_string, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = "cecytej-30-aniversario-secreto"

DB_FILE = "testimonios.json"

def cargar_testimonios():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_testimonio(nuevo):
    datos = cargar_testimonios()
    datos.append(nuevo)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

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
            animation: fadeIn 0.8s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to   { opacity: 1; transform: translateY(0); }
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
            animation: slideDown 0.8s ease;
        }

        @keyframes slideDown {
            from { opacity: 0; transform: translateY(-20px); }
            to   { opacity: 1; transform: translateY(0); }
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
            transition: transform 0.3s ease;
        }
        .foto-plantel:hover {
            transform: scale(1.02);
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
            transition: transform 0.3s ease;
        }
        .card:hover .card-img {
            transform: scale(1.05);
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
            transition: transform 0.2s ease;
        }
        .info-item:hover {
            transform: translateX(5px);
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
            animation: slideDown 0.6s ease;
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
            transition: transform 0.3s ease;
        }
        .especial-bloque:hover {
            transform: translateY(-3px);
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
            transition: transform 0.3s ease;
        }
        .timeline-card:hover {
            transform: scale(1.02);
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
            transition: transform 0.2s ease;
        }
        .item-lista:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        .item-lista strong {
            display: block;
            color: var(--color-primario);
            margin-bottom: 5px;
            font-size: 1.1em;
        }

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
            transition: transform 0.3s ease;
        }
        .cifra:hover {
            transform: scale(1.05);
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
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .testimonio:hover {
            transform: translateY(-6px);
        }

        .testimonio img {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid var(--color-dorado);
            margin-bottom: 15px;
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
            padding: 0 15px;
            flex-grow: 1;
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
            transition: transform 0.2s ease;
        }
        .formacion-item:hover {
            transform: translateY(-4px);
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

        .galeria-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }
        .galeria-item {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 99, 65, 0.15);
            transition: transform 0.3s ease;
        }
        .galeria-item:hover {
            transform: scale(1.03);
        }
        .galeria-item img {
            width: 100%;
            height: 180px;
            object-fit: cover;
        }
        .galeria-item .info {
            padding: 20px;
        }
        .galeria-item h4 {
            color: var(--color-primario);
            margin-bottom: 10px;
        }

        .form-futuro {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border-top: 5px solid var(--color-dorado);
        }
        .form-group {
            margin-bottom: 20px;
            text-align: left;
        }
        .form-group label {
            display: block;
            font-weight: bold;
            color: var(--color-primario);
            margin-bottom: 8px;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #ccc;
            border-radius: 8px;
            font-family: inherit;
            font-size: 1em;
            transition: border 0.3s;
        }
        .form-group input:focus, .form-group textarea:focus {
            border-color: var(--color-primario);
            outline: none;
        }
        .btn-enviar {
            width: 100%;
            padding: 15px;
            font-size: 1.1em;
        }
        .flash {
            background: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 5px solid #28a745;
            text-align: center;
            font-weight: bold;
            animation: slideDown 0.5s ease;
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

        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for message in messages %}
                    <div class="flash">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

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
            <p class="bloque-desc">Voces de exalumnos, docentes y alumnos.</p>
            
            <h3 style="color: var(--color-primario); margin-bottom: 15px; border-bottom: 2px solid var(--color-dorado); padding-bottom: 5px;">Fundadores y Docentes</h3>
            <div class="grid-testimonios" style="margin-bottom: 40px;">
                {% for t in seccion.testimonios %}
                    {% if t.tipo == 'Fundador' or t.tipo == 'Docente' %}
                    <div class="testimonio">
                        <img src="{{ t.foto }}" alt="{{ t.nombre }}">
                        <span class="testimonio-tipo">{{ t.tipo }}</span>
                        <div class="nombre">{{ t.nombre }}</div>
                        {% if t.generacion %}<div class="generacion">{{ t.generacion }}</div>{% endif %}
                        <p class="frase">{{ t.frase }}</p>
                    </div>
                    {% endif %}
                {% endfor %}
            </div>

            <h3 style="color: var(--color-primario); margin-bottom: 15px; border-bottom: 2px solid var(--color-dorado); padding-bottom: 5px;">Egresados y Alumnos</h3>
            <div class="grid-testimonios" style="margin-bottom: 40px;">
                {% for t in seccion.testimonios %}
                    {% if t.tipo == 'Exalumno' or t.tipo == 'Alumno' %}
                    <div class="testimonio">
                        <img src="{{ t.foto }}" alt="{{ t.nombre }}">
                        <span class="testimonio-tipo">{{ t.tipo }}</span>
                        <div class="nombre">{{ t.nombre }}</div>
                        {% if t.generacion %}<div class="generacion">{{ t.generacion }}</div>{% endif %}
                        <p class="frase">{{ t.frase }}</p>
                    </div>
                    {% endif %}
                {% endfor %}
            </div>
        </div>

        <div class="especial-bloque">
            <h2>Déjanos tu testimonio</h2>
            <p class="bloque-desc">Comparte tu experiencia con el CECyTEJ.</p>
            <form action="/guardar-testimonio" method="POST" class="form-futuro">
                <div class="form-group">
                    <label>Nombre completo:</label>
                    <input type="text" name="nombre" required placeholder="Tu nombre">
                </div>
                <div class="form-group">
                    <label>¿Quién eres?</label>
                    <select name="tipo" required style="width: 100%; padding: 12px; border: 2px solid #ccc; border-radius: 8px; font-family: inherit; font-size: 1em;">
                        <option value="Alumno">Alumno actual</option>
                        <option value="Exalumno">Exalumno</option>
                        <option value="Docente">Docente</option>
                        <option value="Fundador">Fundador</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Generación / Años de servicio:</label>
                    <input type="text" name="generacion" placeholder="Ej. Generación 2020-2023" required>
                </div>
                <div class="form-group">
                    <label>Tu testimonio:</label>
                    <textarea name="frase" rows="4" required placeholder="Escribe lo que CECyTEJ significa para ti..."></textarea>
                </div>
                <button type="submit" class="btn btn-enviar">Enviar mi testimonio</button>
            </form>
        </div>
        {% endif %}

        {% if seccion.galeria_orgullo %}
        <div class="especial-bloque">
            <h2>Galería de Logros</h2>
            <p class="bloque-desc">Nuestro orgullo en Tecnología, Ciencia, Deportes, Cultura y Logros Académicos.</p>
            <div class="galeria-grid">
                {% for item in seccion.galeria_orgullo %}
                <div class="galeria-item">
                    <img src="{{ item.img }}" alt="{{ item.categoria }}">
                    <div class="info">
                        <h4>{{ item.categoria }}</h4>
                        <p style="color: var(--color-texto-suave); font-size: 0.95em;">{{ item.descripcion }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
            <div style="margin-top: 30px; text-align: left; background: var(--color-tarjeta-info); padding: 20px; border-radius: 10px; border-left: 4px solid var(--color-dorado);">
                <h3 style="color: var(--color-primario); margin-bottom: 10px;">Proyectos Destacados</h3>
                <ul style="margin-left: 20px; color: var(--color-texto-suave); line-height: 1.8;">
                    <li>Aplicaciones web de Programación.</li>
                    <li>Proyectos de los estudiantes de Electromecánica.</li>
                    <li>Ferias de ciencia, concursos de ajedrez y torneos deportivos.</li>
                </ul>
            </div>
        </div>
        {% endif %}

        {% if seccion.agenda %}
        <div class="especial-bloque">
            <h2>Agenda de Actividades</h2>
            <p class="bloque-desc">Acompáñanos a celebrar nuestros 30 años.</p>
            <div class="galeria-grid">
                {% for evento in seccion.agenda %}
                <div class="galeria-item">
                    <img src="{{ evento.img }}" alt="{{ evento.titulo }}">
                    <div class="info">
                        <h4>{{ evento.titulo }}</h4>
                        <p style="font-size: 0.9em; margin-bottom: 5px; font-weight: bold; color: var(--color-secundario);">📅 {{ evento.fecha }} | ⏰ {{ evento.horario }}</p>
                        <p style="color: var(--color-texto-suave); font-size: 0.95em;">{{ evento.descripcion }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {% if seccion.formulario_futuro %}
        <div class="especial-bloque">
            <h2>Mi mensaje para el futuro</h2>
            <p class="bloque-desc">¿Qué le deseas al CECyTEJ en sus próximos 30 años?</p>
            <form action="/guardar-futuro" method="POST" class="form-futuro">
                <div class="form-group">
                    <label>Tu nombre:</label>
                    <input type="text" name="nombre_futuro" required placeholder="Ej. Juan Pérez">
                </div>
                <div class="form-group">
                    <label>Tu generación:</label>
                    <input type="text" name="generacion_futuro" required placeholder="Ej. 2026">
                </div>
                <div class="form-group">
                    <label>Tu mensaje:</label>
                    <textarea name="mensaje_futuro" rows="4" required placeholder="Escribe tu mensaje para las próximas generaciones..."></textarea>
                </div>
                <button type="submit" class="btn btn-enviar">Enviar mi mensaje</button>
            </form>
            <p style="text-align: center; margin-top: 30px; font-style: italic; color: var(--color-primario); font-weight: bold; font-size: 1.2em;">
               
            </p>
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
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for message in messages %}
                    <div class="flash">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

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
        
        "linea_tiempo": [
            {"fecha": "2000", "titulo": "Inauguración del Plantel 08", "descripcion": "Abre sus puertas en Ixtlahuacán del Río y comienza a formar a las primeras generaciones.", "img": "https://www.geocities.ws/cecytej08ixtlahuacan/IMG_0017.JPG"},
            {"fecha": "2005", "titulo": "Logo del Plantel", "descripcion": "Logo del Plantel.", "img": "data:image/webp;base64,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"},
            {"fecha": "2019", "titulo": "Cambio de logo y color", "descripcion": "El plantel adopta el logo y los colores institucionales actuales.", "img": "https://tse1.mm.bing.net/th/id/OIP.gtGHr1XdSWXQyOuZJZScyQHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"},
            {"fecha": "2024", "titulo": "Torneo", "descripcion": "Los estudiantes del CECyTEJ organizan un torneo de voleibol en acción por la diabetes.", "img": "https://cdn.phototourl.com/member/2026-11-22-067aa110-e462-48f6-a799-3f6c948b6296.jpg"},
            {"fecha": "2024", "titulo": "Programación como carrera", "descripcion": "Se incorpora la carrera de Programación al plantel.", "img": "https://www.geocities.ws/cecytej08ixtlahuacan/DSC06101.JPG"},
            {"fecha": "2024", "titulo": "25 años", "descripcion": "25 años de historia del CECyTEJ.", "img": "https://scontent-qro1-2.xx.fbcdn.net/v/t39.30808-6/492230248_1259108679550023_2689160221924469700_n.jpg?stp=dst-jpg_tt6&cstp=mx1280x720&ctp=s1280x720&_nc_cat=106&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFfqhtvhb21_Rn6ZSzkZT_6v1EzwuhWTay_UTPC6FZNrGO64O6sinrA8AgJ_pnr5yFVT1zapl8RZ6JhwAsLITSv&_nc_ohc=2vJOIyxs4b0Q7kNvwEmcznE&_nc_oc=AdomDIyxzV9kUolN7YrTznWBK1OJVImSTVRt8Sk33kQ34kGo-MfjgSWaso7lgkdrP24&_nc_pt=1&_nc_zt=23&_nc_ht=scontent-qro1-2.xx&_nc_gid=dP6xOIaNa7XX9EpDr24KXQ&_nc_ss=7b2a8&oh=00_AQRgBhUVTsHF860nfc4f5zmHMV6QqYFsVfKIoDDkLmP_xA&oe=6B0935D0"},
            {"fecha": "2026", "titulo": "30 años de historia", "descripcion": "El CECyTEJ celebra tres décadas formando mentes, inspirando sueños y construyendo futuros.", "img": "https://cdn.imagetourls.com/uploads/tyImg/sIiBLhPV.jpg"},
            {"fecha": "2026", "titulo": "Familia CECyTEJ", "descripcion": "Docentes y todo el personal del CECyTEJ Ixtlahuacán del Río.", "img": "https://cdn.phototourl.com/member/2026-11-23-a7896351-17c4-4822-ba62-93bf96f9a64a.jpg"},
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
            {"fecha": "2021", "titulo": "25 Aniversario", "descripcion": "Celebración de los primeros 25 años de historia y formación del CECyTEJ."},
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
        "id": "Orgullo",
        "tipo": "especial",
        "titulo": "Orgullo CECyTEJ",
        "descripcion_corta": "Logros, talento y proyectos.",
        "descripcion_larga": "Nuestros estudiantes destacan en múltiples áreas, demostrando que el talento y la dedicación no tienen límites.",
        "img": "https://cdn.imagetourls.com/uploads/tyImg/sIiBLhPV.jpg",
        "galeria_orgullo": [
            {"categoria": "Tecnología", "descripcion": "Desarrollo de aplicaciones web y proyectos de programación.", "img": "https://www.geocities.ws/cecytej08ixtlahuacan/DSC06101.JPG"},
            {"categoria": "Ciencia", "descripcion": "Participación en ferias de ciencia con proyectos innovadores.", "img": "https://tse1.mm.bing.net/th/id/OIP.SfYkl_uLLn9z2U_mkwgU3QHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"},
            {"categoria": "Deportes", "descripcion": "Trofeos en torneos de voleibol, fútbol y básquetbol.", "img": "https://cdn.phototourl.com/member/2026-11-22-067aa110-e462-48f6-a799-3f6c948b6296.jpg"},
            {"categoria": "Cultura", "descripcion": "Danza folclórica, altar de muertos y desfiles cívicos.", "img": "https://th.bing.com/th/id/OIP.B-bwqvyRccYgnYyhEjY2mQHaEt?w=268&h=180&c=7&r=0&o=7&pid=1.7&rm=3"},
            {"categoria": "Logros académicos", "descripcion": "Concursos de conocimiento y olimpiadas.", "img": "https://www.geocities.ws/cecytej08ixtlahuacan/estante_trofeos.jpg"}
        ]
    },
    
    {
        "id": "Celebremos",
        "tipo": "especial",
        "titulo": "Celebremos Juntos",
        "descripcion_corta": "30 años de orgullo y tradición.",
        "descripcion_larga": "Acompáñanos en las actividades conmemorativas por nuestro 30 Aniversario.",
        "img": "https://cdn.imagetourls.com/uploads/tyImg/sIiBLhPV.jpg",
        "agenda": [
            {
                "titulo": "Expo-ciencia y Danza Folclórica",
                "fecha": "Jueves",
                "horario": "10:00 AM - 2 PM",
                "descripcion": "Exhibición de proyectos de todas las áreas (Tecnología, Programación, Electromecánica, Ciencias, Matemáticas, Español). Al final del día, presentación de danza folclórica.",
                "img": "https://th.bing.com/th/id/OIP.B-bwqvyRccYgnYyhEjY2mQHaEt?w=302&h=192&c=7&r=0&o=7&pid=1.7&rm=3"
            },
            {
                "titulo": "Torneos Deportivos y Bastoneras",
                "fecha": "Miércoles y Jueves ",
                "horario": "11:00 AM - 1 PM",
                "descripcion": "Práctica y partidos de deportes. Los ensayos de bastoneras y los equipos de fútbol femenil y varonil son los días viernes.",
                "img": "https://scontent-qro1-1.xx.fbcdn.net/v/t39.30808-6/482252884_1214969293963962_7967753541040649622_n.jpg?stp=dst-jpg_tt6&cstp=mx1280x720&ctp=s1280x720&_nc_cat=106&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=833d8c&_nc_eui2=AeGMg47cfRpSA3xtbSwMxGYb3P1Gy_w5AnDc_UbL_DkCcKjTWFWH8rGjMHeaxh-nBcSN7yl5d1NZjIM1PBy-DtsE&_nc_ohc=_n58kK3sdmoQ7kNvwE1O88s&_nc_oc=AdqtyqaBmWkbc7vV99b6MklHEtZvvL1v0j6yzJ05hEED_VQ-i1qlJHQcT_Htznzr3us&_nc_pt=1&_nc_zt=23&_nc_ht=scontent-qro1-1.xx&_nc_gid=CYM9hDlBnWtkiDc97UjlJQ&_nc_ss=7b2a8&oh=00_AQQQBPCB2CPqjOOKyQsiwftUGV3OtNIY6maoTEjkNX0xYg&oe=6B0A9366"
            },
            {
                "titulo": "Desfile Cívico",
                "fecha": "16 de Septiembre",
                "horario": "Por definir",
                "descripcion": "Desfile conmemorativo por la Independencia de México en el que participa toda la escuela.",
                "img": "https://scontent-qro3-1.xx.fbcdn.net/v/t51.82787-15/548877391_18423178672103797_8886909494706652018_n.webp?stp=dst-jpg_tt6&cstp=mx1440x1440&ctp=s1440x1440&_nc_cat=107&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeGeY3ANO_lXufkPlJP11by4OAloEs_ICHw4CWgSz8gIfCIsNOmrTwtlfLcc0R1UOPt58jCZ_JilW3EG2gEgBc5o&_nc_ohc=XWcWtp0rVSMQ7kNvwFquFDy&_nc_oc=AdrhlRMJCNde9ig9PGkiiImj9gB7L4o2MnmW718eLb3UVdqLcLOvXDfq2m5LQRsAO_0&_nc_pt=1&_nc_zt=23&_nc_ht=scontent-qro3-1.xx&_nc_gid=hA3K5wTzN5wMj0mTAHJJhw&_nc_ss=7b2a8&oh=00_AQQI8xJLHrG9zBw0S2M2k2iI5Ohxeyt_R6okpJjOtccC3g&oe=6B0A99DE"
            },
            {
                "titulo": "Altar de Muertos y Concurso de Catrines",
                "fecha": "2 de Noviembre",
                "horario": "8 PM - 10 PM",
                "descripcion": "Todos los grupos participan montando un altar. Los estudiantes muestran trajes de catrín/catrina y se premian a los 3 primeros lugares (tanto en altares como en trajes).",
                "img": "https://scontent-qro1-2.xx.fbcdn.net/v/t51.82787-15/882773508_18500145853103797_6251780938634054178_n.webp?stp=dst-jpg_tt6&cstp=mx1440x1440&ctp=s1440x1440&_nc_cat=110&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeF9rDOr8XLSS1wN-0cruIOW6W7Nlxze0xTpbs2XHN7TFJtufV9_gl9L6KFheoD2uKyoBWPcYPS3KFf4VF05KiYO&_nc_ohc=nVvxC-qzKOoQ7kNvwF5fQoo&_nc_oc=AdpkSFOdf8r9UqAm5mWE5kE90Cg-Zq2ElU1eRH2U6Ex7tEi9qA2TLyQkVCrXlZ-Q27Q&_nc_pt=1&_nc_zt=23&_nc_ht=scontent-qro1-2.xx&_nc_gid=hLoecb2BYdYquWB9bSfXkw&_nc_ss=7b2a8&oh=00_AQSDaGye0OQCOtcxQlVYkim_sMdq5nEeLO1rwZGxzyEXEQ&oe=6B0AB2F1"
            },
            {
                "titulo": "Día de pijamas",
                "fecha": "25 Noviembre",
                "horario": "7 AM - 2 PM",
                "descripcion": "Un día para poder asistir en pijama a la escuela.",
                "img": "data:image/webp;base64,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"
            }
        ]
    },
    
    {
        "id": "Futuro",
        "tipo": "especial",
        "titulo": "Nuestro Futuro",
        "descripcion_corta": "Los próximos 30 años.",
        "descripcion_larga": "Lo que imaginasde cómo podría ser el plantel en un futuro.",
        "img": "https://cdn.imagetourls.com/uploads/tyImg/sIiBLhPV.jpg",
        "formulario_futuro": True
    },
    
    {
        "id": "Testimonios",
        "tipo": "especial",
        "titulo": "Testimonios",
        "descripcion_corta": "Exalumnos y alumnos.",
        "descripcion_larga": "Voces de quienes han formado parte del CECyTEJ Plantel 08: exalumnos y alumnos comparten su experiencia.",
        "img": "https://tse1.mm.bing.net/th/id/OIP.PsJRDP5auWe9qYhFWzLGkgHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
        "testimonios": [
            {"tipo": "Fundador", "nombre": "Erwin Bojorge Gutiérrez", "frase": "Soñamos con un plantel y hoy es una realidad que ha superado todas nuestras expectativas.", "foto": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9KUofQcAXJKcljwAOi2nR4dZu2yR2vyMjkvwgL3IMDOdS8BZpuObRAjh9jZdM2DcOtI_eYoGesQPF5FTrygYsyOTciYm5gRoqQx6CjoBIj9yfSi7tBpmTS8XGtdNKWYJiAOfMouLsjwI/s1600/DSC04962.JPG"},
            {"tipo": "Docente", "nombre": "Prof. Adán Nóe","frase": "Echenle ganas jovenes.", "foto": "https://cdn.phototourl.com/member/2026-11-24-b10e602f-2bce-4b24-bb2a-58d4e8dc70a3.jpg"},
            {"tipo": "Exalumno", "nombre": "Fernando", "frase": "La escuela es bien bonita, convives y haces amigos, lo que importa es sentirse bien.", "foto": "https://th.bing.com/th/id/OIP.AJ7s-dLPwGPP1Wcq5LairgHaH4?w=170&h=182&c=7&r=0&o=7&pid=1.7&rm=3"},
            {"tipo": "Alumna", "nombre": "Valeria",  "frase": "Me gusta la experiencia, aunque sea de último año agradezco todo lo que pasé aquí.", "foto": "https://th.bing.com/th/id/OIP.FinoSANszfF2Ij5UkjNkkgHaHa?w=178&h=182&c=7&r=0&o=7&pid=1.7&rm=3"},
            {"tipo": "Exalumno", "nombre": "Cristopher",  "frase": "Sean autodidactas, nunca dejen de aprender.", "foto": "https://th.bing.com/th/id/OIP.AJ7s-dLPwGPP1Wcq5LairgHaH4?w=170&h=182&c=7&r=0&o=7&pid=1.7&rm=3"}
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
    if identificador == "Testimonios":
        seccion_testimonios = next((s for s in SECCIONES if s["id"] == "Testimonios"), None)
        if seccion_testimonios:
            nuevos = cargar_testimonios()
            seccion_testimonios = dict(seccion_testimonios)
            seccion_testimonios["testimonios"] = seccion_testimonios["testimonios"] + nuevos
            
            indice = next((i for i, s in enumerate(SECCIONES) if s["id"] == identificador), None)
            anterior = SECCIONES[indice - 1]["id"] if indice > 0 else None
            siguiente = SECCIONES[indice + 1]["id"] if indice < len(SECCIONES) - 1 else None
            
            return render_template_string(
                HTML, secciones=SECCIONES, seccion=seccion_testimonios, indice=indice,
                total=len(SECCIONES), anterior=anterior, siguiente=siguiente
            )

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


@app.route("/guardar-testimonio", methods=["POST"])
def guardar_testimonio_route():
    nombre = request.form.get("nombre")
    tipo = request.form.get("tipo")
    generacion = request.form.get("generacion")
    frase = request.form.get("frase")
    
    if nombre and tipo and generacion and frase:
        nuevo_testimonio = {
            "tipo": tipo,
            "nombre": nombre,
            "generacion": generacion,
            "frase": frase,
            "foto": "https://via.placeholder.com/80x80?text=" + nombre[0].upper()
        }
        guardar_testimonio(nuevo_testimonio)
        flash("¡Gracias! Tu testimonio ha sido guardado exitosamente.")
    else:
        flash("Por favor, completa todos los campos del formulario.")
        
    return redirect(url_for("detalle", identificador="Testimonios"))


@app.route("/guardar-futuro", methods=["POST"])
def guardar_futuro():
    flash("¡Gracias! Tu mensaje para el futuro ha sido recibido.")
    return redirect(url_for("detalle", identificador="Futuro"))


if __name__ == "__main__":
    app.run(debug=True)