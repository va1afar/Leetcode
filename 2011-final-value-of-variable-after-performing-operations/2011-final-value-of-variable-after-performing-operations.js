var finalValueAfterOperations = function (operations) {
  let answer = 0;

  for (let i = 0; i < operations.length; i++) {
    let currentOperation = operations[i];
    if (currentOperation === "++X" || currentOperation === "X++") {
      answer += 1;
    } else {
      answer -= 1;
    }
  }

  return answer;
};