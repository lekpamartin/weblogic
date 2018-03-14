# Supervision
Weblogic est installe dans (adapater le chemin si Weblogic est installe dans un autre repertoire) :
<pre><code>/appli/oracle/middleware</code></pre>
Ce qui nous donne par exemple ceci comme chemin pour les binaires Weblogic : /appli/oracle/middleware/wlserver_10.3/server/bin
<br>Les scripts weblogic sont deposes dans le même repertoire : 
<pre><code>/appli/scripts/weblogic</code></pre>
Les codes de sorties sont standard (compatible avec Nagios)
<pre><code>0 : OK
1 : Warning
2 : Error </code></pre>


<h1>Server</h1>
Par defaut utilise le compte weblogic et le port 7001 pour se connecter a Weblogic
<pre><code>/appli/scripts/check-server-status.sh PASSWORD [PORT]</code></pre>
