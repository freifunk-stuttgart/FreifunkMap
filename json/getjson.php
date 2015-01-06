<?php
/*
 * @author     Flip
 * @package    ffMap
 * @version    1.0
 * @licenses	CC-BY-SA Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz. https://creativecommons.org/licenses/by-sa/4.0/

 
 provides access to the json data
 example requests
  
 GET: /alfred-json-map.json <-- JSON 
 */
header('Content-type: application/json'); // Always talk JSON
	
header('Cache-Control: no-cache, must-revalidate');
header('Expires: Mon, 26 Jul 1997 05:00:00 GMT');
    
$ressource = $_GET['ressource'];

$ressourceData = file_get_contents('http://gw01.freifunk-stuttgart.de/map/json/'.$ressource);

echo $ressourceData;

?>