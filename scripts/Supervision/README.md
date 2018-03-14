# Supervision
Weblogic est installe dans (adapater le chemin si Weblogic est installe dans un autre repertoire) :
<pre><code>/appli/oracle/middleware</code></pre>
Ce qui nous donne par exemple ceci comme chemin pour les binaires Weblogic : /appli/oracle/middleware/wlserver_10.3/server/bin
<br>Les scripts weblogic sont deposes dans le même repertoire : 
<pre><code>/appli/scripts/weblogic</code></pre>
Les codes sont standard (compatible avec Nagios)
<pre><code>0 : OK
1 : Warning
2 : Error </code></pre>
Par defaut utilise le compte "weblogic" et le port "7001" pour se connecter a Weblogic

<h1>Server</h1>
<pre><code>/appli/scripts/check-server-status.sh PASSWORD [PORT]</code></pre>
Ce qui nous donne par exemple comme sortie :
<pre><code>0 : [SUP] DOMAINE1_ADMIN : RUNNING>[SUP] DOMAINE2 : RUNNING>
1 : [SUP] DOMAINE1_ADMIN : RUNNING>[SUP] DOMAINE2 : STARTING>
2 : [SUP] DOMAINE1_ADMIN : RUNNING>[SUP] DOMAINE2 : SHUTDOWN></code></pre>

<h1>Application</h1>
<pre><code>/appli/scripts/check-application-status.sh PASSWORD [PORT]</code></pre>
Ce qui nous donne comme sortie :
<pre><code>0 : [SUP] APPLICATION : STATE_ACTIVE>
1 : [SUP] APPLICATION : STATE_NEW/PREPARED>
2 : [SUP] APPLICATION : ERROR></code></pre>

<h1>Datasource</h1>
<pre><code>/appli/scripts/check-datasource-status.sh PASSWORD [PORT]</code></pre>
Ce qui nous donne comme sortie :
<pre><code>0 : [SUP] DATASOURCE : Running>
1 : [SUP] DATASOURCE : Suspended>
2 : [SUP] DATASOURCE : ERROR></code></pre>
