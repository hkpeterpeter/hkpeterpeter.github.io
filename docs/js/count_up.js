var CountUp = (function () {
    function CountUp(id, startVal, endVal, decimal_places, duration) {
        var _this = this;
        this.count = function (timestamp) {
            if (!_this.startTime) {
                _this.startTime = timestamp;
            }
            var progress = timestamp - _this.startTime;
            var frameVal = _this.startVal + (_this.endVal - _this.startVal) * (progress / _this.duration);
            frameVal = Number(frameVal.toFixed(_this.decimal_places));
            if (frameVal > _this.endVal)
                frameVal = _this.endVal;
            _this.el.textContent = frameVal.toString();
            if (progress < _this.duration) {
                requestAnimationFrame(_this.count);
            }
        };
        this.startVal = startVal;
        this.endVal = endVal;
        this.decimal_places = decimal_places;
        this.duration = duration * 1000;
        this.el = document.getElementById(id);
    }
    CountUp.prototype.start = function () {
        requestAnimationFrame(this.count);
    };
    return CountUp;
}());
