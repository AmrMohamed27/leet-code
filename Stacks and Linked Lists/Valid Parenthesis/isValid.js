/**
 * @param {string} s
 * @return {boolean}
 */

var isValid = function (s) {
  if (s.length % 2 !== 0) return false;
  let stack = [];
  for (const c of s) {
    if (c === "(" || c === "{" || c === "[") stack.push(c);
    else if (c === ")" && stack[stack.length - 1] === "(") stack.pop();
    else if (c === "}" && stack[stack.length - 1] === "{") stack.pop();
    else if (c === "]" && stack[stack.length - 1] === "[") stack.pop();
    else return false;
  }
  return stack.length > 0 ? false : true;
};
console.log(isValid("([}}])"));
