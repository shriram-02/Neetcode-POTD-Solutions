class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    decodeString(s) {
        let numStack = [];
        let strStack = [];
        let currentStr = "";
        let currentNum = 0;

        for (let char of s) {
            if (!isNaN(char)) {
                currentNum = currentNum * 10 + Number(char);
            }
            else if (char === "[") {
                numStack.push(currentNum);
                strStack.push(currentStr);

                currentNum = 0;
                currentStr = "";
            }
            else if (char === "]") {
                let repeatTimes = numStack.pop();
                let prevStr = strStack.pop();

                currentStr = prevStr + currentStr.repeat(repeatTimes);
            }
            else {
                currentStr += char;
            }
        }

        return currentStr;
    }
}