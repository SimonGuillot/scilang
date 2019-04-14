<?xml version="1.0" encoding="UTF-8"?>

<!--+
    + A Copier sous le prologue du fichier xml : <?xml-stylesheet type="text/xsl" href="un fichier.xsl" ?> 
    +-->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:strip-space elements="*"/>
  <xsl:output method="html" />

  <xsl:template match="/">
        <html>
            <head>
              <meta charset="UTF-8" />
            	<link rel="stylesheet" href="un fichier css" />
            	<title>Mon titre</title>
            </head>
            <body>
              <table border="2" style="text-align: center;">
            	<tr>
            	  <th>titre</th>
            	  <th>nom</th>
            	  <th>annee</th>
				  <th>pays</th>
				  <th>compagnie</th>
				  <th>critique</th>
				  <th>prix</th>
            	</tr>
            	<xsl:for-each select="catalogue/album">
				<xsl:sort select="annee"/>
				<xsl:sort select="titre"/>
				<xsl:if test="number(prix) &gt; 10 ">
					<tr>
							<td><xsl:value-of select="titre" /></td>
							<td><xsl:value-of select="nom" /></td>
							<td><xsl:value-of select="annee" /></td>
							<td><xsl:value-of select="pays" /></td>
							<td><xsl:value-of select="compagnie" /></td>
							<td><xsl:value-of select="critique/@avis" /></td>
							<td><xsl:value-of select="prix" /></td>
					</tr>
				</xsl:if>
            	</xsl:for-each>
            </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>        
