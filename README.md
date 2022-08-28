<h1 class="title">Maslow</h1>

[![Windows Supported](https://img.shields.io/badge/Windows-Supported-blue?style=flat-square&logo=windows)](#)
[![Linux Supported](https://img.shields.io/badge/Linux-Supported-red?style=flat-square&logo=linux)](#)
[![Python Programming](https://img.shields.io/badge/Python-Supported-red?style=flat-square&logo=python)](#)
[![By](https://img.shields.io/badge/By-j0fr4s3cr-yellow?style=flat-square&logo=github)](#)

<p> Proyecto desarrollado con el fin de poder apoyar a toda la comunidad para comenzar con el uso de APi en los equipos meraki, aún se encuentra en mejoras pero lo que puede hacer se deja mostrado en este readme.</p>

<img src="https://user-images.githubusercontent.com/111472825/186256825-9b5c8e02-1c1f-49b4-afed-0e5630487cf5.png">


<h1>Requisitos</h1>
<p> 1 - Para poder uso de las APIs en los equipos meraki primero debes habilitar una opcion en cada organización que viene  Organization > Settings > Dashboard API access. </p>
 
 ![image](https://user-images.githubusercontent.com/111472825/186730526-e971f78c-5f41-4e32-b493-4d2585d3197c.png)

<p> 2 - Despues para poder utilizar las API debes generar una y eso lo haces en el apartado de mi profile que se encuentra en la parte superior izquierda donde esta tu correo, le das click y despliega el menu donde vendra esta opción. </p>

![image](https://user-images.githubusercontent.com/111472825/186732020-f9514de7-940e-454b-9233-7b45bec90b10.png)


<p>3 - Instala el archivo requirements.txt con el siguiente comando:<p>
 <h3>Comando en windows</h3>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 pip install -r /path/to/requirements.txt
</code>
</pre>
</div>
<h3>Comando en linux</h3>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 pip3 install -r /path/to/requirements.txt
</code>
</div>
 </pre>
<p>Esto instalará todas las librerias que pudieras necesitar en el proyecto.</p>


<h1>Uso</h1>
<p> Esta herramienta tiene estas funcionalidades activas hasta el momento:</p>
<ol>
<li> Listar todas las organizaciones de un dashboard</li>
<li> Buscar organizaciones por ID o Nombre</li>
<li> Listar networks por ID o Nombre </li>
<li> Listar todos los dispositivos de un dashboard </li>

<h3> Escribe este comando para ver la ayuda de la herramienta</h3>
<p> Comando en Windows </p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 python path/main.py -h
</code>
</pre>
</div>
<p> Comando en Linux</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 python3 path/main.py -h
</code>
</pre>
</div>
<!---- Comando para traer todas las organizaciones !---->
<h3> Para traer todas las organizaciones de un dashboard usa este comando:</h3>
<p> Comando en Windows </p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 python path/main.py -a API_KEY -ao all
</code>
</pre>
</div>
<p> Comando en Linux </p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 python3 path/main.py -a API_KEY -ao all
</code>
</pre>
</div>
<!---- Comando para traer organizaciones por ID o NAME !---->
<h3> Para traer una organización por ID o por Nombre usa este comando:</h3>
<p> Comando en Windows </p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 python path/main.py -a API_KEY -o ID
</code>
</pre>
</div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 python path/main.py -a API_KEY -o "NAME"
</code>
</pre>
</div>
<p> Comando en Linux </p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 python3 path/main.py -a API_KEY -o ID
</code>
</pre>
</div>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 python3 path/main.py -a API_KEY -o "NAME"
</code>
</pre>
</div>
<!---- Comando para traer networks !---->
<h3> Para traer una network por ID o por Nombre usa este comando:</h3>
<p> Comando en Windows </p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 python path/main.py -a API_KEY -n ID
</code>
</pre>
</div>
<p> Comando en Linux </p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
 <code>
 python3 path/main.py -a API_KEY -n ID
</code>
</pre>
</div>
<p> Solo las network tiene la funcionalidad de exportarlas a los formatos csv,xls y txt en esta versión del proyecto.</p>
<img src="https://user-images.githubusercontent.com/111472825/187052238-7474d8c9-8376-4462-92b5-31a087c2cd60.png">
<img src="https://user-images.githubusercontent.com/111472825/187052253-0ced6edd-7a5b-4707-b7de-e58151778148.png">


