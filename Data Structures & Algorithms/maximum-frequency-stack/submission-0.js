class FreqStack {
    constructor() {
        this.freq = new Map();
        this.group = new Map();
        this.maxFreq = 0;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        let f = (this.freq.get(val) || 0) + 1;
        this.freq.set(val, f);

        if (!this.group.has(f)) {
            this.group.set(f, []);
        }

        this.group.get(f).push(val);

        this.maxFreq = Math.max(this.maxFreq, f);
    }

    /**
     * @return {number}
     */
    pop() {
        let val = this.group.get(this.maxFreq).pop();

        this.freq.set(val, this.freq.get(val) - 1);

        if (this.group.get(this.maxFreq).length === 0) {
            this.maxFreq--;
        }

        return val;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * var obj = new FreqStack()
 * obj.push(val)
 * var param_2 = obj.pop()
 */