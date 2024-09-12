<?php
// Define the Solution class as per your environment's expectations
class Solution {
    // Add the countConsistentStrings function inside the Solution class
    public function countConsistentStrings($allowed, $words) {
        // Convert the allowed string into an array of allowed characters
        $allowedSet = array_flip(str_split($allowed));

        // Count the consistent words
        $consistentCount = 0;

        foreach ($words as $word) {
            $isConsistent = true;

            // Check if every character in the word is in the allowed set
            foreach (str_split($word) as $char) {
                if (!isset($allowedSet[$char])) {
                    $isConsistent = false;
                    break;
                }
            }

            if ($isConsistent) {
                $consistentCount++;
            }
        }

        return $consistentCount;
    }
}

// Instantiate the Solution class
$solution = new Solution();

// Test cases

// Example 1
$allowed = "ab";
$words = ["ad", "bd", "aaab", "baa", "badab"];
echo $solution->countConsistentStrings($allowed, $words) . PHP_EOL; // Output: 2

// Example 2
$allowed = "abc";
$words = ["a", "b", "c", "ab", "ac", "bc", "abc"];
echo $solution->countConsistentStrings($allowed, $words) . PHP_EOL; // Output: 7

// Example 3
$allowed = "cad";
$words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"];
echo $solution->countConsistentStrings($allowed, $words) . PHP_EOL; // Output: 4
?>
