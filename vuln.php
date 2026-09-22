<?php
$id = $_GET['id'] ?? '1';
echo "ID: $id <br>";
if (strpos($id, "'") !== false) {
    echo "Warning: mysql_fetch_array() SQL syntax error";
} else {
    echo "No error";
}
?>
