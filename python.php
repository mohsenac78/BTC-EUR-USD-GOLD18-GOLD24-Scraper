<?php
// Execute the Python script
$pythonCommand = 'python3 script.py';
exec($pythonCommand);
$pythonCommand = 'python3 data.json';
exec($pythonCommand);

// Read data from the generated file
$data = file_get_contents('data.json');
$jsonData = json_decode($data, true);

// Output the retrieved data
echo "<pre>"; 
print_r($jsonData);
echo "</pre>"; 
?>