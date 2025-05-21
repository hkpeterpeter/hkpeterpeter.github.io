/*
    My own simpified implementation of CountUp
    - I only need count up
    - I am not interested in other unrelated options
    Reference: https://github.com/inorganik/countUp.js/blob/master/src/countUp.ts
*/
class CountUp {
    startVal: number;
    endVal: number;
    decimal_places: number;
    duration: number;
    private startTime: number;
    private el: HTMLElement;

    constructor(id: string, startVal: number, endVal: number, decimal_places: number, duration: number) {
        this.startVal = startVal;
        this.endVal = endVal;
        this.decimal_places = decimal_places;
        this.duration = duration * 1000;
        this.el = document.getElementById(id);
    }

    // Note: here, count needs to be an arrow function to preserve this
    count = (timestamp: number) => {

        if (!this.startTime) { this.startTime = timestamp; }
        const progress = timestamp - this.startTime;

        let frameVal = this.startVal + (this.endVal - this.startVal) * (progress / this.duration);
    
        frameVal = Number(frameVal.toFixed(this.decimal_places));
        if ( frameVal > this.endVal )
            frameVal = this.endVal;  // set the frameVal to endVal at the end

        // console.log(frameVal);

        this.el.textContent = frameVal.toString();

        if ( progress < this.duration ) {
            requestAnimationFrame(this.count);
        }  
    } 
    start() {
        requestAnimationFrame(this.count);
    }
}

