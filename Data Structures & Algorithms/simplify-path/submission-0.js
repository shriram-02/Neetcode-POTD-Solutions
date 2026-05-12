class Solution {
    /**
     * @param {string} path
     * @return {string}
     */
    simplifyPath(path) {
        const stack = [];
        const parts = path.split('/');

        for (const part of parts) {
            if (part === '' || part === '.') {
                continue;
            }
            else if (part === '..') {
                if (stack.length > 0) {
                    stack.pop();
                }
            }
            else {
                stack.push(part);
            }
        }

        return '/' + stack.join('/');
    }
}