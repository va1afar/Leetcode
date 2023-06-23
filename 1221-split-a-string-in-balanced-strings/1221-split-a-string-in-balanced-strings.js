/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let count = 0;
    let consecutiveRCount = 0;
    let consecutiveLCount = 0;
    
    for (let i = 0; i < s.length; i++) {
       if (s[i] === "R") {
          consecutiveRCount++; 
       } else {
          consecutiveLCount++; 
       }
       if (consecutiveRCount === consecutiveLCount) {
           count++;
           consecutiveRCount = 0;
           consecutiveLCount = 0;
       } 
    }
    
    return count;
};