<?php
// I hate php so much it's insane, but we're getting to the point with JS that we may as well just be using PHP again
function getSmartdLogsAsHTML($fileName, $hoursBack) {
    // Check if the file exists and is readable
    if (!file_exists($fileName) || !is_readable($fileName)) {
        return "<p>Unable to read log file. Please check if the file exists and is readable.</p>";
    }

    // Calculate the time limit to filter logs
    $timeLimit = time() - ($hoursBack * 3600); // Convert hours to seconds

    // Open the log file
    $fileContent = file_get_contents($fileName);
    $logLines = explode("\n", $fileContent);

    // Start building the HTML output
    $htmlOutput = "<div>";

    // Iterate over each log line and check if it's within the time limit and contains 'smartd'
    foreach ($logLines as $line) {
        if (!empty(trim($line))) {
            $lineParts = explode(' ', trim($line), 4); // Split to get the date part
            if (count($lineParts) > 3 && strtotime($lineParts[0] . ' ' . $lineParts[1] . ' ' . $lineParts[2]) >= $timeLimit && strpos($lineParts[3], 'smartd') !== false) {
                $htmlOutput .= "<p>" . htmlspecialchars($lineParts[3]) . "</p>";
            }
        }
    }

    // Close the div tag
    $htmlOutput .= "</div>";

    return $htmlOutput;
}

// Example usage: get logs from the past 5 hours from 'system.log'
echo getSmartdLogsAsHTML('entries.log', 5000);
?>